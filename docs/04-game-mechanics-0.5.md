# 04 — Game Mechanics in 0.5

Curated summary of mechanics that are **new in 0.5** or **substantially changed**. Sources: official patch notes, Maxroll, Mobalytics, conquestcapped, skycoach.

For anything not covered here, query the wiki via `poe2_wiki_search`.

---

## Runic Ward (new defensive layer)

A third defensive resource that sits on top of Life and Energy Shield.

**How it works:**
- Added to armour pieces via **Verisium Runeforging**.
- When your Life reaches 1, Runic Ward absorbs further damage. **You don't die while Runic Ward has charges.**
- When Runic Ward is depleted and you take more damage, you die.
- Runic Ward regenerates independently of Life and ES (rate depends on the item's roll).
- Armours **below ilvl 55** gain Runic Ward **with no downside**.
- Armours **ilvl 55 and above** trade some of their normal Armour/Evasion/ES for Runic Ward. Check the Verisium Anvil preview before committing.

**Why it matters:** the closest thing 0.5 ships to a safety net against one-shot windows. With the ES Recharge nerf, hybrid Life + ES + Runic Ward setups are stronger than pure ES.

**Crafting flow:**
1. Get Verisium from Ezomyte Remnant encounters.
2. Go to the Verisium Anvil (Farrow's hub).
3. Apply Verisium to a piece of armour. Item gains the "Runeforged" tag.

**On Unique armour (Act 3+):**
- Verisium Runeforging on a Unique grants Runic Ward.
- Kalguuran Uniques (the new league uniques) can also gain **additional properties** when Runeforged.

---

## Verisium

A new league crafting metal, dropped from Ezomyte Remnant encounters.

**Uses:**
- **Verisium Runeforging** — adds Runic Ward to armour (see above).
- **Genesis Tree** — a new crafting layer that builds on existing Rune sockets (does not replace them).
- **Acts as fuel** for several Kalguuran skill gems (alongside Runic Ward as the resource).

---

## Runeshapes

Items collected during exploration. Used to **activate Ezomyte Remnants** by being placed into the Remnant's slots.

Different Runeshape combinations create different **Runic Recipes**, which produce different output items.

**Example combination:** Tempest Rune + Lightning Rune → Orb of Augmentation.

More combinations are documented in the wiki. As you progress, you unlock more advanced recipes.

---

## Runic Recipes

The "menu" of craftable outputs at an Ezomyte Remnant. Each Remnant has a set of Runic Recipes inscribed on it. The number of slots (2 to 10) determines how complex the recipe and how rare the output. **10-slot Remnants are very rare and produce the rarest items.**

**Crucially:** when you select a recipe and place the Runeshapes, **the enemies you killed to reach the Remnant are resurrected and empowered by the runes you used.** Kill them again to claim the crafted item.

Each additional Runeshape used increases the number of waves and adds runic modifiers to the enemies — risk scales with reward.

---

## Runic Alloys

A new crafting currency. **5 different types.** Used to add **non-standard modifiers** to items — modifiers that normally can't roll on that item type.

Useful for adding rare mods to crafted gear without breaking the item.

---

## Fluxes (Resistance Swap)

Crafted at Remnants. Three different Flux types let you **swap one elemental resistance for another of the same tier without breaking the item.**

---

## Ancient Runes (13 new)

Granted via Farrow's Act 4 questline. Each Ancient Rune provides **weapon-type-specific bonuses** — there's an Ancient Rune for each weapon type in the game.

---

## Mythical Runes (13 new)

Early-game runes that give significant boosts to **level 15+ characters**. Designed to smooth out the leveling experience.

---

## Runic Ward Runes (15+ new)

Specifically modify or add properties related to Runic Ward.

---

## Runes from Uniques (60+ new)

A new mechanic: **destroying a Unique item** produces a Rune that **gains some of the properties of that Unique.** This effectively gives Uniques a "second life" as crafting fuel.

---

## Leech rework

Major systemic change in 0.5. Applies to **Life, Mana, and Energy Shield** leech.

**The new rules:**
1. **Only one leech instance per resource can apply at once.** Stacking multiple leech sources no longer multiplies recovery. The instance with the **highest recovery rate** is the one active; others are ignored while it's active.
2. **Damage cap:** hits dealing more than **40,000 damage** are capped for leech calculations. Big-hit builds (Cast-on-Crit Comet, one-shot burst builds) lose most of their leech sustain.
3. **All instant leech has been removed.** Atziri's Acuity (the historical instant-leech glove) was reworked.
4. **Maximum recovery per second** caps at approximately **50% of total Life/ES per second** with full investment, down from the previous 50k/sec ceiling.

**Builds that lose hardest:** Blood Mage (leech-immortality archetype), any build that stacked multiple leech sources on weapons or jewels, Cast-on-Crit Comet variants.

**Builds that gain (relatively):** non-leech-based sustain — life regen, ES regen, hybrid Runic Ward, flask sustain.

---

## Energy Shield Recharge nerf

Across the board ES Recharge values reduced **~50-66%** on:
- Passive tree nodes (Rapid Recharge, Essence Infusion, Convalescence, Refocus all roughly halved)
- Item modifiers
- Idols
- Most "faster start of ES Recharge" affixes removed or replaced with "increased ES Recharge Rate"

**Specific gear changes:**
- **Apep's Supremacy** (Unique Focus): no longer has 30-50% faster start of ES Recharge.
- **Sierran Inheritance** (Unique Body Armour): now grants 15-30% increased ES Recharge Rate instead of 30-50% faster start.
- **Subterfuge Mask**: ES-to-Evasion conversion halved.
- **Quick Response** (passive): removed entirely.
- **Ghost Dance**: now only regenerates ES equal to 2% of Evasion Rating per second instead of immediate ES recovery based on 5% of Evasion. Acts more like a slow regen than the old panic-button mechanic.
- **Intelligence armour bases**: can no longer roll ES Recharge related mods.

**Practical impact:** pure ES stacking is no longer the default best defense. Hybrid Life + ES + Runic Ward, or Evasion + ES, are now the strongest defensive shapes.

---

## Armour and Evasion buff

**Base Armour and Evasion** (and the mods that grant more of them) now grant **~33% more in the early game**, dropping to **~15% more at level 80+**. This partially compensates for the ES nerf.

---

## Deflect rework

The Deflect formula in PoE 2 has been changed to make reaching **100% chance to Deflect** much easier. Combined with Blind and notables like Glancing Blows, you can hit **40% damage reduction** much more reliably than before.

---

## Ancestral Bond rework

**New text:** "Your totem limit is doubled, no charge requirements for placing totems, and your totems reserve 75 spirit each."

**What changed:**
- ✅ **Removed:** "totems cost nothing to cast" line.
- ✅ **Added:** "no charge requirements" (you don't need to spend a charge to place a totem).
- ✅ **Added:** "totems reserve 75 spirit each" — significant Spirit cost.

**Impact:**
- **Arch Mage + totem combo is DEAD** — Arch Mage adds flat lightning damage to spells but scales the cost; with totems no longer free, the spell cost is real again.
- Grenade Ballista Totem Warbringer is still strong (no charge requirements + double totem limit = easy placement).
- Builds need to plan Spirit budget carefully.

---

## Other balance touches worth knowing

### Pathfinder (Ranger ascendancy)
- **Overwhelming Toxicity:** now applies **50% less Poison Duration** (up from 35%).
- **Running Assault:** now gives **30% less movement speed penalty** (down from 50%).
- Net effect: poison Pathfinder weaker but viable; speed Pathfinder more comfortable.

### Tempest Bell
- Can now be Ancestrally Boosted.
- Now has a **limit of 3** (up from 1).
- Damage and trigger cooldown nerfed slightly, but with 3 bells the total potential damage is higher.

### Gathering Storm + Ice Wall
- Interaction **removed**.
- Gathering Storm now interacts with **Tempest Bell** instead — creates a massive shockwave.

### Shield Wall
- Now deals **~15% less damage per 15 Armour on your Shield**.

### Fortifying Cry
- Shockwaves can no longer hit the same enemy multiple times.

### Splash damage on melee
- Multi-instance splash (Whirling Slash, Wyvern's Rend) can now only deal **one splash instance per damaging area**.

---

## Crafted-mod slot limit

A subtle but important change: **crafted methods that guarantee a modifier** (Essences, Perfect Essences, new Alloys, etc.) now **count as a single crafted mod slot.** You can't stack 4 essences to fill all 4 affix slots with guaranteed mods anymore.

This is a stealth nerf to the deterministic-craft strategy.

---

## Cross-references

- For full Spirit Walker / Martial Artist details, see `docs/05-ascendancies-new.md`.
- For Chronomancer / Gemling / Blood Mage / Pathfinder ascendancy reworks, see `docs/06-ascendancies-changes.md`.
- For Runes of Aldur league progression flow, see `docs/07-runes-of-aldur.md`.
- For Atlas / Fortress / Pinnacle bosses, see `docs/08-endgame-atlas.md`.
