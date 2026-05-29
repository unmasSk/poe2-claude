# 01 — MCP Tools: Full Inventory & Decision Matrix

Three MCP servers are configured. Use this file to pick the right tool for each question.

---

## Server A: `poe2` (sergeyklay/poe2-mcp-server)

**Stack:** TypeScript / Node ≥22. **Primary source for 0.5 content** because all data is fetched live from upstream sources.

| Tool | Description | Source | Use when |
|---|---|---|---|
| `poe2_currency_prices` | Current exchange rates for **all** currencies in the active league | poe.ninja | "Show me all current currency prices" / general market snapshot |
| `poe2_currency_check` | Look up **one** specific currency by name | poe.ninja | "How much is a Divine Orb worth?" |
| `poe2_item_price` | Price check items across exchange categories (including uniques in some categories) | poe.ninja | "Price check Mageblood" / "What does this unique sell for?" |
| `poe2_exchange_top` | Most valuable items per exchange category | poe.ninja | "What are the most expensive uniques right now?" |
| `poe2_wiki_search` | Search the community wiki for game mechanics, items, skills, mechanics | poe2wiki.net | First step for any "explain how X works" question about 0.5 |
| `poe2_wiki_page` | Retrieve full content of a wiki page (requires exact title) | poe2wiki.net | Follow-up to `poe2_wiki_search` |
| `poe2_db_lookup` | Datamined game data: gems, mods, items, passives, translations | poe2db.tw | Exact stat values, mod tiers, gem scaling, passive node details |
| `poe2_meta_builds` | Ladder class distribution with percentages and trends | poe.ninja | "What's the meta?" / "Which ascendancies are popular?" — unreliable in first 48h of league |

**Repo:** https://github.com/sergeyklay/poe2-mcp-server  
**Auth:** None required. No API keys, no GGG OAuth, no accounts.

---

## Server B: `poe2-optimizer` (HivemindOverlord/poe2-mcp)

**Stack:** Python ≥3.9. **Strong for character analysis and computation. Local DB is pre-0.5 (extracted Dec 2025) — see CLAUDE.md Hard Rule #4.**

### Character analysis

| Tool | Description |
|---|---|
| `analyze_character` | Full analysis: defenses, skills, gear, passives. Needs character name + account + league. |
| `import_poe_ninja_url` | Import a character directly from a poe.ninja URL |
| `compare_to_top_players` | Compare your build vs top ladder players of same ascendancy |
| `analyze_passive_tree` | Analyze allocated passive nodes (uses local pre-0.5 tree data) |

### Validation & inspection (LOCAL DATA, PRE-0.5)

| Tool | Description |
|---|---|
| `validate_support_combination` | Check if support gems work together (catches invalid combos) |
| `validate_build_constraints` | Validate a build against game rules |
| `inspect_support_gem` | View support gem data |
| `inspect_spell_gem` | View spell gem data |
| `list_all_supports` | List all support gems |
| `list_all_spells` | List all spell gems |
| `list_all_keystones` | List keystones with full stats |
| `inspect_keystone` | Get keystone details by name |
| `list_all_notables` | List notable passives |
| `inspect_passive_node` | Get any passive node details |

### Item data (LOCAL DATA, PRE-0.5)

| Tool | Description |
|---|---|
| `list_all_base_items` | List all base item types |
| `inspect_base_item` | Specific base item details |
| `inspect_mod` | Mod details by ID |
| `list_all_mods` | Mods filtered by PREFIX/SUFFIX/IMPLICIT |
| `search_mods_by_stat` | Search mods by keyword (e.g. "fire", "life", "critical") |
| `get_mod_tiers` | All tier variations of a mod family |
| `validate_item_mods` | Check if mods can legally coexist on an item |
| `get_available_mods` | List mods available for a generation type |

### Trade

| Tool | Description |
|---|---|
| `search_items` | Search the local item database |
| `search_trade_items` | Search the official trade site — **requires Playwright + POESESSID setup via `setup_trade_auth`** |
| `setup_trade_auth` | One-time setup flow for trade auth |

### Path of Building

| Tool | Description |
|---|---|
| `import_pob` | Import a Path of Building code |
| `export_pob` | Export a build to PoB format |
| `get_pob_code` | Get the PoB code for a character |

### Knowledge & utility

| Tool | Description |
|---|---|
| `explain_mechanic` | Explain a PoE 2 mechanic (pre-0.5 baseline) |
| `get_formula` | Get calculation formulas (EHP, DPS components) |
| `health_check` | Check server status |
| `clear_cache` | Clear cached data |

