# 00 — Patch 0.5 Overview: Return of the Ancients & Runes of Aldur

**Sources:** GGG official patch notes (released 21 May 2026), Maxroll patch notes summary, Game8, Mobalytics, poe2wiki.net Version_0.5.0, gamer.org breakdown, official poe2 wiki Fextralife.

## At a glance

| Item | Value |
|---|---|
| Patch version | **0.5.0** |
| Patch name | **Return of the Ancients** |
| Challenge league | **Runes of Aldur** |
| Launch date/time | **29 May 2026, 20:00 UTC** (13:00 PDT, 22:00 CEST/Spain) |
| Final EA league before 1.0? | Yes. GGG has confirmed this is the last major Early Access update before the 1.0 full release later in 2026. No 0.6 is planned. |
| Old league that ended | 0.4.0 "The Last of the Druids" (Fate of the Vaal core systems shipped with it) ended 25 May 2026 22:00 UTC |
| Free weekend? | 29 May 2026 (13:00 PT) through 1 June 2026 (13:00 PT) |
| League variants | Standard, Hardcore, SSF (Solo Self-Found), plus Hardcore SSF; private league versions available |
| Existing characters | Old EA characters remain on Standard. **Free passive tree refund** granted to all old characters due to the magnitude of changes. |

## The five big headline changes

1. **Runes of Aldur league** — A new crafting-encounter mechanic centered on **Ezomyte Remnants**, **Runeshapes**, **Verisium**, **Runic Ward**, and a new NPC named **Farrow**. First league in PoE 2 with a full Challenge system (8 challenges, **Knight of Aldur** armour set as reward).
2. **Endgame overhaul ("Origins of Divinity")** — The Atlas is fully rebuilt around a new central structure called the **Fortress**, a new pinnacle boss called the **Arbiter of Divinity**, three Atlas Masters with ascendancy-style nodes (**Doryani**, **Hilda**, **Jado**), and an expanded **Atlas Passive Tree with ~300 nodes**. Every endgame boss now reachable via dedicated questlines instead of random key drops.
3. **Two new ascendancies** — **Spirit Walker** (Huntress, beast-taming + Azmeri Wisps) and **Martial Artist** (Monk, Hollow Form clones + bell shockwaves).
4. **Big systemic combat rework** — **Leech rework** (one instance per resource, hits >40k damage capped, all instant leech removed), **Energy Shield Recharge nodes nerfed ~50-66%**, **Ancestral Bond** reworked (totems no longer cost nothing to cast), **Pathfinder** Overwhelming Toxicity and Running Assault nerfed, **Chronomancer** and **Gemling Legionnaire** reworked.
5. **Build Planner system** — In-game support for loading **.build JSON files** from third-party guides into Claude-friendly tooltips on the passive tree, skill gems, and gear slots.

## Other notable additions

- **20+ new Lineage gems** and **40+ new Uniques**.
- **21 Kalguuran skill gems** and **8 Kalguuran support gems** (powered by Runic Ward instead of mana).
- **100+ new runes** (15+ Runic Ward Runes, 13 Ancient Ruins for weapon-type bonuses, 13 Mythical early-game runes for level 15+).
- **Runic Alloys** — new crafting currency for adding non-standard modifiers (5 types).
- **Fragment Stash Tab** — new premium tab for Fragments (Breach Splinters, Simulacrums, Audience with the King), Inscribed Ultimatums, Baryas, and Tablets.
- **Voices in PoE2** — first appearance, with rune-related jewel sockets that don't cost passive points.
- **Mageblood** introduced — flask-utility-based effects; verify exact 0.5 function with `poe2_db_lookup term="Mageblood"`.
- **Atziri's Acuity reworked** — now grants 150-200% Armour, 100-150 max Life, 10% Physical Attack Leech as Life, 10% Physical Hit causes Blood Loss + Vaal Pact, and grants Herald of the Royal Queen.
- **Campaign streamlined** — clearer navigation, smoother Act 3, simplified objectives (e.g. auto-solving Waterways pressure pads), reduced monster density in later campaign and Interludes.
- **Free passive tree refund** for all pre-existing characters.

## What was removed / disabled

- **Recombinator** — removed from this league. **Omen of Recombination is deleted on login.**
- **Old Expedition** — disabled; replaced by Grand Expeditions integrated into Runes of Aldur questline.
- **Eastern Atlas cracks** — fixed (Abyss revamp).
- **Gathering Storm + Ice Wall** interaction removed (Gathering Storm now interacts with Tempest Bell instead).
- **Quick Response** passive — removed from tree.

## Time-of-launch warnings (29 May – 31 May 2026)

- **Ladder data is noisy.** `poe2_meta_builds` will give unreliable distribution data until at least 48h into the league.
- **poe2db.tw and poe2wiki.net** need time to fully index new uniques and gems. Brand-new content may not be queryable in the first hours.
- **Trading volume is sparse** on day 1; price-check tools will warn about low volume — trust those warnings.
- **Build guides published before 21 May 2026** are pre-patch-notes and may have stale skill values or rotations.

## Confirmed launch time across regions

| Region | Local time on 29 May 2026 |
|---|---|
| US Pacific | 13:00 PDT |
| US Eastern | 16:00 EDT |
| UTC | 20:00 |
| UK | 21:00 BST |
| Spain (CEST) | 22:00 |
| Central Europe (CEST) | 22:00 |
| Most of Asia | early hours of 30 May local |
