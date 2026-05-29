# poe2-claude — Runes of Aldur (0.5)

A shared Claude Code project for playing **Path of Exile 2 patch 0.5 "Return of the Ancients"** with the **Runes of Aldur** challenge league.

This project gives Claude Code:
- Up-to-date knowledge about patch 0.5 mechanics, league content, and balance changes.
- Pre-configured MCP servers for live data (currency prices, wiki, datamined items, ladder meta).
- Slash commands for common workflows (character analysis, price check, build validation, `.build` file management).
- Bilingual support (English + Spanish), with automatic translation of game terms when calling tools.

## Prerequisites (must be installed by you, before Claude can do the rest)

| Requirement | Why | Install command |
|---|---|---|
| Claude Code | The CLI itself | https://docs.claude.com/en/docs/claude-code/overview |
| Node.js ≥ 22 | Runs the JS MCP servers | `brew install node` / `winget install OpenJS.NodeJS.LTS` / `apt install nodejs` |
| Python ≥ 3.11 | Runs the Python MCP server (3.11 verified at launch) | `brew install python` / `winget install Python.Python.3.12` / `apt install python3 python3-pip` |
| git | Cloning | `brew install git` / `winget install Git.Git` / `apt install git` |
| A pathofexile.com account | For trade and character tools | https://www.pathofexile.com |

## Install (3 commands, then Claude does the rest)

```bash
git clone https://github.com/unmasSk/poe2-claude.git
cd poe2-claude
claude
```

That's it. The first time you run `claude` in this folder:

1. Claude reads `CLAUDE.md`, runs a setup check, and detects that nothing is installed yet.
2. Claude asks for permission to clone the 3 MCP servers into `../mcps/` and build them.
3. Claude asks once for an email address (any valid email of yours) needed by the POE2Scout API.
4. Claude creates `.mcp.json` from the template with the correct absolute paths, your email, and freshly generated optimizer keys.
5. Claude tells you to close `claude` (Ctrl+D) and reopen it.
6. On reopen, Claude Code asks you to approve the 3 project-scope MCPs — accept all 3.
7. Done. Ask Claude anything.

Total interaction: a few `y` confirmations and one email. Maybe 5 minutes total depending on `npm install` speed.

## Usage / Cómo usar

Once installed and reopened, just talk to Claude. You don't need to memorize commands — ask in plain language, in **English or Spanish**. The slash commands are shortcuts for common workflows, not the only way in.

> Una vez instalado y reabierto, simplemente habla con Claude. No necesitas memorizar comandos — pregunta en lenguaje normal, en **inglés o español**. Los slash commands son atajos para tareas comunes, no la única forma de usarlo.

### First message / Primer mensaje

You don't need a special opening. A good first message just states what you play and what you want:

> No necesitas un mensaje especial. Un buen primer mensaje dice qué juegas y qué quieres:

```
EN:  Hi! I'm playing a Spirit Walker in Runes of Aldur. What can you help me with?
ES:  ¡Hola! Estoy jugando un Caminante Espiritual en Runes of Aldur. ¿En qué me puedes ayudar?
```

Tip: the very first time, tell Claude your account/character names so it can look you up — or set them once in `CLAUDE.local.md` (see below) and never repeat them.

> Consejo: la primera vez, dile a Claude tu nombre de cuenta/personaje para que pueda buscarte — o ponlos una vez en `CLAUDE.local.md` (ver abajo) y no los repitas más.

### Typical questions / Preguntas típicas

You can just ask. Each pair below does the same thing in both languages:

> Puedes simplemente preguntar. Cada par hace lo mismo en ambos idiomas:

```
Price / Precio
EN:  How much is a Divine Orb right now?
ES:  ¿Cuánto vale ahora mismo un Divine Orb?

Build advice / Consejo de build
EN:  Is Spirit Walker good for league start? What archetype works?
ES:  ¿Es bueno Spirit Walker para empezar la liga? ¿Qué arquetipo funciona?

Wiki / mechanics / Mecánicas
EN:  How does Runic Ward work in 0.5?
ES:  ¿Cómo funciona Runic Ward (Guardia Rúnica) en 0.5?

Character analysis / Análisis de personaje
EN:  Analyze my character "MyChar" on account "MyAccount#1234".
ES:  Analiza mi personaje "MiPersonaje" de la cuenta "MiCuenta#1234".

Upgrade hunting / Buscar mejoras
EN:  What's the cheapest way to get more fire resistance on my character?
ES:  ¿Cuál es la forma más barata de subir resistencia a fuego en mi personaje?

Build files / Ficheros .build
EN:  Read examples/example-titan-warrior.build and explain it to me.
ES:  Lee examples/example-titan-warrior.build y explícamelo.
```

### Slash commands (shortcuts / atajos)

Type `/` in Claude Code to see them. One use-case each:

> Escribe `/` en Claude Code para verlos. Un caso de uso por cada uno:

| Command | What it does / Qué hace | Example / Ejemplo |
|---|---|---|
| `/price` | Price check an item or currency / Precio de un item o moneda | `/price Divine Orb` |
| `/analyze-char` | Full character analysis from poe.ninja / Análisis completo de personaje | `/analyze-char MyChar` |
| `/build-check` | Validate gem combos & defensive gaps / Valida gemas y huecos defensivos | `/build-check` |
| `/meta` | Current ladder meta snapshot / Foto del meta actual | `/meta huntress` |
| `/upgrade-stat` | Cheapest way to gain a stat / Forma más barata de subir un stat | `/upgrade-stat fire resistance` |
| `/wiki` | Search the wiki + fetch the article / Busca en la wiki y trae el artículo | `/wiki Energy Shield` |
| `/build-file` | Read/validate/translate/template `.build` files / Operaciones sobre `.build` | `/build-file read examples/example-titan-warrior.build` |
| `/dps` | Interpret a PoB build's DPS or diagnose damage / Interpreta el DPS de un PoB o diagnostica daño | `/dps https://pobb.in/xxxx` |

### What Claude CANNOT do here / Lo que Claude NO puede hacer aquí

Set your expectations honestly. This pack does **not**:

> Para que no te lleves sorpresas. Este pack **no**:

- **Calculate exact DPS/EHP** for 0.5 builds. No tool does PoB-level math for the new ascendancies. Use Path of Building 2 for final numbers. / **Calcular DPS/EHP exactos** de builds 0.5. Usa Path of Building 2 para números finales.
- **Buy, sell, or whisper traders.** It reads the market; it doesn't act on it. / **Comprar, vender ni susurrar.** Lee el mercado; no actúa en él.
- **Invent uniques, mods, or node IDs.** If a tool can't confirm it, Claude says "not found" instead of guessing. / **Inventar uniques, mods o IDs.** Si una tool no lo confirma, Claude dice "no encontrado" en vez de adivinar.
- **Give reliable meta in the first 24-48h** of the league — ladder data is too noisy. / **Dar un meta fiable en las primeras 24-48h** de liga — la ladder es demasiado ruidosa.

Full philosophy in [`docs/PROJECT.md`](docs/PROJECT.md). / Filosofía completa en [`docs/PROJECT.md`](docs/PROJECT.md).

### Troubleshooting

| Symptom / Síntoma | Fix |
|---|---|
| Price tools return "No items found" for Runes of Aldur / Las tools de precio devuelven "No items found" | Normal in the first 6-24h of league — poe.ninja/poe2scout haven't indexed it yet. Try again later, or ask for a `Standard` price as a rough reference. / Normal las primeras 6-24h — aún no han indexado la liga. Reintenta más tarde o pide precio en `Standard` como referencia. |
| Claude says an MCP isn't loaded / Claude dice que un MCP no está cargado | Close (`Ctrl+D`) and reopen `claude`; approve the 3 MCPs when asked. / Cierra (`Ctrl+D`) y reabre `claude`; aprueba los 3 MCPs. |
| `search_items` / "list all helmets" fails / falla | Known upstream limitation (empty items DB). Ask Claude to use the wiki or poe2db.tw instead. / Limitación upstream conocida (DB de items vacía). Pide usar la wiki o poe2db.tw. |
| Setup check keeps failing / El chequeo de setup sigue fallando | Tell Claude "run the setup check and fix what's broken" — it re-runs §0 of `CLAUDE.md`. / Dile a Claude "run the setup check and fix what's broken". |