**Repo:** https://github.com/HivemindOverlord/poe2-mcp  
**Auth for trade tools only:** Playwright + POESESSID cookie via `python -m poe2_mcp.scripts.setup_trade_auth`

**Upstream packaging bugs (confirmed 29 May 2026, version 1.0.0):**

- Module is published as top-level `src` (not `poe2_mcp`). Importing `poe2_mcp` will always fail; the canonical import is `import src.mcp_server`.
- Console script `poe2-mcp` is broken: the setuptools entrypoint forgets to await the async `main` coroutine. The server prints its startup banners and exits with code 0 without starting the MCP stdio loop. **Do not use the `poe2-mcp` command.**
- Settings require `SECRET_KEY` and `ENCRYPTION_KEY` env vars not documented in the upstream README. Without them, pydantic raises `Field required` errors on startup.
- Top-level `src` module pollutes the global Python namespace — if another installed package also exposes `src` as a top-level module, there will be a collision. Low probability in practice but worth knowing.

**Workaround in this pack (no external wrapper needed):**
- Launch with `python -m src.mcp_server` (or `python3 -m src.mcp_server` on systems where only `python3` exists). The package's `__main__` block awaits the coroutine correctly.
- Set `SECRET_KEY` and `ENCRYPTION_KEY` as `env` vars in the `poe2-optimizer` block of `.mcp.json`. Generate them locally with `python -c "import secrets; print(secrets.token_hex(32)); print(secrets.token_urlsafe(32))"`. Each user generates their own; never commit.
- Setup check in CLAUDE.md §0.1 verifies the package is installed via `importlib.metadata.distribution('poe2-mcp')` (the only reliable way given the broken module name) and detects the `GENERATED_PER_USER` placeholder to force key generation on first run.

---

## Server C: `poe2scout` (vanzan01/poe2scout-mcp)

**Stack:** TypeScript / Node. **Currency trading specialist only.**

| Tool | Description |
|---|---|
| `analyze_price_history` | Advanced market analysis: trend detection, volatility assessment, trading signals |
| `get_leagues` | Current league data with Divine Orb pricing |
| `basic_search` | Find currency items by name with price history |
| `get_currency_items` | Major currency exchange rates and volume |
| `get_unique_items` | High-value unique discovery (limited coverage) |
| `get_item_categories` | Available trading categories |
| `get_unique_base_items` | Base item reference data |
| `get_uniques_by_base_name` | Filter uniques by base type |
| `get_api_status` | Rate limiting and system health |
| `get_item_filters` | Available search filters/categories |
| `get_landing_splash_info` | Platform status |

**Repo:** https://github.com/vanzan01/poe2scout-mcp  
**Auth:** Requires `POE2SCOUT_CONTACT_EMAIL` env var (set in `.mcp.json`).  
**Rate limit:** 2 requests/second, burst 5.

**Important limitation (from the project README):** POE2Scout indexes only **high-volume traded items**. Most specific gear searches return empty — this is normal. For gear, use poe.ninja via Server A or the official trade site.

---

## Decision matrix — which tool for which question

| Question type | First tool | Second tool (if needed) |
|---|---|---|
| "Explain how Runic Ward / Verisium / Runeforging works" | `poe2_wiki_search` | `poe2_wiki_page` |
| "What's the exact stat scaling of skill X?" | `poe2_db_lookup` | `poe2_wiki_page` |
| "Show me all tiers of a mod" | `get_mod_tiers` (HivemindOverlord, **pre-0.5**) | `poe2_db_lookup` for 0.5 verification |
| "What's the current price of X?" | `poe2_currency_check` or `poe2_item_price` | `poe2scout/analyze_price_history` for deep analysis |
| "Should I sell my Divine Orbs now?" | `poe2scout/analyze_price_history` | `poe2scout/get_currency_items` for volume |
| "Analyze my character `Xyz`" | `import_poe_ninja_url` or `analyze_character` | `compare_to_top_players` |
| "Can these support gems combo?" | `validate_support_combination` | — |
| "What ascendancies are people playing?" | `poe2_meta_builds` | — (note: noisy <48h into league) |
| "Search the trade site for an item with these stats" | `search_trade_items` (after `setup_trade_auth`) | — |
| "Find unique uniques by base type" | `get_uniques_by_base_name` | — |
| "What does this PoB code translate to?" | `import_pob` | `compare_to_top_players` |

**Default fallback:** when in doubt about 0.5 content, prefer the **live-fetch** tools (`poe2_*` from Server A) over HivemindOverlord's local-DB tools (Server B).
