#!/usr/bin/env python3
"""Build www.atom-extensions.com: the product page (index.html) and the plugin
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
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGINS = next(p for p in (os.environ.get('AHG_PLUGINS_DIR', ''),
                           os.path.normpath(os.path.join(HERE, '..', '..', 'atom-ahg-plugins')),
                           '/usr/share/nginx/archive/atom-ahg-plugins') if p and os.path.isdir(p))
# Built into a staging folder and swapped in only when every check passes, so a
# refused build never leaves the live site half-written. AHG_SITE_OUT lets the
# tests build somewhere harmless.
OUT_FINAL = os.environ.get('AHG_SITE_OUT') or os.path.join(HERE, 'public')
OUT = OUT_FINAL + '.building'
SITE = 'https://www.atom-extensions.com'
DEMO = 'https://psis.theahg.co.za'
REPO = 'https://github.com/ArchiveHeritageGroup/atom-ahg-plugins'
DOCS = 'https://github.com/ArchiveHeritageGroup/atom-extensions-catalog/tree/main/docs'
YOUTUBE = 'https://www.youtube.com/@TheArchiveandHeritageGroup'
DOWNLOADS = REPO + '/blob/main/docs/plugins/README.md'
SUPPORT_EMAIL = 'support@theahg.co.za'
WHATSAPP = 'https://wa.me/27648830533?text=' + 'Tell%20me%20about%20the%20AHG%20Plugins'
CALLHUB = 'https://callhub.theahg.co.za/login'
LICENCE = 'AGPL-3.0-or-later'
# The "status" field in each extension.json. Anything unassessed shows as not verified.
STATUS = {
    'packaged': 'Packaged download with its own installer',
    'tested': 'Installs from source',
    'source': 'Installs from source',
    'experimental': 'Experimental: not for production',
    'deprecated': 'Deprecated: will be removed',
}
# Labels for the catalogue's Status filter.
STATUS_FILTER = {'packaged': 'Packaged download', 'tested': 'Clean-install verified, from source', 'source': 'Source, not yet verified',
                 'experimental': 'Experimental', 'deprecated': 'Deprecated'}
# The clean-database run behind tested_at (README "Verified standalone set").
VERIFIED_RUN = 'plugins v3.103.12'
# Foundations rather than features: installed because other plugins need them.
FOUNDATIONS = {
    'ahgRuntimePlugin': 'a shared runtime, downloaded once as its own package and installed before any other; on its own it adds nothing to AtoM',
    'ahgCorePlugin': 'shared services (database access, settings, file storage) that the other plugins build on; on its own it adds no screens',
}
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

CONTENT = os.path.join(HERE, 'content')          # hand-written sections: content/<slug>.md
DOC_IMAGES = os.path.normpath(os.path.join(HERE, '..', 'docs', 'images'))

# External services a plugin can use, found in its own code (PHP, Python, shell).
# The settings and theme plugins only configure or display these, so they are skipped.
SERVICES = {
    'Cantaloupe IIIF image server': r'cantaloupe|:8182',
    'Apache Jena Fuseki triplestore': r'fuseki|:3030',
    'ExifTool': r'exiftool',
    'ClamAV virus scanner': r'clamdscan|clamscan',
    'Siegfried format identification': r"siegfried|'sf'",
    'Qdrant vector database': r'qdrant|:6333',
    'AHG AI gateway': r'AiGatewayClient|ai\.theahg\.co\.za',
    'Tesseract OCR': r'tesseract',
    'FFmpeg': r'ffmpeg',
    'LibreOffice': r'soffice|libreoffice',
    'Gearman job server': r'gearman',
    'DataCite (DOIs)': r'datacite',
}
SERVICE_SKIP = {'ahgSettingsPlugin', 'ahgThemeB5Plugin'}

# Pages on the live demo that work without signing in, checked 15 Oct 2026.
DEMO_PAGES = {
    'ahgDiscoveryPlugin': ('/discovery', 'Discover search'),
    'ahgIiifPlugin': ('/iiif-viewer-photo-taken-with-phase-one-iq3-100mp-captured-on-november-17-2017-80mm-f-11', 'a record in the IIIF viewer'),
    'ahg3DModelPlugin': ('/3d-more-glb', 'a record with a 3D model'),
    'ahgHeritagePlugin': ('/heritage', 'the heritage discovery portal'),
    'ahgGalleryPlugin': ('/gallery/browse', 'the gallery browse'),
    'ahgMarketplacePlugin': ('/marketplace', 'the marketplace'),
    'ahgLibraryPlugin': ('/library', 'the library catalogue'),
    'ahgDisplayPlugin': ('/glam/browse', 'the GLAM browse'),
    'ahgMuseumPlugin': ('/glam/browse?type=museum', 'museum objects in the GLAM browse'),
    'ahgActorManagePlugin': ('/actor/browse', 'the authority record browse'),
    'ahgRepositoryManagePlugin': ('/repository/browse', 'the archival institution browse'),
    'ahgFunctionManagePlugin': ('/function/browse', 'the function browse'),
    'ahgSearchPlugin': ('/search/descriptionUpdates', 'newest additions'),
    'ahgUserRegistrationPlugin': ('/register', 'the registration form'),
    'ahgFeedbackPlugin': ('/feedback/general', 'the feedback form'),
    'ahgChatbotPlugin': ('/', 'the home page: use "Ask the archive"'),
}


def code_services():
    """{machine_name: [service, ...]} from a scan of each plugin's own code."""
    found = {}
    for label, pattern in SERVICES.items():
        rx = re.compile(pattern, re.I)
        for path in glob.glob(os.path.join(PLUGINS, 'ahg*Plugin', '**', '*.*'), recursive=True):
            if not path.endswith(('.php', '.py', '.sh')) or '/vendor/' in path or '/test' in path:
                continue
            machine = os.path.relpath(path, PLUGINS).split(os.sep)[0]
            if machine in SERVICE_SKIP or label in found.get(machine, []):
                continue
            try:
                if rx.search(open(path, encoding='utf-8', errors='ignore').read()):
                    found.setdefault(machine, []).append(label)
            except OSError:
                pass
    return found


