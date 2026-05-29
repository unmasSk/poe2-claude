---
description: Search the PoE 2 community wiki and retrieve the most relevant article
allowed-tools: mcp__poe2__poe2_wiki_search, mcp__poe2__poe2_wiki_page, mcp__poe2__poe2_db_lookup
---

Search the PoE 2 wiki and explain: $ARGUMENTS

Steps:

1. **Translate Spanish to English** if needed (`docs/11-glossary-es-en.md`).

2. **Search the wiki** with `poe2_wiki_search` using a concise English query.

3. **Pick the most relevant result** from the snippets (max 5 returned).

4. **Retrieve the full page** with `poe2_wiki_page` using the **exact** title from the search result.

5. **For numerical/stat detail**, supplement with `poe2_db_lookup` using the English term with **underscores** and Roman numerals for ranks (see `docs/02-mcp-quirks.md`).

6. **Summarize**:
   - **What it is** (1-2 sentences).
   - **How it works** (the mechanic, with values if available).
   - **Why it matters** in 0.5 (any patch-related context).
   - **Source link** to the wiki page (https://www.poe2wiki.net/wiki/<title>).

7. **If the topic is brand-new in 0.5** (Spirit Walker nodes, Martial Artist Hollow techniques, Runic Ward, Verisium, Runic Alloys, Fluxes, etc.):
   - **Cross-reference `docs/04-game-mechanics-0.5.md`, `docs/05-ascendancies-new.md`, or `docs/07-runes-of-aldur.md`** in this pack for the curated explanation.
   - The wiki may have less detail than the pack docs in the first week of league.

8. **If nothing found**:
   - The topic may be brand-new and not yet indexed by the wiki.
   - Try a broader synonym (e.g. "Hollow" instead of "Hollow Focus II").
   - If still nothing, fall back to `docs/` in this pack or tell the user the wiki doesn't have it yet.

Respond in the user's language. Game term names stay in English with Spanish translation in parentheses where useful.
