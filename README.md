# minecraft-modpacks

Modpacks for the family Minecraft servers, defined as [packwiz](https://packwiz.infra.link/)
manifests and published as Modrinth `.mrpack` files through GitHub Releases.

Each pack lives in its own directory under `packs/`:

```text
packs/
└── cobblemon/            # one directory per pack
    ├── pack.toml         # name, version, Minecraft + loader versions
    ├── index.toml        # hashes of every file below (maintained by packwiz)
    ├── mods/*.pw.toml    # one file per mod: Modrinth project, pinned version, hash
    ├── config/…          # optional: any other file here ships as a pack override
    └── .packwizignore    # files to keep out of the pack (README.md, notes)
```

The `.mrpack` itself is only a few KB: it lists download URLs and hashes, and
the server or launcher fetches the jars from Modrinth's CDN.

## Releasing a pack

1. Bump `version` in `packs/<pack>/pack.toml` and merge to `main`.
2. Tag the merge commit `<pack>-v<version>` and push the tag:

   ```sh
   git tag cobblemon-v1.0.0 && git push origin cobblemon-v1.0.0
   ```

3. The **Release modpack** workflow exports the pack and creates a GitHub Release
   with the asset. The tag's version must match `pack.toml`, or the job fails.

The asset URL is stable and is what servers and players use:

```text
https://github.com/jimsimon/minecraft-modpacks/releases/download/<pack>-v<version>/<pack>-<version>.mrpack
```

Always cut a new version rather than re-uploading an asset. Servers detect an
update by the URL changing.

## Using a release

**Server (Crafty, via `start-server.sh` from simonfamily.io):**

```text
bash /crafty/mc-image-helper/start-server.sh --modrinth https://github.com/jimsimon/minecraft-modpacks/releases/download/cobblemon-v1.0.0/cobblemon-1.0.0.mrpack --java /usr/lib/jvm/java-21-openjdk-amd64/bin/java --jvm "-Xms2G -Xmx6G"
```

To update the server, change the URL to the new release and restart.

**Players:** in the Modrinth App choose *Create instance → From file* (or paste
the URL) and import the same `.mrpack`.

## Editing a pack

You need `packwiz`. With Go installed, `scripts/install-packwiz.sh` builds the
pinned commit CI uses; otherwise download a CI build from
<https://nightly.link/packwiz/packwiz/workflows/go/main> and put it on your `PATH`.

Work inside the pack directory:

```sh
cd packs/cobblemon
packwiz modrinth add <slug>       # add a mod (resolves dependencies, pins the version)
packwiz remove <name>             # remove one
packwiz update --all              # move every mod to its newest compatible version
packwiz update cobblemon          # or just one
packwiz refresh                   # after editing files by hand (config/, side = "…")
```

Then bump `version` in `pack.toml`, commit and open a pull request. The
**Validate packs** workflow refreshes the index, fails if it is out of sync
with the committed files, and exports every pack as a build artifact.

`scripts/export.sh <pack>` does the same check locally and writes
`dist/<pack>-<version>.mrpack`.

## Adding a new pack

```sh
mkdir packs/<name> && cd packs/<name>
packwiz init --name "<Display name>" --author "Jim Simon" --version 0.1.0 \
  --mc-version 1.21.1 --modloader fabric --fabric-latest
packwiz modrinth add …
```

Pack directory names are lowercase letters, digits and hyphens; they become the
first half of the release tag.

Every file in the pack directory that is not a `.pw.toml` ships as an override,
so list docs and anything else that must not reach the server in
`.packwizignore` (gitignore syntax).
