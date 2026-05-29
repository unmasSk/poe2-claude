---
description: Price check an item or currency in the current Runes of Aldur league
allowed-tools: mcp__poe2__poe2_currency_check, mcp__poe2__poe2_currency_prices, mcp__poe2__poe2_item_price, mcp__poe2scout__analyze_price_history, mcp__poe2scout__get_currency_items
---

Price-check the item or currency: $ARGUMENTS

Steps:

1. **Classify the input**:
   - If it's clearly a currency (Divine Orb, Exalted Orb, Mageblood, etc.) → use `poe2_currency_check` or `poe2_item_price`.
   - If it's a unique or named item → use `poe2_item_price`.
   - If unclear → ask the user.

2. **Get the price**:
   - For Spanish input, translate the term to English first (see `docs/11-glossary-es-en.md`).
   - Make the appropriate tool call.

3. **Check volume**:
   - If volume <100, **add a manipulation warning**.
   - If volume 100-999, mention it briefly.
   - If volume 1000+, the price is reliable.

4. **For deeper analysis** (if user wants trend / signals / arbitrage):
   - Call `poe2scout/analyze_price_history` for the same item/currency.
   - Comment on volatility, trend, and any trading signal (buy/sell/hold).

5. **League phase caveat**:
   - **First 48h (29-31 May 2026)**: prices are wildly volatile, warn explicitly.
   - **Days 3-7**: stabilizing, normal market behavior.
   - **Week 2+**: mature economy, full reliability.

6. **Output format**:
   - State the price in Exalted Orbs first, then equivalents (Divine Orbs, etc.) if it makes sense.
   - State the volume.
   - State the league phase caveat.
   - For currency, mention the time of the snapshot.

Respond in the user's language. If the user asked in Spanish, name the item in English but provide the Spanish translation in parentheses for clarity (e.g. "Mageblood (Sangre Maga)").

If the tool returns empty:
- **Brand-new league + new unique**: it may not be indexed yet. Say so plainly.
- **Low-volume item**: redirect to https://www.pathofexile.com/trade2 for direct trade-site browsing.
- **Unknown item**: ask the user to clarify the exact name.
