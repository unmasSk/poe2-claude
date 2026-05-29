# 19 — PoB Deep Read ("PoB2 → Claude": the real DPS calculator)

This is the capability that makes Claude a **real build analyst** instead of a guesser.
A Path of Building 2 share is not just names — it embeds the **entire build**, including
**every stat PoB already calculated**. We read that directly. Claude does not re-derive DPS
by hand (that was unreliable — see the failure recorded in `docs/KNOWN-ISSUES.md`); Claude
reads the number PoB computed and **analyses it across every layer of the build**.

## What a PoB share actually contains

A pobb.in share is a **zlib-compressed, base64url-encoded XML**. Decoded, it has:

- **`<PlayerStat>` entries — the stats PoB itself computed** (≈100+ of them): `AverageDamage`,
  `TotalDPS`, `CombinedDPS`, `FullDPS`, `WithDotDPS`, `CritChance`, `CritMultiplier`, `Speed`,
  `Life`, `EnergyShield`, `Mana`, resistances, attributes, and more. **This is the gold** —
  no hand-math needed.
- The **full allocated passive tree** (every node id).
- **Every item with all its mods**, sockets, and runes/soul cores.
- All **skill gems + support gems** per socket group.
- The config (enemy level, buffs/flags assumed in the calc).

The shallow MCP tool `poe2_pob_decode` does NOT expose most of this (it returns names,
"0 nodes", no mods, no computed stats). So for any real DPS/optimisation work, use the
deep-read method below, not `poe2_pob_decode` alone.

## The method (how Claude reads a build fully)

**Source rule:**
- ✅ **pobb.in/`<id>`/raw** returns the raw PoB code → decodable. **This is the supported path.**
- ❌ **poe.ninja/poe2/pob/`<id>`** returns an HTML/JS page, NOT the code. It cannot be deep-read.
  **Ask the user to re-upload to pobb.in** (in PoB2: *Import/Export → Upload to pobb.in*) and
  give that URL. This is the one thing the pack needs from the user.

**Extraction:** run the bundled script (stdlib only, no install):

```bash
python tools/pob_extract.py https://pobb.in/<id>
```

It prints the computed stats, the build header (+ node count), skills/supports, and every
item with its full mod list. Under the hood it does: fetch `/raw` → base64url decode → zlib
inflate → parse the XML. Claude then reasons on top of the real data.

## How Claude works once the build is read (the analyst role)

This is the workflow the user asked for — **be the DPS calculator nobody accounts for, and
scrutinise the build across ALL layers for upgrades**:

1. **Anchor on PoB's own numbers.** Read `AverageDamage` / `TotalDPS` / `CombinedDPS` — that's
   the baseline, exact, no estimation.
2. **Decompose every layer** (see `docs/18-dps-and-damage.md`): base gem damage, more vs
   increased buckets, crit (chance × multi), penetration/resists, attack/cast speed, ailments,
   then defences (Life/ES/Spirit/res) and utility.
3. **Hunt upgrades everywhere, not just gems:**
   - **Skill gems & supports** — swap a low-value support for a bigger *more* multiplier;
     verify each support's real value with `poe2_db_lookup` (live 0.5).
   - **Passive tree** — find dead/low-value allocated nodes; find unallocated notables/keystones
     near the current path that add a missing layer.
   - **Items & mods** — read every mod; flag missing damage/defence affixes, empty sockets,
     wrong bases. Use `poe2_parse_item` for items the user pastes.
   - **Crit setup** — is crit chance/multi balanced? Is a crit-conditional support dead?
   - **Penetration / resist reduction** — the most commonly missing multiplier.
   - **Defences** — resist caps (75%), Life/ES pool, Spirit reservation, one-leech-source (0.5).
4. **Propose a concrete change**, predict the direction/magnitude, then **the user applies it in
   PoB2 and reports the new number** — if it improves, keep it. PoB confirms; Claude proposes.

## Honest limits (state these, don't pretend past them)

- The **exact post-change number** still comes from PoB after the user applies the change. Claude
  predicts direction and approximate magnitude; PoB is the source of truth. (When Claude predicted
  a node's value from a screenshot + assumptions it was off by ~16 points — see KNOWN-ISSUES.
  Reading PoB's computed stats avoids that; predicting blind does not.)
- For a precise prediction *before* touching PoB, Claude needs the **Calcs-tab breakdown**
  (crit-chance sources, damage-by-type) — with it, predictions tighten from a range to ~1%.
- New-0.5 interactions (Runic Ward, brand-new ascendancy nodes) may not be modelled even by PoB2
  itself (PoB2 for PoE2 is in development) — flag those as `[Unverified]`.

## One-line summary for the user

Upload your build to **pobb.in**, give me the URL, and I read the whole thing — tree, items,
mods, and the DPS PoB already calculated — then I scrutinise every layer for upgrades. You test
each change in PoB2; if it's stronger, you keep it.
