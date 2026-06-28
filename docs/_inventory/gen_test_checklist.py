#!/usr/bin/env python3
"""Generate the master manual-test checklist markdown from manuals + plugin code."""
import os, re, glob

ROOT = '/usr/share/nginx/archive'
PLUGDIR = f'{ROOT}/atom-ahg-plugins'
CAT = f'{ROOT}/atom-extensions-catalog/docs'

plugins = sorted(d for d in os.listdir(PLUGDIR) if re.match(r'ahg.*Plugin$', d) and os.path.isdir(f'{PLUGDIR}/{d}'))
user_md = [os.path.basename(f) for f in glob.glob(f'{CAT}/*.md')]
tech_md = {os.path.basename(f)[:-3]: f for f in glob.glob(f'{CAT}/technical/*.md')}

def toks(n):
    s = re.sub(r'^ahg|Plugin$', '', n)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s).lower()
    return [x for x in s.split('-') if len(x) > 2]

def find_user_guide(p):
    parts = toks(p)
    if not parts:
        return None
    best = None
    for fn in user_md:
        if 'user-guide' not in fn.lower() and 'manual' not in fn.lower():
            continue
        score = sum(1 for pt in parts if pt in fn.lower())
        if score >= max(1, len(parts) - 1):
            if best is None or len(fn) < len(best):
                best = fn
    return best

def extract_user_items(ugfile):
    items = []
    for l in open(f'{CAT}/{ugfile}', errors='ignore'):
        m = re.match(r'^#{2,4}\s+(.+)', l.strip())
        if not m:
            continue
        h = m.group(1).strip()
        if re.match(r'(Overview|User Guide|Table of|Quick Reference|Troubleshooting|Introduction|Conclusion|Index)$', h, re.I):
            continue
        if len(h) > 90 or h.startswith('+'):
            continue
        items.append(h)
    return items[:40]

def extract_routes(p):
    routes = []
    for cf in glob.glob(f'{PLUGDIR}/{p}/config/*Configuration.class.php'):
        txt = open(cf, errors='ignore').read()
        for m in re.finditer(r"->(?:any|get|post|put|delete)\(\s*'[^']*'\s*,\s*'([^']+)'\s*,\s*'([^']+)'", txt):
            routes.append((m.group(1), m.group(2)))
    seen = set(); out = []
    for path, act in routes:
        if path in seen: continue
        seen.add(path); out.append((path, act))
    return out[:60]

def extract_cli(p):
    cli = []
    for tf in glob.glob(f'{PLUGDIR}/{p}/lib/task/*.php'):
        txt = open(tf, errors='ignore').read()
        ns = re.search(r"\$this->namespace\s*=\s*'([^']+)'", txt)
        nm = re.search(r"\$this->name\s*=\s*'([^']+)'", txt)
        if ns and nm:
            cli.append(f"php symfony {ns.group(1)}:{nm.group(1)}")
    return sorted(set(cli))

