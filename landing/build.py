#!/usr/bin/env python3
"""Build atom-extensions.theahg.co.za: the product page (index.html) and the plugin
catalogue (plugins/), from the plugins' own extension.json files and the flagship
table in atom-ahg-plugins/README.md. Static HTML, no JavaScript.

    python3 landing/build.py          # writes landing/public/

Run it after a plugins release so versions and descriptions stay current.
"""
import datetime
import glob
import html
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGINS = next(p for p in (os.environ.get('AHG_PLUGINS_DIR', ''),
                           os.path.normpath(os.path.join(HERE, '..', '..', 'atom-ahg-plugins')),
                           '/usr/share/nginx/archive/atom-ahg-plugins') if p and os.path.isdir(p))
OUT = os.path.join(HERE, 'public')
SITE = 'https://atom-extensions.theahg.co.za'
DEMO = 'https://psis.theahg.co.za'
REPO = 'https://github.com/ArchiveHeritageGroup/atom-ahg-plugins'
DOCS = 'https://github.com/ArchiveHeritageGroup/atom-extensions-catalog/tree/main/docs'
YOUTUBE = 'https://www.youtube.com/@TheArchiveandHeritageGroup'
e = html.escape

CATEGORY_LABELS = {
    'sector': 'GLAM sectors', 'browse': 'Browse and manage', 'admin': 'Administration',
    'integration': 'Integration and APIs', 'compliance': 'Compliance', 'viewer': 'Viewing',
    'user-engagement': 'Public engagement', 'rights': 'Rights', 'preservation': 'Digital preservation',
    'ingest': 'Ingest and import', 'descriptive-standard': 'Descriptive standards',
    'collection-management': 'Collection management', 'search': 'Search and discovery', 'export': 'Export',
    'ai': 'AI-assisted description', 'research': 'Research services', 'reporting': 'Reporting',
    'records-management': 'Records management', 'provenance': 'Provenance', 'metadata': 'Metadata',
    'core': 'Foundation', 'security': 'Security', 'finance': 'Heritage finance',
    'authority': 'Authority records', 'workflow': 'Workflow', 'theme': 'Theme', 'data-quality': 'Data quality',
}

# Readable slugs where the package name would give a poor one. The collections
# procedures plugin's package name is never shown as text on these pages.
SLUGS = {'ahg3DModelPlugin': '3d-model', 'ahgSpectrumPlugin': 'collections-procedures'}
HIDE_PACKAGE = {'ahgSpectrumPlugin'}

# AHG palette (theahg.co.za): gold primary, green as background, cream on green.
CSS = """
:root{--gold:#E1B34F;--green:#10373E;--cream:#F2EDE6;--body:#262626;--link:#653332;--muted:#55656a}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.6 Arial,Helvetica,sans-serif;color:var(--body);background:#fff}
a{color:var(--link)}a:hover{text-decoration:none}
code{font-size:15px;background:var(--cream);padding:1px 5px;border-radius:3px}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px}
header.top{background:var(--green);color:var(--cream)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 16px;flex-wrap:wrap}
header.top a{color:var(--cream);text-decoration:none}
header.top .brand{font-weight:bold;color:var(--gold)}
header.top nav a{margin-left:18px}
.hero{background:var(--green);color:var(--cream);padding:56px 0 64px}
.hero h1{color:var(--gold);font-size:40px;line-height:1.15;margin:0 0 16px}
.hero p{font-size:20px;max-width:760px;margin:0 0 26px}
.btn{display:inline-block;background:var(--gold);color:var(--green);padding:12px 22px;border-radius:4px;font-weight:bold;text-decoration:none;margin:0 10px 10px 0}
.btn.ghost{background:transparent;color:var(--cream);border:2px solid var(--gold)}
main section{padding:44px 0;border-bottom:1px solid #e6e2da}
h2{color:var(--green);font-size:28px;line-height:1.25;margin:0 0 14px}
h3{color:var(--green);font-size:19px;margin:0 0 6px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}
.card{border:1px solid #ddd6ca;border-top:4px solid var(--gold);padding:18px;border-radius:4px;background:#fff}
.card p{margin:0 0 10px}.card .by{font-size:15px;color:var(--muted)}
.tag{display:inline-block;font-size:14px;background:var(--cream);border-radius:3px;padding:1px 8px;margin:2px 4px 2px 0}
table{border-collapse:collapse;width:100%;margin:12px 0}
th,td{border:1px solid #ddd6ca;padding:8px 10px;text-align:left;vertical-align:top}
th{background:var(--green);color:#fff;font-weight:bold;width:150px}
.cat h2{margin-top:32px;font-size:23px}
.plugin-list{columns:2 300px;padding-left:20px}.plugin-list li{margin:0 0 8px;break-inside:avoid}
footer{background:var(--green);color:var(--cream);padding:28px 0;font-size:15px}footer a{color:var(--gold)}
.crumb{font-size:15px;margin:0 0 14px}
@media(max-width:600px){.hero{padding:40px 0 44px}.hero h1{font-size:30px}.hero p{font-size:18px}
header.top nav a{margin:0 14px 0 0}th{width:auto}}
"""


