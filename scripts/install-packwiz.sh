#!/usr/bin/env bash
# Install a pinned build of packwiz with `go install`. Used by CI and usable
# locally when Go is available. Bump PACKWIZ_COMMIT deliberately; packwiz has
# no tagged releases, so the commit is the only reproducible pin.
set -euo pipefail

PACKWIZ_COMMIT="ef87d964f8cbd52b3b13ea42453ef322290e2b9e" # main as of 2026-09-06

if command -v packwiz >/dev/null 2>&1 && [ "${1:-}" != "--force" ]; then
  echo "packwiz already on PATH: $(command -v packwiz) (use --force to reinstall)"
  exit 0
fi

command -v go >/dev/null 2>&1 || {
  echo "go is required (https://go.dev/dl/), or download a CI build from" >&2
  echo "https://nightly.link/packwiz/packwiz/workflows/go/main and put it on PATH" >&2
  exit 1
}

go install "github.com/packwiz/packwiz@${PACKWIZ_COMMIT}"
bin="$(go env GOPATH)/bin"
echo "installed ${bin}/packwiz"
# Make it visible to later steps of a GitHub Actions job.
if [ -n "${GITHUB_PATH:-}" ]; then
  echo "$bin" >> "$GITHUB_PATH"
fi