def md_html(text):
    """GitHub markdown to HTML through pandoc (no python-markdown on this host)."""
    if not text.strip():
        return ''
    out = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html5', '--wrap=none'], input=text,
                         capture_output=True, text=True, check=True).stdout
    # links into the repository are relative: point them at GitHub
    out = re.sub(r'href="(?!https?:|#|/|mailto:)([^"]+)"', lambda m: f'href="{REPO}/blob/main/{m.group(1)}"', out)
    return focusable_pre(out)


def focusable_pre(html_text):
    """Code blocks scroll sideways on phones; tabindex lets keyboard users scroll them (WCAG 2.1.1)."""
    return re.sub(r'<pre(?![^>]*tabindex)', '<pre tabindex="0" aria-label="Code"', html_text)


def readme_sections(machine):
    """The README's level-2 sections, {title: markdown}."""
    path = os.path.join(PLUGINS, machine, 'README.md')
    if not os.path.isfile(path):
        return {}
    sections, title = {}, None
    for line in open(path, encoding='utf-8', errors='replace'):
        m = re.match(r'^## (.+?)\s*$', line)
        if m:
            title = m.group(1)
            sections[title] = ''
        elif title:
            sections[title] += line
    return sections


def content_html(slug):
    """Hand-written page content (content/<slug>.md), copying the screenshots it uses."""
    path = os.path.join(CONTENT, slug + '.md')
    if not os.path.isfile(path):
        return ''
    text = open(path, encoding='utf-8').read()
    for rel in re.findall(r'\(/img/([^)]+)\)', text):
        src = os.path.join(DOC_IMAGES, rel)
        if not os.path.isfile(src):
            raise SystemExit(f'build refused: {slug}.md uses missing image {rel}')
        # Served as WebP (quality 82): about a fifth of the PNG size, same look.
        dst = os.path.join(OUT, 'img', os.path.splitext(rel)[0] + '.webp')
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        from PIL import Image
        with Image.open(src) as im:
            im.save(dst, 'WEBP', quality=82, method=6)
    html_out = md_html(text)

    def sized(m):
        # width/height reserve the space, so the page does not jump as lazy images arrive
        src = re.search(r'src="/img/([^"]+)"', m.group(0))
        attrs = ' loading="lazy"'
        if src:
            with open(os.path.join(DOC_IMAGES, src.group(1)), 'rb') as f:
                head = f.read(24)
            if head[:8] == b'\x89PNG\r\n\x1a\n':
                attrs += f' width="{int.from_bytes(head[16:20], "big")}" height="{int.from_bytes(head[20:24], "big")}"'
        tag = re.sub(r'(src="/img/[^"]+)\.png"', r'\1.webp"', m.group(0))
        return '<img' + attrs + tag[4:]
    html_out = re.sub(r'<img [^>]*>', sized, html_out)
    return html_out


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
h2,main h1{color:var(--green);font-size:28px;line-height:1.25;margin:0 0 14px}
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
.detail h2{font-size:22px;margin:28px 0 10px}
.detail img{max-width:100%;height:auto;border:1px solid #ddd6ca;border-radius:4px;margin:6px 0}
.detail pre{background:var(--cream);padding:10px 12px;overflow-x:auto;font-size:14px;border-radius:4px}
.detail pre code{background:none;padding:0}
.filters{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0 6px}
.filters label{display:flex;flex-direction:column;font-size:14px;color:var(--muted);gap:2px}
.filters input,.filters select{font:16px Arial,sans-serif;padding:7px 9px;border:1px solid #bdb5a6;border-radius:4px;min-width:200px}
.filters input:focus,.filters select:focus,a:focus{outline:3px solid var(--gold);outline-offset:2px}
.badge{display:inline-block;font-size:13px;border-radius:3px;padding:0 6px;margin-left:6px;background:var(--cream);color:var(--green)}
#count{font-weight:bold}
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
<footer><div class="wrap">AHG Extensions for AtoM were developed by <a href="https://plainsailingisystems.co.za/">Plain Sailing Information Systems</a> and are offered by <a href="https://theahg.co.za">The Archive and Heritage Group (Pty) Ltd</a>, South Africa. Open source under AGPL-3.0-or-later: <a href="{REPO}">source code</a> and <a href="{DOCS}">documentation</a>.</div></footer>
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
        html_out += '<h2>Features</h2><ul>' + ''.join(f'<li>{inline_md(f)}</li>' for f in feats[:15]) + '</ul>'
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


def packaged():
    """Plugins with a packaged download today: the release links on the
    downloads page, so the site never claims a package that does not exist."""
    path = os.path.join(PLUGINS, 'docs', 'plugins', 'README.md')
    text = open(path, encoding='utf-8').read() if os.path.isfile(path) else ''
    return set(re.findall(r'releases/tag/(ahg\w+Plugin)-v', text))


# Catalogue filter. The full list is plain HTML; without JavaScript nothing is hidden.
FILTER_JS = """<script>
(function(){var q=document.getElementById('q'),c=document.getElementById('cat'),s=document.getElementById('status'),i=document.getElementById('install');
var items=[].slice.call(document.querySelectorAll('#catalogue li')),groups=[].slice.call(document.querySelectorAll('#catalogue .cat'));
function run(){var t=q.value.trim().toLowerCase(),n=0;items.forEach(function(li){var ok=(!t||t.split(/\\s+/).every(function(w){return (' '+li.dataset.text).indexOf(' '+w)>-1;}))&&(!c.value||li.dataset.cat===c.value)&&(!s.value||li.dataset.status===s.value)&&(!i.value||li.dataset.install===i.value);li.hidden=!ok;if(ok)n++;});
groups.forEach(function(g){g.hidden=!g.querySelector('li:not([hidden])');});document.getElementById('count').textContent=n;document.getElementById('none').hidden=n>0;
var u=new URLSearchParams();if(t)u.set('q',t);if(c.value)u.set('group',c.value);if(s.value)u.set('status',s.value);if(i.value)u.set('install',i.value);history.replaceState(null,'',u.toString()?'?'+u:location.pathname);}
var p=new URLSearchParams(location.search);q.value=p.get('q')||'';c.value=p.get('group')||'';s.value=p.get('status')||'';i.value=p.get('install')||'';
[q,c,s,i].forEach(function(el){el.addEventListener('input',run);el.addEventListener('change',run);});run();})();
</script>"""


def verified_set():
    """Plugin names in the README's "Verified standalone set" paragraph: the one
    source for which plugins may carry a clean-install date."""
    readme = open(os.path.join(PLUGINS, 'README.md'), encoding='utf-8').read()
    m = re.search(r'### Verified standalone set\s+(.*?)\n\n', readme, re.S)
    if not m:
        raise SystemExit('build refused: README has no "Verified standalone set" section')
    names = re.findall(r'\b(ahg[A-Z]\w*?)(?=[,.\s])', m.group(1).split(':', 1)[1])
    return {n if n.endswith('Plugin') else n + 'Plugin' for n in names}


def check(plugins):
    """Refuse to publish a catalogue with gaps a visitor would notice."""
    problems, seen = [], {}
    # Counts: the README total must agree with the manifests.
    readme = open(os.path.join(PLUGINS, 'README.md'), encoding='utf-8').read()
    total = re.search(r'^Totals: (\d+) plugins', readme, re.M)
    if not total:
        problems.append('README.md has no "Totals: N plugins" line')
    elif int(total.group(1)) != len(plugins):
        problems.append(f'README.md says {total.group(1)} plugins, the manifests give {len(plugins)}')
    # No unjustified test status: a clean-install date only for the verified set.
    verified = verified_set()
    for p in plugins:
        m = p['machine_name']
        if p.get('tested_at') and m not in verified:
            problems.append(f'{m}: tested_at set but not in the README verified standalone set')
        if m in verified and not p.get('tested_at'):
            problems.append(f'{m}: in the README verified standalone set but has no tested_at')
    for p in plugins:
        m = p['machine_name']
        for field in ('license', 'version', 'description'):
            if not p.get(field):
                problems.append(f'{m}: no {field} in extension.json')
        if p.get('license') and p['license'] != LICENCE:
            problems.append(f'{m}: licence {p["license"]} is not {LICENCE}')
        if p['slug'] in seen:
            problems.append(f'{m}: slug {p["slug"]} also used by {seen[p["slug"]]}')
        seen[p['slug']] = m
    if problems:
        raise SystemExit('build refused:\n  ' + '\n  '.join(problems))


def check_site(root):
    """Every internal link and #anchor in the built site must resolve."""
    problems = []
    pages = {}
    for path in glob.glob(os.path.join(root, '**', '*.html'), recursive=True):
        rel = '/' + os.path.relpath(path, root).replace(os.sep, '/')
        pages[rel] = open(path, encoding='utf-8').read()
    def ids(html_text):
        return set(re.findall(r'\bid="([^"]+)"', html_text))
    for rel, text in pages.items():
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(('http:', 'https:', 'mailto:')):
                continue
            target, _, anchor = href.partition('#')
            if not target:
                target_rel = rel
            elif target.startswith('/'):
                target_rel = target + 'index.html' if target.endswith('/') else target
            else:
                continue
            if not os.path.exists(os.path.join(root, target_rel.lstrip('/'))):
                problems.append(f'{rel}: link to {href} has no page')
            elif anchor and target_rel.endswith('.html') and anchor not in ids(pages.get(target_rel, '')):
                problems.append(f'{rel}: link to {href} has no #{anchor} on that page')
    return problems


def check_external(plugins, bundles, flags):
    """Optional (--check-external): packaged downloads and walkthrough videos exist."""
    import urllib.request
    urls = [f'{REPO}/releases/tag/{t}' for t in sorted(set(re.findall(r'releases/tag/(ahg\w+Plugin-v[\w.]+)',
            open(os.path.join(PLUGINS, 'docs', 'plugins', 'README.md'), encoding='utf-8').read())))]
    urls += [f['video'] for f in flags if f['video']]
    problems = []
    for u in urls:
        try:
            req = urllib.request.Request(u, method='HEAD', headers={'User-Agent': 'atom-extensions-build/1.0'})
            code = urllib.request.urlopen(req, timeout=20).status
        except Exception as ex:
            code = getattr(ex, 'code', str(ex))
        if code != 200:
            problems.append(f'{u}: {code}')
    return problems


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


def build(check_ext=False):
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'plugins'))
    open(os.path.join(OUT, 'style.css'), 'w').write(CSS.strip() + '\n')
    plugins = load_plugins()
    check(plugins)
    bundles = packaged()
    services = code_services()
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
    body = f"""<main><div class="hero"><div class="wrap">
<h1>AHG Extensions for AtoM</h1>
<p>Preservation, provenance, Records in Contexts, AI-assisted description, museum, library and digital asset workflows, rights and privacy, added to Access to Memory 2.9 and 2.10 as plugins. Base AtoM stays as upstream ships it, and an institution installs only the capabilities it needs.</p>
<a class="btn" href="{DEMO}">Try the live demo</a><a class="btn ghost" href="/plugins/">Browse all {len(plugins)} plugins</a>
</div></div>
<section id="capabilities"><div class="wrap">
<h2>Nine flagship capabilities</h2>
<p>Each is a family of plugins rather than a single module. Most have a short walkthrough recorded on the live demo.</p>
<div class="grid">{''.join(cards)}</div>
</div></section>
<section><div class="wrap">
<h2>Not a fork of AtoM</h2>
<p>AtoM is installed and updated as normal. The extensions sit beside it: a shared framework, <code>atom-framework</code>, and the plugins, <code>atom-ahg-plugins</code>. Each plugin is switched on or off from the administration screens. None of them edits AtoM's own code, so upstream upgrades stay open to you.</p>
</div></section>
<section><div class="wrap">
<h2>Who it is for</h2>
<div class="grid">
<div class="card"><h3>Archives</h3><p>ISAD(G), RAD, DACS and Dublin Core description. OAIS ingest with SIP, AIP and DIP packages. Fixity, format identification and PREMIS events. Records in Contexts.</p></div>
<div class="card"><h3>Museums and galleries</h3><p>Object cataloguing to museum standards, collections procedures run as workflows, condition checks, provenance, loans, exhibitions, and heritage asset accounting under GRAP 103 and IPSAS 45.</p></div>
<div class="card"><h3>Libraries</h3><p>Cataloguing with ISBN lookup, copies and barcodes, circulation with holds and fines, and a public catalogue, on the same platform as the archive.</p></div>
<div class="card"><h3>Public bodies and regulated institutions</h3><p>Tools that support POPIA, GDPR and other privacy obligations, security classification, embargoes, audit trails and retention rules, inside the catalogue rather than beside it. They help an institution meet its obligations; they do not certify compliance.</p></div>
</div></div></section>
<section><div class="wrap">
<h2>Learn it</h2>
<p>Training videos take you through the research portal, compliance and rights, museum collections, digital preservation and discovery, step by step, each with a written guide. Watch them on the <a href="{YOUTUBE}">AHG YouTube channel</a> and read the guides in the <a href="{DOCS}">documentation</a>.</p>
</div></section>
<section id="contact"><div class="wrap">
<h2>Installation, hosting and support</h2>
<p>The software is free and open source. The Archive and Heritage Group offers the services around it: installation, hosting, migration of existing AtoM catalogues, staff training and support in production. None of them is required to use the plugins.</p>
<ul>
<li>Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> with your institution, your AtoM version and the extensions you are interested in.</li>
<li>Message us on <a href="{WHATSAPP}">WhatsApp</a>.</li>
<li>Existing clients: log a call in <a href="{CALLHUB}">CallHub</a>.</li>
</ul>
<p>Packaged downloads and install steps are on the <a href="{DOWNLOADS}">downloads page</a>. Install on a staging copy first, with a backup.</p>
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
        items = ''.join(
            f'<li data-cat="{e(label)}" data-status="{e(p.get("status") or "unknown")}" '
            f'data-install="{"packaged" if p["machine_name"] in bundles else "source"}" '
            f'data-text="{e(re.sub(r"[^a-z0-9]+", " ", ((p.get("name") or "") + " " + p.get("description", "") + " " + p["machine_name"]).lower()).strip())}">'
            f'<a href="/plugins/{p["slug"]}.html">{e(p.get("name") or p["machine_name"])}</a>'
            f'{"<span class=badge>packaged</span>" if p["machine_name"] in bundles else ""}: {e(p.get("description", ""))}</li>'
            for p in sorted(groups[label], key=lambda x: (x.get('name') or '').lower()))
        sections.append(f'<div class="cat"><h2>{e(label)}</h2><ul class="plugin-list">{items}</ul></div>')
    cat_opts = ''.join(f'<option>{e(l)}</option>' for l in sorted(groups))
    status_opts = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in STATUS_FILTER.items())
    filters = (f'<form class="filters" role="search" onsubmit="return false">'
               f'<label>Search<input id="q" type="search" placeholder="e.g. preservation, IIIF, POPIA" autocomplete="off"></label>'
               f'<label>Group<select id="cat"><option value="">All groups</option>{cat_opts}</select></label>'
               f'<label>Status<select id="status"><option value="">Any status</option>{status_opts}</select></label>'
               f'<label>Install<select id="install"><option value="">Any</option><option value="packaged">Packaged download</option><option value="source">From source</option></select></label>'
               f'</form><p aria-live="polite">Showing <span id="count">{len(plugins)}</span> of {len(plugins)} plugins.</p>')
    verified_count = sum(1 for p in plugins if p.get('tested_at'))
    foundations_text = '; '.join(f'<a href="/plugins/{by_machine[m]["slug"]}.html">{e(by_machine[m].get("name") or m)}</a>, {e(why)}'
                                 for m, why in FOUNDATIONS.items() if m in by_machine)
    open(os.path.join(OUT, 'plugins', 'index.html'), 'w').write(page(
        f'All {len(plugins)} AtoM plugins: AHG Extensions for AtoM catalogue',
        f'Every plugin in AHG Extensions for AtoM, grouped by what it does: {len(plugins)} plugins for archives, museums, libraries and galleries running AtoM 2.10.',
        '/plugins/',
        f'<main><section><div class="wrap"><p class="crumb"><a href="/">Home</a> / Plugins</p><h1>All {len(plugins)} plugins</h1>'
        f'<p>Grouped by what they do. Each page gives the plugin\'s purpose, what it depends on, and where its source and documentation are.</p>'
        f'<p>Two of the {len(plugins)} are foundations rather than features: {foundations_text}. You install them because the other plugins need them, not for what they do alone.</p>'
        f'<p>{len(bundles - {"ahgRuntimePlugin"})} plugins are currently offered as <a href="{DOWNLOADS}">packaged downloads</a> with installers, together with the shared runtime. Additional plugins can be installed from source. '
        f'The project documents a verified standalone installation set of {verified_count} components, installed onto an empty database on 18 August 2026 ({VERIFIED_RUN}); '
        f'testing and deployment evidence for other plugins varies by module and environment. Each plugin page shows its status: consult it, and the plugin\'s documentation, before deployment.</p>'
        f'{filters}<div id="catalogue">{"".join(sections)}</div><p id="none" hidden>No plugin matches. Clear a filter to see more.</p></div></section></main>{FILTER_JS}'))

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
        status = STATUS.get(p.get('status', ''), 'Not verified')
        if p.get('tested_at'):
            when = datetime.date.fromisoformat(p['tested_at']).strftime('%-d %B %Y')
            status += f'. Clean-database install verified {when} ({VERIFIED_RUN}).'
        elif p.get('status') in ('packaged', 'tested', 'source'):
            status += '. Clean-database install not yet verified.'
        rows.append(('Status', status))
        if deps:
            rows.append(('Requires', deps))
        optional = []
        for field in ('optional', 'optional_dependencies', 'suggests'):
            v = p.get(field) or []
            if isinstance(v, dict):  # {"extensions": [...]} or {"ahgXPlugin": "why"}
                v = v.get('extensions', []) if 'extensions' in v else list(v)
            optional += [o for o in v if isinstance(o, str) and re.match(r'^ahg\w+Plugin$', o)]
        optional = list(dict.fromkeys(optional))
        if optional:
            rows.append(('Works with', ''.join(f'<a class="tag" href="/plugins/{by_machine[o]["slug"]}.html">{e(by_machine[o].get("name") or o)}</a>' if o in by_machine else f'<span class="tag">{e(o)}</span>' for o in optional)))
        if services.get(p['machine_name']):
            rows.append(('External services', 'Can use, when installed: ' + ', '.join(e(x) for x in services[p['machine_name']])))
        if p.get('license'):
            rows.append(('Licence', e(p['license'])))
        if p['machine_name'] in bundles:
            rows.append(('Install', f'Packaged download with its own installer: see the <a href="{DOWNLOADS}">downloads page</a>'))
        else:
            rows.append(('Install', 'From the source repository: see <a href="#install">Installation</a> below. No packaged download yet.'))
        if p['machine_name'] in FOUNDATIONS:
            rows.append(('Role', 'Foundation: ' + e(FOUNDATIONS[p['machine_name']])))
        flag = next((f for f in flags if any(m == p['machine_name'] for _, m in f['plugins'])), None)
        flag_html = ''
        if flag:
            flag_html = f'<p>Part of the <a href="/#capabilities">{e(flag["name"])}</a> capability.'
            flag_html += (f' <a href="{e(flag["video"])}">Watch the walkthrough</a>.' if flag['video'] else '') + '</p>'
        table = ''.join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)

        sec = readme_sections(p['machine_name'])
        extra = content_html(p['slug'])
        req = sec.get('Requirements', '')
        limits = sec.get('Not implemented', '')
        if p['machine_name'] in bundles:
            install = (f'<p>Download the bundle and the runtime from the <a href="{DOWNLOADS}">downloads page</a>, '
                       'then follow the bundle\'s INSTALL.md. In short, from the AtoM root, after a backup and on a staging copy first:</p>'
                       '<pre tabindex="0" aria-label="Code"><code>unzip ahgRuntimePlugin-&lt;version&gt;.zip -d plugins/\n'
                       f'unzip {e(p["machine_name"])}-&lt;version&gt;.zip -d plugins/\n'
                       f'php plugins/{e(p["machine_name"])}/bin/install-plugin-schema.php \\\n'
                       '    --database=&lt;database&gt; --user=&lt;user&gt; --password=&lt;password&gt;</code></pre>'
                       '<p>Then enable it in Admin &gt; Plugins, clear the cache and reload PHP.</p>')
        else:
            install = md_html(sec.get('Installation', '')) or f'<p>See the <a href="{REPO}/tree/main/{e(p["machine_name"])}">README on GitHub</a>.</p>'
        demo = DEMO_PAGES.get(p['machine_name'])
        if demo:
            demo_html = f'<p>See it on the live demo (sample data, no sign-in): <a href="{DEMO}{e(demo[0])}">{e(demo[1])}</a>.</p>'
        elif flag and flag['video']:
            demo_html = f'<p>This feature is for signed-in staff, so it is not open on the public demo. <a href="{e(flag["video"])}">Watch the walkthrough</a> instead.</p>'
        else:
            demo_html = '<p>This feature is for signed-in staff, so it is not open on the public demo.</p>'
        body = f"""<main><section><div class="wrap detail"><p class="crumb"><a href="/">Home</a> / <a href="/plugins/">Plugins</a> / {e(name)}</p>
