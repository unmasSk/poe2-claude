---
description: Validate a build for common issues, gem combo problems, and 0.5-specific traps
allowed-tools: mcp__poe2-optimizer__validate_support_combination, mcp__poe2-optimizer__validate_build_constraints, mcp__poe2-optimizer__analyze_character, mcp__poe2-optimizer__import_poe_ninja_url, mcp__poe2-optimizer__compare_to_top_players, mcp__poe2__poe2_meta_builds, mcp__poe2-optimizer__inspect_support_gem, mcp__poe2-optimizer__inspect_spell_gem
---

Validate the build: $ARGUMENTS

If $ARGUMENTS contains a character name or poe.ninja URL, use it. Otherwise ask the user.

Steps:

1. **Load the character**: `import_poe_ninja_url` or `analyze_character`. League is **Runes of Aldur** unless specified.

2. **Identify the main skill and support gems** from the gear loadout.

3. **Validate support gem combinations**: call `validate_support_combination` for each linked skill setup. Flag any invalid combos (e.g. supports that don't apply to the skill type, or two supports of the same kind).

4. **Check 0.5-specific traps**:
   - **Leech sources**: how many leech instances does the build have? After 0.5, only one applies. List them and identify which is dominant.
   - **Energy Shield Recharge dependency**: if the build leans on ES Recharge passives, flag the 50-66% nerf and suggest hybrid Runic Ward.
   - **Ancestral Bond + Arch Mage**: if both are allocated, the combo is dead. Recommend dropping one.
   - **Pure ES**: if no Life pool and no Runic Ward, the build is much more glass-cannon than pre-0.5.
   - **Removed nodes**: if the build's PoB shows Quick Response allocated, that node is gone.
   - **Pre-0.5 unique combos**: Atziri's Acuity, Sierran Inheritance, Apep's Supremacy, Blackflame all changed — flag if used.

5. **Validate resistances**:
   - All four (Fire, Cold, Lightning, Chaos) at 75% cap? Flag any deficits.

6. **Validate Spirit reservation**:
   - With Ancestral Bond now reserving 75 Spirit per totem, check if the user has enough Spirit for their auras + totems + companions.

7. **Compare to top ladder**:
   - `compare_to_top_players` for the same ascendancy.
   - Highlight 1-2 things top players do differently that the user might want to adopt.

8. **Output**:
   - **Verdict**: ✅ healthy / ⚠️ has issues / ❌ broken.
   - **Top 3 issues to fix**, ranked by impact.
   - **What top players do differently** (1-2 points).
   - **Estimated upgrade cost** for the top issue, if applicable.

**Caveats**:
- HivemindOverlord's local data is pre-0.5; for any **0.5-introduced gem/passive/unique**, cross-check with `poe2_db_lookup` or the wiki.
- In the first 48h of league, `compare_to_top_players` is noisy.

Respond in the user's language.
