# cobblemon

Server-oriented Cobblemon pack: Cobblemon 1.8.x on Fabric / Minecraft 1.21.1
with gyms, raids, Mega/Dynamax/Z-Move/Tera battles, a Safari, Ultra Wormhole events, an economy, a GTS, NPC trainers, breeding, homes/teleports/waystones, starter kits, plushies and furniture, Pokémon fusion, Pokédex rewards and voice chat, with LuckPerms for permissions. Built to replace the
Cobblemon Delta client pack, which does not ship any of its server features.

| Mod | Why |
|---|---|
| Cobblemon | The Pokémon mod. 1.8 includes native TMs. |
| Rad Gyms | Gym leaders and badges; built against Cobblemon 1.8.1 |
| Cobblemon: Mega Showdown | Mega Evolution, Dynamax/Gigantamax, Z-Moves, Terastallization; datapack-driven (pulls oωo, Accessories, Architectury) |
| Cobblemon Ultra Wormholes | Timed Ultra Beast invasion events with a shared boss HP pool; `config/ultra_wormholes.json`, `/wormhole start\|stop\|status\|reload` (server-side only; optional client visuals) |
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
| Terralith | Overworld biome overhaul using vanilla blocks; Cobblemon's spawn data targets its biomes. Same worldgen Cobbleverse uses |
| Tectonic | Larger-scale terrain: taller mountains, deeper valleys and caves; layers on top of Terralith |
| Radical Cobblemon Trainers | 1,500+ NPC trainers roaming the world (Radical Red, Unbound, BDSP); requires Cobblemon 1.8 since 0.19.0 (pulls RCT API, Forge Config API Port) |
| Cobbreeding | Pokémon breeding through pastures; 2.3.0 is the Cobblemon 1.8 build (pulls Cloth Config) |
| Cobblemon Capture XP | Team gains XP on capture; 1.8.1 build (pulls Tim Core; server-side only) |
| Cobblemon: SafePastures | Pastured Pokémon cannot be killed or stolen; 1.8 build (server-side only) |
| Cobblemon Spawn Notification | Chat announcements for legendary/shiny/rare spawns; 1.8.1 build (server-side only) |
| Hidden Ability Spawns | Configurable chance of wild hidden abilities; 1.8 build (server-side only) |
| Cobblemon PokeNav | PokéNav device for tracking spawns and party info |
| Waystones | Teleport network via waystone blocks (pulls Balm) |
| Repurposed Structures | More vanilla-structure variants (pulls MidnightLib; server-side only) |
| MobsBeGone | Blocks vanilla mob spawns; blocklist in `config/mobsbegone-blacklist.json` (copied from Cobbleverse: all hostile mobs and vanilla animals, villagers kept) (server-side only) |
| Global Packs | Loads the bundled `datapacks/` on every world; `datapacks/no-hunger` keeps the hunger bar full (server-side only) |
| Pokeblocks | Placeable Pokémon dolls/plushies (pulls GeckoLib) |
| CobbleFurnies | Cobblemon-themed furniture: Poké Ball chairs, PC-style desks and more (pulls Resourceful Lib) |
| Handcrafted | General furniture: tables, chairs, benches, shelves, kitchen blocks |
| Nava's ZA Megas | All Pokémon Legends: Z-A Megas on top of Mega Showdown; 1.8 build |
| Cobble Café Forms | Café ReMix outfits/costumes for Pokémon; 1.8 build |
| Cobblemon Smartphone | In-game phone for party/PC/Pokédex shortcuts; 1.8 patch |
| Cobblemon Counter | KO/capture streaks per species (shiny chaining); 1.8.1 build |
| Cobblemon PlayerXP | Players earn Minecraft XP from battles |
| Catch Indicator | Unseen/seen/caught icon on wild Pokémon; requires 1.8 (client-side only) |
| Catch Rate Display | Live catch percentage per ball in battle; 1.8.1 (client-side only) |
| Cobblethemes | Battle music themes incl. per-Pokémon tracks (client-side only) |
| Ok Zoomer | Zoom key (default C) with scroll-to-adjust; chosen over Zoomify, which crashes on Steam Deck (client-side only) |
| Xaero's Minimap | Corner minimap with waypoints and entity radar (client-side only) |
| Xaero's World Map | Full-screen explored-world map, shares waypoints with the minimap (client-side only) |
| Controlify | Controller / Steam Deck support with in-game button prompts and a virtual cursor for menus (pulls YACL). Also installed server-side so clients get analogue stick movement without a whitelist prompt and Bedrock-style reach-around placement; policies in `config/controlify/server.json` |
| Lithium | Server performance |
| Fabric API, Fabric Language Kotlin | Libraries |

Requires Java 21 (Cobblemon refuses 25).

**Worldgen note.** Terralith and Tectonic only affect chunks generated after
they are installed. A world created before pack 1.6.0 keeps vanilla terrain in
explored chunks with hard seams at the edge of new generation; regenerate the
world (delete `world/` while the server is stopped) for a clean result.

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

- **Fight or Flight Reborn** (wild Pokémon attack outside battle): works on
  1.8 per its author but deliberately left out.
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
