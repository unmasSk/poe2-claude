# 13 — `.build` File Format Reference

PoE 2 patch 0.5 introduced an **in-game Build Planner** that loads JSON files with the `.build` extension. Third-party guide creators (Mobalytics, Maxroll, individuals) export their builds in this format and players drop them into a specific folder.

**Format version:** `1 (Experimental)` — GGG has stated the format will evolve.

**Official documentation:** https://www.pathofexile.com/developer/docs/game#buildplanner

This file is Claude's working reference. It covers the schema, the markup language, ID sources, translation rules, the JSON Schema for validation, the limits of the format, and the workflow for handling `.build` files in this pack.

---

## 1. What the Build Planner is (and isn't)

**Is:**
- An in-game system that **reads** `.build` JSON files from a watched directory.
- Visible inside the client on the **passive skill tree**, **skill gems panel**, **gear slots**, and **crafting window**.
- A way for guide creators to ship build instructions that overlay onto the player's UI.
- Read-only at the client level — the game does not edit or write `.build` files.

**Isn't:**
- A theorycrafting tool. Use **Path of Building 2** (https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2) for DPS math.
- A character editor.
- A trade automation system.
- A way to ship official GGG-curated builds. GGG explicitly stated: "it is not on us to decide what's good."

---

## 2. File location (where the game looks)

The game watches `Documents/My Games/Path of Exile 2/BuildPlanner/` for `.build` files. Drop files in, restart the client, they appear in the in-game selector.

| Platform | Path |
|---|---|
| **Windows** | `C:/Users/<Name>/Documents/My Games/Path of Exile 2/BuildPlanner` |
| **Steam Deck (SteamOS)** | `/home/deck/.local/share/Steam/steamapps/compatdata/2315204395/pfx/drive_c/users/steamuser/Documents/My Games/Path of Exile 2/BuildPlanner` |
| **macOS** | `[Unverified]` — not officially documented. Likely `~/Documents/My Games/Path of Exile 2/BuildPlanner` or `~/Library/Application Support/.../BuildPlanner`. Have the user check by listing the contents of `~/Documents/My Games/`. |
| **Linux (Steam non-Deck)** | `[Unverified]` — same Proton path pattern as Steam Deck but with the user's Steam dir, e.g. `~/.steam/steam/steamapps/compatdata/2315204395/pfx/drive_c/users/steamuser/Documents/My Games/Path of Exile 2/BuildPlanner` |
| **Linux (native)** | If GGG ships a native Linux client (not yet at 0.5), location unknown. `[Unverified]` |

The game uses an **automated File Watcher** — changes are picked up without restart in most cases, but a client restart is the safe fallback.

---

## 3. The schema (official, v1)

A `.build` file is a single JSON object. The root is type `Build`.

### 3.1 `Build` (root object)

| Key | Type | Required | Notes |
|---|---|---|---|
| `name` | string | **Yes** | Display name in the in-game selector. |
| `author` | string | No | Creator credit. |
| `description` | string | No | Long-form description. Supports markup. |
| `ascendancy` | string | No | Ascendancy identifier. See §6 for known values. |
| `passives` | array of (string \| `BuildPassive`) | No | Passive tree nodes to highlight. |
| `skills` | array of (string \| `BuildSkill`) | No | Active skills to suggest. |
| `inventory_slots` | array of `BuildInventorySlot` | No | Gear slot hints. |

**Shorthand:** if you don't need any optional fields on a passive/skill/support, you can use a plain string (the ID) instead of the full object. The arrays mix both forms freely.

### 3.2 `BuildPassive`

Used inside `Build.passives`. Shown in the Passive Skill Tree panel.

| Key | Type | Required | Notes |
|---|---|---|---|
| `id` | string | **Yes** | PassiveSkills table ID. Examples: `strength89`, `melee17`, `marauder_brute_notable1`, `AscendancyWarrior1Notable4`, `jewel_slot1956`. |
| `level_interval` | uint or `[uint, uint]` | No | A single level or `[min, max]`. E.g. `[0, 100]`. |
| `weapon_set` | uint | No | Weapon set index 0-2. For weapon-swap builds. |
| `additional_text` | string | No | Tooltip text on hover. Markup supported. |