## What's in this repo

```
poe2-claude/
├── CLAUDE.md                       # Project memory + auto-setup instructions
├── README.md                       # This file
├── .mcp.json.canonical             # MCP config template (Claude copies it to .mcp.json on first run)
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
│   ├── 13-build-file-format.md     # .build planner JSON format + JSON Schema
│   ├── 14-campaign-guide.md        # Campaign router (Acts 1-4 + trials), wiki-sourced
│   ├── 15-ascendancy-trials.md     # Sekhemas vs Chaos trials, wiki-sourced
│   ├── 18-dps-and-damage.md        # How DPS maths works + what Claude can/can't compute
│   └── KNOWN-ISSUES.md             # Verified upstream tooling limitations (team-shared)
├── LICENSE                         # MIT
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

If you want to use the official trade site search (`search_trade_items`), you need a logged-in pathofexile.com session (POESESSID). First install the browser dependency **outside `claude`**:

```bash
pip3 install playwright
playwright install chromium
```

Then, **inside `claude`**, ask it to run the `setup_trade_auth` tool. A browser opens, you log into pathofexile.com, and the session is saved. Trade search then works inside Claude.

> Note: the standalone CLI command some older docs mention (`python -m poe2_mcp.scripts.setup_trade_auth`) does **not** exist in the published `poe2-mcp` package — the trade-auth flow is only available as the in-Claude `setup_trade_auth` tool.

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

# Generate the two crypto keys the optimizer needs (NOT in its README).
# Run this once and copy both values:
python -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32)); print('ENCRYPTION_KEY=' + secrets.token_urlsafe(32))"

cd ../poe2-claude
cp .mcp.json.canonical .mcp.json
# Now edit .mcp.json:
#  - Replace ABSOLUTE_PATH_TO_sergeyklay_poe2-mcp-server/dist/index.js with the
#    absolute path to ../mcps/poe2-mcp-server/dist/index.js (same for poe2scout).
#  - Replace YOUR_EMAIL_HERE with your email.
#  - Replace GENERATED_PER_USER_HEX_64 / GENERATED_PER_USER_URLSAFE_32 with the
#    two keys you just generated.

claude
```

> **Why the optimizer entry looks unusual.** The published `poe2-mcp` package has upstream packaging bugs: its console script is broken, its module is named `src` (not `poe2_mcp`), and it needs `SECRET_KEY`/`ENCRYPTION_KEY` env vars that aren't documented. The `.mcp.json.canonical` template already encodes the working invocation (`python -m src.mcp_server` + the two keys), so just fill in the placeholders. Details in [`docs/01-mcps-and-tools.md`](docs/01-mcps-and-tools.md) and [`docs/KNOWN-ISSUES.md`](docs/KNOWN-ISSUES.md).

### Reproducibility (pinned versions)

The manual install pulls the latest version of each dependency. The documented workarounds (the `python -m src.mcp_server` optimizer entry, the key generation, the `dist/index.js` build steps) were verified against **specific versions on 29 May 2026**:

- **`poe2-mcp`** (HivemindOverlord optimizer): pip `poe2-mcp==1.0.0`
- **`poe2-mcp-server`** (sergeyklay): git commit `d2c9a7e`
- **`poe2scout-mcp`** (vanzan01): git commit `14187e6`

Newer releases may *fix* the documented bugs — or *break* the workarounds. If a fresh install misbehaves, pin to the versions above and re-verify before debugging further:

```bash
pip install poe2-mcp==1.0.0
git -C ../mcps/poe2-mcp-server checkout d2c9a7e
git -C ../mcps/poe2scout-mcp checkout 14187e6
```

## License & disclaimer

Licensed under the [MIT License](LICENSE). Community project, not affiliated with Grinding Gear Games or Anthropic. Path of Exile is a trademark of GGG. The MCP servers referenced are third-party community projects.
