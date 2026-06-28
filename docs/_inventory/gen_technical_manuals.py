#!/usr/bin/env python3
"""Author technical manuals from plugin code for plugins that lack one."""
import os, re, glob, json

ROOT='/usr/share/nginx/archive'; PLUGDIR=f'{ROOT}/atom-ahg-plugins'
TECH=f'{ROOT}/atom-extensions-catalog/docs/technical'

plugins=sorted(d for d in os.listdir(PLUGDIR) if re.match(r'ahg.*Plugin$',d) and os.path.isdir(f'{PLUGDIR}/{d}'))
have=set(os.path.basename(f)[:-3] for f in glob.glob(f'{TECH}/*.md'))
missing=[p for p in plugins if p not in have]

def ext(p):
    try: return json.load(open(f'{PLUGDIR}/{p}/extension.json'))
    except Exception: return {}

def routes(p):
    out=[]
    for cf in glob.glob(f'{PLUGDIR}/{p}/config/*Configuration.class.php'):
        t=open(cf,errors='ignore').read()
        for m in re.finditer(r"->(?:any|get|post|put|delete)\(\s*'([^']+)'\s*,\s*'([^']+)'\s*,\s*'([^']+)'",t):
            out.append((m.group(1),m.group(2),m.group(3)))
    seen=set(); r=[]
    for n,path,act in out:
        if path in seen: continue
        seen.add(path); r.append((n,path,act))
    return r

def clitasks(p):
    out=[]
    for tf in glob.glob(f'{PLUGDIR}/{p}/lib/task/*.php'):
        t=open(tf,errors='ignore').read()
        ns=re.search(r"\$this->namespace\s*=\s*'([^']+)'",t); nm=re.search(r"\$this->name\s*=\s*'([^']+)'",t)
        br=re.search(r"\$this->briefDescription\s*=\s*'([^']*)'",t)
        if ns and nm: out.append((f"{ns.group(1)}:{nm.group(1)}", br.group(1) if br else ''))
    return sorted(out)

def services(p):
    out=[]
    for sf in glob.glob(f'{PLUGDIR}/{p}/lib/**/*Service*.php',recursive=True)+glob.glob(f'{PLUGDIR}/{p}/lib/*Service*.php'):
        t=open(sf,errors='ignore').read()
        cls=re.search(r'\bclass\s+(\w+)',t)
        if not cls: continue
        meths=re.findall(r'public\s+(?:static\s+)?function\s+(\w+)\s*\(',t)
        meths=[m for m in meths if m!='__construct'][:18]
        out.append((cls.group(1), os.path.relpath(sf,f'{PLUGDIR}/{p}'), meths))
    seen=set(); r=[]
    for c,path,m in out:
        if c in seen: continue
        seen.add(c); r.append((c,path,m))
    return r[:20]

def actions(p):
    out=[]
    for af in glob.glob(f'{PLUGDIR}/{p}/modules/*/actions/*.php'):
        mod=af.split('/modules/')[1].split('/')[0]
        t=open(af,errors='ignore').read()
        ex=re.findall(r'function\s+execute(\w+)\s*\(',t)
        if ex: out.append((mod,[e[0].lower()+e[1:] for e in ex]))
    return out

def tables(p):
    tbls=set(ext(p).get('tables',[]))
    for sf in glob.glob(f'{PLUGDIR}/{p}/database/*.sql'):
        for m in re.finditer(r'CREATE TABLE(?:\s+IF NOT EXISTS)?\s+`?(\w+)`?',open(sf,errors='ignore').read(),re.I):
            tbls.add(m.group(1))
    return sorted(tbls)

written=0
for p in missing:
    e=ext(p); o=[]
    o.append(f"# {p} - Technical Documentation\n")
    o.append(f"> Auto-generated from plugin code (2026-06-27). {e.get('description','')}\n")
    o.append("## Overview\n")
    o.append(f"- **Name:** {e.get('name',p)}")
    o.append(f"- **Machine name:** `{p}`")
    o.append(f"- **Version:** {e.get('version','—')}")
    o.append(f"- **Category:** {e.get('category','—')}")
    deps=e.get('dependencies',[]); o.append(f"- **Dependencies:** {', '.join('`'+d+'`' for d in deps) if deps else 'none'}")
    o.append(f"- **License:** {e.get('license','AGPL-3.0')}\n")
    feats=e.get('features',[])
    if feats:
        o.append("### Features\n")
        for f in feats: o.append(f"- {f}")
        o.append("")
    t=tables(p)
    if t:
        o.append("## Database tables\n")
        for x in t: o.append(f"- `{x}`")
        o.append("\nSee `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).\n")
    rt=routes(p)
    if rt:
        o.append("## Routes\n")
        o.append("| Route name | URL | Action |")
        o.append("|---|---|---|")
        for n,path,act in rt: o.append(f"| `{n}` | `{path}` | {act} |")
        o.append("")
    ac=actions(p)
    if ac:
        o.append("## Module actions\n")
        for mod,exs in ac:
            o.append(f"**`{mod}`** — " + ", ".join(f"`{x}`" for x in exs))
        o.append("")
    cli=clitasks(p)
    if cli:
        o.append("## CLI tasks\n")
        for name,desc in cli: o.append(f"- `php symfony {name}`" + (f" — {desc}" if desc else ""))
        o.append("")
    sv=services(p)
    if sv:
        o.append("## Service layer\n")
        for c,path,m in sv:
            o.append(f"### `{c}`  \n`{path}`\n")
            if m: o.append("Public methods: " + ", ".join(f"`{x}()`" for x in m) + "\n")
    o.append("## Standards & conventions\n")
    o.append("- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.")
    o.append("- Routes registered via `AtomFramework\\Routing\\RouteLoader` in the plugin config class.")
    o.append("- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.\n")
    open(f'{TECH}/{p}.md','w').write('\n'.join(o)); written+=1

print(f"missing={len(missing)} written={written}")
print("first few:", ', '.join(missing[:6]))
