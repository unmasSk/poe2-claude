# 02 — MCP Tool Quirks — READ BEFORE FIRST TOOL CALL

These are non-obvious tool requirements. **Get them wrong and the tools return empty results or errors.** Memorize them.

---

## `poe2_db_lookup` (sergeyklay) — the trickiest

This tool queries poe2db.tw. Two rules:

### Rule 1: Underscores, not spaces

The `term` parameter uses **English names with underscores** to replace spaces.

✅ Correct: `term="Essence_Drain"`, `term="Chaos_Bolt"`, `term="Atziri's_Rule"`, `term="Tempest_Bell"`  
❌ Wrong: `term="Essence Drain"`, `term="essence_drain"` (case matters — start with capitals)

### Rule 2: Roman numerals for ranks

Skills, passives, and ascendancy nodes that have rank levels use **Roman numerals**, not Arabic.

✅ Correct: `term="Urgent_Totems_II"`, `term="War_Cry_III"`, `term="Hollow_Focus_I"`  
❌ Wrong: `term="Urgent_Totems_2"`, `term="Urgent_Totems"`, `term="War_Cry_3"`

Conversion: 1→I, 2→II, 3→III, 4→IV, 5→V.

If the user mentions a specific rank, **always append the Roman numeral suffix**. If they don't mention a rank, try `_I` first.

### Rule 3: Language parameter

The `lang` parameter accepts `us` (default, English) or `ru` (Russian). **No explicit Spanish/French/etc.** support documented.

For Spanish-speaking users: translate the term to English first (see `docs/11-glossary-es-en.md`), pass `lang="us"`, then translate the response back to Spanish if the user asked in Spanish.

### Rule 4: Output is truncated

Returns HTML-stripped text **truncated at 6000 chars**. If you need the full content of a wiki page, use `poe2_wiki_page` instead.

---

## `poe2_wiki_search` and `poe2_wiki_page` (sergeyklay)

### Workflow: search first, then fetch

`poe2_wiki_page` requires the **exact** wiki page title. Don't guess. Always call `poe2_wiki_search` first to get the canonical title from the results.

### Output truncation

`poe2_wiki_page` truncates at **8000 chars**. For very long pages (e.g. full version notes), expect the bottom of the article to be cut.

### Search returns 5 results max

`poe2_wiki_search` returns up to 5 matches. If none look relevant, refine the query (broader or narrower terms) — don't fabricate.

---

## `import_poe_ninja_url` and `analyze_character` (HivemindOverlord)

### Character must be public

The character's poe.ninja profile must be public. If you get "character not found":
1. Verify the character is on the **ladder** of the current league (high enough level).
2. Verify the user's poe.ninja privacy settings (their pathofexile.com profile → Privacy Settings → "Hide Characters" must be unchecked).
3. Character names are **case-sensitive**.

### League name matters

When calling, pass the correct league name:
- `"Runes of Aldur"` for Standard
- `"Hardcore Runes of Aldur"` for Hardcore
- `"Solo Self-Found Runes of Aldur"` for SSF
- `"Hardcore Solo Self-Found Runes of Aldur"` for HC SSF
- `"Standard"` for Standard (pre-existing)
- `"Hardcore"` for permanent Hardcore

If unsure, ask the user.

---

## `search_trade_items` (HivemindOverlord)

### Requires one-time setup

This tool needs Playwright + a POESESSID cookie. The user installs the browser dependency once, outside Claude:

```bash
pip install playwright
playwright install chromium
```

Then, **inside Claude**, invoke the `setup_trade_auth` MCP tool. A browser opens, the user logs in to pathofexile.com, and the session is saved.

**Note (verified 29 May 2026):** the standalone CLI `python -m poe2_mcp.scripts.setup_trade_auth` does NOT exist in the published `poe2-mcp` package (the top-level module is `src`, and there is no `scripts` submodule). Trade auth is only reachable via the `setup_trade_auth` MCP tool.

### If it fails

The tool will tell you it can't authenticate. **Stop and tell the user to run the setup.** Don't try other workarounds.

---

## All `poe2_*` tools (sergeyklay) — rate limit

A built-in rate limiter respects poe.ninja's limits automatically. You don't need to throttle — but don't loop excessively. If you call the same currency 10 times in a row, you're wasting cache cycles.

---

## `poe2scout/*` tools (vanzan01)

### Empty results on gear searches are NORMAL

POE2Scout focuses on **high-volume items**. Searching for a specific rare or low-volume unique will usually return empty. **This is not a bug.** For gear, use poe.ninja via Server A or direct the user to the official trade site.

### Volume warnings

When `volume/quantity` is shown:
- **1000+**: instant execution, reliable price.
- **100-999**: normal trading.
- **<100**: low liquidity, **flag price as potentially manipulated or stale**. Tell the user.

### Required env var

`POE2SCOUT_CONTACT_EMAIL` must be set. If the tool fails with auth errors, this is the first thing to check.

---

## Tool failure handling

When a tool returns an error or empty result:

1. **Don't fabricate.** If `poe2_db_lookup` returns nothing for an item, the item may be brand-new (early league) and not yet indexed. **Say so plainly.**
2. **Try the wiki as fallback.** `poe2_wiki_search` indexes faster than poe2db for some content.
3. **Don't retry the same call >2 times.** If it failed twice, the parameters are likely wrong (Roman numerals, underscores, exact title).
4. **Always re-check the quirks on this page before assuming the tool is broken.**

---

## When tools disagree

If two tools return contradicting data (e.g. HivemindOverlord's local DB says one thing, `poe2_db_lookup` says another):

1. **For 0.5 content**, trust `poe2_db_lookup` and `poe2_wiki_*`. HivemindOverlord's DB is pre-0.5.
2. **For pre-0.5 content**, both should agree. If they don't, flag the discrepancy to the user and pick the one with more detail.
3. **Never silently merge contradictory data.**