### 3.3 `BuildSkill`

Used inside `Build.skills`. Shown in the gem crafting window.

| Key | Type | Required | Notes |
|---|---|---|---|
| `id` | string | **Yes** | BaseItemTypes table ID. E.g. `Metadata/Items/Gems/SkillGemEarthquake`. |
| `level_interval` | uint or `[uint, uint]` | No | |
| `additional_text` | string | No | Markup supported. |
| `support_skills` | array of (string \| `BuildSupport`) | No | Linked support gems. |

**Restriction:** meta gems are **not supported** in v1. The docs say so explicitly.

### 3.4 `BuildSupport`

Used inside `BuildSkill.support_skills`.

| Key | Type | Required | Notes |
|---|---|---|---|
| `id` | string | **Yes** | E.g. `Metadata/Items/Gems/SupportGemFastForward`. |
| `level_interval` | uint or `[uint, uint]` | No | |
| `additional_text` | string | No | |

### 3.5 `BuildInventorySlot`

Used inside `Build.inventory_slots`. Shown as a popup indicator on the inventory panel.

| Key | Type | Required | Notes |
|---|---|---|---|
| `inventory_id` | string | **Yes** | Inventories table ID. See §7. |
| `level_interval` | uint or `[uint, uint]` | No | |
| `unique_name` | string | No | UniqueName entry from the Words table. E.g. `Kalandra's Touch`. |
| `additional_text` | string | No | Markup supported. |

---

## 4. Markup language for `additional_text`

Available in `additional_text`, `description`, and `name`-like text fields. Syntax: `<TAG>{content}`. Tags nest.

### 4.1 Font tags

| Tag | Meaning |
|---|---|
| `<r>` | Regular |
| `<b>` | Bold |
| `<i>` | Italic |
| `<u>` | Underline |
| `<s>` | Small |
| `<m>` | Medium |
| `<l>` | Large |

### 4.2 Colour tags

`<red>`, `<orange>`, `<yellow>`, `<green>`, `<blue>`, `<indigo>`, `<violet>`, `<black>`, `<white>`, `<grey>`, `<bronze>`, `<silver>`, `<gold>`, and custom `<rgb(R, G, B)>` where R, G, B are 0-255.

### 4.3 Nesting

`<m>{<red>{Strength +5 is recommended}}` → medium-sized red text.

`<silver>{Any Two Handed Mace}\n\n<grey>{Stat Priority\n-------------------\n1. Prioritize highest physical dps}` → silver header, grey body, with newlines.

### 4.4 What renders, what doesn't

`\n` produces a line break inside the tooltip. Plain text outside tags renders in the default font and colour.

Unsupported HTML-like tags (e.g. `<br>`, `<p>`) are **not** rendered. Stick to the tag list above.

---

## 5. ID sources (where to look up the canonical IDs)

GGG does not publish a PoE 2 data export. Period. The docs say: "We are currently unable to provide any PoE2-specific data."

In practice, the community has reverse-engineered the canonical IDs:

| ID type | Source |
|---|---|
| **Passive tree node IDs** | https://github.com/repoe-fork/poe2 → `data/passive_skill_trees/Default.json`. Actively maintained (288+ commits as of 29 May 2026), current with the live game. |
| **Skill / Support gem IDs** | Already embedded in **PoB2 XML** as `gemId="Metadata/Items/Gems/..."`. The format is the canonical GGG format. |
| **Inventory slot IDs** | https://github.com/LocalIdentity/poe2-data → `data/inventories.json`. Hand-curated by the PoB2 maintainer. |
| **Ascendancy identifiers** | Both repos above, plus the official `.build` example (which uses `Warrior1` for Titan). |

For Claude in this pack: **never invent IDs.** If you need to translate a human-readable name (e.g. "Strength notable in the Warrior cluster") into a canonical ID, fetch the relevant repo's JSON via `web_fetch` or `bash_tool` and search the data structure. If the lookup fails, **say so** and ask the user to provide the ID or paste a `.build` file that already contains it.

