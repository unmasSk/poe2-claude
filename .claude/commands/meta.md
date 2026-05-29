---
description: Current Runes of Aldur ladder meta — distribution, top ascendancies, popular builds
allowed-tools: mcp__poe2__poe2_meta_builds, mcp__poe2-optimizer__compare_to_top_players
---

Show the current 0.5 Runes of Aldur meta. Optional ascendancy filter: $ARGUMENTS

Steps:

1. **Determine the league age**:
   - If today is **29-31 May 2026**: state explicitly that ladder data is **noisy** and may not reflect the final meta. Patch-notes-based expectations are the best available signal.
   - If we're past 48h post-launch: data is more reliable.

2. **Fetch the meta**: call `poe2_meta_builds`.

3. **Filter** by ascendancy if $ARGUMENTS specifies one (e.g. "Spirit Walker", "Martial Artist", "Pathfinder"). Translate from Spanish if needed.

4. **Present**:
   - **Top 5 ascendancies by count** with percentage.
   - **Trending up** (compared to early-week snapshots, if available).
   - **Trending down**.
   - **Notable patch-notes-driven expectations**:
     - Spirit Walker and Martial Artist (new) — expected popular.
     - Warbringer totem (Ancestral Bond rework) — expected strong.
     - Evasion + ES hybrid (Rangers, Mercenaries) — expected to rise.
     - Blood Mage, Cast-on-Crit Comet — expected to drop.
     - Pure ES Lich/Monk/Amazon — weaker, less popular.

5. **For a specific ascendancy** (when $ARGUMENTS gives one):
   - Show the top builds by skill choice (e.g. for Pathfinder: Lightning Arrow / Toxic Rain / Poison melee — distribution).
   - Highlight common gear / unique items.
   - If user wants to compare their character: prompt them to run `/analyze-char <name>`.

6. **Caveats**:
   - **Popular ≠ best.** Top of the ladder is also "what was easy to play to 95+ first."
   - **SSF and Hardcore have separate metas.** Filter if relevant.
   - **The first 48h sample size is unreliable.** State explicitly when applicable.

Respond in the user's language.
