---
description: DPS help — read a Path of Building build and interpret it, or diagnose/approximate damage with 0.5 caveats. Never invents a final DPS number.
allowed-tools: mcp__poe2__poe2_pob_decode, mcp__poe2__poe2_pob_compare, mcp__poe2-optimizer__import_pob, mcp__poe2-optimizer__analyze_character, mcp__poe2-optimizer__import_poe_ninja_url, mcp__poe2-optimizer__explain_mechanic, mcp__poe2-optimizer__inspect_spell_gem, mcp__poe2__poe2_db_lookup, mcp__poe2__poe2_wiki_search, mcp__poe2__poe2_wiki_page
---

Help with DPS / damage: $ARGUMENTS

## The honest framing (state this up front if the user expects a number)

This pack **cannot compute a final DPS number for a 0.5 build itself.** No MCP tool
implements full PoB-level damage math, and the new-ascendancy / Runic Ward interactions
aren't modelled anywhere. **Path of Building 2 is the calculator; this command is the
interpreter.** So there are two modes:

- **If the user has a PoB build** → read it (PoB already computed the DPS) and interpret it.
- **If not** → do relative diagnosis and approximation, clearly labelled, never an absolute number.

Also note: the optimizer's `get_formula` tool is **broken upstream** (`No module named
'src.knowledge.formulas'` — see `docs/KNOWN-ISSUES.md`). Use `explain_mechanic` for the
underlying formulas instead, but treat its values as **pre-0.5 baseline** (CLAUDE.md Rule #4)
and verify any 0.5-changed number live with `poe2_db_lookup` / the wiki.

## Mode A — the user has a Path of Building build (preferred for real numbers)

Trigger: $ARGUMENTS contains a `pobb.in` URL, a `poe.ninja/poe2/pob/...` URL, or a local
build name.

1. `poe2_pob_decode` on the URL/name. **Do NOT ask for a raw base64 export code** — it
   corrupts in transit (`docs/02-mcp-quirks.md`); ask for a pobb.in/poe.ninja URL instead.
2. Report the DPS **as PoB computed it**, naming the exact configuration PoB assumed
   (which skill, was it the "full DPS" / combined hit, were flasks/charges/buffs active,
   single-target vs clear). **A PoB DPS number is only meaningful with its assumptions** —
   always state them, don't quote a bare number.
3. If the user gave two builds, or wants a before/after, use `poe2_pob_compare` and report
   item-by-item / gem / tree differences and how they move damage.
4. To *improve* it: identify the biggest missing multiplier layer (see §C) and say what to
   change. Re-import the modified PoB to confirm — let PoB recompute, don't assert the gain.

## Mode B — no PoB build (diagnosis & approximation only)

Trigger: a character name / poe.ninja URL, or a general "how do I do more damage" question.

1. If a character was given, load it: `import_poe_ninja_url` / `analyze_character`
   (league **Runes of Aldur** unless stated; needs the character public on poe.ninja).
2. Explain the relevant formula with `explain_mechanic` (e.g. `critical strike`). **Caveat
   it as pre-0.5 baseline** and verify any 0.5-changed value live.
3. Give **relative** guidance only — "swapping support X for Y is a larger *more* multiplier",
   "you're not penetrating resistances", "your crit multi is low relative to your crit chance".
   Use `[Inference]` for anything not directly read from a tool.
4. **Never output an absolute DPS figure in Mode B.** If the user insists on a number, route
   them to PoB2: "build it in Path of Building 2, then `/dps <pobb.in URL>` and I'll interpret it."

## C — the damage layers (use to find what to improve, and what to verify live)

A hit's DPS multiplies these layers; the biggest *missing* one is usually the best upgrade:

- **Base skill damage** (per gem level) → **`poe2_db_lookup` first** (live, 0.5 — verified
  reliable). `inspect_spell_gem` also works but its data is **pre-0.5 (Dec 2025 PoB dump)** —
  use only as a cross-check, never as the 0.5 source of truth.
- **"More" multipliers** (supports) → **`poe2_db_lookup "<Support_Name>"`** (live, 0.5).
  More-multipliers stack multiplicatively — usually the highest-leverage layer.
- **"Increased" damage** (passive tree + gear) → additive with each other; diminishing returns.
- **Crit** (chance × multiplier) → `explain_mechanic critical strike` for the formula
  (pre-0.5 baseline — verify the 0.5 base crit multi live with `poe2_db_lookup` / wiki).
- **Attack/cast speed** → linear DPS scaler.
- **Resistance penetration / enemy resists** → easy to overlook; often a big real-world gap.
- **Conversion / added damage / ailments** → skill-dependent; check the gem.

> **Tool reliability (verified live 29 May 2026 — do not assume otherwise):**
> - ✅ `poe2_db_lookup` — works, returns **live 0.5** data from poe2db.tw. **Primary source.**
> - ⚠️ `inspect_spell_gem` — works but **pre-0.5** (labels its own data `2025-12-13`). Cross-check only.
> - ❌ `inspect_support_gem` — **unreliable**: returns "not found" for real supports (e.g. Brutality). Don't rely on it; use `poe2_db_lookup` for supports.
> - ❌ `validate_support_combination` — **do NOT use here**: it returns "valid / compatible" even for gems it doesn't actually know, i.e. **false positives**. (It stays in `/build-check` only with that caveat.)
> - ❌ `get_formula` — **broken upstream** (missing `src.knowledge.formulas`). Use `explain_mechanic` instead. See `docs/KNOWN-ISSUES.md`.

## Hard limits (do not cross — `docs/12-anti-hallucination.md`, CLAUDE.md §6)

- Don't fabricate a DPS number. PoB computes; you interpret.
- Don't trust the optimizer's local DB for 0.5-new skills/ascendancies — verify live.
- Don't model Runic Ward / new-ascendancy damage interactions as if solved — they aren't.
- Always state the assumptions behind any number you *do* report (it came from PoB's config).

Respond in the user's language. Translate game terms to English before tool calls
(CLAUDE.md §6, `docs/11-glossary-es-en.md`).
