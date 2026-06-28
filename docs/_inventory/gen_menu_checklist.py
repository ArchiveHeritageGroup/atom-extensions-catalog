#!/usr/bin/env python3
"""Menu-driven manual test checklist: each menu item = a screen; under it every link/URL."""
import os, re, glob, subprocess

ROOT='/usr/share/nginx/archive'; PLUGDIR=f'{ROOT}/atom-ahg-plugins'; CAT=f'{ROOT}/atom-extensions-catalog/docs'

# --- menu hierarchy from /tmp/menu.tsv (parent\tname\tlabel) ---
menu=[]
for ln in open('/tmp/menu.tsv'):
    parts=ln.rstrip('\n').split('\t')
    if len(parts)==3: menu.append(parts)  # (parent, name, label)
children={}
for parent,name,label in menu:
    children.setdefault(parent,[]).append((name,label))

# --- all routes from plugin configs: (path, action, plugin) ---
routes=[]
for cf in glob.glob(f'{PLUGDIR}/*/config/*Configuration.class.php'):
    plug=cf.split('/atom-ahg-plugins/')[1].split('/')[0]
    t=open(cf,errors='ignore').read()
    for m in re.finditer(r"->(?:any|get|post|put|delete)\(\s*'[^']+'\s*,\s*'([^']+)'\s*,\s*'([^']+)'",t):
        routes.append((m.group(1),m.group(2),plug))
# dedupe by path
seen=set(); R=[]
for p,a,pl in routes:
    if p in seen: continue
    seen.add(p); R.append((p,a,pl))

def keywords(name,label):
    """derive path keywords from a menu item name/label"""
    s=re.sub(r'([a-z0-9])([A-Z])',r'\1 \2',name).lower()
    s=s.replace('browse','').replace('add','').replace('manage','').replace('menu','')
    words={w for w in re.split(r'[^a-z]+',s) if len(w)>3}
    # singularise crude
    extra=set()
    for w in list(words):
        if w.endswith('s'): extra.add(w[:-1])
    return words|extra

def routes_for(name,label):
    kws=keywords(name,label)
    if not kws: return []
    out=[]
    for p,a,pl in R:
        path=p.lower()
        if any(k in path for k in kws):
            out.append((p,a,pl))
    return out[:40]

# Authored rich sub-functions for the core ISAD-style entity screens (the linked panels)
PANELS={
 'addInformationObject':"Core ISAD(G) fields; linked panels — Provenance, AI (NER/summarise/translate/spellcheck/suggest/face), Rights (PREMIS/CC/RightsStatements/embargo/TK), Digital object (upload/IIIF/media/3D/watermark/metadata), Security classification, Custom fields, Audit, Version control, Preservation, Share link",
 'addActor':"Core ISAAR-CPF fields; Authority resolution (ULAN/LCNAF/VIAF/Wikidata/ORCID), Contact, AI, linked descriptions, custom fields, audit",
 'addRepository':"Core ISDIAH fields; logo/theme, holdings, uploads path, custom fields, audit",
 'addAccessionRecord':"Core accession; Donor + donor agreement, Rights holder, Physical storage, create-description, deaccession, audit",
 'addTerm':"Term labels/scope/relationships (SKOS); semantic/thesaurus sync, used-in, SKOS export",
 'addFunction':"Core ISDF fields; relationships, linked records",
}

TOP={'add':'Add (create records)','manage':'Manage','import':'Import','admin':'Admin',
     'browse':'Browse / Discovery','browseInstitution':'Browse — our collection',
     'mainMenu':'Main menu','clipboard':'Clipboard','users':'Admin — Users',
     'groups':'Admin — Groups','staticPagesMenu':'Static pages'}

out=["# AHG — Menu-Driven Manual Test Checklist","",
 "Every navigation menu item is a **screen**; under each, every link/URL reachable from it is a tick-box test item. Walk the menus top-to-bottom. Tick ☐→☑; record Pass/Fail + notes.","",
 "Source: AtoM `menu` table + plugin route registrations. Generated 2026-06-27.",""]

done_items=set()
for top in ['add','manage','import','admin','users','groups','staticPagesMenu','browse','browseInstitution','mainMenu','clipboard']:
    if top not in children: continue
    out.append(f"\n# MENU: {TOP.get(top,top)}\n")
    for name,label in children[top]:
        if name in done_items: continue
        done_items.add(name)
        out.append(f"\n## {label}  ·  `{name}`\n")
        if name in PANELS:
            out.append(f"*Linked panels & sub-functions:* {PANELS[name]}\n")
        rs=routes_for(name,label)
        out.append("| ✔ | Link / URL | Action | Plugin | Result | Notes |")
        out.append("|---|---|---|---|---|---|")
        if rs:
            for p,a,pl in rs:
                out.append(f"| ☐ | `{p}` | {a} | {pl} | | |")
        else:
            out.append(f"| ☐ | (open **{label}** from the menu) | {name} | core | | |")
        out.append("")

dest=f'{CAT}/_inventory/AHG_Menu_Test_Checklist.md'
open(dest,'w').write('\n'.join(out))
print(f"wrote {dest}: {len(done_items)} menu-item screens, {sum(1 for l in out if l.startswith('| ☐'))} link/URL items")