---

## 6. Known ascendancy IDs (partial list)

The `ascendancy` field is a string. **The full canonical mapping for 0.5 is not in the official docs.** What is known:

| Ascendancy | ID (confirmed by GGG example or community) |
|---|---|
| Titan (Warrior) | `Warrior1` (from official example) |
| Warbringer (Warrior) | `Warrior2` (community-confirmed pattern) |
| Smith of Kitava (Warrior) | `Warrior3` `[Unverified, Inference]` |
| Invoker (Monk) | `Monk1` `[Inference]` |
| Acolyte of Chayula (Monk) | `Monk2` `[Inference]` |
| **Martial Artist (Monk, NEW 0.5)** | `Monk3` `[Inference, must verify with repoe-fork data]` |
| Amazon (Huntress) | `Huntress1` `[Inference]` |
| Ritualist (Huntress) | `Huntress2` `[Inference]` |
| **Spirit Walker (Huntress, NEW 0.5)** | `Huntress3` `[Inference, must verify with repoe-fork data]` |
| Other ascendancies | `[Unverified]` — fetch `repoe-fork/poe2` for current mapping |

**For Claude:** when generating a `.build` template, use the inferred ID **only with a clear `[Inference]` warning to the user, and tell them to verify by loading the file into the game and checking the ascendancy renders correctly.**

---

## 7. Known inventory slot IDs

From the official example + community sources:

| Slot | `inventory_id` |
|---|---|
| Main hand weapon | `Weapon1` |
| Off-hand weapon | `Weapon2` `[Inference, common naming]` |
| Body armour | `BodyArmour1` |
| Helmet | `Helm1` |
| Gloves | `Gloves1` |
| Boots | `Boots1` |
| Belt | `Belt1` |
| Amulet | `Amulet1` |
| Left ring | `Ring1` |
| Right ring | `Ring2` |
| Quiver | `Quiver1` `[Inference]` |
| Shield (when not held as weapon) | `Shield1` `[Inference]` |
| **Charms / Flasks** | **NOT YET PUBLISHED.** GGG has not released `inventory_id` values for charm slots. **Do not include charm/flask slots in `.build` files** — the game will reject or ignore them. |

For Claude: if a user asks to add a charm slot to a `.build`, tell them this is currently not supported by the schema. Suggest noting the charm setup in the `description` field instead.

---

## 8. Translation rules (Spanish ↔ English `.build` files)

This is the most important section for the bilingual use case.

### 8.1 What does NOT get translated

**IDs.** Every `id` and `inventory_id` value. These are internal references the game resolves to the player's localized text automatically. A `.build` with `"id": "strength89"` will display "+5 to Strength" in English clients and "+5 a Fuerza" in Spanish clients **without any change to the file.**

This is by design and is a major benefit of the format: **one file, many languages, zero duplication.**

### 8.2 What DOES get translated

Only the human-authored prose:

- `name` (root field).
- `author` (rarely translated — usually a handle).
- `description` (root field).
- All `additional_text` fields, at any nesting level.
- `unique_name` — **special case**: this is the **English unique-name string** from the Words table. **Do not translate it.** The game resolves it to the localized unique name when displayed.

### 8.3 Translation workflow

When the user asks "translate this `.build` to Spanish":

1. Parse the JSON.
2. For each field that gets translated (see §8.2):
   - Translate the prose, preserving all markup tags (`<red>`, `<m>`, `<rgb(...)>`).
   - Preserve all line breaks (`\n`).
   - Preserve all game-specific terms in the prose — game item names, skill names, etc. — **keep them in English** if the original used English. Or use the canonical Spanish translation from `docs/11-glossary-es-en.md` if the original used Spanish. The user picks the convention; don't switch on them mid-build.
