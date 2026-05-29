# 10 — Passive Tree Changes in 0.5

The base passive tree (not the Atlas tree — that's `docs/08-endgame-atlas.md`) received major rebalancing in 0.5. This document catalogs the changes that affect existing builds the most.

---

## Free passive tree refund

**Every existing character on Standard gets a free passive tree refund** when 0.5 launches. The patch is explicit: "we would highly encourage you to join the new leagues to fully take in the changes."

If your colleagues are returning Standard players, they should know this — they don't have to throw away their characters.

---

## Energy Shield Recharge — biggest cluster of nerfs

Specific node-by-node changes (verify exact percentages with `poe2_db_lookup term="<node>_I"`):

| Node | Change |
|---|---|
| **Rapid Recharge** | ES Recharge value roughly **halved**. |
| **Essence Infusion** | Roughly halved. |
| **Convalescence** | Roughly halved. |
| **Refocus** | Roughly halved. |
| **Quick Response** | **REMOVED ENTIRELY** from the tree. |
| **Subterfuge Mask** | ES-to-Evasion conversion **halved**. |

The "faster start of ES Recharge" line is gone from most sources. The new dominant ES affix is **"increased ES Recharge Rate"** which is mathematically distinct (and weaker for burst-recovery purposes).

**Build impact:** pure ES stacking (Lich, hybrid ES Monk, hybrid ES Amazon, hybrid ES Ranger) loses significant defensive uptime. Hybrid Life + ES + Runic Ward is the new default.

---

## Small passive nodes adjusted

- **Increased Energy Shield** small passives: cut from **15% to 6%** in many clusters.
- Various life/mana small nodes minorly tweaked.
- Detailed list at `poe2_wiki_search "0.5 passive tree changes"` — content is too long to enumerate here.

---

## Keystones reworked

### Ancestral Bond

**Already covered in `docs/04-game-mechanics-0.5.md`** — totems no longer free to cast, reserve 75 spirit each.

### Trusted Kinship

Reworked. Verify text with `poe2_db_lookup term="Trusted_Kinship"`.

### Vaal Pact

Reworked. Connected to the **new Atziri's Acuity** mechanic (grants Vaal Pact via the unique now).

Verify text with `poe2_db_lookup term="Vaal_Pact"`.

---

## Notable passives — winners and losers

### Storm Charged (former crit/damage node)

- **Reworked** from a top-tier crit/damage node into a **penetration/cast speed node.**
- Old Storm Charged builds need to repath.

### Glancing Blows

- Buffed in conjunction with the **Deflect rework**.
- Now reaches **40% damage reduction** much more easily.
- Dex hybrid builds are clear beneficiaries.

### Bond of the Cat

- Mentioned positively in tier lists for league start — helps mobility.

---

## Crit notables

Most crit-related passives are **untouched**. **Critical Strike** as a damage strategy remains viable in 0.5. Specific exception: see Storm Charged rework above.

For Martial Artist Hollow Resonance builds, **crit is the primary trigger** for the back-bell. Crit-stacking remains a strong archetype.

---

## Minion / Companion nodes

The tree received new Companion-themed clusters to support Spirit Walker. Detail with `poe2_db_lookup` per node.

**[Inference]** Companion-focused passives synergize with Spirit Walker's The Catha's Balance (Main Hand Weapon damage scales Companion damage).

---

## Cluster relocations

The patch notes mention that "some clusters were moved, replaced, or removed entirely." Specific cluster relocations:
- Witch/Sorceress region received new Companion-themed nodes (and corresponding tree path tweaks).
- Strength clusters lightly reshaped.
- Dexterity Evasion-Energy-Shield hybrid clusters expanded slightly.

For the exact map: query the wiki page for the 0.5 passive tree, or use the Maxroll/poeplanner online visualizers.

---

## Block changes

Patch notes mention block adjustments. Specific:
- **Shield Wall**: now deals ~15% less damage per 15 Armour on your Shield.
- General block notables retain their general shape but had small numerical tweaks.

For full block math: verify with the wiki.

---

## Movement speed

No major movement-speed nodes added. Pathfinder's **Running Assault** now gives a smaller movement-speed penalty (30% less, was 50% less) — net positive for movement-Pathfinder.

---

## How to investigate any passive

For any specific node:

```
poe2_db_lookup term="Quick_Response"
poe2_db_lookup term="Rapid_Recharge_I"
poe2_db_lookup term="Glancing_Blows_I"
```

If `_I` returns nothing, try without the suffix (some nodes don't have ranks). Names use **underscores** and **start with capitals**.

For the visual layout of the passive tree, use:
- https://maxroll.gg/poe2/passive-tree (browser planner)
- https://poeplanner.com (alternative planner with import/export)

These external tools are **outside the MCP scope** — they're URLs for the user to open in their browser.

---

## Idol-related changes

Idols (the slot-able items) received expanded support in 0.5:
- More Idol-augment-based gear (especially gloves for Spirit Walker).
- Idol scaling systems are central to Spirit Walker's endgame.

For complete Idol mechanics: `poe2_wiki_search "Idol"` and follow up.

---

## Summary: what to do if your character feels weaker after 0.5

Check these in order:

1. **Did you rely on ES Recharge?** Most likely cause. Allocate Runic Ward via Verisium Runeforging.
2. **Did you stack multiple leech sources?** Pick the highest-rate one and abandon the others; build alternate sustain.
3. **Was your build "Arch Mage + totem free cast"?** It's dead. Re-strategize Spirit reservation.
4. **Was your build Cast-on-Crit Comet?** The 40k leech damage cap and rework hits hard. Consider switching to non-leech sustain.
5. **Were you a pure Pathfinder poison build?** Still viable, but you need 15-20% more poison investment to maintain old DPS.
6. **Did Quick Response anchor your defenses?** It's gone from the tree. Replace with Runic Ward or hybrid defenses.

Use `compare_to_top_players` after the 48h+ mark to see what high-performing builds of your ascendancy are doing post-0.5.
