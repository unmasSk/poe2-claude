# 15 — Ascendancy Trials (Trial of the Sekhemas & Trial of Chaos)

> **Scope.** This doc tells Claude how to *orient a teammate* on the two ascendancy trial
> systems in PoE2, and where to send them for exact numbers. It is a **router**, not an
> encyclopedia. Every game claim below is cited. Anything not confirmed by a cited source
> is marked `[Unverified — check wiki]`.
>
> **Sourcing discipline (read CLAUDE.md Hard Rules #1–#3 first).** Trial Boon names,
> Affliction names, Honour values, and difficulty tier numbers change between patches —
> **only state what a cited source confirms**, and for live specifics prefer
> `poe2_wiki_page` / `poe2_db_lookup` over memory.

---

## 1. High-level distinction (use this to orient a teammate in one breath)

There are **two** Ascension Trials in PoE2, and they are the only two as of early access.
You complete trials to unlock your Ascendancy class and earn Ascendancy passive points.

- **Trial of the Sekhemas** — a roguelike dungeon (challenge rooms, boons, a treasure trove,
  and bosses) governed by a special **Honour** "health bar." Introduced in Act 2. Run with a
  **Barya / Djinn Barya** key item. *Source: PoE2 Wiki, Ascension trials; Maxroll Trials of
  Ascendancy guide — checked 29 May 2026.*
- **Trial of Chaos** — a combat-focused gauntlet of consecutive rooms where you pick a
  negative modifier before each encounter, ending in a randomized boss. Introduced in Act 3.
  Run with an **Inscribed Ultimatum**. *Source: PoE2 Wiki, Ascension trials; Maxroll Trials
  of Ascendancy guide — checked 29 May 2026.*

**One-line steer for "which suits my build?":**
- The Sekhemas Honour bar punishes **getting hit at all** (even mitigated hits chip Honour),
  so it rewards **avoidance / not taking hits** more than raw EHP. *[Inference from the
  Honour mechanic below — confirm exact behavior on the wiki.]*
- The Trial of Chaos is a more conventional **clear-and-survive** fight, so it tends to suit
  **high-DPS / high-EHP** builds that don't mind standing in a fight.

Tell the teammate: both paths grant the same points; pick whichever your build survives more
comfortably, then verify the current room/affix details on the wiki (they get rebalanced).

---

## 2. How ascendancy points are earned (the 4-tier structure)

A character ascends fully by completing **4 tiers**, each granting **2 ascendancy points**,
for **8 points total**. *Source: PoE2 Wiki, Ascension trials; Maxroll Trials of Ascendancy
guide — checked 29 May 2026.*

The two trials are **interchangeable** for earning points — you can mix and match. A commonly
cited route (per Maxroll's guide; **verify level/tier requirements live, these are exactly
the kind of numbers GGG rebalances**):

| Tier | Points | Typical unlock (verify on wiki) |
|------|--------|----------------------------------|
| 1 | 1–2 | Trial of the Sekhemas via the early Barya quest (Act 2) |
| 2 | 3–4 | Trial of Chaos via the Inscribed Ultimatum quest (Act 3) |
| 3 | 5–6 | Higher-level **Djinn Barya** (Sekhemas) **OR** a higher-level Inscribed Ultimatum (Chaos) |
| 4 | 7–8 | Highest-level Djinn Barya (Sekhemas, +pinnacle boss) **OR** Inscribed Ultimatum with all three Fate fragments (Chaos) |

*Source for the tier/route table: Maxroll, "Trials of Ascendancy Guide" — checked 29 May 2026.*

> **Route the exact numbers to the wiki.** The specific **level requirements** (e.g.
> "Level 60+ Djinn Barya", "Level 75+", "Level 65+ Ultimatum"), **floor counts**, and the
> **three Fate fragment** names for the final Chaos tier are guide-sourced and patch-sensitive.
> When a teammate needs the precise gate for tier 3/4, use `poe2_wiki_page` on
> **"Ascension trials"** / **"Trial of the Sekhemas"** / **"Trial of Chaos"** or
> `poe2_db_lookup`, and cite it. Do **not** state these numbers from memory.

---

## 3. The Honour mechanic (Trial of the Sekhemas) — what's confirmed

Honour is a separate "health bar" used only inside the Trial of the Sekhemas. **If your
Honour reaches 0, you fail the trial** (the run ends). *Source: PoE2 Wiki, "Trial of the
Sekhemas" (as quoted in search results) and Maxroll Trials of Ascendancy guide — checked
29 May 2026.*

Confirmed behavior:
- **Taking damage to Life / Energy Shield also damages Honour.** This is why "don't get hit"
  matters more here than elsewhere. *Source: Maxroll Trials of Ascendancy guide — checked
  29 May 2026.*
- **Honour is maintained between rooms** (it does not reset each room) and **cannot be healed
  normally** — it is restored only through specific in-trial means: **trading with the
  Merchant (Balbala) using Sacred Water**, certain **Maraketh Shrines**, **Boons**, and
  **Relics / Artifacts**. *Source: PoE2 Wiki, "Trial of the Sekhemas" (as quoted in search
  results) — checked 29 May 2026.*

> **Route exact Honour numbers to the wiki.** Your **starting Honour value** is derived from
> your character's defenses (Life/ES — see the 0.5 change in §5), but the **exact formula and
> base values** are patch-sensitive. Do not quote a number unless a cited source gives it.
> Use `poe2_wiki_page` "Trial of the Sekhemas" and cite it.

### Boons, Afflictions, Sacred Water, Relics, Merchant (concepts only)
- **Boons** — beneficial buffs gained from Maraketh Shrines or bought from the Trial Merchant
  with **Sacred Water**; come in Minor/Major flavors. *Source: PoE2 Wiki, "Trial of the
  Sekhemas" (as quoted in search results) — checked 29 May 2026.*
- **Afflictions** — debuffs picked up during the run that make it harder (reduced Honour,
  reduced damage/defense, etc.). *Source: PoE2 Wiki, "Trial of the Sekhemas" (as quoted in
  search results) — checked 29 May 2026.*
- **Sacred Water** — the in-trial currency spent at the Merchant for Boons/Relics and to
  restore Honour. **Merchant** rooms let you trade with Balbala mid-run. *Source: PoE2 Wiki,
  "Trial of the Sekhemas" (as quoted in search results) — checked 29 May 2026.*

> **Do NOT invent specific Boon or Affliction names or their values.** The full Boon/Affliction
> lists live on the wiki and change between patches. When asked "what does Boon/Affliction X
> do," look it up via `poe2_wiki_page` and cite it; otherwise answer `[Unverified — check wiki]`.

---

## 4. The Trial of Chaos — what's confirmed

- A series of consecutive challenge rooms, ending in a **randomized boss**; clear it to unlock
  your Ascendancy and claim points + rewards. *Source: PoE2 Wiki, Ascension trials — checked
  29 May 2026.*
- Before encounters you choose **negative modifiers** (commonly called Tribulations in guides)
  that escalate difficulty. *Source: Maxroll Trials of Ascendancy guide — checked 29 May 2026.*
- Entry uses an **Inscribed Ultimatum**; the final ascendancy tier via Chaos requires an
  Ultimatum carrying all three **Fate** fragments (Cowardly / Deadly / Victorious Fate per
  guides). *Source: Maxroll Trials of Ascendancy guide — checked 29 May 2026.* **Verify the
  fragment names and level gate on the wiki before quoting them — patch-sensitive.**

> **Route exact Chaos affix lists and level gates to the wiki** (`poe2_wiki_page`
> "Trial of Chaos"). Do not enumerate specific Tribulation modifiers from memory.

---

## 5. 0.5 "Return of the Ancients" changes to the trials (confirmed)

The 0.5.0 patch notes mention the trials in only two places, both for the **Trial of the
Sekhemas**:

1. **"Your maximum Runic Ward is now added to your starting Honour when beginning a Trial of
   the Sekhemas."** This means the new 0.5 **Runic Ward** defense layer now feeds your starting
   Honour pool (alongside Life/ES). *Source: GGG 0.5.0 patch notes, reproduced on Maxroll
   "0.5.0 Patch Notes – Return of the Ancients" — checked 29 May 2026.*
2. **"Added a Reforging Bench to the entrance of the Trial of the Sekhemas."** *Source: GGG
   0.5.0 patch notes, reproduced on Maxroll "0.5.0 Patch Notes – Return of the Ancients" —
   checked 29 May 2026.*

**No Trial of Chaos changes** were found in the 0.5.0 patch notes as searched. *Source:
GGG 0.5.0 patch notes (Maxroll reproduction) and pathofexile.com forum thread 3932540 —
checked 29 May 2026.* If a teammate believes Chaos changed in 0.5, treat it as
`[Unverified — check wiki/patch notes]` until confirmed.

> **Not the same thing: "Masters of the Atlas."** The 0.5 patch also adds an endgame
> *"Masters of the Atlas"* progression (per the patch notes) which is **Ascendancy-style** but
> is **endgame Atlas content, not the ascendancy trials**. Don't conflate them. For Atlas/Masters
> see `docs/08-endgame-atlas.md`. *Source: Maxroll 0.5.0 patch notes — checked 29 May 2026.*

---

## 6. Question patterns → how to answer

| Teammate asks… | Do this |
|---|---|
| "How do I ascend / get all 8 points?" | Give §2's 4-tier structure (2 points × 4 tiers = 8, trials interchangeable). Route exact level/item gates to the wiki and cite. |
| "Which trial suits my build?" | Use §1's steer: Honour punishes getting hit (favors avoidance) → Sekhemas is harder for hit-tank builds; Chaos is a conventional clear/survive fight. Mark the suitability call `[Inference]`. |
| "How does Honour work?" | §3: separate bar, fail at 0, even mitigated hits chip it, restore via Merchant/Sacred Water/Shrines/Boons/Relics. Route the **starting value/formula** to the wiki. |
| "What does Boon/Affliction X do?" / "What's the best Boon?" | **Do not recall from memory.** `poe2_wiki_page` "Trial of the Sekhemas", cite it. Otherwise `[Unverified — check wiki]`. |
| "What level Barya/Ultimatum do I need for tier 3/4?" | Route to wiki/db — these are exactly the patch-sensitive numbers. Cite the lookup. |
| "Did the trials change in 0.5?" | §5: Sekhemas now adds **max Runic Ward to starting Honour**, and a **Reforging Bench** was added at the entrance. No Chaos changes found. Cite the 0.5 patch notes. |

**Default tool order for trial questions:** `poe2_wiki_page` / `poe2_wiki_search` →
`poe2_db_lookup`. The HivemindOverlord local DB predates 0.5 (CLAUDE.md Hard Rule #4), so do
**not** rely on it for the 0.5 Honour/Runic Ward interaction.

---

## 7. Sources (all checked 29 May 2026)

- PoE2 Wiki — *Ascension trials*: https://www.poe2wiki.net/wiki/Ascension_trials
- PoE2 Wiki — *Trial of the Sekhemas*: https://www.poe2wiki.net/wiki/Trial_of_the_Sekhemas
  (note: poe2wiki.net returned 403 to direct fetch on 29 May 2026; mechanic details above are
  from search-engine excerpts quoting this page — re-verify with `poe2_wiki_page` in-session)
- Maxroll — *Trials of Ascendancy Guide*:
  https://maxroll.gg/poe2/getting-started/trials-of-ascendancy
- Maxroll — *0.5.0 Patch Notes – Return of the Ancients*:
  https://maxroll.gg/poe2/news/0-5-0-patch-notes-return-of-the-ancients
- GGG official 0.5.0 patch notes (forum):
  https://www.pathofexile.com/forum/view-thread/3932540
- Maxroll — *Trial of the Sekhemas* resource:
  https://maxroll.gg/poe2/resources/trial-of-the-sekhemas

> Maintainer note: Boon/Affliction lists, Honour starting values, and tier level gates are the
> volatile parts of this topic. If the wiki and these guides disagree after a 0.5.x patch,
> trust the wiki/patch notes and flag this doc (CLAUDE.md §8).
