# 14 — Campaign Guide (Router / Cheatsheet)

This pack is endgame-heavy, but teammates spend the **first ~6–15 h of every fresh league in the campaign**. This doc is a **router**, not an encyclopedia. Its job: route each campaign question to the right live tool (`poe2_wiki_search` → `poe2_wiki_page`, or `poe2_db_lookup`) instead of hardcoding numbers that drift between patches.

> **Hard rule reminder (CLAUDE.md §1):** **Do not state any campaign number — boss name, level target, act count, resistance penalty, quest reward — from memory.** Confirm it live in-session or label it `[Unverified]`. Patch 0.5 launched **29 May 2026**; some community pages still mix in earlier Early Access info, so cross-check.

---

## 0. What is structurally confirmed for 0.5 (with citations)

Everything in this section was checked against real sources on **29 May 2026**. Treat anything *not* here as **`[Unverified — check wiki in-session]`**.

### Act count and overall shape

- The current campaign runs **Act 1 (Ogham) → Act 2 (Vastiri) → Act 3 (Aggorat) → Act 4 (Ngamakanui)**, plus **Interlude quests**. Confirmed live via `poe2_wiki_search` against the official PoE 2 wiki **Act** page on 29 May 2026 (also corroborated: Hideouts unlock in Act 4, Rogue exiles first appear in Act 4). ([poe2wiki — Act](https://www.poe2wiki.net/wiki/Act), checked 29 May 2026)
- The earlier **"3 Acts + a Cruel difficulty pass"** layout was the **Version 0.1.0** structure; it no longer reflects 0.5. Do **not** tell teammates the campaign is 3 acts or that they replay acts on Cruel. ([poe2wiki — Version 0.1.0](https://www.poe2wiki.net/wiki/Version_0.1.0), checked 29 May 2026)
- **Act 5 and Act 6 are marked TBA** on the wiki — a long-term goal, **not** the 0.5 state. Do **not** tell teammates 0.5 has 5 or 6 acts. ([poe2wiki — Act](https://www.poe2wiki.net/wiki/Act), checked 29 May 2026)

> `[Unverified — check wiki in-session]` Whether a *new* post-Act-4 difficulty loop exists in 0.5. The wiki confirms the four acts above; it does **not** confirm any replacement second pass. If a teammate asks "do I replay the acts?", answer: *as of the wiki, the campaign is one pass through Acts 1–4 + Interludes, then endgame. Let me confirm the current page for your exact patch.*

### 0.5 campaign changes (streamlining) — confirmed in official 0.5.0 notes

These are explicitly listed in the **official 0.5.0 patch notes** ([pathofexile.com forum — Content Update 0.5.0](https://www.pathofexile.com/forum/view-thread/3932540), checked 29 May 2026):

- **"The Dreadnaught Vanguard" (second dreadnaught area) was removed.** The Act 2 boss is now in **"The Dreadnaught."**
- **Act 3 area order was rearranged** for smoother progression.
- **Some areas throughout the game were shortened.**
- **Waterways:** levers became walk-over pressure pads; the final section is pre-drained.
- **Monster density in the second half + Interludes was reduced** to speed up those stretches.
- **Environmental/directional cues added** to guide experienced players (e.g. visual tells pointing toward the next area). ([Maxroll — 0.5 reveal summary](https://maxroll.gg/poe2/news/patch-0-5-return-of-the-ancients-reveal-summary), checked 29 May 2026)
- **Martial weapon mod levels adjusted** so better weapons roll earlier, *especially in Act 1*. ([VULKK — 0.5.0 changes overview](https://vulkk.com/2026/05/22/path-of-exile-2-patch-0-5-0-changes-overview/), checked 29 May 2026)

> Because Act 3 was reordered and areas were cut in 0.5, **any act-walkthrough written before 29 May 2026 may list zones/bosses in the wrong order.** Always prefer a fresh `poe2_wiki_page` lookup over a remembered route.

### Ascendancy trials — where they unlock

- **Trial of the Sekhemas** unlocks in **Act 2** (accessed after the Balbala / Traitor's Passage quest line). First clear grants your **Ascendancy class + 2 points**. ([Maxroll — Trials of Ascendancy](https://maxroll.gg/poe2/getting-started/trials-of-ascendancy), checked 29 May 2026)
- **Trial of Chaos** unlocks in **Act 3** (Temple/Trial of Chaos via a key from the Trialmaster). First clear grants **2 more points** (3rd & 4th ascendancy points). ([Maxroll — Trials of Ascendancy](https://maxroll.gg/poe2/getting-started/trials-of-ascendancy), checked 29 May 2026)
- Recommended path: Sekhemas in Act 2 for points 1–2, then Trial of Chaos in Act 3 for points 3–4; higher points (5–8) come from higher-level/harder trial runs in endgame. ([Maxroll](https://maxroll.gg/poe2/getting-started/trials-of-ascendancy), checked 29 May 2026)

> **Verified trial gates** (`poe2_wiki_page "Ascension trials"`, checked 29 May 2026): first Sekhemas = Area Level **22+ / 1 floor**; first Chaos = Area Level **39+ / 4 rounds**. Full tier table (levels, floors, rounds for all 8 points) is in **`docs/15-ascendancy-trials.md`** — use it, don't re-derive from memory.

### Resistance penalty (campaign tax)

- Completing acts imposes a **negative all-elemental-resistance penalty** (a "campaign tax"); **chaos resistance is not penalized**. Boss kills in campaign zones drop **single-use permanent resistance bonus items** that partially offset it. ([Mobalytics — Resistances guide](https://mobalytics.gg/poe-2/guides/resistances), checked 29 May 2026)
- **The penalty scales with zone level** (verified live on the wiki **Interlude** page, `poe2_wiki_page "Interlude"`, checked 29 May 2026):
  - Zone Level **54–59 → −40%** all elemental resistance
  - Zone Level **60–64 → −50%**
  - Zone Level **65+ → −60%**
- So a teammate entering endgame should plan to **cap at 75% with roughly +60% resistance to overcome** the campaign tax. ([poe2wiki — Interlude](https://www.poe2wiki.net/wiki/Interlude), checked 29 May 2026.) If a teammate sees a different number for an earlier act, pull the specific zone's page live — the table above is the Interlude/late-campaign tier.

---

## 1. Routing table — campaign question → tool

For every pattern below: **translate game terms to English with underscores first** (CLAUDE.md §6, see `docs/11-glossary-es-en.md`), then call the tool. Cite the page you pulled from when you answer.

| Teammate asks… | Route to | Notes / what to watch |
|---|---|---|
| "What's the **boss of Act _N_**?" / "How do I beat _X_?" | `poe2_wiki_search "Act N"` → `poe2_wiki_page` on the act or boss page | Act 3 was reordered in 0.5; don't trust remembered order. |
| "**Where is quest/NPC _X_**?" / "Where do I turn in _Y_?" | `poe2_wiki_search "<quest name>"` → `poe2_wiki_page` | Some zones were cut/shortened in 0.5 (Dreadnaught Vanguard gone, Waterways changed). |
| "**What level should I be** for Act _N_ / for maps?" | `poe2_wiki_search "<act> walkthrough"` → `poe2_wiki_page` | Treat any level target as `[Unverified]` unless the page is 0.5-current; campaign was shortened in 0.5, so pre-0.5 targets may be high. |
| "**How much resistance** do I need by Act _N_?" / "Why are my resists negative?" | Answer from §0 verified table (zone Lvl 54-59 → -40%, 60-64 → -50%, 65+ → -60%), cite the wiki Interlude page. For a specific earlier zone, `poe2_wiki_page` on that zone. | Endgame target: cap 75%, plan ~+60% to overcome the late tax. |
| "**Where do I unlock my Ascendancy / Trial**?" | Sekhemas = Act 2 (Lvl 22+), Chaos = Act 3 (Lvl 39+); full tier/level table in `docs/15-ascendancy-trials.md`. | Verified 29 May 2026 via wiki. 8 points = 4 tiers × 2. |
| "**Which vendor** sells _X_ / has the gem I need?" | `poe2_wiki_search "<vendor/NPC>"` → `poe2_wiki_page` | Vendor offers can shift per patch; confirm. |
| "**Is there a campaign unique** for _slot/build_?" | `poe2_db_lookup term="<Item_Name>"` (underscores, see `docs/02-mcp-quirks.md`) | If `poe2_db_lookup` returns nothing on a 0.5 item, **say "not found / not yet indexed"** — do NOT invent (CLAUDE.md §3, §6). |
| "**What skill gems** are available by Act _N_?" | `poe2_db_lookup term="<Skill_Name>"` for a specific gem; `poe2_wiki_page` for availability | Roman numerals for ranked skills (`_I`, `_II`). |
| "Do I have to replay acts on **Cruel**?" | Answer from §0: in 0.5 it's a single pass through Acts 1–4 + Interludes (the old 3-acts-+-Cruel layout was Version 0.1.0). Offer to confirm on wiki. | Flag any old guide that assumes a Cruel loop. |
| "What changed in the **campaign in 0.5**?" | Answer from §0 (Dreadnaught Vanguard removed, Act 3 reorder, Waterways, density cuts). Cite the 0.5.0 patch notes. | This is the one place you *can* speak from confirmed 0.5 sources. |

### How to phrase answers when sources are silent
> "The structure (Acts 1–4 + Interludes, Sekhemas in Act 2, Chaos in Act 3) is confirmed. The exact level target / resistance number you're asking about isn't in my confirmed 0.5 sources — let me pull the current wiki page so we use a real number, not a pre-0.5 one." Then call `poe2_wiki_page` and cite it.

---

## 2. Proposed `/act` slash command

A campaign quick-reference command. **Spec only** — implement under `.claude/commands/act.md` following the existing command pattern.

**Usage:** `/act <N>` (e.g. `/act 2`) or `/act <boss-or-quest name>`

**Behavior:**
1. If given an act number `N`: `poe2_wiki_search "Act N"`, then `poe2_wiki_page` on the best match. Return a tight summary: zones in order, main boss(es), the ascendancy trial if that act has one, and notable quest rewards — **each line tagged with the wiki page it came from**.
2. If given a boss/quest name: `poe2_wiki_search "<name>"` → `poe2_wiki_page`; return location, mechanics, and reward.
3. **Always** prepend the confirmed-structure header from §0 (4 acts + Interludes, no Cruel pass, trials in Act 2 / Act 3) so the user has the skeleton even if a sub-lookup is thin.
4. **Never fabricate** zone order or level targets. If `poe2_wiki_page` is empty or stale, say so and show what was searched. Mark unconfirmed numbers `[Unverified — check wiki in-session]`.
5. Respect the user's language (ES/EN); translate terms to English before the tool call (CLAUDE.md §6).

**Guardrails baked into the command prompt:**
- "Patch 0.5 reordered Act 3 and cut areas — do not output a remembered route; only output what the live wiki page returns."
- "If the wiki page predates 29 May 2026 or doesn't say '0.5', flag it and present numbers as `[Unverified]`."

---

## 3. Sources

All checked **29 May 2026** (patch 0.5 launch day; some pages may still contain pre-0.5 / Early Access content — cross-check in-session):

- Official 0.5.0 patch notes — https://www.pathofexile.com/forum/view-thread/3932540
- Maxroll — Patch 0.5 "Return of the Ancients" reveal summary — https://maxroll.gg/poe2/news/patch-0-5-return-of-the-ancients-reveal-summary
- Maxroll — Trials of Ascendancy guide — https://maxroll.gg/poe2/getting-started/trials-of-ascendancy
- VULKK — Patch 0.5.0 changes overview — https://vulkk.com/2026/05/22/path-of-exile-2-patch-0-5-0-changes-overview/
- Game8 — Full Campaign Walkthrough and List of All Acts — https://game8.co/games/Path-of-Exile-2/archives/486659
- poe2wiki — Act (act list: Ogham / Vastiri / Aggorat / Ngamakanui, Act 5-6 TBA) — https://www.poe2wiki.net/wiki/Act (confirmed live in-session via poe2_wiki_search, 29 May 2026)
- poe2wiki — Version 0.1.0 (the old 3-acts-+-Cruel layout, now superseded) — https://www.poe2wiki.net/wiki/Version_0.1.0
- Mobalytics — Resistances guide — https://mobalytics.gg/poe-2/guides/resistances

> Maintenance note (per CLAUDE.md §8): if a `poe2_wiki_*` lookup in-session contradicts this doc, **trust the tool** and flag this file for update.
