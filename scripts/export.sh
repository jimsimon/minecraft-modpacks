#!/usr/bin/env bash
# Validate one pack and export it as a Modrinth .mrpack into dist/.
#
#   scripts/export.sh <pack> [expected-version]
#
# <pack> is a directory under packs/. If expected-version is given it must
# match the version in pack.toml (CI passes the version from the git tag so a
# tag can never ship a pack whose pack.toml says something else).
#
# Outputs:
#   dist/<pack>-<version>.mrpack
#   dist/<pack>-<version>.notes.md   (release notes: loader + mod list)
set -euo pipefail

pack="${1:-}"
expected="${2:-}"
[ -n "$pack" ] || { echo "usage: $0 <pack> [expected-version]" >&2; exit 2; }

root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/packs/$pack"
[ -f "$dir/pack.toml" ] || { echo "no pack at packs/$pack (missing pack.toml)" >&2; exit 1; }

command -v packwiz >/dev/null 2>&1 || { echo "packwiz not on PATH; run scripts/install-packwiz.sh" >&2; exit 1; }

version="$(sed -n 's/^version = "\(.*\)"$/\1/p' "$dir/pack.toml" | head -n1)"
[ -n "$version" ] || { echo "packs/$pack/pack.toml has no version" >&2; exit 1; }
if [ -n "$expected" ] && [ "$expected" != "$version" ]; then
  echo "version mismatch: tag says $expected but packs/$pack/pack.toml says $version" >&2
  exit 1
fi

cd "$dir"

# The index must be in sync with the files on disk; a stale index.toml means
# someone edited a file without running `packwiz refresh`. Compare the index
# before and after a refresh rather than against git, so local uncommitted
# edits that *were* refreshed still pass.
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
cp index.toml pack.toml "$tmp/"
packwiz refresh >/dev/null
if ! cmp -s index.toml "$tmp/index.toml" || ! cmp -s pack.toml "$tmp/pack.toml"; then
  echo "packs/$pack was out of sync with its index; 'packwiz refresh' changed:" >&2
  diff -u "$tmp/index.toml" index.toml >&2 || true
  diff -u "$tmp/pack.toml" pack.toml >&2 || true
  echo "commit the refreshed index.toml/pack.toml and retry" >&2
  exit 1
fi

mkdir -p "$root/dist"
out="$root/dist/$pack-$version.mrpack"
packwiz modrinth export -o "$out" >/dev/null
echo "exported $out"

notes="$root/dist/$pack-$version.notes.md"
{
  echo "## $pack $version"
  echo
  sed -n '/^\[versions\]/,/^\[/p' pack.toml | sed -n 's/^\([a-z-]*\) = "\(.*\)"$/- \1 \2/p'
  echo
  echo "## Mods"
  echo
  for f in mods/*.pw.toml; do
    [ -e "$f" ] || continue
    name="$(sed -n 's/^name = "\(.*\)"$/\1/p' "$f" | head -n1)"
    file="$(sed -n 's/^filename = "\(.*\)"$/\1/p' "$f" | head -n1)"
    side="$(sed -n 's/^side = "\(.*\)"$/\1/p' "$f" | head -n1)"
    echo "- $name (\`$file\`, ${side:-both})"
  done
  echo
  echo "Server install: \`--modrinth https://github.com/jimsimon/minecraft-modpacks/releases/download/$pack-v$version/$pack-$version.mrpack\`"
  # Optional per-pack notes (client memory, setup steps) appended verbatim.
  if [ -f RELEASE_NOTES.md ]; then
    echo
    cat RELEASE_NOTES.md
  fi
} > "$notes"
echo "wrote $notes"
