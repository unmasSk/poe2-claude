# 07 — Runes of Aldur League Mechanic

The challenge league of patch 0.5. NPC is **Farrow**, a young blacksmith on a quest to rediscover **Ezomyte Runesmithing** (which turns out to be of **Kalguuran** origin).

---

## The core loop

1. **Find an Ezomyte Remnant** — stone structures scattered across every area, guarded by monster packs.
2. **Kill the guardians** to access the Remnant.
3. **Inspect the Remnant.** It has a number of slots (2 to 10) with pre-inscribed Runic Recipes. Higher slot count = rarer Remnant = rarer rewards.
4. **Place Runeshapes** into the slots to imprint a recipe.
5. **The choice of runes determines two things simultaneously:**
   - The **item produced** when you complete the encounter.
   - The **modifiers applied to the resurrected enemies** in the fight.
6. **Confirm the recipe.** The enemies you killed are **resurrected** with the chosen empowerments.
7. **Defeat the resurrected enemies** (which now have rune-based modifiers and may come in waves — more Runeshapes = more waves).
8. **Break the Remnant** to claim the crafted item.

**Risk/reward dial in your hands.** Pick cheap rewards → easy fight. Pick rare rewards → harder fight with more dangerous modifiers.

---

## Where you meet Farrow

- **Act 1, Blackwater** — Farrow is being attacked by undead. Rescuing him starts the questline.
- **Act 1 progression** — **Verisium Runeforging** is unlocked (apply Runic Ward to armour).
- **Act 3 progression** — **Unique Verisium Runeforging** is unlocked (apply Verisium to Uniques).
- **Act 4** — Farrow joins forces with **Expedition** team. Runes of Aldur content starts blending with **familiar Expedition encounters**.

---

## Endgame: Grand Expeditions

- The endgame hub is **The Ruins of Kingsmarch**, located **south-east** of the Atlas starting location.
- Largely destroyed in the lore — now lies off the coast on the Atlas map.
- **Verisium meteor** has hit the area, scattering Kalguuran tech.
- **Grand Expeditions** (formerly known as **Logbooks** in PoE 1 / earlier coverage):
  - Run by Farrow + Expedition team.
  - Take place across the **Uncharted Seas** — unveils a section of ocean with islands to explore.
  - Many **new underground areas** can be uncovered during Expeditions.
  - Many **new islands** with their own Grand Expedition encounters.
  - **Old Expedition is DISABLED** — replaced by this system.

---

## Pinnacle boss: Olroth (key) → New Pinnacle Boss

- Defeating **Olroth** grants a key to access the **new Pinnacle Boss** of Runes of Aldur.
- The Pinnacle Boss identity and full mechanics are documented in the wiki — query `poe2_wiki_search "Runes of Aldur Pinnacle"` for current details. [Unverified specific name at time of pack creation]

---

## Challenges (first time in PoE 2)

- **8 challenges total**, ranging from beginner-friendly to extreme endgame.
- Rewards: every 2 completed challenges grants a piece of the **Knight of Aldur Armour Set** (microtransaction skin, league-exclusive).
- Every completed challenge also grants a piece of the **Runes of Aldur Totem decoration** for your hideout.
- Press **H in-game** to view the Challenges UI.

### Confirmed challenge categories (per pre-launch coverage)

1. **Remnant Crafting Progression** — find and complete Remnants with increasing socket counts. The final tier requires completing a **7-slot Remnant** (6 waves, endgame-level difficulty).
2. **Unique Identification** — identify **50 unique items.** Atlas Master **Jado** has mechanics that improve unique drop rate (Spycraft tree). Easier for trade league, harder for SSF.
3. **Crafting Variety** — use a wide variety of crafting Remnant outputs. Teaches the rune-recipe system. Probably the league-mechanic tutorial challenge.
4. **Atlas Tree Completion** — allocate **all 300+ Atlas passive nodes**.
5. **Pinnacle Boss Kills** — defeat the **Arbiter of Divinite** (Fortress pinnacle). Each kill auto-completes a large Fortress section. After 4 kills, the entire Fortress becomes accessible.
6-8. **[Unverified]** — remaining 3 challenge categories should be documented in the wiki post-launch. Query `poe2_wiki_search "Runes of Aldur Challenge"` for current list.

---

## Recipe combinations to know

**Tempest + Lightning** → Orb of Augmentation (campaign-early example).

For complete recipe documentation: `poe2_wiki_search "Runic Recipes"` and follow up with `poe2_wiki_page`.

---

## Recipe complexity tiers

| Slots used | Difficulty | Output tier |
|---|---|---|
| 2-3 | Easy | Basic Currency (Augmentation, Transmutation, Alchemy) |
| 4-5 | Medium | Standard Runes, mid-tier Currency, Fluxes |
| 6-7 | Hard | Specific Runes for Augment Sockets, advanced Crafting Materials |
| 8-10 | Very hard | Greater Runes, rare crafting outputs, build-defining items |

**Beginner tip (per league guides):** start with **4-7 slot Remnants** while doing Farrow's quests. Smaller Remnants are too cheap; larger ones get you killed before you're geared.

---

## Verisium economy

Verisium is the **primary fuel** of the league. Drops from Ezomyte Remnant encounters. Used for:
- Runic Ward Runeforging on armour (mandatory for all serious builds with Life-based defense).
- Unique Runeforging (Act 3+).
- Kalguuran Skill Gem activation (some skills consume Runic Ward, which is fuelled by Verisium).

**Trade implications:** Verisium will be one of the most-traded resources in the first weeks of the league. Watch its price trend with `poe2scout/analyze_price_history`.

---

## Kalguuran Skill & Support Gems (21 + 8 new)

A new category of skill/support gems introduced with the league.

**Key trait:** powered by **Runic Ward instead of Mana.**

This makes them naturally synergistic with Verisium Runeforging and Martial Artist's Runic Meridians. Builds that lean into Runic Ward defense get free fuel for Kalguuran skills.

For full Kalguuran gem list: `poe2_db_lookup` per gem name, or `poe2_wiki_search "Kalguuran gem"`.

---

## Lore arc (no spoilers, light strokes)

- Farrow introduces himself as an Ezomyte runesmith.
- Through the campaign you discover the Remnants are not Ezomyte at all — they're **Kalguuran in origin.**
- The Kalguuran connection ties the league to existing PoE 2 lore (Kingsmarch was a Kalguuran settlement in 0.1).
- The lore culminates in the endgame Pinnacle encounter, with the Verisium meteor as a focal event.

---

## What to do day 1 of the league

A condensed launch-day strategy (per multiple league guides):

1. **Don't overbuild around theorycraft.** Meta is unknown.
2. **Pick up everything** in Acts 1-3 — Alteration, Augmentation, Transmutation Orbs are free crafting fuel.
3. **Engage with Remnants** during campaign — start with 4-7 slot Remnants for the Farrow questline.
4. **Apply Runic Ward to armour** as soon as Verisium Runeforging is unlocked.
5. **Goal: complete campaign + early Atlas in 1-3 days** depending on skill and build.
6. **Sell to bulk first**, hoard Exalted Orbs.
7. **Don't buy gear you don't need yet** — economy stabilizes around days 3-5.

For build-specific day-1 routes: query the wiki or community guides per ascendancy. **Don't rely on memory from previous patches.**
