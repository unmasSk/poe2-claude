# 03 — Workflows: Common Question Patterns

Each workflow is a sequence of tool calls + reasoning steps. Use these as templates, adapt to the user's exact question. **Always state what you're going to do before making >2 tool calls in a row** so the user can interrupt if needed.

---

## Workflow A — "How do I get more X stat on my character?"

Example: "How do I reach more crit chance on my Spirit Walker?"

Steps:

1. **Identify the character.** Ask for character name + account + league, or take it from the user's `CLAUDE.local.md` if available. Or accept a poe.ninja URL.
2. **Snapshot the current state.** `analyze_character` or `import_poe_ninja_url`.
3. **Identify sources of the target stat.** 
   - For mods on gear: `search_mods_by_stat` with the stat keyword (e.g. "critical strike chance"). **Caveat: this uses pre-0.5 local data; for new 0.5 mods, also query `poe2_db_lookup` with the mod name.**
   - For passive tree: `analyze_passive_tree` to see unallocated nodes that grant the stat.
   - For uniques: `get_uniques_by_base_name` or search by mod keyword.
4. **Cost estimation.** For each candidate upgrade, `poe2_item_price` or `analyze_price_history`. Flag low-volume items.
5. **Present options ranked.** "Cheapest upgrade: X for ~Y exalts gives +Z stat. Mid-tier: ... High-end: ..."

**Stop and ask before deep diving** if the character is doing something unusual (off-meta build, SSF, hardcore). The trade-economy answers may not apply.

---

## Workflow B — "Is this build good for league start?"

Steps:

1. Ask which ascendancy and primary skill.
2. `poe2_meta_builds` to check ladder distribution **— skip or caveat if first 48h of league.**
3. `compare_to_top_players` if the user has a character on the ladder.
4. `validate_support_combination` on the gem links the user has chosen.
5. Cross-check against 0.5 changes that hit common builds:
   - Leech rework: any build that relied on stacking multiple leech sources is weaker.
   - ES Recharge nerf: pure ES builds are weaker; hybrid ES+Evasion benefits.
   - Ancestral Bond change: totem builds still strong but mana cost is back; Arch Mage + totem combo is dead.
   - Pathfinder Overwhelming Toxicity nerf: poison Pathfinder weaker but still viable.
6. State strengths, weaknesses, expected pain points. **Flag everything build-meta-related as `[Inference]` until ladder data stabilizes.**

---

## Workflow C — "Price check this item"

Steps:

1. `poe2_currency_check` if it's a currency.
2. `poe2_item_price` if it's a tradeable unique/category item.
3. If the result is low-volume (<100 listings/day), **add a volume warning**.
4. For deep market analysis (volatility, trend, signals), use `poe2scout/analyze_price_history`.
5. If the item returns empty from all sources, it might be:
   - Brand new (early league, not yet indexed) → say so.
   - Very low volume (not enough listings) → suggest the user check the trade site directly.
   - Not tradeable (corrupted, etc.) → say so.

---

## Workflow D — "Explain how X mechanic works"

Examples: "How does Runic Ward work?", "How does Leech work in 0.5?"

Steps:

1. `poe2_wiki_search` with the mechanic name.
2. Pick the most relevant result from the snippets.
3. `poe2_wiki_page` with the exact title.
4. For exact stat formulas, supplement with `poe2_db_lookup` if applicable.
5. If the mechanic is brand-new in 0.5 and the wiki is sparse, **fall back to `docs/04-game-mechanics-0.5.md`** in this repo for the curated summary.

**Do not** explain mechanics from memory if they are 0.5-introduced. **Do not** apply PoE 1 mechanic knowledge to PoE 2.

---

## Workflow E — "What ascendancy should I play?"

Steps:

1. Ask what the user enjoys: melee, ranged, summons, spell-caster, hybrid.
2. Ask if they're playing trade or SSF.
3. Ask if they care about meta or want to play off-meta.
4. **`poe2_meta_builds`** for current distribution (caveat first 48h).
5. Cross-reference with 0.5 winners/losers:
   - **Winners (per pre-launch coverage):** Evasion+ES hybrid builds (Rangers, Mercenaries), the new Spirit Walker (companion archetype), the new Martial Artist (Hollow Form clones), totem Warbringer (Ancestral Bond rework removed totem charge requirement), critical Monk (Martial Artist bell synergy).
   - **Losers:** Blood Mage leech-immortality (leech rework hits hard), pure ES stacking (ES Recharge cut 50-66%), poison Pathfinder (Overwhelming Toxicity 50% less duration), Cast-on-Crit Comet (automation nerf), Arch Mage + totem (Ancestral Bond no longer makes totems free to cast).
6. Suggest 2-3 candidates that match the user's preferences. **Flag every recommendation as `[Inference]`** based on patch notes, not on live ladder data.

---

## Workflow F — "Help me identify what's wrong with my build"

Steps:

1. `analyze_character` or `import_poe_ninja_url`.
2. Look for common failure modes:
   - **Resistances** capped at 75% (lightning, fire, cold, chaos)? If not, this is the first problem.
   - **Effective HP** too low for the content tier (e.g. <5k for endgame mapping).
   - **Sustain**: with the 0.5 leech rework, builds need life leech + flask + regen working together. Single-instance leech caps make stacking pointless.
   - **Defenses**: Runic Ward via Verisium Runeforging is a major new defensive layer (see `docs/04-game-mechanics-0.5.md`). If the user has none, suggest the upgrade.
   - **Gem links**: `validate_support_combination` on the main skill setup.
   - **Spirit reservation**: with 0.5's Ancestral Bond change, totems reserve 75 spirit each — a common cause of over-reservation.
3. Present 1-3 highest-priority fixes. Don't dump a 15-item checklist; pick the worst offenders.

---

## Workflow G — "I want to import a PoB code / share my build / work with `.build` files"

The 0.5 patch added an in-game **Build Planner** that reads `.build` JSON files from `Documents/My Games/Path of Exile 2/BuildPlanner/`. The pack has full support for this format. **Full schema, markup, and ID sources are in `docs/13-build-file-format.md`.** Use the `/build-file` slash command as the entry point.

### G.1 — Import from a Path of Building 2 code/URL

1. Decide how the user wants the output:
   - **They want a `.build` file for the in-game planner** → direct them to https://github.com/NickWeder99/DotBuildExporter (Windows binary, MIT) or https://poe2buildplanner.com/ (browser-based). Don't reimplement.
   - **They want to import into HivemindOverlord for analysis** → use `import_pob` with the code or URL.
2. If converting to `.build`, remind them the output goes in their `BuildPlanner/` directory and the in-game planner will pick it up on next client restart.
3. Validate against 0.5 changes: ask whether the build was published before 21 May 2026 (patch notes day). If yes, flag that values may be stale.

### G.2 — Read / validate a `.build` file

`/build-file read <path>` — parse the file, summarize: name, author, ascendancy, passives count, skills with their supports, gear hints. Markup-stripped.

`/build-file validate <path>` — schema validation per `docs/13-build-file-format.md` §9. Optionally with `--check-ids` to fetch `repoe-fork/poe2` and verify passive IDs are real.

Common validation failures to flag:
- **Missing `name`** (required).
- **Skill ID doesn't match `Metadata/Items/Gems/SkillGem...`** — typo or wrong format.
- **`inventory_id` for charm/flask slots** — not supported in v1.
- **Meta gem in `skills[].id`** — not supported in v1.

### G.3 — Translate a `.build` file (ES ↔ EN)

`/build-file translate <path> <es|en>` — translates only the prose. **IDs, `inventory_id` values, and `unique_name` values are never modified** because the game resolves them to the player's locale automatically.

Translatable fields (full list):
- root `name`
- root `author` (ask the user first; usually a handle)
- root `description`
- every `additional_text` at any nesting depth

When translating game terms inside prose, use the canonical mappings in `docs/11-glossary-es-en.md`. Preserve every markup tag and `\n` byte.

Output: a new file named `<original-stem>.<lang>.build`. Never overwrite the source.