# Authored feature-level functionality for plugins with no user manual yet (#enrich-6).
AUTHORED = {
    'ahgRdmPlugin': [
        "Create a dataset (title, description, optional research project)",
        "Deposit files into a dataset (each becomes a child IO + master digital object)",
        "Run POPIA scan (deterministic SA-ID/email/phone/passport + special-category lexicon + gateway NER + scanned-PDF OCR)",
        "View masked scan findings + dataset verdict (CLEAR / PERSONAL / SPECIAL_CATEGORY)",
        "Human gate: confirm or dismiss each finding with a decision note",
        "Open release is BLOCKED while any PERSONAL/SPECIAL finding is pending or confirmed",
        "Apply a disposition: restrict / embargo / de-identify / release",
        "Restricted dataset files relocated off /uploads; raw URL returns 404; download only via ODRL-gated controller",
        "DataCite DOI minted on disposition (live only on a production DOI config; else reserved test-prefix)",
        "Public citable landing page (DataCite-style citation + DOI + access badge; binaries stay gated)",
        "Link or create-and-link a Data Management Plan (DMP) to a dataset",
        "Compliance scoreboard, filterable by institution / verdict / disposition (admin)",
        "Roll-up dashboard: 8 KPI cards + 5 Chart.js charts + date/faculty filters (admin)",
        "ACL: dataset mutations deny a non-owner non-admin; index scoped to depositor; dashboard/compliance admin-only",
    ],
    'ahg3DModelPlugin': [
        "View a 3D model on an information object (Google <model-viewer>)",
        "Gaussian Splat model rendering",
        "Augmented-reality (AR) view on a supported device",
        "Upload a 3D model (GLB/OBJ/PLY/STL/USDZ) — staff",
        "Select the primary model when an object has several",
        "Hotspots: add / edit / delete annotations on a model (staff)",
        "Camera bookmarks: save / load named viewpoints (staff)",
        "Auto-generated thumbnail / poster preview",
        "IIIF 3D manifest generated for the model",
        "Public API returns only published-object models/hotspots (guest)",
        "Model settings (admin)",
    ],
    'ahgDedupePlugin': [
        "Configure duplicate-detection rules (fields, thresholds, match strategy)",
        "Run a dedup scan job over the catalogue",
        "View duplicate-candidate groups with match scores",
        "Compare two candidate records side by side",
        "Merge duplicates via the merge workflow (choose surviving record)",
        "Dedup report (counts, merges, history)",
        "CLI: dedupe:scan / dedupe:merge / dedupe:report",
    ],
    'ahgDisplayPlugin': [
        "GLAM browse interface renders (display modes)",
        "Display search via Elasticsearch with facets",
        "Guests see PUBLISHED records only (incl. the fuzzy-fallback path)",
        "Auto-detect display mode for a record",
        "Reindex display data (CLI display:reindex)",
        "DisplayRegistry: extensions register actions / panels / badges",
        "Treeview renders children/siblings (core ACL honoured)",
    ],
    'ahgThemeB5Plugin': [
        "Bootstrap 5 theme renders on public + admin pages (parity with AtoM)",
        "Responsive layout (mobile / tablet / desktop)",
        "Navigation menus + dropdowns render per permissions/enabled plugins",
        "Digital-object viewers (image / IIIF / media / 3D) render in-theme",
        "Admin BS5 bundle loads (no alien Tailwind / unstyled fallback)",
        "CSP nonce applied to inline scripts/styles (no console CSP violations)",
    ],
    'ahgUiOverridesPlugin': [
        "Viewer dispatch routes to the correct viewer (image / PDF / media / 3D)",
        "Registered action overrides replace the base AtoM actions",
        "Helper functions are available to templates",
        "No regression on un-overridden core actions",
    ],
}


def hdr(rows):
    o = ["| ✔ | Functionality | Source | Result (P/F) | Tester / Date | Notes |",
         "|---|---|---|---|---|---|"]
    for fn, src in rows:
        fn = fn.replace('|', '\\|')
        o.append(f"| ☐ | {fn} | {src} | | | |")
    return o

out = ["# AHG Plugins — Master Manual Test Checklist",
       "",
       "Manual end-to-end test checklist for every plugin. For each functionality, tick ☐→☑ when verified, record Pass/Fail, tester/date, and notes. **Source** column: UG = user manual, TECH = technical manual, CODE = derived from plugin config/tasks (where no manual exists yet).",
       "",
       f"Plugins: {len(plugins)}. Generated 2026-06-27.",
       ""]

stats = {'ug': 0, 'tech': 0, 'code_only': 0}
for p in plugins:
    ug = find_user_guide(p)
    has_tech = p in tech_md
    out.append(f"\n## {p}\n")
    src_note = []
    if ug: src_note.append(f"user guide `{ug}`")
    if has_tech: src_note.append("technical manual")
    if not src_note: src_note.append("**no manual — surface derived from code**")
    out.append(f"Sources: {', '.join(src_note)}.\n")

    rows = []
    if p in AUTHORED:
        rows += [(it, "AUTHORED") for it in AUTHORED[p]]
    if ug:
        rows += [(it, "UG") for it in extract_user_items(ug)]
        stats['ug'] += 1
    routes = extract_routes(p)
    rows += [(f"Route {path} → {act}", "CODE" if not has_tech else "TECH") for path, act in routes]
    cli = extract_cli(p)
    rows += [(f"CLI: {c}", "CODE") for c in cli]
    if has_tech: stats['tech'] += 1
    if not ug and not has_tech: stats['code_only'] += 1

    if not rows:
        rows = [("(no routes/CLI/manual items found — verify plugin scope manually)", "—")]
    out += hdr(rows)
    out.append("")

dest = f'{CAT}/_inventory/AHG_Master_Manual_Test_Checklist.md'
open(dest, 'w').write('\n'.join(out))
print(f"wrote {dest}")
print(f"plugins={len(plugins)} with_user_guide={stats['ug']} with_tech={stats['tech']} code_only={stats['code_only']}")
print(f"total lines={len(out)}")
