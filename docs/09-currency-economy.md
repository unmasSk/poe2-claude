# 09 — Currency & Economy in 0.5

The economy is **fully reset** on 29 May 2026. Pre-0.5 prices are useless. This document covers what's changed in the currency system and how to think about value during the first 1-2 weeks of league.

---

## Removed for this league

### Recombinator

- **Permanently removed for the Runes of Aldur league.**
- **Omen of Recombination is deleted on login.** Players who had stockpiles lose them.
- Any build guide that relied on Recombinator crafting (combining mods from two items into one) is **obsolete for this league.**
- Whether the Recombinator returns in future leagues is **[Unverified]** — GGG has been ambiguous.

---

## New currency types in 0.5

### Verisium

The headline new resource. See `docs/04-game-mechanics-0.5.md` and `docs/07-runes-of-aldur.md` for full mechanics. **Always high-demand during league** — used for armour Runeforging.

### Runic Alloys (5 types)

- New crafting currency.
- Each Alloy type allows adding **non-standard modifiers** to items — mods that can't normally roll on that item type.
- Acquired from Remnant encounters.
- **Each Alloy use counts as the single "guaranteed mod" slot** — you can no longer chain 4 Alloys to fill all affixes.

### Fluxes (3 types)

- Crafted at Remnants.
- Each Flux **swaps one elemental resistance for another of the same tier without breaking the item.**
- Use case: you have a great item but the wrong resistance combo. Use Flux to convert.

### Runeshapes

- Not technically currency, but a tradeable resource.
- Used to activate Ezomyte Remnants.
- Different Runeshapes power different Recipes.
- Value scales with rarity of the Runeshape.

### Runes from Uniques (60+)

- New mechanic: **destroy a Unique item** to produce a Rune that gains some of the Unique's properties.
- Effectively turns Uniques into crafting fuel.
- Trade implications: **uniques that are bad for builds but good for rune-extraction** will spike in price.

---

## Standard currency tier reminders

(These are not new in 0.5 but worth listing for context.)

| Tier | Currencies |
|---|---|
| **Vendor trash / starter** | Scroll of Wisdom, Portal Scroll, Whetstones |
| **Common (Acts 1-3 fuel)** | Orb of Transmutation, Orb of Alteration, Orb of Augmentation |
| **Mid-tier (early maps)** | Orb of Alchemy, Orb of Chaos, Orb of Scouring, Regal Orb |
| **High-tier (T8+ maps)** | Exalted Orb (baseline price unit), Divine Orb, Fracturing Orb |
| **Elite** | Greater Essences, Perfect Essences, Mirror of Kalandra, Greater Jeweller's Orb |

In 0.5:
- **Exalted Orb** remains the baseline unit for prices.
- **Divine Orb** remains the stable high-value store.
- **Greater Jeweller's Orb** — high-value, watch for spikes.
- **Perfect Jeweller's Orb** — high value, good liquidity.

---

## League-start trading windows (general advice)

The fresh-economy curve has predictable phases:

### Phase 1: Day 0-1 (May 29-30)
- Almost no items listed.
- Prices wild and unreliable.
- **Volumes <100** are common. **Don't trust prices.**
- Best to play and accumulate, not trade.

### Phase 2: Day 1-3 (May 30 - June 1)
- Early listings appear.
- Top-tier items still under-priced because nobody's reached endgame yet.
- **Profit window for early endgame pushers** — selling Divine Orb-tier items at 2-3x post-stabilization price.
- Casual players: trade for cheap upgrades that will be 2-3x more expensive next week.

### Phase 3: Day 3-7 (June 1-5)
- Prices stabilize.
- Volumes normalize.
- Standard market behavior.

### Phase 4: Week 2+ (June 5+)
- Mature economy.
- Predictable price-history curves.
- `poe2scout/analyze_price_history` becomes most useful here.

---

## Volume warnings (critical for trading)

Always check volume before quoting a price:

