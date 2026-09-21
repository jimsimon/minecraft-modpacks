# cobblemon

Server-oriented Cobblemon pack: Cobblemon 1.8.x on Fabric / Minecraft 1.21.1
with gyms, raids, Mega/Dynamax/Z-Move/Tera battles, a Safari, an economy, a GTS, homes/teleports, starter kits, Pokémon fusion, Pokédex rewards and voice chat, with LuckPerms for permissions. Built to replace the
Cobblemon Delta client pack, which does not ship any of its server features.

| Mod | Why |
|---|---|
| Cobblemon | The Pokémon mod. 1.8 includes native TMs. |
| Rad Gyms | Gym leaders and badges; built against Cobblemon 1.8.1 |
| Cobblemon: Mega Showdown | Mega Evolution, Dynamax/Gigantamax, Z-Moves, Terastallization; datapack-driven (pulls oωo, Accessories, Architectury) |
| Cobblemon Raid Dens | Raid dens with raid bosses incl. Mega/Dynamax raids; 0.12 adds Cobblemon 1.8 support (pulls GeckoLib) |
| CobbleSafari | Safari Zone dimension; 0.3.5 is the Cobblemon 1.8 build |
| Cobblemon Economy | PokéDollars and shops |
| Cobblemon GTS | Global trade station (server-side only) |
| Starter Kit | Configurable gear/items for players on first join (`config/starterkit/`); pulls Collective |
| Cobblemon Poke Fusion | Fuse two or three Pokémon into a configured result; author states Cobblemon 1.7+/1.8 support |
| Cobblemon: Pokedex Rewards | Rewards for Pokédex milestones via chest menus; built for Cobblemon 1.8.1 (server-side only) |
| Fabric Essentials | `/home`, `/sethome`, `/tpa`, `/tpaccept`, `/back`, `/warp`, `/spawn` and more (server-side only) |
| LuckPerms | Permission groups; controls who may use admin commands (server-side only) |
| Simple Voice Chat | Proximity voice; each server needs its own UDP port in the 24454-24470 range |
| Lithium | Server performance |
| Fabric API, Fabric Language Kotlin | Libraries |

Requires Java 21 (Cobblemon refuses 25).

## Permissions

LuckPerms stores its data in `config/luckperms/` (H2 by default; part of the
server backup). Bootstrap from the Crafty console, where commands run as the
server operator:

```text
lp creategroup admin
lp group admin permission set fabric-essentials.* true
lp group admin permission set cobblemon.* true
lp group admin permission set minecraft.command.* true
lp user <player> parent set admin
```

Fabric Essentials permission nodes follow `fabric-essentials.command.<name>`;
the full list is in its
[COMMANDS.md](https://github.com/DrexHD/FabricEssentials/blob/main/COMMANDS.md).
Player commands such as home and tpa are allowed for everyone by default, so
the `default` group needs nothing unless you want to restrict them.

## Not included, and why

- **Area Zero / Paradox Pokémon**: Cobblemon Delta's Area Zero is custom to
  their server; no Modrinth mod provides it.
- **Habitats**: the only match is `cobblemon-pokopia-habitats` (Pokopia-style
  habitat spawning), a tiny experimental mod from August 2026 with no
  Cobblemon 1.8 statement. Revisit if it matures.
- **"Incursions"**: no Modrinth mod by that name; `cobblemon-shadowedhearts`
  (Shadow Pokémon, Colosseum/XD style) is the closest and is still on
  Cobblemon 1.7 (February 2026).

- **Fusion alternative**: `starlightfusion` adds bespoke fusion models
  (Sylvevoir and friends) rather than configurable recipes; it is
  client-required and its Cobblemon 1.8 status is unstated.
- **Dex rewards alternatives**: `dex-rewards` and `cobblemon-simpledexrewards`
  target Cobblemon 1.6 and have not been updated since early 2025.

## Candidates not yet included

These have not published a Cobblemon 1.8 build as of September 2026. Re-check
before adding:

- `cobblemon-wonder-trade` (last release March 2026)
- `simpletms-tms-and-trs-for-cobblemon` (last release December 2025; likely
  redundant now that Cobblemon 1.8 has TMs)
