#!/usr/bin/env python3
"""
pob_extract.py — Extract the FULL build from a Path of Building 2 share URL.

Why this exists: the MCP tool `poe2_pob_decode` only returns a shallow summary
(skill/item names, "0 nodes", no mods, no sockets, no computed stats). But a PoB
share actually embeds the COMPLETE build as a zlib-compressed, base64url-encoded
XML — including every PlayerStat PoB already CALCULATED (AverageDamage, TotalDPS,
CritChance, CritMultiplier, etc.), the full allocated passive tree, every item with
all its mods, sockets/runes, and gems.

So instead of re-deriving DPS by hand from partial data (which is unreliable), we
read the number PoB itself computed. Claude becomes the analyst on top of real data.

USAGE:
    python tools/pob_extract.py <pobb.in URL or id>
    python tools/pob_extract.py https://pobb.in/OMzcWYx0-dMN

NOTE ON SOURCES:
    - pobb.in/<id>/raw  -> returns the raw PoB code directly. WORKS.
    - poe.ninja/poe2/pob/<id> -> returns an HTML/JS page, NOT the code. Does NOT work
      with this script. Ask the user to re-upload their build to pobb.in (PoB2:
      Import/Export -> Upload to pobb.in) and pass that URL instead.

Requires: only the Python stdlib (urllib, base64, zlib, re).
"""
import sys, re, base64, zlib, urllib.request


def fetch_raw(url_or_id: str) -> str:
    """Return the raw PoB code string from a pobb.in URL or bare id."""
    s = url_or_id.strip()
    # extract id if a full URL was given
    m = re.search(r'pobb\.in/([A-Za-z0-9_\-]+)', s)
    pob_id = m.group(1) if m else s
    if 'poe.ninja' in s:
        raise SystemExit(
            "poe.ninja URLs don't expose the raw PoB code. "
            "Re-upload the build to pobb.in (PoB2: Import/Export -> Upload to pobb.in) "
            "and pass that URL instead."
        )
    raw_url = f"https://pobb.in/{pob_id}/raw"
    req = urllib.request.Request(raw_url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", "replace").strip()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise SystemExit(f"pobb.in paste '{pob_id}' not found (404). Check the URL/id and that the paste still exists.")
        raise SystemExit(f"pobb.in returned HTTP {e.code} for '{pob_id}'. Try again, or re-upload the build.")
    except urllib.error.URLError as e:
        raise SystemExit(f"Could not reach pobb.in ({e.reason}). Check your connection.")
    if not body or body.lstrip().startswith("<"):
        raise SystemExit(f"pobb.in/{pob_id}/raw did not return a PoB code (got HTML/empty). Check the id is a real pobb.in paste.")
    return body


def decode_pob(raw: str) -> str:
    """base64url + zlib inflate -> PoB XML."""
    s = raw.replace('-', '+').replace('_', '/')
    s += '=' * (-len(s) % 4)
    try:
        xml = zlib.decompress(base64.b64decode(s)).decode("utf-8", "replace")
    except Exception as e:
        raise SystemExit(f"Could not decode the PoB code ({e}). If you pasted a raw base64 "
                         f"code it may have been corrupted in transit — re-upload to pobb.in "
                         f"and pass the URL instead.")
    if "<PathOfBuilding" not in xml:
        raise SystemExit("Decoded data is not a Path of Building build.")
    return xml


def summarize(xml: str) -> str:
    out = []
    # --- computed stats (the gold: PoB already did the math) ---
    stats = {}
    for val, stat in re.findall(r'<PlayerStat value="([^"]+)" stat="([^"]+)"', xml):
        stats[stat] = val
    for stat, val in re.findall(r'<PlayerStat stat="([^"]+)" value="([^"]+)"', xml):
        stats[stat] = val
    out.append("== COMPUTED STATS (from PoB itself) ==")
    for k in ["AverageDamage", "AverageBurstDamage", "TotalDPS", "CombinedDPS", "FullDPS",
              "WithDotDPS", "TotalDot", "Speed", "PreEffectiveCritChance", "CritChance",
              "CritMultiplier", "HitChance", "Life", "EnergyShield", "Mana",
              "Str", "Dex", "Int"]:
        if k in stats:
            out.append(f"  {k:24} = {stats[k]}")
    out.append(f"  (total stats available: {len(stats)})")

    # --- build header ---
    b = re.search(r'<Build([^>]*)>', xml)
    if b:
        lvl = re.search(r'level="(\d+)"', b.group(1))
        cls = re.search(r'className="([^"]+)"', b.group(1))
        asc = re.search(r'ascendClassName="([^"]+)"', b.group(1))
        out.append("\n== BUILD ==")
        out.append(f"  class={cls.group(1) if cls else '?'} "
                   f"ascend={asc.group(1) if asc else '?'} "
                   f"level={lvl.group(1) if lvl else '?'}")

    # --- passive tree ---
    nodes = re.findall(r'nodes="([0-9,]+)"', xml)
    if nodes:
        out.append(f"  allocated passive nodes: {len(nodes[0].split(','))}")

    # --- skills / gems ---
    out.append("\n== SKILLS / GEMS ==")
    for skill in re.findall(r'<Skill [^>]*>(.*?)</Skill>', xml, re.S):
        gems = re.findall(r'nameSpec="([^"]+)"', skill)
        if gems:
            out.append("  - " + " + ".join(gems))

    # --- items with mods ---
    out.append("\n== ITEMS (full mods) ==")
    for it in re.findall(r'<Item [^>]*>(.*?)</Item>', xml, re.S):
        lines = [l.strip() for l in it.splitlines() if l.strip()
                 and not l.strip().startswith('<')]
        if lines:
            out.append("  ---")
            out.extend("  " + l for l in lines)
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    raw = fetch_raw(sys.argv[1])
    xml = decode_pob(raw)
    print(summarize(xml))
    print("\n# XML fully extracted: %d chars. All tree/items/mods/stats available." % len(xml))
