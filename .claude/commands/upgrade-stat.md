---
description: Find the cheapest way to gain a target stat on a character (e.g. crit chance, life, fire res)
allowed-tools: mcp__poe2-optimizer__analyze_character, mcp__poe2-optimizer__import_poe_ninja_url, mcp__poe2-optimizer__search_mods_by_stat, mcp__poe2-optimizer__get_uniques_by_base_name, mcp__poe2-optimizer__analyze_passive_tree, mcp__poe2__poe2_db_lookup, mcp__poe2__poe2_item_price
---

Find the cheapest upgrade to gain more of the stat: $ARGUMENTS

Steps:

1. **Parse the input**:
   - The user should pass a stat and ideally a character + budget.
   - Examples: "crit chance for Joserules in Runes of Aldur", "fire resistance, budget 5 ex", "life on my Spirit Walker".
   - **Translate Spanish stat names** to English (`docs/11-glossary-es-en.md`): "crítico" → "critical strike chance", "vida" → "life", "resistencia fuego" → "fire resistance", etc.
   - If essential info is missing (character or stat), **ask once**.

2. **Snapshot the current state** of the character:
   - `import_poe_ninja_url` or `analyze_character`.
   - Identify the **current value of the target stat** and which slots/sources contribute to it.

3. **Identify candidate sources** for the stat:
   - **Gear mods**: `search_mods_by_stat` with the stat keyword.
     - Caveat: HivemindOverlord's data is pre-0.5. For 0.5-new mods, cross-check with `poe2_db_lookup`.
   - **Passive tree**: `analyze_passive_tree` for unallocated nodes that grant the stat.
   - **Uniques**: search for uniques that grant the stat (`get_uniques_by_base_name` for the relevant slot, or scan unique list).
   - **Runes (0.5)**: there are 100+ new runes in Runes of Aldur — some grant stats via Augment Sockets.
   - **Runic Ward Runes** specifically for defensive stats.

4. **Estimate cost** for each candidate:
   - For gear mods: target a specific base + mod combo, use `poe2_item_price` to estimate the going rate.
   - For uniques: `poe2_item_price` for the unique itself.
   - For passive tree: cost is in **passive points** (and respec costs if needed).
   - Flag low-volume items with a price warning.

5. **Rank options** by **cost per unit of stat gained**:
   - "+50 crit chance for 2 ex via amulet upgrade" → ratio: 25 crit per ex.
   - "+30 crit chance for 1 passive point" → free if you have unspent points.
   - Cheapest wins, unless the cheapest option is locked (no available points, etc.).

6. **Present 2-4 options** ranked:
   - **Best ratio**: cheapest upgrade per unit.
   - **High budget**: best upgrade if money is no object.
   - **Free / passive tree**: any reallocations that gain the stat without spending currency.
   - **Trade-offs**: if any option requires giving up another stat.

7. **0.5 caveats to surface when relevant**:
   - For defensive stats (life, ES, armour, evasion): mention Runic Ward as an option (apply Verisium Runeforging to armour).
   - For resistance: mention Fluxes (resistance swap without rerolling).
   - For ES Recharge: warn that the nerf makes this stat much less impactful than it was.
   - For crit on Martial Artist Monk: Hollow Resonance triggers on Crit, so crit chance is multiplicatively valuable.

Respond in the user's language. Be concise — 3-5 lines per option, not an essay per item.
