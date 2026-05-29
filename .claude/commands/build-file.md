---
description: Read, validate, translate, template, or annotate PoE 2 .build planner files (v1 Experimental format)
allowed-tools: Read, Write, Edit, Bash, WebFetch
---

Operate on a PoE 2 `.build` file. First argument is the operation. Remaining arguments depend on operation.

Arguments: $ARGUMENTS

# Operations

## `read <path>`
Parse the `.build` file at the given path. Output a human-readable summary:
- Name, author, ascendancy.
- Number of passives, skills, inventory hints.
- Markup-stripped excerpt of `description`.
- List of skills with their support gem links.
- List of inventory slots with their unique_name or stat-priority excerpt.

Respond in the user's language.

## `validate <path>`
Run structural validation against the v1 schema documented in `docs/13-build-file-format.md` §9. Steps:

1. Parse JSON. Fail fast with a clear error if it's malformed.
2. Check required fields: root requires `name`. Passives/skills/supports require `id`. Inventory slots require `inventory_id`.
3. Check types and patterns:
   - Skill IDs match `^Metadata/Items/Gems/SkillGem`.
   - Support IDs match `^Metadata/Items/Gems/SupportGem`.
   - `weapon_set` is integer 0-2.
   - `level_interval` is uint or `[uint, uint]`.
4. Check for known limitations:
   - Warn if any inventory slot uses `inventory_id` for charms or flasks (not supported in v1).
   - Warn if any skill ID corresponds to a known meta gem (not supported in v1).
5. Optionally (if user passed `--check-ids` flag), fetch `https://raw.githubusercontent.com/repoe-fork/poe2/master/data/passive_skill_trees/Default.json` and verify each passive ID exists. Report unknown IDs. **Mention that this requires network access.**

Output: a verdict (✅ valid / ⚠️ valid with warnings / ❌ invalid), followed by a numbered list of issues with line numbers when possible. Respond in the user's language.

## `translate <path> <es|en>`
Translate only the prose fields. **NEVER touch any `id`, `inventory_id`, or `unique_name` values.** Translatable fields are:
- root `name`
- root `author` (rarely translated; ask the user first)
- root `description`
- every `additional_text` at any nesting depth

Steps:

1. Parse the source file.
2. Detect the source language by sampling `description` and the first few `additional_text` fields.
3. If source language matches the target, tell the user and ask if they want to proceed anyway (no-op risk).
4. For each translatable field:
   - Preserve every markup tag (`<red>`, `<m>`, `<rgb(r,g,b)>`, etc.) exactly.
   - Preserve every line break (`\n`).
   - Translate game terms using `docs/11-glossary-es-en.md` as the canonical reference.
   - Keep canonical unique-name strings in English where they appear in prose (those resolve to the localized name in-game).
5. Write to `<original-stem>.<lang>.build` in the same directory (e.g. `joserules.es.build`). **Do not overwrite the original** unless the user explicitly asked to.
6. Show a diff summary: number of fields translated, total characters changed.

## `template <ascendancy>`
Generate a minimal valid `.build` skeleton for the given ascendancy.

1. Map the ascendancy name (Spanish or English) to the canonical ID using `docs/13-build-file-format.md` §6. Use `[Inference]` warnings for IDs marked as such.
2. Output a JSON file with:
   - `name`: "<Ascendancy> Template"
   - `author`: "poe2-claude"
   - `description`: a starter description explaining this is a skeleton, in both languages if the user is bilingual.
   - `ascendancy`: the inferred ID.
   - `passives`: empty array (`[]`).
   - `skills`: empty array (`[]`).
   - `inventory_slots`: array of 9 slots (Weapon1, BodyArmour1, Helm1, Gloves1, Boots1, Belt1, Amulet1, Ring1, Ring2) with empty `additional_text` placeholders.
3. Save to `<lowercase-ascendancy>-template.build` in the user's current directory (or ask the user where).
4. Show the file. Highlight `[Inference]` markers prominently.

## `annotate <path> <element-id> <text>`
Find an existing passive / skill / support / inventory-slot by its `id` (or `inventory_id`) and set or replace its `additional_text`.

1. Parse the file.
2. Search recursively for an element matching the given ID.
3. If found: show the user the current `additional_text` (if any) and the proposed new value. Ask for confirmation.
4. If not found: ask the user if they want to **add** the element to the appropriate array.
5. On confirmation, write the modified file. **Show a diff before writing.**

## `merge <path-a> <path-b>`
Combine two `.build` files into one.

1. Parse both files.
2. If the ascendancies differ, **stop and warn the user.** Merging across ascendancies usually doesn't make sense.
3. Merge rules:
   - `name`: ask the user which to keep (or to provide a new one).
   - `author`: combine as "author-a + author-b" or ask.
   - `description`: concatenate with a separator, or ask.
   - `passives`: union by `id`. If both have an entry with the same `id` but different `additional_text`, **ask the user** which to keep.
   - `skills`: same union-by-id logic. Support skills inside each skill: same union-by-id.
   - `inventory_slots`: union by `inventory_id`. Same conflict-resolution.
4. Save to a new file. **Never overwrite either input.**

## `convert-pob <pob-url-or-code>`
The user has a Path of Building 2 build (URL, share code, or XML) and wants a `.build` file.

1. **Do NOT attempt to reimplement the conversion in this slash command.** A maintained converter already exists: https://github.com/NickWeder99/DotBuildExporter (MIT licensed, single-file Windows executable). For non-Windows users, the in-browser converter at https://poe2buildplanner.com/ works.
2. Detect which kind of input the user has (URL pattern `https://pobb.in/<id>`, raw share code, XML file path).
3. Provide step-by-step instructions:
   - **Windows:** download `pob-to-build.exe` from https://github.com/NickWeder99/DotBuildExporter/releases/latest, run `pob-to-build.exe <input>`, output appears in the current directory.
   - **Cross-platform:** open https://poe2buildplanner.com/, paste the URL or code, click Convert, download the `.build` file.
4. If the user gives a `pobb.in` URL, optionally fetch it (via `WebFetch`) to verify it's a real PoE 2 build (not PoE 1) and offer a structural preview before they convert.
5. Remind the user that the resulting file goes in `Documents/My Games/Path of Exile 2/BuildPlanner/`.

---

# Universal rules

- **Never invent IDs.** If a passive or skill ID is not in the source data and the user can't provide it, say so.
- **Never overwrite a user's file silently.** Always show a diff and confirm.
- **Never write to the user's `BuildPlanner/` directory** unless the user explicitly asked. Write to the current working directory by default.
- **Preserve every markup tag and `\n` byte** during translation or annotation.
- **Validate before writing.** A broken `.build` file in `BuildPlanner/` may cause the in-game Build Planner to refuse to load any builds.

# Output language

Respond in the user's language. Game term names stay in English with Spanish in parentheses when useful. Use the glossary in `docs/11-glossary-es-en.md`.

# Reference

Full schema, markup details, ID sources, and translation rules are in `docs/13-build-file-format.md`. Read it if you haven't.