<h1>{e(name)}</h1><p>{e(desc)}</p>{flag_html}
<table>{table}</table>
{extra or readme_summary(p['machine_name'])}
{('<h2>Requirements</h2>' + md_html(req)) if req.strip() else ''}
{('<h2>Known limits</h2>' + md_html(limits)) if limits.strip() else ''}
<h2 id="install">Installation</h2>{install}
<h2>Try it</h2>{demo_html}
<p><a href="{REPO}/tree/main/{e(p['machine_name'])}">Source and README on GitHub</a> &middot; Questions: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> or <a href="{WHATSAPP}">WhatsApp</a></p>
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
    problems = check_site(OUT) + (check_external(plugins, bundles, flags) if check_ext else [])
    if problems:
        shutil.rmtree(OUT)
        raise SystemExit('build refused, live site left unchanged:\n  ' + '\n  '.join(problems))
    # Swap the checked build in.
    old = OUT_FINAL + '.old'
    if os.path.isdir(old):
        shutil.rmtree(old)
    if os.path.isdir(OUT_FINAL):
        os.rename(OUT_FINAL, old)
    os.rename(OUT, OUT_FINAL)
    if os.path.isdir(old):
        shutil.rmtree(old)
    print(f'built {len(plugins)} plugin pages, {len(flags)} capabilities -> {OUT_FINAL}')


if __name__ == '__main__':
    import sys
    try:
        build(check_ext='--check-external' in sys.argv)
    except BaseException:
        # Any refusal or error: drop the staging folder; the live site was never touched.
        shutil.rmtree(OUT, ignore_errors=True)
        raise
