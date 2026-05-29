# 08 — Endgame: Atlas, Fortress, Masters, Pinnacle Bosses

The endgame is completely rebuilt in 0.5. This is arguably the largest single change in the patch. Codename: **Origins of Divinity**.

---

## Core architecture: Fortress

After clearing your **first Tower map**, a giant **Fortress** erupts on your Atlas.

### Inside the Fortress

- Areas inside the Fortress walls are **enhanced in special ways**:
  - Some areas turn all Rare enemies into **Essences**.
  - Some pack all monsters into **Strongboxes**.
  - **Azmeri Spirits** that do not disappear over time.
  - Many other map modifiers depending on the section.
- The **center of the Fortress** houses the new pinnacle boss.

### Atlas Passive Tree

- **Fully rebuilt.** ~300 nodes total.
- **Every node is allocatable** — no more single optimized path forced. Multi-choice branching nodes shape your playstyle.
- Points are earned exclusively from **map bosses inside the Fortress**.
- **No respec model** — you allocate freely.
- **Hybrid nodes:** certain combinations let **multiple boss encounters appear in the same map simultaneously** (demonstrated with Act 1 + Act 2 bosses in the same map at the reveal).

### Atlas Tree completion shortcut

- **Defeating the Arbiter of Divinity 4 times** auto-completes large Fortress sections.
- After **4 Arbiter kills**, the entire Fortress becomes completable.
- This is a "power-user shortcut" — casual players take the scenic route, killing map bosses one by one.

---

## The new Pinnacle Boss: Arbiter of Divinity

- **Replaces the Arbiter of Ash** as the new top-tier pinnacle encounter.
- Located in the **center of the Fortress**.
- **Reached via questline**, not random key drops — keys are at fixed locations inside the Fortress.
- Required for the most valuable Atlas content.

[Inference] Specific mechanics, drops, and difficulty modes are documented in the wiki — query `poe2_wiki_search "Arbiter of Divinity"`.

### Other pinnacle bosses still reachable

Old pinnacle bosses (Arbiter of Ash, etc.) remain accessible via secondary questlines. Each major League mechanic has its own pinnacle now.

---

## Masters of the Atlas (Ascendancy-style endgame)

Three new NPCs — **Doryani**, **Hilda**, **Jado** — act as **endgame ascendancies**. Each provides their own talent tree.

### Structure

- **Each Master has 12 talent nodes**, arranged in **4 rows of 3 choices**.
- You earn points by completing the **quest chain for each Master.**
- **Allocate up to 4 nodes per Master** (one per row).
- **You can swap which Master is active between maps for free**, but **only one Master is active at a time**.

### Doryani

- Specialization: **science / experimentation** focused.
- Storyline unlock: **Doryani's Science** quest, accessible via the **Corrupted Nexus**.
- Aimed at lore enthusiasts and players who want a science/discovery flavor.

### Hilda

- Specialization: **monster-hunting** focused.
- Storyline pace: aggressive map content.

### Jado

- Specialization: **layout manipulation, in-map mechanics, treasure**.
- Notable example node: massively improves chance of **Strongboxes being Unique Rarity** + more Rare Chests.
- Another row-1 node: **map bosses drop an additional Unique item.**
- The "Spycraft" tree of Jado is the most relevant for **Unique-acquisition challenges**.

---

## Reworked League Mechanics in the endgame

All existing leagues received endgame reworks. Each has its own **storyline + new pinnacle boss + dedicated Atlas region.**

### Delirium — "Hare and Raven"

- Hub area: **Withered Willow**.
- New mechanics: **Grand Mirrors**, **Trial of Madness**, **7-wave Simulacrum**.
- Delirium has a dedicated passive tree.
- Lore: the essence of Delirium ("Strange Voice") has been amplified; the ancient Trickster god has broken free, infecting Wraeclast with madness.

### Breach — "Waking the Dreamer"

- New mechanics: **Genesis Tree**, **Monastery of the Keepers**, **Vruun**, **Tul & Esh**, **Xesht**.
- Classic Breach mechanics overhauled — players now fight **Hive Spawns from an alien realm.**
- Lore tie: NPC **Eilyth** and the **Flamekeepers faction** are losing fighters trying to hold back the onslaught.

### Ritual — "Rite of the Nameless"

- Hub: **Caer Tarth**.
- New mechanics: **King in the Mists**, **5-map Rite chain**.
- New unique: **Sylvan's Effigy** (Stoic Sceptre, key Spirit Walker item, **drops from Ritual pinnacle**).

### Expedition — "Runes of Aldur"

- Now structurally part of the **Runes of Aldur** league questline (see `docs/07-runes-of-aldur.md`).
- Old Expedition is disabled.
- Hub: **Ruins of Kingsmarch** (SE Atlas).
- New mechanic: **Verisium meteor**, **Grand Expeditions** across the Uncharted Seas.

### Abyss

- **Now core content.**
- Eastern Atlas cracks fixed.
- Abyss has its own revamped passive tree.
- **Kulemak's Invitation** is auto-allocated.

### Fate of the Vaal

- **Now core content** in both campaign and endgame (carried over from 0.4 expansion, integrated into 0.5 endgame).
- NPC: **Lira Vaal** (NE Atlas).
- Mechanics: **Beacons**, **Tier 4 rooms**, **Atziri** encounters.

---

## Map content additions

- **30 new Map Areas** added throughout the Atlas.
- **15 new pinnacle-level bosses** (4 of them are top-tier).
- Each new league mechanic has its own pinnacle.

---

## Storylines (5 confirmed)

1. **Fortress — Origins of Divinity** (Arbiter of Divinity, grants Atlas passive tree).
2. **Delirium — Hare and Raven** (Withered Willow, Trial of Madness).
3. **Breach — Waking the Dreamer** (Genesis Tree, Hive Spawns).
4. **Ritual — Rite of the Nameless** (Caer Tarth, King in the Mists).
5. **Masters of the Atlas — endgame ascendancy-style progression** (Doryani, Hilda, Jado).

Plus **two core revamps** (Abyss as core, Fate of the Vaal as core campaign + endgame).

---

## Pre-launch advice

- **Don't skip storylines.** Each storyline gates significant Atlas Passive Points.
- **Pick a Master early.** Jado is the most universally useful (Unique acquisition + map layout boost) for league start; Hilda for monster-hunting-focused builds; Doryani for lore + late-game flex.
- **Build for the Fortress.** Inside-Fortress maps are harder than outside-Fortress maps; you need defenses tuned for the modifiers.
- **Hybrid nodes are powerful.** Multi-boss-per-map hybrid nodes are extremely valuable for boss-rush farming.

---

## Verification

For any specific pinnacle boss mechanic, Master node, or Atlas mechanic:

```
poe2_wiki_search "Fortress"
poe2_wiki_search "Masters of the Atlas"
poe2_wiki_search "Arbiter of Divinity"
poe2_db_lookup term="Origins_of_Divinity"
poe2_wiki_page "Atlas Passive Tree 0.5"
```

Don't rely on pre-launch tier lists for specific node values; they often quote reveal-stream numbers that have since changed.