def no_long_dashes(text):
    """House style: plain hyphens only, whatever the source READMEs use."""
    text = re.sub(r'\s*\u2014\s*', ' - ', text)
    return text.replace('\u2013', '-').replace('&mdash;', ' - ').replace('&ndash;', '-')


def page(title, description, path, body, jsonld=None):
    return no_long_dashes(_page(title, description, path, body, jsonld))


def _page(title, description, path, body, jsonld=None):
    url = SITE + path
    ld = ('<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + '</script>') if jsonld else ''
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}"><meta property="og:type" content="website">
<link rel="stylesheet" href="/style.css">{ld}</head><body>
<header class="top"><div class="wrap"><a class="brand" href="/">AHG Extensions for AtoM</a>
<nav><a href="/#capabilities">Capabilities</a><a href="/plugins/">Plugins</a><a href="{DEMO}">Live demo</a><a href="/#contact">Contact</a></nav></div></header>
{body}
<footer><div class="wrap">AHG Extensions for AtoM were developed by <a href="https://plainsailingisystems.co.za/">Plain Sailing Information Systems</a> and are offered by <a href="https://theahg.co.za">The Archive and Heritage Group (Pty) Ltd</a>, South Africa. Open source under AGPL-3.0: <a href="{REPO}">source code</a> and <a href="{DOCS}">documentation</a>.</div></footer>
</body></html>
"""


def inline_md(text):
    """Escaped HTML for one line of README markdown: bold and code kept, links
    kept only when absolute (relative ones point into the repository)."""
    out = e(text)
    out = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', out)
    out = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', out)
    out = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', out)
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', out)


def readme_summary(machine):
    """The README's opening paragraphs and its Features list, as HTML."""
    path = os.path.join(PLUGINS, machine, 'README.md')
    if not os.path.isfile(path):
        return ''
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    intro, i = [], 0
    while i < len(lines) and not lines[i].startswith('# '):
        i += 1
    for line in lines[i + 1:]:
        if line.startswith('#'):
            break
        t = line.strip()
        if t and not t.startswith(('|', '**Current version', '>', '!', '<')):
            intro.append(t)
    paras = ' '.join(intro).split('  ')
    html_out = ''.join(f'<p>{inline_md(x.strip())}</p>' for x in paras if x.strip())[:1500]
    feats, on = [], False
    for line in lines:
        if re.match(r'^##\s+(Key\s+)?Features\b', line, re.I):
            on = True
            continue
        if on and line.startswith('## '):
            break
        if on and re.match(r'^\s*[-*]\s+', line):
            feats.append(re.sub(r'^\s*[-*]\s+', '', line).strip())
    if feats:
        html_out += '<h3>Features</h3><ul>' + ''.join(f'<li>{inline_md(f)}</li>' for f in feats[:15]) + '</ul>'
    return html_out


def load_plugins():
    out = []
    for f in sorted(glob.glob(os.path.join(PLUGINS, '*', 'extension.json'))):
        try:
            d = json.load(open(f))
        except (OSError, ValueError):
            continue
        machine = d.get('machine_name') or os.path.basename(os.path.dirname(f))
        d['machine_name'] = machine
        base = re.sub(r'^ahg', '', machine.replace('Plugin', ''))
        d['slug'] = SLUGS.get(machine) or re.sub(r'(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', '-', base).lower()
        out.append(d)
    return out