3. Leave all `id`, `inventory_id`, and `unique_name` values **untouched**.
4. Write the new JSON to a new file (don't overwrite the original unless the user explicitly asked to).

### 8.4 Output naming convention

Suggested: `<original-name>.es.build` for the Spanish version, `<original-name>.en.build` for the English version. The user can rename freely.

---

## 9. The JSON Schema (use for validation)

Below is a JSON Schema v7-compatible representation of the `.build` format. Use this in tooling (or in Claude's head) to validate files structurally.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "PoE 2 Build Planner File (v1 Experimental)",
  "type": "object",
  "required": ["name"],
  "additionalProperties": false,
  "properties": {
    "name": { "type": "string", "minLength": 1 },
    "author": { "type": "string" },
    "description": { "type": "string" },
    "ascendancy": { "type": "string" },
    "passives": {
      "type": "array",
      "items": { "$ref": "#/definitions/PassiveOrString" }
    },
    "skills": {
      "type": "array",
      "items": { "$ref": "#/definitions/SkillOrString" }
    },
    "inventory_slots": {
      "type": "array",
      "items": { "$ref": "#/definitions/InventorySlot" }
    }
  },
  "definitions": {
    "LevelInterval": {
      "oneOf": [
        { "type": "integer", "minimum": 0 },
        {
          "type": "array",
          "minItems": 2,
          "maxItems": 2,
          "items": { "type": "integer", "minimum": 0 }
        }
      ]
    },
    "PassiveOrString": {
      "oneOf": [
        { "type": "string", "minLength": 1 },
        { "$ref": "#/definitions/BuildPassive" }
      ]
    },
    "BuildPassive": {
      "type": "object",
      "required": ["id"],
      "additionalProperties": false,
      "properties": {
        "id": { "type": "string", "minLength": 1 },
        "level_interval": { "$ref": "#/definitions/LevelInterval" },
        "weapon_set": { "type": "integer", "minimum": 0, "maximum": 2 },
        "additional_text": { "type": "string" }
      }
    },
    "SkillOrString": {
      "oneOf": [
        { "type": "string", "pattern": "^Metadata/Items/Gems/" },
        { "$ref": "#/definitions/BuildSkill" }
      ]
    },
    "BuildSkill": {
      "type": "object",
      "required": ["id"],
      "additionalProperties": false,
      "properties": {
        "id": { "type": "string", "pattern": "^Metadata/Items/Gems/SkillGem" },
        "level_interval": { "$ref": "#/definitions/LevelInterval" },
        "additional_text": { "type": "string" },
        "support_skills": {
          "type": "array",
          "items": { "$ref": "#/definitions/SupportOrString" }
        }
      }
    },
    "SupportOrString": {
      "oneOf": [
        { "type": "string", "pattern": "^Metadata/Items/Gems/SupportGem" },
        { "$ref": "#/definitions/BuildSupport" }
      ]
    },
    "BuildSupport": {
      "type": "object",
      "required": ["id"],
      "additionalProperties": false,
      "properties": {
        "id": { "type": "string", "pattern": "^Metadata/Items/Gems/SupportGem" },
        "level_interval": { "$ref": "#/definitions/LevelInterval" },
        "additional_text": { "type": "string" }
      }
    },
    "InventorySlot": {
      "type": "object",
      "required": ["inventory_id"],
      "additionalProperties": false,
      "properties": {
        "inventory_id": { "type": "string", "minLength": 1 },
        "level_interval": { "$ref": "#/definitions/LevelInterval" },
        "unique_name": { "type": "string" },
        "additional_text": { "type": "string" }
      }
    }
  }
}
```

**Notes on the schema:**

- `additionalProperties: false` everywhere — extra keys are rejected. This matches the conservative reading of the GGG schema, since the docs do not say "any other keys are ignored."
- The `pattern` constraint on skill / support IDs enforces the `Metadata/Items/Gems/` prefix. This catches typos.
- ID-existence validation (e.g. "is `strength89` a real passive?") is **not** in the schema. That requires data from `repoe-fork/poe2` or `LocalIdentity/poe2-data`, fetched live.

---

## 10. Known limitations of the format

These come from the official docs and the NickWeder99/DotBuildExporter README (which is the most-tested community converter).

1. **Meta gems are not supported.** They will be filtered or rejected.
2. **Charm and flask slots are not supported.** GGG hasn't published `inventory_id` for them yet.
3. **Trigger setups with multiple active gems in one socket group** cannot be expressed. The schema accepts one active skill + supports per group. "Skill A triggers Skill B" requires separate entries with `additional_text` explaining the link.
4. **No DPS, EHP, or stat math.** Use Path of Building 2 for that.
5. **The format is "v1 Experimental."** GGG has said it will evolve. The current schema may receive new fields, deprecate existing ones, or change semantics.
6. **Editing inside the game client is not supported.** Players can only load `.build` files; they cannot edit them via the in-game UI.

---

## 11. Workflow: handling `.build` files in this pack

When a user asks Claude to do anything with a `.build` file, the slash command `/build-file` is the entry point. Behind the scenes, Claude:

1. **Reads** the file from disk (filesystem tool, with user confirmation if needed).
2. **Parses** the JSON.
3. **Validates** against the schema in §9 (structural). Optionally fetches `repoe-fork/poe2` to validate passive IDs (live network call).
4. **Performs the requested operation** (translate / annotate / template / summarize).
5. **Writes** the result to a new file (never overwrites the source unless explicitly told).

### 11.1 Operations supported by `/build-file`

| Operation | What it does |
|---|---|
| `read <path>` | Parse the file, summarize human-readably: name, author, ascendancy, # passives, # skills, gear slot hints. |
| `validate <path>` | Run structural validation against the v1 schema. Report errors with line numbers when possible. Optionally validate IDs against `repoe-fork/poe2` (network required). |
| `translate <path> <es|en>` | Translate only the prose fields (see §8.2). Output to a new file with language suffix. |
| `template <ascendancy>` | Generate a minimal valid `.build` skeleton for a given ascendancy. Useful for starting from scratch. |
| `annotate <path> <id> <text>` | Find an existing element by `id` and set/replace its `additional_text`. Adds the element if missing. |
| `merge <path-a> <path-b>` | Combine two builds into one (e.g. a campaign build + a leveling notes build). Manual conflict resolution. |
| `convert-pob <pob-url-or-code>` | Direct the user to NickWeder99's converter (`pob-to-build.exe`). Optionally fetch and pre-parse the PoB code for a summary. |

### 11.2 What Claude must do before writing

- **Confirm with the user** before writing to disk.
- **Show a diff** if modifying an existing file.
- **Validate** before writing.
- **Never silently overwrite** the user's `BuildPlanner/` directory contents.

### 11.3 What Claude must NOT do

- Invent passive / skill IDs.
- Translate IDs, `inventory_id` values, or `unique_name` values.
- Add charms / flasks / meta gems (will fail).
- Add unknown top-level keys (the conservative schema rejects them).

---

## 12. Quick reference: example `.build` files

This pack ships two reference examples in `examples/`:

- **`example-titan-warrior.build`** — the official GGG example from the developer docs, formatted for readability. A Titan Warrior with Earthquake + Boneshatter + Shockwave Totem + Infernal Cry. Use as a sanity-check fixture: it should parse and validate cleanly.
- **`example-spirit-walker.build`** — a minimal Spirit Walker (Huntress, new in 0.5) template with bilingual ES/EN notes. **Most IDs in this file are `[Inference]`** — labeled in `additional_text` and the file's `description`. Verify against `repoe-fork/poe2` before using in-game.

---

## 13. References

- **Official GGG docs:** https://www.pathofexile.com/developer/docs/game#buildplanner
- **Passive tree IDs:** https://github.com/repoe-fork/poe2/blob/master/data/passive_skill_trees/Default.json
- **Inventory slot IDs:** https://github.com/LocalIdentity/poe2-data/blob/main/data/inventories.json
- **PoB2 → `.build` converter:** https://github.com/NickWeder99/DotBuildExporter
- **In-browser PoB2 → `.build` converter:** https://poe2buildplanner.com/
- **Web-based build planner with `.build` export:** https://www.poe2.dev/build-planner/

---

**Last verified:** 29 May 2026 (league launch day). Schema version: 1 (Experimental).
