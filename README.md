# PoE 2 Claude Code Pack — Runes of Aldur (0.5)

A shared Claude Code project for playing **Path of Exile 2 patch 0.5 "Return of the Ancients"** with the **Runes of Aldur** challenge league.

This pack gives Claude Code:
- Up-to-date knowledge about patch 0.5 mechanics, league content, and balance changes.
- Pre-configured MCP servers for live data (currency prices, wiki, datamined items, ladder meta).
- Slash commands for common workflows (character analysis, price check, build validation, `.build` file management).
- Bilingual support (English + Spanish), with automatic translation of game terms when calling tools.

## Prerequisites (must be installed by you, before Claude can do the rest)

| Requirement | Why | Install command |
|---|---|---|
| Claude Code | The CLI itself | https://docs.claude.com/en/docs/claude-code/overview |
| Node.js ≥ 22 | Runs the JS MCP servers | `brew install node` / `winget install OpenJS.NodeJS.LTS` / `apt install nodejs` |
| Python ≥ 3.9 | Runs the Python MCP server | `brew install python` / `winget install Python.Python.3.12` / `apt install python3 python3-pip` |
| git | Cloning | `brew install git` / `winget install Git.Git` / `apt install git` |
| A pathofexile.com account | For trade and character tools | https://www.pathofexile.com |

## Install (3 commands, then Claude does the rest)

```bash
git clone <REPO_URL_HERE> poe2-claude-pack
cd poe2-claude-pack
claude
```

That's it. The first time you run `claude` in this folder:

1. Claude reads `CLAUDE.md`, runs a setup check, and detects that nothing is installed yet.
2. Claude asks for permission to clone the 3 MCP servers into `../mcps/` and build them.
3. Claude asks once for an email address (any valid email of yours) needed by the POE2Scout API.
4. Claude rewrites `.mcp.json` with the correct absolute paths for your machine.
5. Claude tells you to close `claude` (Ctrl+D) and reopen it.
6. On reopen, Claude Code asks you to approve the 3 project-scope MCPs — accept all 3.
7. Done. Ask Claude anything.

Total interaction: a few `y` confirmations and one email. Maybe 5 minutes total depending on `npm install` speed.

## What's in this repo

```
poe2-claude-pack/
├── CLAUDE.md                       # Project memory + auto-setup instructions
├── README.md                       # This file
├── .mcp.json                       # MCP config (rewritten by Claude on first run)
├── .gitignore
├── docs/                           # Modular knowledge base
│   ├── PROJECT.md                  # Project manifesto — what & why
│   ├── 00-patch-overview.md
│   ├── 01-mcps-and-tools.md
│   ├── 02-mcp-quirks.md
│   ├── 03-workflows.md
│   ├── 04-game-mechanics-0.5.md
│   ├── 05-ascendancies-new.md
│   ├── 06-ascendancies-changes.md
│   ├── 07-runes-of-aldur.md
│   ├── 08-endgame-atlas.md
│   ├── 09-currency-economy.md
│   ├── 10-passive-tree-changes.md
│   ├── 11-glossary-es-en.md
│   ├── 12-anti-hallucination.md
│   └── 13-build-file-format.md     # .build planner JSON format + JSON Schema
├── examples/
│   ├── example-titan-warrior.build  # Official GGG sample
│   └── example-spirit-walker.build  # Spirit Walker template (Inferred IDs)
├── .claude/
│   └── commands/                   # Slash commands
│       ├── analyze-char.md
│       ├── build-check.md
│       ├── build-file.md           # .build file operations
│       ├── meta.md
│       ├── price.md
│       ├── upgrade-stat.md
│       └── wiki.md
└── user/
    ├── README.md                   # How to set up personal context
    └── _template.md                # Template for CLAUDE.local.md
```

## Bilingual support

Two users play in Spanish, the rest in English. Claude responds in whichever language you asked in. Internally, it translates game terms to English before calling tools (the MCPs only accept English). Glossary in `docs/11-glossary-es-en.md`.

## Optional: HivemindOverlord trade auth

If you want to use the official trade site search (`search_trade_items`), run **outside `claude`**:

```bash
pip3 install playwright
playwright install chromium
python3 -m poe2_mcp.scripts.setup_trade_auth
```

A browser opens, you log into pathofexile.com, the session is saved. Then trade search works inside Claude.

## Optional: personal context file

After install, Claude will ask if you want to create `CLAUDE.local.md` (gitignored) with your account name, character names, language preference, etc. See `user/_template.md` for what goes in it.

## Maintenance

When GGG ships a 0.5.x point patch:
1. Update `docs/00-patch-overview.md`.
2. Update affected mechanics docs.
3. Bump the "Last verified content date" at the bottom of `CLAUDE.md`.
4. Push, others pull.

If a tool returns data that contradicts a doc, **trust the tool, not the doc.**

## Manual install (in case the auto-setup fails)

```bash
mkdir -p ../mcps && cd ../mcps

git clone https://github.com/sergeyklay/poe2-mcp-server.git
cd poe2-mcp-server && npm install && npm run build && cd ..

git clone https://github.com/vanzan01/poe2scout-mcp.git
cd poe2scout-mcp && npm install && npm run build && cd ..

pip3 install poe2-mcp

cd ../poe2-claude-pack
# Edit .mcp.json: replace ABSOLUTE_PATH_TO_sergeyklay_poe2-mcp-server with
# the absolute path to ../mcps/poe2-mcp-server, same for poe2scout, and
# replace YOUR_EMAIL_HERE with your email.

claude
```

## License & disclaimer

Community project, not affiliated with Grinding Gear Games or Anthropic. Path of Exile is a trademark of GGG. The MCP servers referenced are third-party community projects.
