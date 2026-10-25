# Ashley's Minecraft Mod Index

Automation-assisted Minecraft mod ports, upgrades, compatibility fixes and original mods — in one searchable place.

**43 projects · 38 with public JAR downloads · 4 source-only entries · 1 upstream snapshot built locally.**

Index checked: **2026-10-25 (UTC)**. Source dates are the latest commits on the listed maintained branches; release dates are when GitHub published the selected JAR release. A documentation-only commit can change a source date. Dates do not promise ongoing maintenance.

Search this page with your browser's Find, or search this repository on GitHub for a mod name, dependency ID, Minecraft version or loader. Each entry has exact JAR links and version-specific requirements. [Machine-readable catalog](catalog.json) · [Project list](projects.json) · [Refresh instructions](#updating-this-index).

Forks and ports are unofficial. Original authors retain credit and ownership; listing a project here does not mean I created the original mod or its original port. The automation-assisted work includes builds and fixes as well as ports. Botania is an unmodified upstream snapshot build.

## Downloads at a glance

Choose the exact Minecraft version and loader in the JAR details. Required dependency links lead to the project or its releases; select a compatible file there. Optional integrations are listed separately. Embedded mods are marked **included**; they usually need no separate download. Dependencies can have their own dependencies.

| Mod | Minecraft / loader | Source updated (UTC) | JAR release (UTC) | Downloads and requirements |
| --- | --- | --- | --- | --- |
| [Aleki's Nifty Ships](#aleki-s-nifty-ships) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/aleki-ships-1.21.1/commit/85f239510872fc5e4bd61dbe8f9489bb34ac38fb) | [2026-10-25](https://github.com/ashleywr/aleki-ships-1.21.1/releases/tag/ashley-2026.10.25-85f23951) | [JARs + dependencies](#aleki-s-nifty-ships) |
| [Alex's Caves](#alex-s-caves) | NeoForge not declared | [2026-10-25](https://github.com/ashleywr/AlexsCaves-1.21.1/commit/01aca2c4bd1df935260158db8a6040c505e97554) | [2026-10-25](https://github.com/ashleywr/AlexsCaves-1.21.1/releases/tag/ashley-2026.10.25-01aca2c4) | [JARs + dependencies](#alex-s-caves) |
| [Alex's Caves Exemplified](#alex-s-caves-exemplified) | NeoForge [1.21.1,1.22) | [2026-10-25](https://github.com/ashleywr/AlexsCavesExemplified-Neoforge/commit/58e5e58c80718d8acb6fed1c78654d87dfd2837b) | [2026-10-25](https://github.com/ashleywr/AlexsCavesExemplified-Neoforge/releases/tag/ashley-2026.10.25-58e5e58c) | [JARs + dependencies](#alex-s-caves-exemplified) |
| [Automated Materials Index](#automated-materials-index) | Fabric ~1.21.1; Forge [1.20.1, 1.21); NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/AutomatedMaterialsIndex/commit/dc5f40f661fabf696e552385f6b8e42a99793388) | [2026-10-25](https://github.com/ashleywr/AutomatedMaterialsIndex/releases/tag/ashley-2026.10.25-dc5f40f6) | [JARs + dependencies](#automated-materials-index) |
| [AutoMine Testing](#automine-testing) | Fabric ~1.21.1; NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/automine-testing/commit/c0df04e9466fcd0bead128cf442f13fb1ebb0692) | [2026-10-25](https://github.com/ashleywr/automine-testing/releases/tag/ashley-2026.10.25-c0df04e9) | [JARs + dependencies](#automine-testing) |
| [Autoturgy](#autoturgy) | NeoForge [1.21.1,1.21.2) | [2026-10-25](https://github.com/ashleywr/Autoturgy/commit/dd27d5d5632aed2506c1d1f387a3fa4b99ab9042) | [2026-10-25](https://github.com/ashleywr/Autoturgy/releases/tag/ashley-2026.10.25-dd27d5d5) | [JARs + dependencies](#autoturgy) |
| [Botania](#botania) | NeoForge 1.21.1 | [2026-10-23](https://github.com/VazkiiMods/Botania/commit/be17ee934e58444a12eb31824c6e45505b5349d1) | No public build of this work | [Local snapshot](#botania) |
| [CobbleCuisine](#cobblecuisine) | Fabric 1.21.1 | [2026-10-25](https://github.com/ashleywr/CobbleCuisine-1.8/commit/7d8794029252373731787f1af4ad1d14a28ae7af) | [2026-10-25](https://github.com/ashleywr/CobbleCuisine-1.8/releases/tag/ashley-2026.10.25-7d879402) | [JARs + dependencies](#cobblecuisine) |
| [Create Factory Controller](#create-factory-controller) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/create-factory-controller/commit/ed4532d70cced16a1e4d2aa71cf0003aa73d1dd5) | [2026-10-25](https://github.com/ashleywr/create-factory-controller/releases/tag/ashley-2026.10.25-ed4532d7) | [JARs + dependencies](#create-factory-controller) |
| [Create: Little Networks](#create-little-networks) | NeoForge [1.21.1,1.22) | [2026-10-25](https://github.com/ashleywr/create-little-networks/commit/9335ca41da630b77e96fb6cce5f696a739608bb6) | [2026-10-25](https://github.com/ashleywr/create-little-networks/releases/tag/ashley-2026.10.25-9335ca41) | [JARs + dependencies](#create-little-networks) |
| [Create: Love and War](#create-love-and-war) | NeoForge [1.21.1,1.22) | [2026-10-25](https://github.com/ashleywr/create-love-and-war/commit/f8728a527a1126d9e87ec5dacbb3138772c2b6cb) | [2026-10-25](https://github.com/ashleywr/create-love-and-war/releases/tag/ashley-2026.10.25-f8728a52) | [JARs + dependencies](#create-love-and-war) |
| [Hexalia Patchouli Fix](#hexalia-patchouli-fix) | NeoForge [1.21.1,) | [2026-10-25](https://github.com/ashleywr/Hexalia/commit/d0945cb8279c2b305f56f5c055304e68464182cf) | [2026-10-25](https://github.com/ashleywr/Hexalia/releases/tag/ashley-2026.10.25-d0945cb8) | [JARs + dependencies](#hexalia-patchouli-fix) |
| [Iceberg AzureLib Fix](#iceberg-azurelib-fix) | Fabric 1.21.1; Forge [1.21.1]; NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/Iceberg/commit/f782c00b5341da80f07732151522b30330226980) | [2026-10-25](https://github.com/ashleywr/Iceberg/releases/tag/ashley-2026.10.25-f782c00b) | [JARs + dependencies](#iceberg-azurelib-fix) |
| [Kaleidoscope Compat](#kaleidoscope-compat) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/Kaleidoscope-Compat/commit/842598bff2ca4fc0a0b75bc35dec1f8397692f91) | [2026-10-25](https://github.com/ashleywr/Kaleidoscope-Compat/releases/tag/ashley-2026.10.25-842598bf) | [JARs + dependencies](#kaleidoscope-compat) |
| [KeyBind Bundles Fabric](#keybind-bundles-fabric) | Fabric 1.21.1 | [2026-10-25](https://github.com/ashleywr/KeyBindBundlesFabric/commit/93a8c810285816b0f660011f35eb62707aff9845) | [2026-10-25](https://github.com/ashleywr/KeyBindBundlesFabric/releases/tag/ashley-2026.10.25-93a8c810) | [JARs + dependencies](#keybind-bundles-fabric) |
| [League Orchestrator](#league-orchestrator) | Fabric ~1.21.1 | [2026-10-25](https://github.com/ashleywr/league-orchestrator/commit/304be140276fd73d646bc56e8476cd3d7de149fa) | [2026-10-25](https://github.com/ashleywr/league-orchestrator/releases/tag/ashley-2026.10.25-304be140) | [JARs + dependencies](#league-orchestrator) |
| [Little Logistics](#little-logistics) | NeoForge [1.21,1.22) | [2026-10-25](https://github.com/ashleywr/LittleLogistics/commit/f2067cd91ceeb75f910c5e24e4a0b823d79badc5) | No public build of this work | [Source only](#little-logistics) |
| [Magitema Ocean](#magitema-ocean) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/magitema-ocean/commit/81fb9884a4690b7683a03e35e55f5e8a37223cbb) | [2026-10-25](https://github.com/ashleywr/magitema-ocean/releases/tag/ashley-2026.10.25-81fb9884) | [JARs + dependencies](#magitema-ocean) |
| [Musubi](#musubi) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/musubi/commit/da90604c706509ea260f8a185650bb523729627d) | [2026-10-25](https://github.com/ashleywr/musubi/releases/tag/ashley-2026.10.25-da90604c) | [JARs + dependencies](#musubi) |
| [MUtil](#mutil) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/mutil/commit/dfcb2cbb865b758f25f84d4e5d0ab09e822c3527) | [2026-10-25](https://github.com/ashleywr/mutil/releases/tag/ashley-2026.10.25-dfcb2cbb) | [JARs + dependencies](#mutil) |
| [NeoMantle](#neomantle) | NeoForge [1.21.1,1.21.2) | [2026-10-25](https://github.com/ashleywr/neomantle/commit/9f47d2010cc04b79803c212f33166d0c99391b18) | [2026-10-25](https://github.com/ashleywr/neomantle/releases/tag/ashley-2026.10.25-9f47d201) | [JARs + dependencies](#neomantle) |
| [NeoTinkers](#neotinkers) | NeoForge [1.21.1,1.21.2) | [2026-10-25](https://github.com/ashleywr/neotinkers/commit/6246bcab38c472c296d25d6963351c0c7e1cbb8e) | [2026-10-25](https://github.com/ashleywr/neotinkers/releases/tag/ashley-2026.10.25-6246bcab) | [JARs + dependencies](#neotinkers) |
| [NukaTeam Gun Library](#nukateam-gun-library) | NeoForge [1.21.1, 1.21.2) | [2026-10-25](https://github.com/ashleywr/NukaTeamGunLib/commit/165ce0e2455d8c2feb62b8057c2b9c332c8e8c7f) | [2026-10-25](https://github.com/ashleywr/NukaTeamGunLib/releases/tag/ashley-2026.10.25-165ce0e2) | [JARs + dependencies](#nukateam-gun-library) |
| [Pack Log Doctor](#pack-log-doctor) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/pack-log-doctor/commit/371c345e6e2899b4b7af20f9e2de4a7a7541f408) | [2026-10-25](https://github.com/ashleywr/pack-log-doctor/releases/tag/ashley-2026.10.25-371c345e) | [JARs + dependencies](#pack-log-doctor) |
| [Pack Repairs](#pack-repairs) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/pack-repairs/commit/3aba7136d0bad4414fd794635d360eecf7a7c58e) | [2026-10-25](https://github.com/ashleywr/pack-repairs/releases/tag/ashley-2026.10.25-3aba7136) | [JARs + dependencies](#pack-repairs) |
| [Rats](#rats) | NeoForge [1.21.1, 1.21.2) | [2026-10-25](https://github.com/ashleywr/Rats-Fix-Port--1.21.1/commit/1d08198c34bdb31ec60f430167d352e3caa4ccd1) | [2026-10-25](https://github.com/ashleywr/Rats-Fix-Port--1.21.1/releases/tag/ashley-2026.10.25-1d08198c) | [JARs + dependencies](#rats) |
| [Rechanted](#rechanted) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/Rechanted/commit/aa24f976b40d0793158e5a511f94df29e588edd8) | [2026-10-25](https://github.com/ashleywr/Rechanted/releases/tag/ashley-2026.10.25-aa24f976) | [JARs + dependencies](#rechanted) |
| [RoadWeaver](#roadweaver) | Fabric ~1.21.1; NeoForge [1.21.1,1.22) | [2026-10-25](https://github.com/ashleywr/RoadWeaver/commit/8501beac4a9b58661602fcb56116d99607b56f2c) | [2026-10-25](https://github.com/ashleywr/RoadWeaver/releases/tag/ashley-2026.10.25-8501beac) | [JARs + dependencies](#roadweaver) |
| [Scorched Guns EMF Fix](#scorched-guns-emf-fix) | NeoForge [1.21.1,1.22) | [2026-10-25](https://github.com/ashleywr/ScorchedGunsNeoforge/commit/ed8e14876f75084b9bcff370f45c14d1b4567356) | [2026-10-25](https://github.com/ashleywr/ScorchedGunsNeoforge/releases/tag/ashley-2026.10.25-ed8e1487) | [JARs + dependencies](#scorched-guns-emf-fix) |
| [Silent's Gems](#silent-s-gems) | NeoForge [1.21,1.21.2) | [2026-10-25](https://github.com/ashleywr/SilentGems/commit/1a2ebf0ece68e4f8933471d0b1622a4c108d4f18) | [2026-10-25](https://github.com/ashleywr/SilentGems/releases/tag/ashley-2026.10.25-1a2ebf0e) | [JARs + dependencies](#silent-s-gems) |
| [Spice of Life: Classic](#spice-of-life-classic) | Fabric ~1.21.1; NeoForge [1.21.1,) | [2026-10-25](https://github.com/ashleywr/solclassic_v2/commit/a5bcd66196bbcd0e3c2a9164aa219b1c94e41bd7) | [2026-10-25](https://github.com/ashleywr/solclassic_v2/releases/tag/ashley-2026.10.25-a5bcd661) | [JARs + dependencies](#spice-of-life-classic) |
| [TACT](#tact) | NeoForge [1.21.1,1.22) | [2026-10-25](https://github.com/ashleywr/TACT/commit/0d1eb7b7df6a81da6c983d9e0232a295a44ca54a) | [2026-10-25](https://github.com/ashleywr/TACT/releases/tag/ashley-2026.10.25-0d1eb7b7) | [JARs + dependencies](#tact) |
| [Tag Lens](#tag-lens) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/tag-lens/commit/aea1ef78c71f689f2f64e5d8367929029075df4d) | [2026-10-25](https://github.com/ashleywr/tag-lens/releases/tag/ashley-2026.10.25-aea1ef78) | [JARs + dependencies](#tag-lens) |
| [Tetra](#tetra) | NeoForge [1.21.1] | 2026-10-25 | No public build of this work | [Source only](#tetra) |
| [Tetranomicon](#tetranomicon) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/Tetranomicon1.21.1/commit/181771529a79d3b0bdd149e8ed68f971a81534d3) | [2026-10-25](https://github.com/ashleywr/Tetranomicon1.21.1/releases/tag/ashley-2026.10.25-18177152) | [JARs + dependencies](#tetranomicon) |
| [Tetratic Combat Expanded](#tetratic-combat-expanded) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/TetraticCombatExpanded-1.21.1/commit/d955a1d0b1d6a2c5be012a953b8ea08fe3e904ae) | [2026-10-25](https://github.com/ashleywr/TetraticCombatExpanded-1.21.1/releases/tag/ashley-2026.10.25-d955a1d0) | [JARs + dependencies](#tetratic-combat-expanded) |
| [Thaumaturge](#thaumaturge) | NeoForge [1.21.1,1.21.2) | [2026-10-25](https://github.com/ashleywr/Thaumaturge/commit/5d0511487d4de4ba504c8b1e1f63e43090fef47d) | No public build of this work | [Source only](#thaumaturge) |
| [Via Romana](#via-romana) | Fabric >=1.21.1; NeoForge [1.21.1,) | [2026-10-25](https://github.com/ashleywr/Via_Romana/commit/0acad74431ec2d9ec258bbb1a2796b7262020995) | No public build of this work | [Source only](#via-romana) |
| [Xaero Seedmap](#xaero-seedmap) | Fabric 1.21.1 | [2026-10-25](https://github.com/ashleywr/xaero-seedmap/commit/e4b254b6b46298ffe2490e98dcb12618fbd6bac4) | [2026-10-25](https://github.com/ashleywr/xaero-seedmap/releases/tag/ashley-2026.10.25-e4b254b6) | [JARs + dependencies](#xaero-seedmap) |
| [Youkai's Homecoming](#youkai-s-homecoming) | NeoForge [1.21.1,1.22) | [2026-10-25](https://github.com/ashleywr/Youkaishomecoming-1.21.1-Unofficial-Port/commit/42c8771b7f6fbe6b4436cb5a7fed924d1dba9b8c) | [2026-10-25](https://github.com/ashleywr/Youkaishomecoming-1.21.1-Unofficial-Port/releases/tag/ashley-2026.10.25-42c8771b) | [JARs + dependencies](#youkai-s-homecoming) |
| [Zen Amphibia](#zen-amphibia) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/zen-amphibia/commit/04a7e19da2989de47fd206cb847b1bcb15e6bea4) | [2026-10-25](https://github.com/ashleywr/zen-amphibia/releases/tag/ashley-2026.10.25-04a7e19d) | [JARs + dependencies](#zen-amphibia) |
| [Zen Atelier](#zen-atelier) | NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/zen-atelier/commit/0490910e7981ad69847b683ac1cecde93dae9ccb) | [2026-10-25](https://github.com/ashleywr/zen-atelier/releases/tag/ashley-2026.10.25-0490910e) | [JARs + dependencies](#zen-atelier) |
| [Zen Diorama](#zen-diorama) | Fabric ~1.21.1; NeoForge [1.21.1] | [2026-10-25](https://github.com/ashleywr/zen-diorama/commit/4a317b0feead4c8162aec133dc454a3db895f7ff) | [2026-10-25](https://github.com/ashleywr/zen-diorama/releases/tag/ashley-2026.10.25-4a317b0f) | [JARs + dependencies](#zen-diorama) |

## Mod details

Version ranges below are copied from each packaged mod's metadata. For example, `[x,)` means at least x, `[x]` means exactly x, and `[x,y)` means x inclusive through y exclusive. `*` means no version constraint was declared. A broad metadata range is not a claim that every version in it was tested. Java minimums without an explicit declaration are inferred from compiled class-file versions.

<a id="aleki-s-nifty-ships"></a>

### Aleki's Nifty Ships

Sloops, rowboats and sailing vehicles, with local NeoForge 1.21.1 fixes.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/aleki-ships-1.21.1) · [Upstream](https://gitlab.com/alekiponi1/alekiships) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [85f23951](https://github.com/ashleywr/aleki-ships-1.21.1/commit/85f239510872fc5e4bd61dbe8f9489bb34ac38fb).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-85f23951](https://github.com/ashleywr/aleki-ships-1.21.1/releases/tag/ashley-2026.10.25-85f23951).

#### [aleki-s-Nifty-Ships-mc1.21.1-2.0.0.jar](https://github.com/ashleywr/aleki-ships-1.21.1/releases/download/ashley-2026.10.25-85f23951/aleki-s-Nifty-Ships-mc1.21.1-2.0.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `2.0.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.197,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.
- **Optional integrations:** [Just Enough Items (JEI)](https://modrinth.com/mod/jei) `[19.9.1.125,)` (client).

SHA-256: `2eed62564a2bfb9426c2d716b502e875bcba8439b884f3b01406087f6d2e97cf`.

<a id="alex-s-caves"></a>

### Alex's Caves

Maintenance build of the unofficial NeoForge 1.21.1 port, including the pack branch fixes and integrated TACT changes.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/AlexsCaves-1.21.1) · [Upstream](https://github.com/Raguto/AlexsCaves-1.21.1) · License: **GPL-3.0**.

Source updated: **2026-10-25 UTC**; commit [01aca2c4](https://github.com/ashleywr/AlexsCaves-1.21.1/commit/01aca2c4bd1df935260158db8a6040c505e97554).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-01aca2c4](https://github.com/ashleywr/AlexsCaves-1.21.1/releases/tag/ashley-2026.10.25-01aca2c4).

**Note:** This JAR also contains the TACT mod. Do not add a separate copy of TACT alongside this combined build. Minecraft is not declared in this JAR dependency list; this maintained build targets NeoForge 1.21.1.

#### [alexscaves-2.0.10.1.jar](https://github.com/ashleywr/AlexsCaves-1.21.1/releases/download/ashley-2026.10.25-01aca2c4/alexscaves-2.0.10.1.jar)

**NeoForge · Minecraft `not declared` · Mod `2.0.10.1, 1.5.3`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Citadel](https://modrinth.com/mod/citadel) `[2.6.0,)`; [Alex's Caves](#alex-s-caves) `[2.0.0,)` (included).

SHA-256: `34738eca20e6d044743a43661951bdcc005f271632ed3954acc55c8657a3cadb`.

<a id="alex-s-caves-exemplified"></a>

### Alex's Caves Exemplified

NeoForge 1.21.1 port of the Alex's Caves addon.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/AlexsCavesExemplified-Neoforge) · [Upstream](https://github.com/CrimsonCrips/AlexsCavesExemplified) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [58e5e58c](https://github.com/ashleywr/AlexsCavesExemplified-Neoforge/commit/58e5e58c80718d8acb6fed1c78654d87dfd2837b).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-58e5e58c](https://github.com/ashleywr/AlexsCavesExemplified-Neoforge/releases/tag/ashley-2026.10.25-58e5e58c).

#### [alexscavesexemplified-2.2.1+1.21.1.jar](https://github.com/ashleywr/AlexsCavesExemplified-Neoforge/releases/download/ashley-2026.10.25-58e5e58c/alexscavesexemplified-2.2.1%2B1.21.1.jar)

**NeoForge · Minecraft `[1.21.1,1.22)` · Mod `2.2.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Alex's Caves](#alex-s-caves) `[2.0.10,)`; [Citadel](https://modrinth.com/mod/citadel) `[2.7.1,)`.
- **Optional integrations:** [TACT](#tact) `[1.5.3,)`; `alexsmobs` `[2.1.11,)`; [Curios API](https://modrinth.com/mod/curios) `[9.5.1,)`; [Create](https://modrinth.com/mod/create) `[6.0.10,6.1.0)`; [Supplementaries](https://modrinth.com/mod/supplementaries) `[1.21.1-3.9.9,)`; [Patchouli](https://modrinth.com/mod/patchouli) `[1.21.1-93,)`.

SHA-256: `45893f84e95b7090e4f7709b4829b20a92b27bdd84ab9bcfa7d30a4da368ecf5`.

<a id="automated-materials-index"></a>

### Automated Materials Index

Browse materials and their uses across installed Minecraft mods.

**Original mod / tool.** [Source](https://github.com/ashleywr/AutomatedMaterialsIndex) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [dc5f40f6](https://github.com/ashleywr/AutomatedMaterialsIndex/commit/dc5f40f661fabf696e552385f6b8e42a99793388).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-dc5f40f6](https://github.com/ashleywr/AutomatedMaterialsIndex/releases/tag/ashley-2026.10.25-dc5f40f6).

#### [ami-fabric-1.21.1-1.8.7.jar](https://github.com/ashleywr/AutomatedMaterialsIndex/releases/download/ashley-2026.10.25-dc5f40f6/ami-fabric-1.21.1-1.8.7.jar)

**Fabric · Minecraft `~1.21.1` · Mod `1.8.7`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.16.0`; [Minecraft](https://www.minecraft.net/) `~1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`.
- **Optional integrations:** [Just Enough Items (JEI)](https://modrinth.com/mod/jei) `*`; [EMI](https://modrinth.com/mod/emi) `*`; [Roughly Enough Items (REI)](https://modrinth.com/mod/rei) `*`.

SHA-256: `2f4aad7aca5012470f6da188a7c71d7a474237df0df34c976501d21dd839e74b`.

#### [ami-forge-1.20.1-1.8.7.jar](https://github.com/ashleywr/AutomatedMaterialsIndex/releases/download/ashley-2026.10.25-dc5f40f6/ami-forge-1.20.1-1.8.7.jar)

**Forge · Minecraft `[1.20.1, 1.21)` · Mod `1.8.7`**

- **Runtime:** [Forge](https://files.minecraftforge.net/) `[47,)`; [Minecraft](https://www.minecraft.net/) `[1.20.1, 1.21)`; [Java](https://adoptium.net/temurin/releases/) `>=17` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `44c3ef97a5ee3882469d57a66081d102d04db864096237a39b887732ee00a45d`.

#### [ami-neoforge-1.21.1-1.8.7.jar](https://github.com/ashleywr/AutomatedMaterialsIndex/releases/download/ashley-2026.10.25-dc5f40f6/ami-neoforge-1.21.1-1.8.7.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.8.7`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.200,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `b2d56b46ad2f5ee7cd5298f0aad6dcb8ebba575541e1ac6ca1696fd268db6882`.

<a id="automine-testing"></a>

### AutoMine Testing

Development helper for deterministic Minecraft UI and world-generation checks; Fabric and NeoForge 1.21.1.

**Original mod / tool.** [Source](https://github.com/ashleywr/automine-testing) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [c0df04e9](https://github.com/ashleywr/automine-testing/commit/c0df04e9466fcd0bead128cf442f13fb1ebb0692).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-c0df04e9](https://github.com/ashleywr/automine-testing/releases/tag/ashley-2026.10.25-c0df04e9).

#### [automine_testing-fabric-1.21.1-0.1.0.jar](https://github.com/ashleywr/automine-testing/releases/download/ashley-2026.10.25-c0df04e9/automine_testing-fabric-1.21.1-0.1.0.jar)

**Fabric · Minecraft `~1.21.1` · Mod `0.1.0`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.19.3`; [Minecraft](https://www.minecraft.net/) `~1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`.

SHA-256: `7cce96bf1d38c0a7c85db0a37a466065a051059fa0cb5ba6a764570eb523ad6f`.

#### [automine_testing-neoforge-1.21.1-0.1.0.jar](https://github.com/ashleywr/automine-testing/releases/download/ashley-2026.10.25-c0df04e9/automine_testing-neoforge-1.21.1-0.1.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `0.1.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)` (client); [Minecraft](https://www.minecraft.net/) `[1.21.1]` (client); [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `00a88eee129dc9b84506c49cafac41a3686c9c19a4acb9e6e71eb6462e0c28dc`.

<a id="autoturgy"></a>

### Autoturgy

Original magical automation addon for NeoForge 1.21.1 and Thaumaturge.

**Original mod / tool.** [Source](https://github.com/ashleywr/Autoturgy) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [dd27d5d5](https://github.com/ashleywr/Autoturgy/commit/dd27d5d5632aed2506c1d1f387a3fa4b99ab9042).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-dd27d5d5](https://github.com/ashleywr/Autoturgy/releases/tag/ashley-2026.10.25-dd27d5d5).

**Note:** Requires Thaumaturge [1.0.4,). The reviewed Thaumaturge fork is source-only; obtain an authorized build that meets this requirement.

#### [autoturgy-neoforge-1.21.1-1.0.0.jar](https://github.com/ashleywr/Autoturgy/releases/download/ashley-2026.10.25-dd27d5d5/autoturgy-neoforge-1.21.1-1.0.0.jar)

**NeoForge · Minecraft `[1.21.1,1.21.2)` · Mod `1.0.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.262,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.21.2)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Thaumaturge](#thaumaturge) `[1.0.4,)`; [Curios API](https://modrinth.com/mod/curios) `[9.5.1,)`.

SHA-256: `390d3d9486b72605b7a5ed3615873a2664d297dd6a1acb6a63f4720f674a25b6`.

<a id="botania"></a>

### Botania

Official upstream NeoForge 1.21.1 porting-branch snapshot, built locally without source changes.

**Upstream snapshot build.** [Source](https://github.com/VazkiiMods/Botania/tree/1.21.1-porting) · [Upstream](https://github.com/VazkiiMods/Botania) · License: **Botania license; separate component terms apply**.

Source updated: **2026-10-23 UTC**; commit [be17ee93](https://github.com/VazkiiMods/Botania/commit/be17ee934e58444a12eb31824c6e45505b5349d1).

**No public JAR for this work.** 457-SNAPSHOT was built from the official porting branch. No public JAR was published as part of this work; the source link is provided for provenance.

The following requirements describe the local build checked on **2026-10-25**, at commit `be17ee93`.

**Note:** This snapshot requires Patchouli and Curios. Upstream discourages Fast Item Frames and Open Parties and Claims and declares a Productive Bees version conflict; see the JAR metadata below. Full-modpack runtime compatibility was not tested.

#### `botania-neoforge-1.21.1-457-SNAPSHOT.jar` (local build; no download)

**NeoForge · Minecraft `1.21.1` · Mod `457-SNAPSHOT`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.262,)`; [Minecraft](https://www.minecraft.net/) `1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Patchouli](https://modrinth.com/mod/patchouli) `*`; [Curios API](https://modrinth.com/mod/curios) `*`.
- **Optional integrations:** [Botania: Garden of Glass](https://modrinth.com/mod/gardenofglass) `[14,)`; [Ears](https://modrinth.com/mod/ears) `*`.
- **Conflicts / discouraged combinations:** [Fast Item Frames](https://modrinth.com/mod/fast-item-frames) `*` — Breaks Botania's various item frame-based filtering functionalities; [Open Parties and Claims](https://modrinth.com/mod/open-parties-and-claims) `*` — Default claiming behavior breaks basic Botania automation (e.g. mana spreaders); [Productive Bees](https://modrinth.com/mod/productivebees) `[1.21.1-13.8.0,1.21.1-13.13.4)` — These versions cause a crash in Botania due to a ClassCastException. This is fixed in later versions of Productive Bees..

SHA-256: `b5c0790c1c3b68b5678e28b131a6fb40aa888d70df4091b43bae63865e1d5739`.

<a id="cobblecuisine"></a>

### CobbleCuisine

Cobblemon 1.8 integration and maintenance changes for CobbleCuisine.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/CobbleCuisine-1.8) · [Upstream](https://github.com/Fyre520/CobbleCuisine-Java) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [7d879402](https://github.com/ashleywr/CobbleCuisine-1.8/commit/7d8794029252373731787f1af4ad1d14a28ae7af).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-7d879402](https://github.com/ashleywr/CobbleCuisine-1.8/releases/tag/ashley-2026.10.25-7d879402).

**Note:** This maintenance branch targets Cobblemon 1.8. The inherited README still mentions 1.6.1, and fabric.mod.json omits Fabric API and Cobblemon. Both are listed here from the build/source requirements; the exact compatible runtime range is not declared.

#### [cobblecuisine-3.0.0.jar](https://github.com/ashleywr/CobbleCuisine-1.8/releases/download/ashley-2026.10.25-7d879402/cobblecuisine-3.0.0.jar)

**Fabric · Minecraft `1.21.1` · Mod `3.0.0`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.18.0`; [Minecraft](https://www.minecraft.net/) `1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*` (build.gradle / README); [Cobblemon](https://modrinth.com/mod/cobblemon) `1.8.0+1.21.1` (build.gradle compile target; runtime range not declared).
- **Optional integrations:** [Mod Menu](https://modrinth.com/mod/modmenu) `>=11.0.3`.

SHA-256: `435841c2b928478488cf5fbd7fe9ca9a91e1eaff6181d0ff3a0e0773ffec8cd8`.

<a id="create-factory-controller"></a>

### Create Factory Controller

Create factory controllers and shared dashboard panels for NeoForge 1.21.1.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/create-factory-controller) · [Upstream](https://github.com/nbcss/create-factory-controller) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [ed4532d7](https://github.com/ashleywr/create-factory-controller/commit/ed4532d70cced16a1e4d2aa71cf0003aa73d1dd5).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-ed4532d7](https://github.com/ashleywr/create-factory-controller/releases/tag/ashley-2026.10.25-ed4532d7).

#### [createfactorycontroller-1.2.2-neoforge-1.21.1-SNAPSHOT.jar](https://github.com/ashleywr/create-factory-controller/releases/download/ashley-2026.10.25-ed4532d7/createfactorycontroller-1.2.2-neoforge-1.21.1-SNAPSHOT.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.2.2-neoforge-1.21.1-SNAPSHOT`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.227,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Create](https://modrinth.com/mod/create) `[6.0.0,)`.
- **Optional integrations:** `createlogisticscontrol` `[0.0,)` (included) — Provides the Filter Link and its API (the virtual gauge bridge). Bundled inside this mod via Jar-in-Jar; the bridge is guarded by LogisticsControlCompat.isLoaded(), so this mod still runs if it is removed.; [Create: Deployer API](https://modrinth.com/mod/deployer) `[0.1.2,)` — Adds the Stock Keeper tab system and generic order dispatch this mod's Production Orders feature hooks into. When absent, Production Orders are reached via an in-GUI button instead..
- **Embedded mods:** `createhigherlogisticspatch`, `createlogisticscontrol`.

SHA-256: `07096eb0646efee8caaf4367c34fcc8c7ab81d37294d96178ec9ffda18fcb94b`.

<a id="create-little-networks"></a>

### Create: Little Networks

Create package couriers, Little Logistics network charts and mimic panels for NeoForge 1.21.1.

**Original mod / tool.** [Source](https://github.com/ashleywr/create-little-networks) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [9335ca41](https://github.com/ashleywr/create-little-networks/commit/9335ca41da630b77e96fb6cce5f696a739608bb6).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-9335ca41](https://github.com/ashleywr/create-little-networks/releases/tag/ashley-2026.10.25-9335ca41).

**Note:** Requires the matching Little Logistics fork/API. The current Little Logistics build is source-only in this index, so this addon download alone does not provide that dependency.

#### [create_little_networks-mc1.21.1-0.1.0.jar](https://github.com/ashleywr/create-little-networks/releases/download/ashley-2026.10.25-9335ca41/create_little_networks-mc1.21.1-0.1.0.jar)

**NeoForge · Minecraft `[1.21.1,1.22)` · Mod `0.1.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Create](https://modrinth.com/mod/create) `[6.0.10]`; [Little Logistics](#little-logistics) `[1.21.1.1-beta.5,)`.

SHA-256: `ab36558322641a8ab42c7d3e9c30764408077f6fb547e8708b0162ce8d28a8b3`.

<a id="create-love-and-war"></a>

### Create: Love and War

Recovered experimental NeoForge 1.21.1 maintenance port.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/create-love-and-war) · [Upstream](https://www.curseforge.com/minecraft/mc-mods/create-love-war) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [f8728a52](https://github.com/ashleywr/create-love-and-war/commit/f8728a527a1126d9e87ec5dacbb3138772c2b6cb).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-f8728a52](https://github.com/ashleywr/create-love-and-war/releases/tag/ashley-2026.10.25-f8728a52).

#### [createloveandwar-1.0.9.1-1.21.1.jar](https://github.com/ashleywr/create-love-and-war/releases/download/ashley-2026.10.25-f8728a52/createloveandwar-1.0.9.1-1.21.1.jar)

**NeoForge · Minecraft `[1.21.1,1.22)` · Mod `1.0.9.1-1.21.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Create](https://modrinth.com/mod/create) `[6.0.10,)`.

SHA-256: `fe7b583f4210733b434abd61e8fba962012d7cc07330a15b2c894281cd4a5c78`.

<a id="hexalia-patchouli-fix"></a>

### Hexalia Patchouli Fix

Hexalia NeoForge 1.21.1 maintenance build with the local Patchouli book fix.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Hexalia) · [Upstream](https://github.com/AstralyaStudios/Hexalia) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [d0945cb8](https://github.com/ashleywr/Hexalia/commit/d0945cb8279c2b305f56f5c055304e68464182cf).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-d0945cb8](https://github.com/ashleywr/Hexalia/releases/tag/ashley-2026.10.25-d0945cb8).

#### [hexalia-neoforge-1.3.7.jar](https://github.com/ashleywr/Hexalia/releases/download/ashley-2026.10.25-d0945cb8/hexalia-neoforge-1.3.7.jar)

**NeoForge · Minecraft `[1.21.1,)` · Mod `1.3.7`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Architectury API](https://modrinth.com/mod/architectury-api) `[13.0.8,)`; [Geckolib](https://modrinth.com/mod/geckolib) `[4.7.6,)`.
- **Optional integrations:** [Accessories](https://modrinth.com/mod/accessories) `*`; [Patchouli](https://modrinth.com/mod/patchouli) `*`; [EMI](https://modrinth.com/mod/emi) `*`; [Roughly Enough Items (REI)](https://modrinth.com/mod/rei) `*`.

SHA-256: `4f29e0d25fd5d7ba91a029d0364ab94c4a80f37bd82fa04587959dfcde80637f`.

<a id="iceberg-azurelib-fix"></a>

### Iceberg AzureLib Fix

Iceberg 1.21.1 maintenance build with AzureLib armor compatibility fixes.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Iceberg) · [Upstream](https://github.com/AHilyard/Iceberg) · License: **upstream LICENSE**.

Source updated: **2026-10-25 UTC**; commit [f782c00b](https://github.com/ashleywr/Iceberg/commit/f782c00b5341da80f07732151522b30330226980).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-f782c00b](https://github.com/ashleywr/Iceberg/releases/tag/ashley-2026.10.25-f782c00b).

#### [Iceberg-1.21.1-fabric-1.3.2.jar](https://github.com/ashleywr/Iceberg/releases/download/ashley-2026.10.25-f782c00b/Iceberg-1.21.1-fabric-1.3.2.jar)

**Fabric · Minecraft `1.21.1` · Mod `1.3.2`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.16.0`; [Minecraft](https://www.minecraft.net/) `1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`.
- **Optional integrations:** [Sodium](https://modrinth.com/mod/sodium) `>=0.6.0`; [prism](https://modrinth.com/mod/prism) `>=1.0.8`.
- **Conflicts / discouraged combinations:** [Advancement Plaques](https://modrinth.com/mod/advancement-plaques) `<1.6.3`; [Legendary Tooltips](https://modrinth.com/mod/legendary-tooltips) `<1.5.2`; [Equipment Compare](https://modrinth.com/mod/equipment-compare) `<1.3.13`; [Merchant Markers](https://modrinth.com/mod/merchant-markers) `<1.3.4`; [Item Borders](https://modrinth.com/mod/item-borders) `<1.2.4`.

SHA-256: `c7ef77ae4782a72d2c187356399cfca1554bc62a8b4c1b3db61f1e1de958c392`.

#### [Iceberg-1.21.1-forge-1.3.2.jar](https://github.com/ashleywr/Iceberg/releases/download/ashley-2026.10.25-f782c00b/Iceberg-1.21.1-forge-1.3.2.jar)

**Forge · Minecraft `[1.21.1]` · Mod `1.3.2`**

- **Runtime:** [Forge](https://files.minecraftforge.net/) `[51,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.
- **Optional integrations:** [Advancement Plaques](https://modrinth.com/mod/advancement-plaques) `[1.6.3,)`; [Legendary Tooltips](https://modrinth.com/mod/legendary-tooltips) `[1.5.2,)`; [Equipment Compare](https://modrinth.com/mod/equipment-compare) `[1.3.13,)`; [Merchant Markers](https://modrinth.com/mod/merchant-markers) `[1.3.4,)`; [Item Borders](https://modrinth.com/mod/item-borders) `[1.2.4,)`.

SHA-256: `a6e349afb2818d2524ff8b2f1c97286988faee541d262872b89206e55d935d8e`.

#### [Iceberg-1.21.1-neoforge-1.3.2.jar](https://github.com/ashleywr/Iceberg/releases/download/ashley-2026.10.25-f782c00b/Iceberg-1.21.1-neoforge-1.3.2.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.3.2`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.54,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.
- **Optional integrations:** [Advancement Plaques](https://modrinth.com/mod/advancement-plaques) `[1.6.3,)`; [Legendary Tooltips](https://modrinth.com/mod/legendary-tooltips) `[1.5.2,)`; [Equipment Compare](https://modrinth.com/mod/equipment-compare) `[1.3.13,)`; [Merchant Markers](https://modrinth.com/mod/merchant-markers) `[1.3.4,)`; [Item Borders](https://modrinth.com/mod/item-borders) `[1.2.4,)`.

SHA-256: `6bb795814ee5a88ab658b29dbbe2fe1ab0d8fa411f2e7ae16786f0d8c84378ca`.

<a id="kaleidoscope-compat"></a>

### Kaleidoscope Compat

Minecraft 1.21.1 compatibility fork for Kaleidoscope Cookery.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Kaleidoscope-Compat) · [Upstream](https://github.com/SShakusora/Kaleidoscope-Compat) · License: **MIT + CC BY-NC-SA 4.0**.

Source updated: **2026-10-25 UTC**; commit [842598bf](https://github.com/ashleywr/Kaleidoscope-Compat/commit/842598bff2ca4fc0a0b75bc35dec1f8397692f91).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-842598bf](https://github.com/ashleywr/Kaleidoscope-Compat/releases/tag/ashley-2026.10.25-842598bf).

#### [kaleidoscope_compat-2.10.0-neoforge+mc1.21.1.jar](https://github.com/ashleywr/Kaleidoscope-Compat/releases/download/ashley-2026.10.25-842598bf/kaleidoscope_compat-2.10.0-neoforge%2Bmc1.21.1.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `2.10.0-neoforge+mc1.21.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.215,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Kaleidoscope Cookery](https://modrinth.com/mod/kaleidoscope-cookery) `[1.4.0-neoforge+mc1.21.1,)`.
- **Optional integrations:** `kaleidoscope_tavern` `[1.0.0,)`; [Artifacts](https://modrinth.com/mod/artifacts) `*`; [Kaleidoscope Doll](https://modrinth.com/mod/kaleidoscope-doll) `[1.3.0,)`.
- **Embedded mods:** `resourcefulconfig`.

SHA-256: `5a978e06430c1a6bd3e226ffa441e806cdb69f6759bae695afd81ae2377f74d0`.

<a id="keybind-bundles-fabric"></a>

### KeyBind Bundles Fabric

Fabric port of KeyBind Bundles for Minecraft 1.21.1.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/KeyBindBundlesFabric) · [Upstream](https://github.com/MatyrobbrtMods/KeyBindBundles) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [93a8c810](https://github.com/ashleywr/KeyBindBundlesFabric/commit/93a8c810285816b0f660011f35eb62707aff9845).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-93a8c810](https://github.com/ashleywr/KeyBindBundlesFabric/releases/tag/ashley-2026.10.25-93a8c810).

#### [keybindbundles-fabric-1.4.1-fabric.2.jar](https://github.com/ashleywr/KeyBindBundlesFabric/releases/download/ashley-2026.10.25-93a8c810/keybindbundles-fabric-1.4.1-fabric.2.jar)

**Fabric · Minecraft `1.21.1` · Mod `1.4.1-fabric.2`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.19.3`; [Minecraft](https://www.minecraft.net/) `1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`; [Cloth Config API](https://modrinth.com/mod/cloth-config) `*`.
- **Optional integrations:** [Controlling](https://modrinth.com/mod/controlling) `*`; [Mod Menu](https://modrinth.com/mod/modmenu) `*`.

SHA-256: `ebacb5e17f791a4bf1ae767f2f22be0960e4a94a68e35aab847dbaa66fc56737`.

<a id="league-orchestrator"></a>

### League Orchestrator

Deterministic league, town and trainer planning for Fabric 1.21.1.

**Original mod / tool.** [Source](https://github.com/ashleywr/league-orchestrator) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [304be140](https://github.com/ashleywr/league-orchestrator/commit/304be140276fd73d646bc56e8476cd3d7de149fa).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-304be140](https://github.com/ashleywr/league-orchestrator/releases/tag/ashley-2026.10.25-304be140).

#### [league_orchestrator-0.1.0.jar](https://github.com/ashleywr/league-orchestrator/releases/download/ashley-2026.10.25-304be140/league_orchestrator-0.1.0.jar)

**Fabric · Minecraft `~1.21.1` · Mod `0.1.0`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.19.3`; [Minecraft](https://www.minecraft.net/) `~1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`; [Cobblemon](https://modrinth.com/mod/cobblemon) `>=1.7.3`; [Radical Cobblemon Trainers API](https://modrinth.com/mod/rctapi) `>=0.15.2-beta`; [Radical Cobblemon Trainers](https://modrinth.com/mod/rctmod) `>=0.18.1-beta`.
- **Optional integrations:** `region_engine` `>=0.7.0`; `otg` `*`.

SHA-256: `67cec8685a6df3ef705db731bd3d39d326b8c37ce5b32f5efa3dc471e9c9bf12`.

<a id="little-logistics"></a>

### Little Logistics

NeoForge 1.21.1 logistics fork with docking fixes and shared network transport support.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/LittleLogistics/tree/fix/docking-station-pickup) · [Upstream](https://github.com/muradakh/LittleLogistics) · License: **LGPL-3.0 code; artwork and name reserved; Little Contraptions MIT**.

Source updated: **2026-10-25 UTC**; commit [f2067cd9](https://github.com/ashleywr/LittleLogistics/commit/f2067cd91ceeb75f910c5e24e4a0b823d79badc5).

**No public JAR for this work.** README reserves rights in artwork/textures/models and the mod name; public full-JAR redistribution permission is not recorded. Use the upstream project for its author-provided downloads; this entry does not advertise a binary of the current fork build.

The following requirements describe the local build checked on **2026-10-25**, at commit `f2067cd9`.

#### `littlelogistics-mc1.21.1-v1.21.1.1-beta.5.jar` (local build; no download)

**NeoForge · Minecraft `[1.21,1.22)` · Mod `1.21.1.1-beta.5`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Ponder for KubeJS](https://modrinth.com/mod/ponder) `[1.0.82+mc1.21.1,)` (client) (included).
- **Embedded mods:** `flywheel`, `ponder`.

SHA-256: `2722346a5ec9a9fd43adeea8c90505e944d75035b575ba86096eda408394238b`.

#### `littlecontraptions-mc1.21.1-v1.21.1.0.jar` (local build; no download)

**NeoForge · Minecraft `[1.21,1.22)` · Mod `1.21.1.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Little Logistics](#little-logistics) `[1.21.1,)`; [Create](https://modrinth.com/mod/create) `[6.0,)`.

SHA-256: `16aa91ef9cab3c1d4b0d688a602542d17237bc0261139bb00fdba6e203f790fb`.

<a id="magitema-ocean"></a>

### Magitema Ocean

Original expanded-depth ocean Overworld presets for NeoForge 1.21.1.

**Original mod / tool.** [Source](https://github.com/ashleywr/magitema-ocean) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [81fb9884](https://github.com/ashleywr/magitema-ocean/commit/81fb9884a4690b7683a03e35e55f5e8a37223cbb).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-81fb9884](https://github.com/ashleywr/magitema-ocean/releases/tag/ashley-2026.10.25-81fb9884).

#### [magitema-ocean-1.21.1-0.1.0.jar](https://github.com/ashleywr/magitema-ocean/releases/download/ashley-2026.10.25-81fb9884/magitema-ocean-1.21.1-0.1.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `0.1.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.262,21.2)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `ece3cf2bb77cc70643fa13bd85c678d6f73e97e84103fc5ffaa0852f6b3d9c4d`.

<a id="musubi"></a>

### Musubi

Sewing, needles and thread crafting for Minecraft 1.21.1 on NeoForge.

**Original mod / tool.** [Source](https://github.com/ashleywr/musubi) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [da90604c](https://github.com/ashleywr/musubi/commit/da90604c706509ea260f8a185650bb523729627d).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-da90604c](https://github.com/ashleywr/musubi/releases/tag/ashley-2026.10.25-da90604c).

#### [musubi-0.1.0.jar](https://github.com/ashleywr/musubi/releases/download/ashley-2026.10.25-da90604c/musubi-0.1.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `0.1.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.220,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Curios API](https://modrinth.com/mod/curios) `*`.
- **Optional integrations:** [Sophisticated Backpacks](https://modrinth.com/mod/sophisticated-backpacks) `*`; [Just Enough Items (JEI)](https://modrinth.com/mod/jei) `*` (client); [Jade 🔍](https://modrinth.com/mod/jade) `*`.

SHA-256: `a322033f571e1f5e339ca8412bd57cdc1ca290291b56de62038ff5b3cf88f3d3`.

<a id="mutil"></a>

### MUtil

NeoForge 1.21.1 library port used by Tetra addons.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/mutil) · [Upstream](https://github.com/mickelus/mutil) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [dfcb2cbb](https://github.com/ashleywr/mutil/commit/dfcb2cbb865b758f25f84d4e5d0ab09e822c3527).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-dfcb2cbb](https://github.com/ashleywr/mutil/releases/tag/ashley-2026.10.25-dfcb2cbb).

#### [mutil-1.21.1-6.3.1.jar](https://github.com/ashleywr/mutil/releases/download/ashley-2026.10.25-dfcb2cbb/mutil-1.21.1-6.3.1.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `6.3.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `230aae7080ad7ab852587ae90c8a5a57af69879ce1fb45659f0b5a71c732c765`.

<a id="neomantle"></a>

### NeoMantle

NeoForge 1.21.1 port and maintenance fixes for Mantle.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/neomantle) · [Upstream](https://github.com/vancevoj/neomantle) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [9f47d201](https://github.com/ashleywr/neomantle/commit/9f47d2010cc04b79803c212f33166d0c99391b18).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-9f47d201](https://github.com/ashleywr/neomantle/releases/tag/ashley-2026.10.25-9f47d201).

#### [NeoMantle-1.21.1-1.21.0-v1.25.jar](https://github.com/ashleywr/neomantle/releases/download/ashley-2026.10.25-9f47d201/NeoMantle-1.21.1-1.21.0-v1.25.jar)

**NeoForge · Minecraft `[1.21.1,1.21.2)` · Mod `1.21.1-1.21.0-v1.25`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.21.2)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `2f2b92b76f18590609e744661f960ec87dc404a775c6769636784ef619186393`.

<a id="neotinkers"></a>

### NeoTinkers

NeoForge 1.21.1 port and maintenance fixes for Tinkers' Construct.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/neotinkers) · [Upstream](https://github.com/vancevoj/neotinkers) · License: **MIT (code); preserve asset notices**.

Source updated: **2026-10-25 UTC**; commit [6246bcab](https://github.com/ashleywr/neotinkers/commit/6246bcab38c472c296d25d6963351c0c7e1cbb8e).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-6246bcab](https://github.com/ashleywr/neotinkers/releases/tag/ashley-2026.10.25-6246bcab).

#### [NeoTinkers-1.21.1-3.11.2-v1.29.jar](https://github.com/ashleywr/neotinkers/releases/download/ashley-2026.10.25-6246bcab/NeoTinkers-1.21.1-3.11.2-v1.29.jar)

**NeoForge · Minecraft `[1.21.1,1.21.2)` · Mod `1.21.1-3.11.2-v1.29`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.21.2)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [NeoMantle](#neomantle) `[1.21.0,)`.
- **Optional integrations:** [Just Enough Items (JEI)](https://modrinth.com/mod/jei) `[19.21.0,)`; `jsonthings` `[0.13.0,)`.

SHA-256: `8f78d60c8225519328137d5c81816e418169e6bc8f1dda9e97bf4a3bfbc823c9`.

<a id="nukateam-gun-library"></a>

### NukaTeam Gun Library

NeoForge 1.21.1 gun library maintenance fork with resource loading improvements.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/NukaTeamGunLib) · [Upstream](https://github.com/Jetug/NukaTeamGunLib) · License: **LGPL-2.1**.

Source updated: **2026-10-25 UTC**; commit [165ce0e2](https://github.com/ashleywr/NukaTeamGunLib/commit/165ce0e2455d8c2feb62b8057c2b9c332c8e8c7f).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-165ce0e2](https://github.com/ashleywr/NukaTeamGunLib/releases/tag/ashley-2026.10.25-165ce0e2).

#### [ntgl-1.21.1-3.1.8-all.jar](https://github.com/ashleywr/NukaTeamGunLib/releases/download/ashley-2026.10.25-165ce0e2/ntgl-1.21.1-3.1.8-all.jar)

**NeoForge · Minecraft `[1.21.1, 1.21.2)` · Mod `3.1.8`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.228,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1, 1.21.2)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Geckolib](https://modrinth.com/mod/geckolib) `[4.8.2,)`.
- **Embedded mods:** `sablecompanion`.

SHA-256: `6f4a0ea062ad1a5d7e60095ceb88eaf60e672cef41f700238606de337498a0c4`.

<a id="pack-log-doctor"></a>

### Pack Log Doctor

Log grouping and diagnostic reports for NeoForge 1.21.1 modpacks.

**Original mod / tool.** [Source](https://github.com/ashleywr/pack-log-doctor) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [371c345e](https://github.com/ashleywr/pack-log-doctor/commit/371c345e6e2899b4b7af20f9e2de4a7a7541f408).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-371c345e](https://github.com/ashleywr/pack-log-doctor/releases/tag/ashley-2026.10.25-371c345e).

#### [packlogdoctor-neoforge-1.21.1-0.1.0.jar](https://github.com/ashleywr/pack-log-doctor/releases/download/ashley-2026.10.25-371c345e/packlogdoctor-neoforge-1.21.1-0.1.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `0.1.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.200,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `51179ef18d4771e32f7d3c9668d2b0346afbf9603953c978bdddbac884d60f45`.

<a id="pack-repairs"></a>

### Pack Repairs

Optional, targeted compatibility and data repairs for NeoForge 1.21.1 modpacks.

**Original mod / tool.** [Source](https://github.com/ashleywr/pack-repairs) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [3aba7136](https://github.com/ashleywr/pack-repairs/commit/3aba7136d0bad4414fd794635d360eecf7a7c58e).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-3aba7136](https://github.com/ashleywr/pack-repairs/releases/tag/ashley-2026.10.25-3aba7136).

#### [packrepairs-neoforge-1.21.1-0.1.8.jar](https://github.com/ashleywr/pack-repairs/releases/download/ashley-2026.10.25-3aba7136/packrepairs-neoforge-1.21.1-0.1.8.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `0.1.8`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.228,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `af8ceb74addfad049db156bbf2416411e0df48e8c6c6708d2abe43b35bf2e77f`.

<a id="rats"></a>

### Rats

NeoForge 1.21.1 maintenance port with local rat AI, inventory and navigation repairs.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Rats-Fix-Port--1.21.1) · [Upstream](https://github.com/eba67/Rats-Fix-Port--1.21.1) · License: **LGPL-3.0**.

Source updated: **2026-10-25 UTC**; commit [1d08198c](https://github.com/ashleywr/Rats-Fix-Port--1.21.1/commit/1d08198c34bdb31ec60f430167d352e3caa4ccd1).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-1d08198c](https://github.com/ashleywr/Rats-Fix-Port--1.21.1/releases/tag/ashley-2026.10.25-1d08198c).

#### [Rats-Unofficial-Port-Fixed--1.21.1-8.2.3B01.jar](https://github.com/ashleywr/Rats-Fix-Port--1.21.1/releases/download/ashley-2026.10.25-1d08198c/Rats-Unofficial-Port-Fixed--1.21.1-8.2.3B01.jar)

**NeoForge · Minecraft `[1.21.1, 1.21.2)` · Mod `8.2.3B01`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1, 1.21.2)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Citadel](https://modrinth.com/mod/citadel) `[2.7.0,)`.
- **Optional integrations:** [Just Enough Items (JEI)](https://modrinth.com/mod/jei) `[19,)` (client); [Jade 🔍](https://modrinth.com/mod/jade) `[15,)` (client); [Create](https://modrinth.com/mod/create) `*`; `create_aeronautics` `*`; [Carryon](https://modrinth.com/mod/carryon) `*`.

SHA-256: `42cd4b2eb21ca44788fe4be08a8bd2298545308d8d16c9ce70ee782b43a13f3a`.

<a id="rechanted"></a>

### Rechanted

NeoForge 1.21.1 enchanting fork with book operations and recipe viewer integration.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Rechanted) · [Upstream](https://github.com/Rechanted-Team/Rechanted) · License: **MIT (as declared in the original source snapshot)**.

Source updated: **2026-10-25 UTC**; commit [aa24f976](https://github.com/ashleywr/Rechanted/commit/aa24f976b40d0793158e5a511f94df29e588edd8).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-aa24f976](https://github.com/ashleywr/Rechanted/releases/tag/ashley-2026.10.25-aa24f976).

#### [rechanted-1.0.0.jar](https://github.com/ashleywr/Rechanted/releases/download/ashley-2026.10.25-aa24f976/rechanted-1.0.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.0.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.217,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.
- **Optional integrations:** [Just Enough Items (JEI)](https://modrinth.com/mod/jei) `[19.27.0.336,)` (client); [EMI](https://modrinth.com/mod/emi) `[1.1.24,)` (client).

SHA-256: `a2eb43d7d4266e92093bba813c3b2161cae351cbae116485c865bda1409db5d5`.

<a id="roadweaver"></a>

### RoadWeaver

Minecraft 1.21.1 road generation maintenance fork.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/RoadWeaver) · [Upstream](https://github.com/shiroha-233/RoadWeaver) · License: **upstream LICENSE and NOTICE**.

Source updated: **2026-10-25 UTC**; commit [8501beac](https://github.com/ashleywr/RoadWeaver/commit/8501beac4a9b58661602fcb56116d99607b56f2c).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-8501beac](https://github.com/ashleywr/RoadWeaver/releases/tag/ashley-2026.10.25-8501beac).

#### [roadweaver-fabric-2.3.1-1.21.1.jar](https://github.com/ashleywr/RoadWeaver/releases/download/ashley-2026.10.25-8501beac/roadweaver-fabric-2.3.1-1.21.1.jar)

**Fabric · Minecraft `~1.21.1` · Mod `2.3.1-1.21.1`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.16.10`; [Minecraft](https://www.minecraft.net/) `~1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`; [Cloth Config API](https://modrinth.com/mod/cloth-config) `*`.
- **Optional integrations:** `another-mod` `*`; `sereneseasons` `*`; [GlitchCore](https://modrinth.com/mod/glitchcore) `*`.
- **Embedded mods:** `architectury`, `cloth-config`, `org_lwjgl_lwjgl`, `org_lwjgl_lwjgl-opencl`.

SHA-256: `a01110101ef068d870c70cba1d0926a3670a266e56598b0b84d18a46bd7e0866`.

#### [roadweaver-neoforge-2.3.1-1.21.1.jar](https://github.com/ashleywr/RoadWeaver/releases/download/ashley-2026.10.25-8501beac/roadweaver-neoforge-2.3.1-1.21.1.jar)

**NeoForge · Minecraft `[1.21.1,1.22)` · Mod `2.3.1-1.21.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.
- **Embedded mods:** `architectury`, `cloth_config`.

SHA-256: `c5c2ed6e093e92f68cee3ff8598a1ba9fcc023358e53bd5d83515969b1c52f22`.

<a id="scorched-guns-emf-fix"></a>

### Scorched Guns EMF Fix

NeoForge 1.21.1 Scorched Guns fork with Entity Model Features compatibility changes.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/ScorchedGunsNeoforge) · [Upstream](https://github.com/sadeast69/ScorchedGunsNeoforge) · License: **GPL-3.0-or-later**.

Source updated: **2026-10-25 UTC**; commit [ed8e1487](https://github.com/ashleywr/ScorchedGunsNeoforge/commit/ed8e14876f75084b9bcff370f45c14d1b4567356).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-ed8e1487](https://github.com/ashleywr/ScorchedGunsNeoforge/releases/tag/ashley-2026.10.25-ed8e1487).

#### [ScorchedGuns-1.5.jar](https://github.com/ashleywr/ScorchedGunsNeoforge/releases/download/ashley-2026.10.25-ed8e1487/ScorchedGuns-1.5.jar)

**NeoForge · Minecraft `[1.21.1,1.22)` · Mod `1.5`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.228,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Framework](https://github.com/MrCrayfish/Framework/releases) `[0.13.9,)` — Required for Scorched Guns networking and synced data support.; [Curios API](https://modrinth.com/mod/curios) `[9.4.1,)` — Required for Scorched Guns equipment and item integration.; [Geckolib](https://modrinth.com/mod/geckolib) `[4.8.4,)` — Animated guns, armor and entities hard-load GeckoLib classes during startup..
- **Optional integrations:** `controllable` `*` (client) — Enables optional controller integration when installed.; `backpacked` `*` (client) — Enables optional Backpacked integration when installed.; [Just Enough Items (JEI)](https://modrinth.com/mod/jei) `*` (client) — Enables optional recipe viewer integration when installed.; [Create](https://modrinth.com/mod/create) `*` — Enables optional Create integration when installed.; [Farmer's Delight](https://modrinth.com/mod/farmers-delight) `*` — Enables optional Farmer's Delight integration when installed.; [Immersive Engineering](https://modrinth.com/mod/immersiveengineering) `*` — Enables optional Immersive Engineering integration when installed.; [Sculk Horde](https://modrinth.com/mod/sculk-horde) `*` — Enables optional Sculk Horde integration when installed.; [Valkyrien Skies](https://modrinth.com/mod/valkyrien-skies) `*` — Enables optional Valkyrien Skies integration when installed.; [Mekanism](https://modrinth.com/mod/mekanism) `*` — Enables optional Mekanism recipe integration when installed.; [PlayerRevive](https://modrinth.com/mod/playerrevive) `*` — Enables optional PlayerRevive integration when installed..

SHA-256: `68ae5fef55061b7172f281fef677d3857dcbf8c074e6abdf7331ac9c87fd075b`.

<a id="silent-s-gems"></a>

### Silent's Gems

NeoForge 1.21.1 maintenance fork with Curios integration.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/SilentGems) · [Upstream](https://github.com/SilentChaos512/SilentGems) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [1a2ebf0e](https://github.com/ashleywr/SilentGems/commit/1a2ebf0ece68e4f8933471d0b1622a4c108d4f18).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-1a2ebf0e](https://github.com/ashleywr/SilentGems/releases/tag/ashley-2026.10.25-1a2ebf0e).

**Note:** Silent Lib is used directly by the source and the build pins 10.5.1, but the packaged dependency list omits it. Install compatible Silent Lib; its source-declared range is included here. Silent Gear is an optional integration.

#### [silentgems-1.21.1-neoforge-5.1.3.jar](https://github.com/ashleywr/SilentGems/releases/download/ashley-2026.10.25-1a2ebf0e/silentgems-1.21.1-neoforge-5.1.3.jar)

**NeoForge · Minecraft `[1.21,1.21.2)` · Mod `5.1.3`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21,)`; [Minecraft](https://www.minecraft.net/) `[1.21,1.21.2)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Silent Lib](https://modrinth.com/mod/silent-lib) `[10.5,)` (gradle.properties / build.gradle).
- **Optional integrations:** [Silent Gear](https://modrinth.com/mod/silent-gear) `[4.0.25,)`.

SHA-256: `279d54e9cb75d1b306b9b9b8efbe456f3c4d2b97bfe2cda1bfea88ae87f6bacc`.

<a id="spice-of-life-classic"></a>

### Spice of Life: Classic

Minecraft 1.21.1 maintenance fork for Fabric and NeoForge.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/solclassic_v2) · [Upstream](https://github.com/leopoko/solclassic_v2) · License: **upstream LICENSE.txt**.

Source updated: **2026-10-25 UTC**; commit [a5bcd661](https://github.com/ashleywr/solclassic_v2/commit/a5bcd66196bbcd0e3c2a9164aa219b1c94e41bd7).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-a5bcd661](https://github.com/ashleywr/solclassic_v2/releases/tag/ashley-2026.10.25-a5bcd661).

#### [spiceoflife_classic-fabric-2.13+1.21.1.jar](https://github.com/ashleywr/solclassic_v2/releases/download/ashley-2026.10.25-a5bcd661/spiceoflife_classic-fabric-2.13%2B1.21.1.jar)

**Fabric · Minecraft `~1.21.1` · Mod `2.13+1.21.1`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.16.10`; [Minecraft](https://www.minecraft.net/) `~1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Architectury API](https://modrinth.com/mod/architectury-api) `>=13`; [Fabric API](https://modrinth.com/mod/fabric-api) `*`.
- **Embedded mods:** `cardinal-components-base`, `cardinal-components-entity`.

SHA-256: `32b5d043385df9944475a65effd998397272eacab7c5311f7375c11f383208e9`.

#### [spiceoflife_classic-neoforge-2.13+1.21.1.jar](https://github.com/ashleywr/solclassic_v2/releases/download/ashley-2026.10.25-a5bcd661/spiceoflife_classic-neoforge-2.13%2B1.21.1.jar)

**NeoForge · Minecraft `[1.21.1,)` · Mod `2.13+1.21.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Architectury API](https://modrinth.com/mod/architectury-api) `[13,)`.

SHA-256: `a34bfeebb13437fb3457b9029d9af18807d24291e201764217bee66f7db57e54`.

<a id="tact"></a>

### TACT

NeoForge 1.21.1 targeted Alex's Caves compatibility tweaks.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/TACT) · [Upstream](https://github.com/TelepathicGrunt/TACT) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [0d1eb7b7](https://github.com/ashleywr/TACT/commit/0d1eb7b7df6a81da6c983d9e0232a295a44ca54a).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-0d1eb7b7](https://github.com/ashleywr/TACT/releases/tag/ashley-2026.10.25-0d1eb7b7).

**Note:** The Alex's Caves build linked in this index already includes TACT. Use this standalone JAR only with an Alex's Caves build that does not already contain it.

#### [tact-1.5.3+1.21.1.jar](https://github.com/ashleywr/TACT/releases/download/ashley-2026.10.25-0d1eb7b7/tact-1.5.3%2B1.21.1.jar)

**NeoForge · Minecraft `[1.21.1,1.22)` · Mod `1.5.3`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Alex's Caves](#alex-s-caves) `[2.0.0,)`.

SHA-256: `5344e37156a942bfa7a11395df9fa8fb30cfa87e42c0e9fcfa6760f3e447346e`.

<a id="tag-lens"></a>

### Tag Lens

Client-side inventory tag summaries and copying for NeoForge 1.21.1.

**Original mod / tool.** [Source](https://github.com/ashleywr/tag-lens) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [aea1ef78](https://github.com/ashleywr/tag-lens/commit/aea1ef78c71f689f2f64e5d8367929029075df4d).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-aea1ef78](https://github.com/ashleywr/tag-lens/releases/tag/ashley-2026.10.25-aea1ef78).

#### [taglens-neoforge-1.21.1-1.0.0.jar](https://github.com/ashleywr/tag-lens/releases/download/ashley-2026.10.25-aea1ef78/taglens-neoforge-1.21.1-1.0.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.0.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.200,)` (client); [Minecraft](https://www.minecraft.net/) `[1.21.1]` (client); [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `659ada076e4bac92718468f69ca743762589f8852a977363b8cb97c0696c4b78`.

<a id="tetra"></a>

### Tetra

Local NeoForge 1.21.1 port and fixes.

**Unofficial port / maintenance fork.** [Source](https://github.com/mickelus/tetra) · [Upstream](https://github.com/mickelus/tetra) · License: **Restricted: README forbids redistribution**.

Source updated: **2026-10-25 UTC**; commit `db387be7`.

**No public JAR for this work.** Restricted: README forbids redistribution Use the upstream project for its author-provided downloads; this entry does not advertise a binary of the current fork build.

The following requirements describe the local build checked on **2026-10-25**, at commit `db387be7`.

**Note:** The reviewed port is committed locally; there is no published Ashley fork for this entry. The Source link opens upstream.

#### `tetra-1.21.1-6.13.0.jar` (local build; no download)

**NeoForge · Minecraft `[1.21.1]` · Mod `6.13.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [MUtil](#mutil) `[6.3.1,]`.
- **Optional integrations:** [Curios API](https://modrinth.com/mod/curios) `[9.5.1+1.21.1,]`.

SHA-256: `3259c4e73817a90c53b9dcb6c0e5f5a2fabf6a30e470b61814eca26530c9a0da`.

<a id="tetranomicon"></a>

### Tetranomicon

NeoForge 1.21.1 port of the Tetra materials addon.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Tetranomicon1.21.1) · [Upstream](https://github.com/Syrikal/Tetranomicon) · License: **LGPL-3.0; preserve Tetra notices**.

Source updated: **2026-10-25 UTC**; commit [18177152](https://github.com/ashleywr/Tetranomicon1.21.1/commit/181771529a79d3b0bdd149e8ed68f971a81534d3).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-18177152](https://github.com/ashleywr/Tetranomicon1.21.1/releases/tag/ashley-2026.10.25-18177152).

**Note:** Requires a compatible NeoForge 1.21.1 Tetra build. The reviewed Tetra port is source-only here; its older author releases are not a substitute for this required port version.

#### [tetranomicon-1.6.2-1.21.1.jar](https://github.com/ashleywr/Tetranomicon1.21.1/releases/download/ashley-2026.10.25-18177152/tetranomicon-1.6.2-1.21.1.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.6.2-1.21.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Tetra](#tetra) `[6.13.0,)`; [MUtil](#mutil) `[6.3.1,)`.
- **Optional integrations:** `oresabovediamonds` `[10.0.0b,)`.

SHA-256: `2e17d572f8ba348c730b8c189b309f59ec5c4eb74f46138f1a1b0ad1abea0ca4`.

<a id="tetratic-combat-expanded"></a>

### Tetratic Combat Expanded

NeoForge 1.21.1 Tetra and Better Combat integration port.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/TetraticCombatExpanded-1.21.1) · [Upstream](https://github.com/ForestWolf99/TetraticCombatExpanded) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [d955a1d0](https://github.com/ashleywr/TetraticCombatExpanded-1.21.1/commit/d955a1d0b1d6a2c5be012a953b8ea08fe3e904ae).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-d955a1d0](https://github.com/ashleywr/TetraticCombatExpanded-1.21.1/releases/tag/ashley-2026.10.25-d955a1d0).

**Note:** Requires a compatible NeoForge 1.21.1 Tetra build. The reviewed Tetra port is source-only here; its older author releases are not a substitute for this required port version.

#### [tetratic_combat_expanded-2.8.3-1.21.1.jar](https://github.com/ashleywr/TetraticCombatExpanded-1.21.1/releases/download/ashley-2026.10.25-d955a1d0/tetratic_combat_expanded-2.8.3-1.21.1.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `2.8.3-1.21.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.0,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Tetra](#tetra) `[6.13.0,)`; [MUtil](#mutil) `[6.3.1,)`; [Better Combat](https://modrinth.com/mod/better-combat) `[2.4.0,)`.

SHA-256: `58fc83d7bd00fc91380e506aad4210e45f0cde34001104d732f99806f55be23c`.

<a id="thaumaturge"></a>

### Thaumaturge

Local NeoForge 1.21.1 compatibility changes.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Thaumaturge/tree/fix/jei-search-reindex-compat) · [Upstream](https://github.com/Leclowndu93150/Thaumaturge) · License: **Restricted: LICENSE section 3.1 forbids fork releases**.

Source updated: **2026-10-25 UTC**; commit [5d051148](https://github.com/ashleywr/Thaumaturge/commit/5d0511487d4de4ba504c8b1e1f63e43090fef47d).

**No public JAR for this work.** Restricted: LICENSE section 3.1 forbids fork releases Use the upstream project for its author-provided downloads; this entry does not advertise a binary of the current fork build.

The following requirements describe the local build checked on **2026-10-25**, at commit `5d051148`.

#### `thaumaturge-1.21.1-NeoForge-1.0.0.jar` (local build; no download)

**NeoForge · Minecraft `[1.21.1,1.21.2)` · Mod `1.0.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.21.2)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Lithostitched](https://modrinth.com/mod/lithostitched) `[1.8.0,)`; [Curios API](https://modrinth.com/mod/curios) `[9.0.0,)`.
- **Optional integrations:** [Jade 🔍](https://modrinth.com/mod/jade) `[15.0.0,)`; [Dynamic Trees](https://modrinth.com/mod/dynamictrees) `[1.7.2,)`.

SHA-256: `40f28fed26e7add1bfba635f94cc7f737cfb9d06ff31d1763df8988dfb365cbd`.

<a id="via-romana"></a>

### Via Romana

Minecraft 1.21.1 destination icon compatibility fork.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Via_Romana/tree/feature/destination-icon-registry) · [Upstream](https://github.com/RasaNovum/Via_Romana) · License: **Restricted: RSL-1.0 public binary distribution requires permission**.

Source updated: **2026-10-25 UTC**; commit [0acad744](https://github.com/ashleywr/Via_Romana/commit/0acad74431ec2d9ec258bbb1a2796b7262020995).

**No public JAR for this work.** Restricted: RSL-1.0 public binary distribution requires permission Use the upstream project for its author-provided downloads; this entry does not advertise a binary of the current fork build.

The following requirements describe the local build checked on **2026-10-25**, at commit `0acad744`.

#### `via_romana-2.2.3+1.21.1-fabric.jar` (local build; no download)

**Fabric · Minecraft `>=1.21.1` · Mod `2.2.3+1.21.1-fabric`**

- **Runtime:** [Minecraft](https://www.minecraft.net/) `>=1.21.1`; [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.16.7`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `>=0.116.6+1.21.1`; [Moonlight Lib](https://modrinth.com/mod/moonlight) `*`; [MidnightLib](https://modrinth.com/mod/midnightlib) `>=1.9.0`; [Data Anchor](https://modrinth.com/mod/data-anchor) `>=2.0.0.16`.

SHA-256: `4847dc7597219380957f3fbfe45843e42a4c369d979ad7dc56876525fe585359`.

#### `via_romana-2.2.3+1.21.1-neoforge.jar` (local build; no download)

**NeoForge · Minecraft `[1.21.1,)` · Mod `2.2.3+1.21.1-neoforge`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.209,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Moonlight Lib](https://modrinth.com/mod/moonlight) `*`; [MidnightLib](https://modrinth.com/mod/midnightlib) `[1.9.0,)`; [Data Anchor](https://modrinth.com/mod/data-anchor) `[2.0.0.16,)`.

SHA-256: `a5010fb3155e4a8d092fdcff69f408fc4f2dd927ba64ba0334798e520695c6c3`.

<a id="xaero-seedmap"></a>

### Xaero Seedmap

Fabric 1.21.1 seed map maintenance fork.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/xaero-seedmap) · [Upstream](https://github.com/TGGamesYT/xaero-seedmap) · License: **upstream LICENSE.txt and cubiomes LICENSE**.

Source updated: **2026-10-25 UTC**; commit [e4b254b6](https://github.com/ashleywr/xaero-seedmap/commit/e4b254b6b46298ffe2490e98dcb12618fbd6bac4).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-e4b254b6](https://github.com/ashleywr/xaero-seedmap/releases/tag/ashley-2026.10.25-e4b254b6).

#### [xaeroseedmap-26.4.3.jar](https://github.com/ashleywr/xaero-seedmap/releases/download/ashley-2026.10.25-e4b254b6/xaeroseedmap-26.4.3.jar)

**Fabric · Minecraft `1.21.1` · Mod `26.4.3`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.19.3`; [Minecraft](https://www.minecraft.net/) `1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`; [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) `>=1.44.2`.

SHA-256: `9c001953c2a36b9520c322a408c2a681c6a569310a9434c84b7eb436b735e38b`.

<a id="youkai-s-homecoming"></a>

### Youkai's Homecoming

NeoForge 1.21.1 unofficial port with local recipe fixes.

**Unofficial port / maintenance fork.** [Source](https://github.com/ashleywr/Youkaishomecoming-1.21.1-Unofficial-Port) · [Upstream](https://github.com/yinyuze/Youkaishomecoming-1.21.1-Unofficial-Port) · License: **LGPL-2.1**.

Source updated: **2026-10-25 UTC**; commit [42c8771b](https://github.com/ashleywr/Youkaishomecoming-1.21.1-Unofficial-Port/commit/42c8771b7f6fbe6b4436cb5a7fed924d1dba9b8c).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-42c8771b](https://github.com/ashleywr/Youkaishomecoming-1.21.1-Unofficial-Port/releases/tag/ashley-2026.10.25-42c8771b).

#### [youkaishomecoming-4.2.14.jar](https://github.com/ashleywr/Youkaishomecoming-1.21.1-Unofficial-Port/releases/download/ashley-2026.10.25-42c8771b/youkaishomecoming-4.2.14.jar)

**NeoForge · Minecraft `[1.21.1,1.22)` · Mod `4.2.14`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.62,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1,1.22)`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.
- **Optional integrations:** [Curios API](https://modrinth.com/mod/curios) `[9.0.15,)`; [Thirst](https://modrinth.com/mod/thirst) `[1.21.1-2.0.0,)`; [Create](https://modrinth.com/mod/create) `*`.
- **Embedded mods:** `danmaku_api`, `fast_projectile_api`, `geckolib`, `l2core`, `l2damagetracker`, `l2harvester`, `l2itemselector`, `l2library`, `l2menustacker`, `smartbrainlib`.

SHA-256: `d38392e3b555c8a8d0ab350556f48ff0416fc15fbcd03299f7fed87efff739a0`.

<a id="zen-amphibia"></a>

### Zen Amphibia

Amphibians, wetland wildlife and related content for NeoForge 1.21.1.

**Original mod / tool.** [Source](https://github.com/ashleywr/zen-amphibia) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [04a7e19d](https://github.com/ashleywr/zen-amphibia/commit/04a7e19da2989de47fd206cb847b1bcb15e6bea4).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-04a7e19d](https://github.com/ashleywr/zen-amphibia/releases/tag/ashley-2026.10.25-04a7e19d).

**Note:** This build targets Create 6 on NeoForge 1.21.1; the packaged minimum says [0.6.0,), which is broader than that tested build target.

#### [zen_amphibia-1.0.0.jar](https://github.com/ashleywr/zen-amphibia/releases/download/ashley-2026.10.25-04a7e19d/zen_amphibia-1.0.0.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.0.0`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.228,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** [Create](https://modrinth.com/mod/create) `[0.6.0,)`.
- **Optional integrations:** [Zen Atelier](#zen-atelier) `[1.0.0,)`.

SHA-256: `efbcd8b7f01176794961d49ffc21e3b7c4ac75ecdbbdea08e3b8b86a688dadaf`.

<a id="zen-atelier"></a>

### Zen Atelier

A peaceful content mod for Minecraft 1.21.1 on NeoForge.

**Original mod / tool.** [Source](https://github.com/ashleywr/zen-atelier) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [0490910e](https://github.com/ashleywr/zen-atelier/commit/0490910e7981ad69847b683ac1cecde93dae9ccb).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-0490910e](https://github.com/ashleywr/zen-atelier/releases/tag/ashley-2026.10.25-0490910e).

#### [zen_atelier-1.0.1.jar](https://github.com/ashleywr/zen-atelier/releases/download/ashley-2026.10.25-0490910e/zen_atelier-1.0.1.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.0.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.220,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.
- **Optional integrations:** [Minecolonies](https://modrinth.com/mod/minecolonies) `*`; [Curios API](https://modrinth.com/mod/curios) `*`.

SHA-256: `a6106a21bf3064717400f2e97a58587a3702bfc66f449b91a2ca553407568bbc`.

<a id="zen-diorama"></a>

### Zen Diorama

Minecraft 1.21.1 building content for Fabric and NeoForge.

**Original mod / tool.** [Source](https://github.com/ashleywr/zen-diorama) · License: **MIT**.

Source updated: **2026-10-25 UTC**; commit [4a317b0f](https://github.com/ashleywr/zen-diorama/commit/4a317b0feead4c8162aec133dc454a3db895f7ff).

JAR release: **2026-10-25 UTC** · [ashley-2026.10.25-4a317b0f](https://github.com/ashleywr/zen-diorama/releases/tag/ashley-2026.10.25-4a317b0f).

#### [zen_diorama-fabric-1.21.1-1.0.2+1.21.1.jar](https://github.com/ashleywr/zen-diorama/releases/download/ashley-2026.10.25-4a317b0f/zen_diorama-fabric-1.21.1-1.0.2%2B1.21.1.jar)

**Fabric · Minecraft `~1.21.1` · Mod `1.0.2+1.21.1`**

- **Runtime:** [Fabric Loader](https://fabricmc.net/use/installer/) `>=0.17.2`; [Minecraft](https://www.minecraft.net/) `~1.21.1`; [Java](https://adoptium.net/temurin/releases/) `>=21`.
- **Required mods:** [Fabric API](https://modrinth.com/mod/fabric-api) `*`.

SHA-256: `b540459689b174ef562f3b1fa729c96a73a102be23cbcf91523fd6d262b0e466`.

#### [zen_diorama-neoforge-1.21.1-1.0.2+1.21.1.jar](https://github.com/ashleywr/zen-diorama/releases/download/ashley-2026.10.25-4a317b0f/zen_diorama-neoforge-1.21.1-1.0.2%2B1.21.1.jar)

**NeoForge · Minecraft `[1.21.1]` · Mod `1.0.2+1.21.1`**

- **Runtime:** [NeoForge](https://neoforged.net/) `[21.1.220,)`; [Minecraft](https://www.minecraft.net/) `[1.21.1]`; [Java](https://adoptium.net/temurin/releases/) `>=21` (runtime class-file version).
- **Required mods:** none declared beyond the runtime above.

SHA-256: `a011a77aa46cd866971419a784250549a4c1908f7e67b2a1fa8a75b2d1a96aa7`.

## Availability, credit and licenses

All builds are offered **AS IS**, without warranty. Updates and support are best effort. Successful builds and archive checks do not establish compatibility with every modpack or gameplay path.

Original mods remain under their original licenses and any separate asset terms. Ashley's original code is MIT where identified. The MIT license in this repository covers the index text and refresh code only; it does not relicense any listed mod. Follow each project's license and credits. Source-only entries intentionally have no link to an older fork binary that could be mistaken for the current build.

This index covers the reviewed workspace projects. Koyo projects and the removed Controlify, Immersive Portals and Vanilla Vehicles projects are omitted. Other historical GitHub forks are not evidence of an automation-assisted port and are not automatically advertised here.

## Updating this index

Run the **Refresh mod index** workflow from this repository's Actions tab, or use Python 3.11+ locally:

```sh
python scripts/refresh.py
```

The refresh checks each curated source branch, selects its newest published GitHub release containing runtime JARs, verifies available GitHub SHA-256 digests, and reads dependencies from those JARs. Prereleases are labelled. It refreshes README.md and catalog.json together. GitHub API access uses GH_TOKEN when set, or the authenticated gh CLI locally. No background schedule is configured.

To add a project, edit projects.json. Source-only/local snapshot requirements are recorded snapshots and need a new reviewed build to change; the refresh never publishes their JARs. Source-derived dependency corrections include their evidence. Dependency URLs live in dependencies.json. Review the generated diff before committing a local refresh.