| Volume | Reliability | Action |
|---|---|---|
| 1000+ | Excellent | Quote price confidently |
| 100-999 | Good | Quote price, note volume |
| <100 | **Manipulation risk** | **Warn the user, suggest checking trade site directly** |

This is built into the tools but the LLM must surface it. Don't quote a $50 exalt price for a low-volume item without saying "but only 12 listings in the last 24h — this could be price-fixed."

---

## Currency exchange in-game vs trade site

- **Currency Exchange** (in-game) — automated for high-volume currencies. Best for routine swaps (Chaos ↔ Divine, Exalted ↔ Divine).
- **Trade site** (https://www.pathofexile.com/trade2) — direct player-to-player. Required for everything else (gear, low-volume items, specific stats).

Tools:
- `poe2_currency_*` → reads the Currency Exchange.
- `search_trade_items` → reads the trade site (needs auth setup).

---

## Currency Tab structure (for reference)

PoE 2's Currency Tab in the stash has dedicated slots for major orbs. If a user mentions "my currency tab is full," they probably mean their Premium Stash Tabs are full of items that should be in dedicated tabs.

**0.5 introduces the Fragment Stash Tab** (purchasable) — holds Breach Splinters, Simulacrums, Audience with the King, Inscribed Ultimatums, Baryas, and Tablets.

---

## Atziri's Acuity reworked (0.5)

Worth noting because it's an iconic high-value unique.

- **Old:** instant Life Leech (broken interaction with the now-removed instant leech).
- **New (0.5):**
  - 150-200% increased Armour.
  - +100-150 max Life.
  - **10% of Physical Attack Damage as Life Leech** (no longer instant).
  - 10% of Physical Damage dealt by your Hits causes **Blood Loss** and **Vaal Pact**.
  - Grants the **Herald of the Royal Queen** skill.
- **Vaal Cultivation Orb outcomes have changed** for this item. **Existing items are NOT affected** — old Acuity is grandfathered.
- **Price implications:** new Acuity is no longer the auto-pick for leech builds. Old Acuity may become a collector item.

---

## Other unique item nerfs/buffs to know

### Sierran Inheritance (Unique Body Armour)
- **Old:** 30-50% faster start of ES Recharge.
- **New:** 15-30% increased ES Recharge Rate.
- Functional but weaker for ES burst-recovery builds.

### Apep's Supremacy (Unique Focus)
- **Old:** had 30-50% faster start of ES Recharge.
- **New:** that mod removed.

### Blackflame (Unique Ring)
- **Old:** had "Enemies Ignited by you take Chaos Damage instead."
- **New:** that line removed. Functionality reworked. [Verify specifics with `poe2_db_lookup term="Blackflame"`].

### Mageblood (new in 0.5)
- **[Inference]** Likely applies persistent Enchantment effects or modifies skill behavior.
- Exact mechanics: verify with `poe2_db_lookup term="Mageblood"` post-launch — do not assume; confirm live.

---

## Quick currency value reference (post-stabilization expectations)

**Do NOT quote these as current prices.** These are **rough relative-value reminders** from previous leagues — actual 0.5 prices must come from tools.

| Currency | Rough relative value (in Exalts, expected after stabilization) |
|---|---|
| Exalted Orb | 1 (baseline) |
| Chaos Orb | ~3-10 Ex (varies league) |
| Divine Orb | ~50-150 Ex (high-volume, stable) |
| Fracturing Orb | ~80-200 Ex |
| Mirror of Kalandra | Astronomical |

**Use tools, not memory, for actual prices.**

---

## Practical workflow

For any economy question:

1. Check the volume first.
2. State the price at the time of the tool call.
3. Flag volatility and league phase.
4. Suggest the trade site or Currency Exchange for execution.

Tools don't execute trades. Even if a user asks "buy me a Mageblood," the answer is "go to pathofexile.com/trade2 or use the in-game Currency Exchange — I can only read the market, not act."
