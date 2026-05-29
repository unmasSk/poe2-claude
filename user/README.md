# User Personal Context

This folder is for **personal context that should NOT be committed to the shared repo**: your pathofexile.com account name, character names, playstyle preferences, language preferences, etc.

You have two options for storing this.

---

## Option A: Project-scoped `CLAUDE.local.md` (recommended)

Create a `CLAUDE.local.md` at the **project root** (the same folder as `CLAUDE.md`):

```bash
cp user/_template.md ../CLAUDE.local.md
# Edit ../CLAUDE.local.md with your details
```

This file is **gitignored**. Each user has their own. Claude Code reads it automatically alongside `CLAUDE.md`.

**Pros:**
- Loaded automatically every session.
- Project-scoped — only applies when working in this folder.
- Different colleagues can have different personal files on the same machine.

**Cons:**
- Re-create per machine.

---

## Option B: User-scoped `~/.claude/CLAUDE.md`

Create a file at `~/.claude/CLAUDE.md` (your home directory's `.claude` folder):

```bash
mkdir -p ~/.claude
cp user/_template.md ~/.claude/CLAUDE.md
# Edit ~/.claude/CLAUDE.md
```

This file is loaded by Claude Code **across all your projects**, not just this one.

**Pros:**
- One place; applies everywhere.
- Survives if you re-clone this repo.

**Cons:**
- Mixes PoE-specific preferences with any other project preferences you have. Not recommended unless you only use Claude Code for PoE 2.

---

## What goes in your personal file

See `user/_template.md` for the template. The essential fields:

- **Account name** on pathofexile.com.
- **Character names** in the active league (and which ascendancy each is).
- **Preferred language** for Claude's responses (English / Spanish).
- **League variant** (Standard / Hardcore / SSF / HC SSF / Standard pre-existing).
- **Playstyle preferences** (trade vs SSF, mapping focus vs bossing, etc.).
- **Standing instructions** (e.g. "Always state which tool you used", "Never recommend gear over 10 exalts unless I ask").

---

## What does NOT go in the personal file

- **Passwords** — never.
- **POESESSID cookie** — this is set up via the in-Claude `setup_trade_auth` MCP tool (not the non-existent `python -m poe2_mcp.scripts.setup_trade_auth` CLI) and stored by the MCP server, not in any markdown file.
- **API keys** — there are no API keys needed for the standard tool set (`poe2`, `poe2-optimizer`); only `POE2SCOUT_CONTACT_EMAIL` for poe2scout (set that in `.mcp.json` directly).
- **Personal info that isn't relevant to PoE** — keep Claude focused on PoE.

---

## Sharing builds within the team

The shared repo is fine for **non-personal** team knowledge:
- Build guides specific to this group.
- Currency-pooling agreements.
- Shared SSF rules if you're playing private league.

If you want to share builds in the repo (not personal account info), create a new `docs/builds/` folder (not gitignored) and put public build-guides there. Add a PR.

---

## Privacy reminder

Even gitignored files can leak via screenshots, accidental commits (`git add -A`), or Discord pastes. Treat your `CLAUDE.local.md` as **mildly sensitive** — character names map back to your account, which is public on poe.ninja anyway, but the file may also contain personal preferences you don't want shared.
