# 18 — DPS & Damage (how the calculation actually works)

This doc gives Claude the **structure** of PoE 2 damage maths so it can reason about DPS from
first principles — not just defer everything to Path of Building. The **formulas/structure
here are stable** (they're core PoE mechanics and don't change patch to patch). The **specific
numbers** (base crit multiplier, per-gem base damage, support multipliers) **do** drift with
patches — those are flagged "verify live" and must be confirmed with `poe2_db_lookup` / the
wiki before being quoted for 0.5.

> **The one hard limit (CLAUDE.md §6):** Claude does **not** produce a final DPS number for a
> 0.5 build. No MCP implements full PoB-level math, and new-ascendancy / Runic Ward
> interactions aren't modelled. **Path of Building 2 is the calculator; Claude is the
> interpreter and the diagnostician.** See the `/dps` command.

---

## 1. The damage pipeline (this is the mental model)

A single hit's damage is built by multiplying layers in this order:

```
Final hit damage =
      Base skill damage (gem, scales with level/quality)
    × (1 + Σ all "increased" %)        ← ADDITIVE bucket (tree + gear + gems)
    × More₁ × More₂ × More₃ …          ← each "more"/"less" is its OWN multiplier
    × Crit factor (expected)           ← see §3
    × Penetration / enemy-resist factor ← see §4
```

Then **DPS = hit damage × hits per second** (attack/cast speed × projectiles/repeats that
actually land on the target).

This pipeline is the same whether it's an attack, spell, DoT base, or ailment base — only the
inputs differ. **DoT and ailments do not crit** (crit only multiplies hits).

## 2. "Increased" vs "More" — the single most important rule

Verified live via `explain_mechanic damage scaling` (29 May 2026; tool notes this is a stable
core mechanic):

- **"Increased" / "Reduced"** → all **add together** into one bucket, then multiply once.
  `50% + 30% + 20% increased = +100% = ×2.0`.
- **"More" / "Less"** → each is a **separate multiplier**. `30% more × 20% more = ×1.3 × ×1.2 = ×1.56`.

```
Final = Base × (1 + TotalIncreased%) × More₁ × More₂ × …
Example: 100 × (1 + 1.00) × 1.3 × 1.2 = 312
```

**Why it matters for advice:** if a build already has lots of "increased", **another "more"
multiplier (usually a support gem) is worth far more than another "increased" source** —
"increased" has diminishing returns, "more" always gives its full value. This is the core of
almost every "what should I upgrade for damage?" answer.

## 3. Crit (expected-value formula)

Verified live via `explain_mechanic critical strike` (29 May 2026 — **values are pre-0.5
baseline, verify the 0.5 base crit multiplier live**):

```
Expected damage = Base × [ (1 − CritChance) + (CritChance × CritMultiplier) ]
```
- Crit chance is capped at **100%**; crit multiplier has **no cap**.
- `[Verify live for 0.5]` the **base crit multiplier** (the pre-0.5 dump says +100% i.e. ×2.0
  on crit — confirm with `poe2_db_lookup` / wiki before quoting a 0.5 number).
- In PoE 2, **crits do NOT guarantee ailments** (unlike older PoE) — they just deal more.
- Both layers matter: high chance with low multi (or vice-versa) is weak. Balance them.

## 4. Penetration & enemy resistance (the commonly-missed layer)

Damage of an element is scaled by `(1 − effectiveEnemyResist%)`. **Penetration** and
**resistance reduction** lower that resist, multiplying your real damage — and it's the layer
players most often forget when they say "my tooltip is high but I feel weak." When diagnosing,
always ask whether the build has any pen / res-reduction against the target's resists.
`[Verify live]` exact pen values and any 0.5 changes.

## 5. How Claude should answer DPS questions (and with which tools)

**Tool reliability — verified live 29 May 2026, do not assume otherwise:**

| Need | Use | Status |
|---|---|---|
| Base gem damage / support multipliers (0.5) | **`poe2_db_lookup "<name>"`** | ✅ live 0.5 — **primary** |
| The formulas above | `explain_mechanic` | ✅ works, but **pre-0.5 values** — structure good, numbers verify |
| Read a real build's computed DPS | `poe2_pob_decode` (pobb.in / poe.ninja URL) | ✅ PoB did the math; interpret it |
| Compare two builds | `poe2_pob_compare` | ✅ |
| A character's gear/skills | `analyze_character` / `import_poe_ninja_url` | ✅ if public on poe.ninja |
| ~~Formula tool~~ `get_formula` | — | ❌ **broken** (`KNOWN-ISSUES.md` #4) — use `explain_mechanic` |
| ~~`inspect_support_gem`~~ | — | ❌ unreliable / pre-0.5 (`KNOWN-ISSUES.md` #5) — use `poe2_db_lookup` |
| ~~`validate_support_combination`~~ | — | ❌ false positives (`KNOWN-ISSUES.md` #5) — don't use for DPS |

**Two answer modes (full flow in `.claude/commands/dps.md`):**
- **Has a PoB build →** read it, report PoB's number **with the assumptions PoB used**
  (which skill, buffs/charges/flasks on, single-target vs combined). A bare number is
  meaningless without its config.
- **No PoB →** relative diagnosis only (find the biggest missing layer from §1–§4), label
  `[Inference]`, and **never output an absolute number** — route them to PoB2 for the figure.

## 6. What changes with patches (so this doc stays honest)

- **Stable (rarely needs updating):** the pipeline in §1, the increased/more rule in §2, the
  crit EV formula shape in §3, the pen relationship in §4.
- **Verify-live every patch:** base crit multiplier value, per-gem base damage and
  multipliers, support "more" values, any new 0.5 damage layer (e.g. how Runic Ward or the new
  ascendancies interact with damage — currently **not modelled anywhere**, treat as
  `[Unverified]`).

> Maintenance (CLAUDE.md §8): if a live `poe2_db_lookup` / wiki value contradicts a number in
> this doc, **trust the tool** and flag the doc. The formulas are structure; the numbers are
> snapshots.
