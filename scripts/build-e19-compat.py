#!/usr/bin/env python3
"""Build a Cobblemon-1.8-compatible copy of the E19 Cobblemon Minimap Icons pack.

    scripts/build-e19-compat.py packs/<pack> [--out DIR]

E19 (Modrinth: e19_cobblemon_minimap_icons) bundles its own copies of many
Cobblemon *resolver* files so that every variant renders with a texture path
Xaero's icon system can key on. Its last release predates Cobblemon 1.8, and
1.8 renamed a number of posers and models, so any E19 resolver that still
references an old name makes that species render as the substitute doll.

This script downloads the E19 zip and the Cobblemon jar pinned in the pack,
finds every E19 resolver whose poser or model name no longer exists in
Cobblemon, and writes a copy of the zip without those files (Cobblemon's own
resolvers then apply for those species; their icons keep working because the
E19 definition also lists Cobblemon's stock texture paths). A NOTICE file
records the modification, as MPL-2.0 requires. Output is reproducible from
the same inputs.
"""
import argparse, hashlib, io, json, os, re, sys, urllib.request, zipfile

def pw(path):
    t = open(path, encoding="utf-8").read()
    g = lambda k: re.search(rf'^{k} = "(.*)"$', t, re.M).group(1)
    return {"url": g("url"), "filename": g("filename"), "hash": g("hash"),
            "hash_format": g("hash-format"), "version": re.search(r'^version = "(.*)"$', t, re.M).group(1)}

def fetch(url, cache):
    os.makedirs(cache, exist_ok=True)
    p = os.path.join(cache, hashlib.sha1(url.encode()).hexdigest() + ".bin")
    if not os.path.exists(p):
        with urllib.request.urlopen(url) as r, open(p, "wb") as f:
            f.write(r.read())
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack")
    ap.add_argument("--out", default="dist")
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/minecraft-modpacks/jars"))
    a = ap.parse_args()
    e19_meta = pw(os.path.join(a.pack, "addons-client", "e19_cobblemon_minimap_icons.pw.toml")) \
        if os.path.exists(os.path.join(a.pack, "addons-client", "e19_cobblemon_minimap_icons.pw.toml")) \
        else pw(os.path.join(a.pack, "addons-client", "e19_cobblemon_minimap_icons.source.toml"))
    cob_meta = pw(os.path.join(a.pack, "mods", "cobblemon.pw.toml"))
    e19_path, cob_path = fetch(e19_meta["url"], a.cache), fetch(cob_meta["url"], a.cache)
    for meta, path in ((e19_meta, e19_path), (cob_meta, cob_path)):
        h = hashlib.new(meta["hash_format"], open(path, "rb").read()).hexdigest()
        if h != meta["hash"]:
            sys.exit(f"hash mismatch for {meta['filename']}")
    e19, cob = zipfile.ZipFile(e19_path), zipfile.ZipFile(cob_path)
    cn = cob.namelist()
    posers = {re.sub(r".*/posers/[^/]+/(.*)\.json$", r"cobblemon:\1", n)
              for n in cn if "/bedrock/pokemon/posers/" in n and n.endswith(".json")}
    def geo_ids(z, names):
        out = set()
        for n in names:
            if "/bedrock/pokemon/models/" in n and n.endswith(".geo.json"):
                try:
                    for g in json.loads(z.read(n).decode("utf-8", "replace"), strict=False)["minecraft:geometry"]:
                        out.add("cobblemon:" + g["description"]["identifier"].replace("geometry.", "") + ".geo")
                except (KeyError, ValueError):
                    pass
        return out
    geos = geo_ids(cob, cn) | geo_ids(e19, e19.namelist())
    drop = {}
    for n in e19.namelist():
        if not (n.startswith("assets/cobblemon/bedrock/pokemon/resolvers/") and n.endswith(".json")):
            continue
        r = json.loads(e19.read(n).decode("utf-8", "replace"), strict=False)
        vs = r.get("variations", [])
        bad = sorted({v["poser"] for v in vs if v.get("poser") and v["poser"] not in posers} |
                     {v["model"] for v in vs if v.get("model") and v["model"] not in geos})
        if bad:
            drop[n] = bad
    os.makedirs(a.out, exist_ok=True)
    base = re.sub(r"\.zip$", "", e19_meta["filename"]).replace(" ", "-")
    out = os.path.join(a.out, f"{base}-cobblemon-{cob_meta['version'] if False else 'compat'}.zip")
    notice = (
        "This is a modified copy of 'E19 - Cobblemon Minimap Icons' (Mozilla Public License 2.0)\n"
        f"https://modrinth.com/resourcepack/e19_cobblemon_minimap_icons, file '{e19_meta['filename']}'.\n\n"
        "Modification: the following Cobblemon resolver files were removed because they reference\n"
        "poser/model names that no longer exist in the Cobblemon version shipped by this modpack;\n"
        "Cobblemon's own resolvers apply for those species instead. No other file was changed.\n"
        "Built by scripts/build-e19-compat.py in https://github.com/jimsimon/minecraft-modpacks.\n\n"
        + "\n".join(f"- {n}  (missing: {', '.join(b)})" for n, b in sorted(drop.items())) + "\n"
    )
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for info in e19.infolist():
            if info.filename in drop:
                continue
            z.writestr(info, e19.read(info.filename))
        z.writestr("NOTICE-MODIFICATIONS.txt", notice)
    json.dump(drop, open(out + ".dropped.json", "w"), indent=1)
    print(f"dropped {len(drop)} resolver files; wrote {out} ({os.path.getsize(out)/1e6:.1f} MB)")
    print("sha512:", hashlib.sha512(open(out, "rb").read()).hexdigest())

if __name__ == "__main__":
    main()
