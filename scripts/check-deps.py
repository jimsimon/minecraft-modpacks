#!/usr/bin/env python3
"""Verify that every Fabric mod's declared dependencies are present on the
side(s) it is installed on, and that no two mods on a side share a mixin
config file name (Fabric Loader refuses to launch in that case).

    scripts/check-deps.py packs/<pack> [--cache DIR]

Reads mods/*.pw.toml, downloads each jar (cached), parses fabric.mod.json
(including nested jars) and reports any `depends` id that is not provided by
another mod installed on the same side. Modrinth's side metadata is not always
right (e.g. Athena listed client-only but needed by CobbleFurnies on the
server), so run this before tagging a release. Exit status 1 if anything is
missing.
"""
import argparse, hashlib, io, json, os, re, sys, urllib.request, zipfile

BUILTIN = {"minecraft", "java", "fabricloader", "fabric"}

def parse_pw(path):
    t = open(path, encoding="utf-8").read()
    g = lambda k: re.search(rf'^{k} = "(.*)"$', t, re.M).group(1)
    return {"slug": os.path.basename(path)[:-8], "side": g("side"),
            "url": g("url"), "filename": g("filename")}

def fetch(url, cache):
    os.makedirs(cache, exist_ok=True)
    p = os.path.join(cache, hashlib.sha1(url.encode()).hexdigest() + ".jar")
    if not os.path.exists(p):
        with urllib.request.urlopen(url) as r, open(p, "wb") as f:
            f.write(r.read())
    return p

def read_mod(zf):
    """[(id, provides, depends, environment)] for the jar and nested jars."""
    out = []
    try:
        fm = json.loads(zf.read("fabric.mod.json").decode("utf-8", "replace"), strict=False)
    except (KeyError, ValueError):
        return out
    dep = fm.get("depends") or {}
    if isinstance(dep, list):
        dep = {d: "*" for d in dep}
    mixins = [m if isinstance(m, str) else m.get("config") for m in (fm.get("mixins") or [])]
    out.append((fm["id"], fm.get("provides") or [], dep, fm.get("environment", "*"), mixins))
    for j in fm.get("jars") or []:
        try:
            out += read_mod(zipfile.ZipFile(io.BytesIO(zf.read(j["file"]))))
        except (KeyError, zipfile.BadZipFile):
            pass
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack")
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/minecraft-modpacks/jars"))
    a = ap.parse_args()
    mods = {}
    for f in sorted(os.listdir(os.path.join(a.pack, "mods"))):
        if not f.endswith(".pw.toml"):
            continue
        m = parse_pw(os.path.join(a.pack, "mods", f))
        if not m["filename"].endswith(".jar"):
            continue
        try:
            mods[m["slug"]] = (m["side"], read_mod(zipfile.ZipFile(fetch(m["url"], a.cache))))
        except Exception as e:  # noqa: BLE001
            print(f"!! {m['slug']}: {e}", file=sys.stderr)
    bad = 0
    for label, sides in (("server", {"both", "server"}), ("client", {"both", "client"})):
        have = set(BUILTIN)
        for side, entries in mods.values():
            if side in sides:
                for mid, prov, _, _, _ in entries:
                    have.add(mid); have.update(prov)
        print(f"== {label}: {len(have)} mod ids present")
        for slug, (side, entries) in sorted(mods.items()):
            if side not in sides or not entries:
                continue
            mid, _, dep, _, _ = entries[0]
            missing = [d for d in dep if d not in have]
            if missing:
                bad += 1
                print(f"   MISSING on {label}: {slug} ({mid}, side={side}) needs {missing}")
        # Fabric Loader requires mixin config file names to be unique across all
        # loaded mods; two mods shipping e.g. "mixins.json" crash at launch.
        seen = {}
        for slug, (side, entries) in sorted(mods.items()):
            if side not in sides:
                continue
            for mid, _, _, _, mixins in entries:
                for cfg in mixins:
                    if cfg in seen and seen[cfg] != mid:
                        bad += 1
                        print(f"   DUPLICATE mixin config on {label}: {cfg} used by {seen[cfg]} and {mid}")
                    seen.setdefault(cfg, mid)
    print("OK: no missing dependencies or mixin clashes" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
