# 06 — Existing Ascendancy Reworks in 0.5

Three existing ascendancies received notable reworks in 0.5. Others received minor balance touches; for those, consult `poe2_db_lookup` or the wiki.

---

## Chronomancer (Sorceress)

**Headline:** new defensive node + two existing nodes reworked.

### Phased Form (new)

- New **defensive** ascendancy node.
- Full text and values: verify with `poe2_db_lookup term="Phased_Form_I"`. Reported pre-launch as "a new defensive node" without exact numbers in public sources.

### Now and Again (reworked)

- Moved on the ascendancy tree to **replace Rapid River**.
- Functionality reworked (verify with `poe2_db_lookup term="Now_and_Again_I"`).

### Inevitable Agony (reworked)

- **Old:** applied a curse to enemies.
- **New:** applies a **life-loss debuff** to enemies, with **instant culling** above a life threshold.
- This is a meaningful damage tool for boss-killing variants of Chronomancer.

### Verdict

Pre-launch tier-list coverage views Chronomancer as **stronger than 0.4** after these changes, especially for bossing.

---

## Gemling Legionnaire (Mercenary)

**Headline:** two notable nodes reworked.

### Essence of Virtue (new/reworked)

- Grants a **Virtuous Barrier**. Acts as a defensive layer (verify mechanics with `poe2_db_lookup`).

### Advanced Theurgy (reworked)

- Gem quality now grants an **additional effect on all socketed skills.**
- Substantial buff for builds that invest heavily in gem quality.

### Verdict

Gemling Legionnaire becomes more defensive-friendly while gaining damage scaling via gem quality. Pre-launch sources project it as still a strong league option.

---

## Blood Mage (Witch)

**Headline:** hit hardest by the **leech rework**, since its core fantasy depended on life leech.

### What changed (indirectly)

Blood Mage didn't receive direct ascendancy node changes per the public reveals — the damage comes from the **systemic leech rework**:
- One leech instance per resource (kills the "stack 4 leech sources" build).
- 40,000 damage cap on leech hits (kills big-hit leech-immortality).
- All instant leech removed.

### Verdict

Blood Mage's **leech-immortality archetype is dead.** GGG explicitly stated leech-based immortality is "no longer a design we're willing to tolerate." Existing Blood Mage builds need to pivot to alternate sustain (Runic Ward, life regen, flask synergy) or accept lower defense.

---

## Pathfinder (Ranger)

**Headline:** poison Pathfinder weakened, but viable.

### Overwhelming Toxicity

- **New:** applies **50% less Poison Duration** (was 35% less).
- Poison damage-over-time builds lose ~15% effective DoT damage.

### Running Assault

- **New:** **30% less movement speed penalty** (was 50% less).
- The movement-speed Pathfinder becomes more comfortable but the penalty is still real.

### Verdict

Poison Pathfinder still clears but **demands more gear investment.** Movement-Pathfinder slightly buffed in feel. Both viable.

---

## Other reworks / minor touches

The patch notes mention adjustments to many notable and small passive nodes for Energy Shield Recharge, leech, crit, block, minion, and defensive mechanics, plus reworks to keystones:

- **Ancestral Bond** — see `docs/04-game-mechanics-0.5.md`.
- **Trusted Kinship** — reworked. Verify text with `poe2_db_lookup term="Trusted_Kinship"`.
- **Vaal Pact** — reworked. Verify text with `poe2_db_lookup term="Vaal_Pact"`.

For specific node-by-node values on any ascendancy, always query `poe2_db_lookup` or read the relevant wiki page. Don't rely on pre-launch tier lists for exact numbers — they often quote pre-patch values.

---

## Ascendancies NOT covered above

Ascendancies that received only minor balance touches (or none confirmed by patch notes):
- Acolyte of Chayula (Monk)
- Invoker (Monk)
- Amazon (Huntress)
- Ritualist (Huntress)
- Deadeye (Ranger)
- Infernalist (Witch)
- Lich (Witch) — note: hit indirectly by ES Recharge nerf
- Abyssal Lich (Witch)
- Stormweaver (Sorceress)
- Smith of Kitava (Warrior)
- Titan (Warrior)
- Warbringer (Warrior) — note: **benefits massively** from Ancestral Bond rework for totem builds
- Witchhunter (Mercenary)
- Tactician (Mercenary)
- Shaman (Druid)
- Oracle (Druid)
- Disciple of Varashta (Druid)

For any of these, ask `poe2_db_lookup` for each notable (e.g. `term="Endless_Hunger_I"`) to confirm if the values are 0.5-current.

---

## Winners and losers — at-a-glance

### Pre-launch winners
- **Warbringer** (Ancestral Bond + double totem limit + no charge requirements = grenade ballista totem heaven).
- **Spirit Walker** (Huntress, new).
- **Martial Artist** (Monk, new).
- **Chronomancer** (Phased Form + Inevitable Agony culling).
- **Evasion + ES hybrid** builds in general (Rangers, Mercenaries).
- **Deflect-stacking** Dex builds (formula rework).

### Pre-launch losers
- **Blood Mage** (leech rework destroys core fantasy).
- **Pure ES stacking** anything (~50-66% recharge nerf).
- **Poison Pathfinder** (still viable, demands more investment).
- **Arch Mage + totem** (Ancestral Bond rework + reservation = combo dead).
- **Cast-on-Crit Comet** (40k damage cap + leech rework hits hard).

**[Inference]** Validate these with `poe2_meta_builds` after the league is 48h+ in.