def flagships():
    readme = open(os.path.join(PLUGINS, 'README.md')).read()
    block = readme.split('## Nine flagship capabilities', 1)[1].split('\n## ', 1)[0]
    rows = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) != 4 or not cells[0].startswith('**'):
            continue
        rows.append({
            'name': cells[0].strip('*'),
            'what': cells[1],
            'plugins': re.findall(r'\[([^\]]+)\]\((ahg\w+Plugin)/\)', cells[2]),
            'video': (re.findall(r'\((https://youtu\.be/[^)]+)\)', cells[3]) or [None])[0],
        })
    return rows


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'plugins'))
    open(os.path.join(OUT, 'style.css'), 'w').write(CSS.strip() + '\n')
    plugins = load_plugins()
    by_machine = {p['machine_name']: p for p in plugins}
    flags = flagships()

    # Product page
    cards = []
    for f in flags:
        links = ', '.join(f'<a href="/plugins/{by_machine[m]["slug"]}.html">{e(label)}</a>'
                          for label, m in f['plugins'] if m in by_machine)
        video = f' <a href="{e(f["video"])}">Watch the walkthrough</a>.' if f['video'] else ''
        cards.append(f'<div class="card"><h3>{e(f["name"])}</h3><p>{e(f["what"])}</p>'
                     f'<p class="by">Plugins: {links}.{video}</p></div>')
    body = f"""<div class="hero"><div class="wrap">
<h1>AHG Extensions for AtoM</h1>
<p>Preservation, provenance, Records in Contexts, AI-assisted description, museum, library and digital asset workflows, rights and privacy, added to Access to Memory 2.10 as plugins. Base AtoM stays exactly as upstream ships it, and an institution installs only the capabilities it needs.</p>
<a class="btn" href="{DEMO}">Try the live demo</a><a class="btn ghost" href="/plugins/">Browse all {len(plugins)} plugins</a>
</div></div>
<main>
<section id="capabilities"><div class="wrap">
<h2>Nine flagship capabilities</h2>
<p>Each is a family of plugins rather than a single module. Most have a short walkthrough recorded on the live demo.</p>
<div class="grid">{''.join(cards)}</div>
</div></section>
<section><div class="wrap">
<h2>Not a fork of AtoM</h2>
<p>AtoM 2.10 is installed and updated as normal. The extensions sit beside it: a shared framework, <code>atom-framework</code>, and the plugins, <code>atom-ahg-plugins</code>. Each plugin is switched on or off from the administration screens. None of them edits AtoM's own code, so upstream upgrades stay open to you.</p>
</div></section>
<section><div class="wrap">
<h2>Who it is for</h2>
<div class="grid">
<div class="card"><h3>Archives</h3><p>ISAD(G), RAD, DACS and Dublin Core description. OAIS ingest with SIP, AIP and DIP packages. Fixity, format identification and PREMIS events. Records in Contexts.</p></div>
<div class="card"><h3>Museums and galleries</h3><p>Object cataloguing to museum standards, collections procedures run as workflows, condition checks, provenance, loans, exhibitions, and heritage asset accounting under GRAP 103 and IPSAS 45.</p></div>
<div class="card"><h3>Libraries</h3><p>Cataloguing with ISBN lookup, copies and barcodes, circulation with holds and fines, and a public catalogue, on the same platform as the archive.</p></div>
<div class="card"><h3>Public bodies and regulated institutions</h3><p>POPIA, GDPR and other privacy regimes, security classification, embargoes, audit trails and retention rules, inside the catalogue rather than beside it.</p></div>
</div></div></section>
<section><div class="wrap">
<h2>Learn it</h2>
<p>Training videos take you through the research portal, compliance and rights, museum collections, digital preservation and discovery, step by step, each with a written guide. Watch them on the <a href="{YOUTUBE}">AHG YouTube channel</a> and read the guides in the <a href="{DOCS}">documentation</a>.</p>
</div></section>
<section id="contact"><div class="wrap">
<h2>Installation, hosting and support</h2>
<p>The Archive and Heritage Group installs and hosts the extensions, migrates existing AtoM catalogues, trains staff and supports institutions in production. To talk about your collection, contact <a href="https://theahg.co.za">The Archive and Heritage Group</a>.</p>
</div></section>
</main>"""
    ld = {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'AHG Extensions for AtoM',
          'applicationCategory': 'BusinessApplication', 'operatingSystem': 'Linux',
          'description': 'Plugins that extend Access to Memory (AtoM) 2.10 into a GLAM platform: preservation, provenance, Records in Contexts, AI-assisted description, museum, library and DAM workflows, rights and privacy.',
          'license': 'https://www.gnu.org/licenses/agpl-3.0.html', 'url': SITE + '/',
          'author': {'@type': 'Organization', 'name': 'Plain Sailing Information Systems', 'url': 'https://plainsailingisystems.co.za/'},
          'provider': {'@type': 'Organization', 'name': 'The Archive and Heritage Group (Pty) Ltd', 'url': 'https://theahg.co.za'},
          'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'ZAR'}}
    open(os.path.join(OUT, 'index.html'), 'w').write(page(
        'AHG Extensions for AtoM: preservation, museum, library and AI plugins for Access to Memory',
        'Plugins that extend AtoM 2.10 with preservation, provenance, Records in Contexts, AI-assisted description, museum, library and DAM workflows, rights and privacy, without modifying base AtoM.',
        '/', body, ld))

    # Catalogue index
    groups = {}
    for p in plugins:
        label = CATEGORY_LABELS.get(p.get('category', ''), (p.get('category') or 'Other').replace('-', ' ').capitalize())
        groups.setdefault(label, []).append(p)
    sections = []
    for label in sorted(groups):
        items = ''.join(f'<li><a href="/plugins/{p["slug"]}.html">{e(p.get("name") or p["machine_name"])}</a>: {e(p.get("description", ""))}</li>'
                        for p in sorted(groups[label], key=lambda x: (x.get('name') or '').lower()))
        sections.append(f'<div class="cat"><h2>{e(label)}</h2><ul class="plugin-list">{items}</ul></div>')
    open(os.path.join(OUT, 'plugins', 'index.html'), 'w').write(page(
        f'All {len(plugins)} AtoM plugins: AHG Extensions for AtoM catalogue',
        f'Every plugin in AHG Extensions for AtoM, grouped by what it does: {len(plugins)} plugins for archives, museums, libraries and galleries running AtoM 2.10.',
        '/plugins/',
        f'<main><section><div class="wrap"><p class="crumb"><a href="/">Home</a> / Plugins</p><h2>All {len(plugins)} plugins</h2>'
        f'<p>Grouped by what they do. Each page gives the plugin\'s purpose, what it depends on, and where its source and documentation are.</p>{"".join(sections)}</div></section></main>'))

    # One page per plugin
    for p in plugins:
        name = p.get('name') or p['machine_name']
        desc = p.get('description', '')
        cat = CATEGORY_LABELS.get(p.get('category', ''), p.get('category', ''))
        deps = ''.join(f'<span class="tag">{e(by_machine[d].get("name") or d) if d in by_machine else e(d)}</span>'
                       for d in p.get('dependencies', []))
        rows = [('Category', e(cat))]
        if p['machine_name'] not in HIDE_PACKAGE:
            rows.append(('Package', f'<code>{e(p["machine_name"])}</code>'))
        rows.append(('Version', e(str(p.get('version', '')))))
        if deps:
            rows.append(('Requires', deps))
        if p.get('license'):
            rows.append(('Licence', e(p['license'])))
        flag = next((f for f in flags if any(m == p['machine_name'] for _, m in f['plugins'])), None)
        flag_html = ''
        if flag:
            flag_html = f'<p>Part of the <a href="/#capabilities">{e(flag["name"])}</a> capability.'
            flag_html += (f' <a href="{e(flag["video"])}">Watch the walkthrough</a>.' if flag['video'] else '') + '</p>'
        table = ''.join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
        body = f"""<main><section><div class="wrap"><p class="crumb"><a href="/">Home</a> / <a href="/plugins/">Plugins</a> / {e(name)}</p>
<h2>{e(name)}</h2><p>{e(desc)}</p>{flag_html}
<table>{table}</table>
{readme_summary(p['machine_name'])}
<p><a href="{REPO}/tree/main/{e(p['machine_name'])}">Source and README on GitHub</a> &middot; <a href="{DEMO}">Try it on the live demo</a></p>
</div></section></main>"""
        open(os.path.join(OUT, 'plugins', p['slug'] + '.html'), 'w').write(page(
            f'{name}: AtoM plugin from AHG Extensions for AtoM',
            (desc or f'{name} plugin for AtoM 2.10')[:300], f'/plugins/{p["slug"]}.html', body))

    # Sitemap and robots
    today = datetime.date.today().isoformat()
    urls = ['/', '/plugins/'] + [f'/plugins/{p["slug"]}.html' for p in plugins]
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    print(f'built {len(plugins)} plugin pages, {len(flags)} capabilities -> {OUT}')


if __name__ == '__main__':
    build()
