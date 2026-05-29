---
description: Full character analysis via poe.ninja — defenses, gear, gems, passive tree, ladder comparison
allowed-tools: mcp__poe2-optimizer__analyze_character, mcp__poe2-optimizer__import_poe_ninja_url, mcp__poe2-optimizer__compare_to_top_players, mcp__poe2-optimizer__analyze_passive_tree, mcp__poe2__poe2_meta_builds
---

Analyze the Path of Exile 2 character: $ARGUMENTS

Steps:
1. If the user passed a poe.ninja URL, use `import_poe_ninja_url`. Otherwise treat the argument as a character name and ask for the account name and league if not in the conversation context. The league is **Runes of Aldur** unless the user specifies otherwise.
2. Once the character is loaded, perform `analyze_character` for the full snapshot.
3. Call `analyze_passive_tree` for tree-specific insights.
4. Call `compare_to_top_players` to benchmark against the top ladder of the same ascendancy.
5. Summarize in this order:
   - **Ascendancy + main skill**: what they're playing.
   - **Defensive state**: Life, ES, Runic Ward (if applicable), resistances (flag any <75%).
   - **Offensive snapshot**: estimated DPS, key damage sources.
   - **Key passive tree investments**: notable nodes allocated.
   - **Identified weaknesses**: 1-3 highest-priority issues (e.g. "no Runic Ward", "32% chaos res", "leech without backup sustain in post-0.5 leech rework").
   - **Comparison to top ladder**: what the top players of this ascendancy are doing differently.
   - **Recommended next 1-3 upgrades**, with rough budget estimates if applicable.

Critical caveats to apply:
- Remind the user that HivemindOverlord's local data is pre-0.5. For 0.5-specific content (Spirit Walker / Martial Artist nodes, Runic Ward, new runes/mods), supplement with `poe2_db_lookup` and the wiki.
- If we're in the first 48h of league (29-31 May 2026), state explicitly that ladder data may not be representative yet.

Respond in the language the user asked in. Translate game terms with `docs/11-glossary-es-en.md` if needed.
