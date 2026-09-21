# cobblemon

Server-oriented Cobblemon pack: Cobblemon 1.8.x on Fabric / Minecraft 1.21.1
with gyms, raids, Mega/Dynamax/Z-Move/Tera battles, a Safari, Ultra Wormhole events, an economy, a GTS, NPC trainers, breeding, homes/teleports/waystones, starter kits, plushies and furniture, Pokémon fusion, Pokédex rewards and voice chat, with LuckPerms for permissions. Built to replace the
Cobblemon Delta client pack, which does not ship any of its server features.

| Mod | Why |
|---|---|
| Cobblemon | The Pokémon mod. 1.8 includes native TMs. |
| Rad Gyms | Gym leaders and badges; built against Cobblemon 1.8.1 |
| Cobblemon: Mega Showdown | Mega Evolution, Dynamax/Gigantamax, Z-Moves, Terastallization; datapack-driven (pulls oωo, Accessories, Architectury) |
| Wild Battle API | Library required by Ultra Wormholes but undeclared on Modrinth (server-side only) |
| Cobblemon Ultra Wormholes | Timed Ultra Beast invasion events with a shared boss HP pool; `config/ultra_wormholes.json`, `/wormhole start\|stop\|status\|reload` (server-side only; optional client visuals) |
| Cobblemon Raid Dens | Raid dens with raid bosses incl. Mega/Dynamax raids; 0.12 adds Cobblemon 1.8 support (pulls GeckoLib) |
| CobbleSafari | Safari Zone dimension; 0.3.5 is the Cobblemon 1.8 build |
| Cobblemon Economy | PokéDollars and shops |
| Cobblemon GTS | Global trade station (server-side only) |
| Starter Kit | First-join kit defined in `config/starterkit/kits/Default.txt`: 64 Poké Balls, 10 each Quick/Great/Ultra Balls, 64 torches, Rotom Phone (CobbleSafari), Poké Rod, PokéNav, Pokédex, diamond pickaxe and axe, netherite-tier Traveler's Backpack; pulls Collective |
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
| AllTheMons x Mega Showdown (addon) | Community merge of "missing Pokémon" addons, v4.0 built for Cobblemon 1.8 and Mega Showdown. A combined data+resource pack in `addons/`; Global Packs loads it on the server and auto-enables it on clients |
| Global Packs | Loads the bundled `datapacks/` and `addons/` on every world and client; `datapacks/no-hunger` keeps the hunger bar full and `datapacks/keep-inventory` sets `keepInventory` and `playersSleepingPercentage 1` (one sleeper skips the night) on world load (server-side only) |
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
| Ok Zoomer | Zoom key (default C) with scroll-to-adjust; chosen over Zoomify, which crashes on Steam Deck (client-side only) |
| Xaero's Minimap | Corner minimap with waypoints and entity radar (client-side only) |
| Xaero's World Map | Full-screen explored-world map, shares waypoints with the minimap (client-side only) |
| E19 Cobblemon Minimap Icons (resource pack) | Pokémon head icons on Xaero's minimap/world map instead of generic dots. Lives in `addons-client/`, which Global Packs force-enables on clients, so no manual step (client-side only) |
| Default Options | Ships default keybinds (`config/defaultoptions/keybindings.txt`) and first-run configs (`config/defaultoptions/extra/`) without overwriting player changes on updates (client-side only) |
| Controlify | Controller / Steam Deck support with in-game button prompts and a virtual cursor for menus (pulls YACL). Also installed server-side so clients get analogue stick movement without a whitelist prompt and Bedrock-style reach-around placement; policies in `config/controlify/server.json` |
| Sodium, ImmediatelyFast, Entity Culling, ModernFix, Dynamic FPS | Client performance; the set the Steam Deck needs (client-side only) |
| FerriteCore | Lower memory use for block states (both sides) |
| Iris + Complementary Reimagined / Unbound | Shader support with both Complementary variants in `shaderpacks/`; off until a player picks one under Video Settings → Shader Packs, K toggles (client-side only) |
| Neruina | Removes entities that throw ticking exceptions instead of crashing the server (server-side only; pulls Configurable) |
| Krypton | Network stack optimisation (server-side only) |
| spark | Profiler: `/spark tps`, `/spark profiler` (server-side only) |
| Chunky | Chunk pre-generation, e.g. `/chunky radius 2000` then `/chunky start` (server-side only) |
| Ping Wheel | Hold the ping key and click to drop a marker everyone sees |
| Emotecraft | Emote wheel; server side relays emotes between players |
| Better Third Person | Free-look third-person camera (client-side only) |
| Mod Menu | In-game mod list with config screens (client-side only; pulls Text Placeholder API) |
| Jade + Cobblemon Integrations | Hover info for blocks and entities; Integrations adds Pokémon name/level, apricorn growth, healer charge, berry bushes, and a Pokémon teleport-to-Waystone option (1.8 build) |
| EMI | Recipe viewer, R on any item (client-side only) |
| Traveler's Backpack | Wearable backpacks (pulls Cloth Config and its own lib) |
| Tom's Simple Storage | Storage terminal that searches every linked chest |
| 3D Skin Layers, Mouse Tweaks, Not Enough Crashes | Client QoL: layered skins, drag-stacking in inventories, return to title screen on client crash (client-side only) |
| Falling Leaves, Visuality | Ambience particles (client-side only) |
| Distant Horizons | Level-of-detail terrain far beyond render distance. Installed on the server too, so it generates and streams LODs and clients only render; toggle on the client via its settings. Server data lives in `world/data/DistantHorizons.sqlite`. Tune with `/dh config` (generation rate limit, max request distance, real-time updates); `/dh pregen` pre-builds LODs, but not while Chunky is running |
| Lithium | Server performance |
| Fabric API, Fabric Language Kotlin | Libraries |