### G.4 — Generate a starter template

`/build-file template <ascendancy>` — produces a minimal valid `.build` for the given ascendancy. Useful for the user starting a new build from scratch.

For 0.5 new ascendancies (Spirit Walker, Martial Artist), warn that ascendancy and node IDs are `[Inference]` and should be verified against `repoe-fork/poe2`.

### G.5 — Annotate an existing element

`/build-file annotate <path> <element-id> <text>` — set or replace the `additional_text` on a passive, skill, support, or inventory slot identified by its `id` / `inventory_id`.

If the element doesn't exist, offer to add it. Confirm before writing. Always show a diff.

### G.6 — Merge two builds

`/build-file merge <path-a> <path-b>` — combine two files (e.g. a campaign build + a leveling notes build). Refuses to merge across different ascendancies unless the user overrides. Conflict resolution is interactive.

### G.7 — Working with the new in-game Build Planner

The Build Planner only **reads** files. It doesn't edit them. The flow is always:

1. Edit the `.build` file outside the game (via Claude Code, or any text editor).
2. Place / replace in `Documents/My Games/Path of Exile 2/BuildPlanner/`.
3. The File Watcher picks up the change; the client renders it on the next session open or sometimes immediately.
4. The user sees the build hints overlaid on the Passive Tree, Skill Gem panel, and gear slots.

### G.8 — Important format limits (don't propose what won't work)

- **No charm or flask slots.** `inventory_id` values for those aren't published. Suggest noting the charm setup in `description` instead.
- **No meta gems.** Filter them or warn the user.
- **No "skill A triggers skill B"** as a structural relationship. Express it in `additional_text` as a hint.
- **No DPS / EHP math.** Send the user to Path of Building 2 for that.

---

## Workflow H — "What's a good upgrade for slot X within budget Y?"

Steps:

1. Get current character state (`analyze_character`).
2. Identify the slot's main responsibilities (e.g. amulet = primary stat + resistances + life/ES + jewel implicit).
3. `search_mods_by_stat` for desired mods (caveat: pre-0.5 data).
4. `get_uniques_by_base_name` if uniques are in scope.
5. `poe2_item_price` for budget filtering.
6. Recommend 2-3 specific item shapes (e.g. "rare amulet with +1 to all spell skills and 30%+ all-res in your budget; or unique X if you can stretch to Y exalts").
7. Mention any 0.5 trap: e.g. "this base is now incompatible with ES Recharge mods due to 0.5 changes."

---

## Workflow I — "What's the current meta?"

Steps:

1. **Check league age.** If <48h, state explicitly that meta is noisy and provide only directional info ("currently trending: X, Y" from patch-notes-informed expectations).
2. **At >48h**, `poe2_meta_builds` for the distribution.
3. Cross-reference with `compare_to_top_players` for individual ascendancies the user is curious about.
4. Be honest about uncertainty: ladder ≠ optimal. Popular ≠ best. State both.

---

## Workflow J — "Can my Spirit Walker tame this boss?"

Specific to the new Huntress ascendancy.

Steps:

1. Confirm the user has allocated **The Natural Order** ascendancy node (gives Tame Beast on Unique Beasts).
2. List confirmed tameable bosses: Mighty Silverfist, Chimeral Beast, Rakkar, Icefang Claw (per patch notes / Spanish coverage).
3. For uncertain bosses, `poe2_wiki_search "Tame Beast"` or check the Spirit Walker wiki page.
4. Note that Sylvan's Effigy (new unique sceptre, drops from Ritual pinnacle boss) removes the companion limit.

---

## Universal anti-patterns

- **Don't run more than 3 tool calls without summarizing for the user.** They want answers, not a transcript of your search process.
- **Don't speculate about future patches.** 0.5 is the last EA league before 1.0; speculation about 0.5.1 or 1.0 should be labelled `[Speculation]`.
- **Don't recommend specific build guides** unless the user asked for them. Many old guides are obsolete after 0.5.
- **Don't promise specific prices.** State the price observed at the time of the tool call; markets move.