Requires Java 21 (Cobblemon refuses 25).

## Client requirements

| | PC | Steam Deck |
|---|---|---|
| Max memory (`-Xmx`) | 8 GB | 6 GB |
| Shaders | optional | leave off, or Complementary Reimagined on Low |
| Distant Horizons | on | on, lower its render distance if frames drop |

The `.mrpack` format cannot carry launcher settings, so set memory yourself:

- **Prism Launcher**: Settings → Java → *Maximum memory allocation* sets the
  default for new instances; per instance it is Edit → Settings → Java →
  Memory. Launchers default to 4 GB, which is too little for this pack.
- **Modrinth App**: Settings → Java and memory, or per instance under the
  instance's Options.


**Worldgen note.** Terralith and Tectonic only affect chunks generated after
they are installed. A world created before pack 1.6.0 keeps vanilla terrain in
explored chunks with hard seams at the edge of new generation; regenerate the
world (delete `world/` while the server is stopped) for a clean result.

## Default keybinds

Several mods ship the same default keys (B was Emotecraft, Traveler's Backpack,
Tom's Storage and Xaero's new-waypoint at once). `config/defaultoptions/keybindings.txt`
resolves the clashes; Default Options applies it as the *default*, so players can
still rebind. Cobblemon's debug portrait keys are unbound.

| Key | Action |
|---|---|
| M / R / N / O | Cobblemon summary / throw Pokémon / PokéNavigator / hide party |
| V, G, . | Voice chat menu, group, mute mic (push-to-talk: Caps Lock) |
| K | Iris shader toggle |
| P, ; | Smartphone open, scanner |
| C | Zoom |
| X | Emotes |
| B | Backpack |
| Y | Storage terminal |
| H | Accessories |
| I, U, Z, J, `,`, keypad + | Xaero minimap settings, waypoints, enlarge, world map, new waypoint, instant waypoint |
| F6 / F7 | Raid accept / deny |
| Mouse 5 | Ping |

The minimap radar defaults come from `config/defaultoptions/extra/config/`
(entity radar on, every category displayed with icons, so Pokémon show up).

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
- **Cobblethemes** (battle music): removed in 1.21.0. Its mixin config is named
  plain `mixins.json`, the same as PlayerXP's, and Fabric Loader refuses to
  launch a client with two mods sharing that name. It is an unmaintained
  pre-1.8 beta, so PlayerXP stays. `scripts/check-deps.py` now flags this.
- **Fusion alternative**: `starlightfusion` adds bespoke fusion models
  (Sylvevoir and friends) rather than configurable recipes; it is
  client-required and its Cobblemon 1.8 status is unstated.
- **Dex rewards alternatives**: `dex-rewards` and `cobblemon-simpledexrewards`
  target Cobblemon 1.6 and have not been updated since early 2025.

## Checking dependencies before a release

Modrinth metadata is not always right: Athena is listed client-only but
CobbleFurnies needs it on the server, and Ultra Wormholes does not declare Wild
Battle API at all. Before tagging, download every jar and compare each mod's
`fabric.mod.json` `depends` (including nested jars) against the mod ids present
on each side. `scripts/check-deps.py` does this for a pack directory, and also rejects duplicate mixin config names.

## Candidates not yet included

These have not published a Cobblemon 1.8 build as of September 2026. Re-check
before adding:

- `cobblemon-wonder-trade` (last release March 2026)
- `simpletms-tms-and-trs-for-cobblemon` (last release December 2025; likely
  redundant now that Cobblemon 1.8 has TMs)
