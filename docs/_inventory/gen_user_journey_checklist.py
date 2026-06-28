#!/usr/bin/env python3
"""Per-plugin USER-JOURNEY manual test checklist — functionality as a user uses it."""
import os, re, glob, json

ROOT='/usr/share/nginx/archive'; PLUGDIR=f'{ROOT}/atom-ahg-plugins'; CAT=f'{ROOT}/atom-extensions-catalog/docs'
plugins=sorted(d for d in os.listdir(PLUGDIR) if re.match(r'ahg.*Plugin$',d) and os.path.isdir(f'{PLUGDIR}/{d}'))
user_md=[os.path.basename(f) for f in glob.glob(f'{CAT}/*.md')]
INFRA={'ahgThemeB5Plugin','ahgUiOverridesPlugin','ahgCorePlugin'}

# authored user-journey steps for plugins whose user manual is absent/thin
AUTHORED={
 'ahgRdmPlugin':["Open Research datasets (/research/datasets)","Create a new dataset (title, description, optional project)","Deposit one or more files into the dataset","Run the POPIA scan and wait for the verdict","Review the masked findings (PERSONAL / SPECIAL_CATEGORY)","Confirm or dismiss each finding with a note","Try to Release openly — confirm it is blocked while PII is unresolved","Apply a disposition (restrict / embargo / de-identify / release)","Confirm a DOI is shown and the public landing page renders","Link or create a Data Management Plan for the dataset","Open the Compliance scoreboard and filter by faculty/verdict (admin)","Open the RDM dashboard and read the KPI cards + charts (admin)"],
 'ahg3DModelPlugin':["Open an information object that has a 3D model","Rotate / zoom the 3D model in the viewer","Switch to AR view on a supported device","Open a hotspot and read its annotation","Load a saved camera bookmark","(staff) Upload a new 3D model to an object","(staff) Add a hotspot to the model","(staff) Save a camera bookmark"],
 'ahgDedupePlugin':["Open the dedupe area","Configure a duplicate-detection rule","Run a dedup scan","Open a duplicate-candidate group","Compare two records side by side","Merge the duplicates and pick the surviving record","Open the dedup report"],
 'ahgDisplayPlugin':["Open the GLAM browse interface","Search and apply facets","Confirm only published records show when logged out","Open a record from the results"],
}

def toks(n):
    s=re.sub(r'^ahg|Plugin$','',n); s=re.sub(r'([a-z0-9])([A-Z])',r'\1-\2',s).lower(); return [x for x in s.split('-') if len(x)>2]
def find_ug(p):
    parts=toks(p)
    if not parts: return None
    best=None
    for fn in user_md:
        if 'user-guide' not in fn.lower() and 'manual' not in fn.lower(): continue
        if sum(1 for pt in parts if pt in fn.lower())>=max(1,len(parts)-1):
            if best is None or len(fn)<len(best): best=fn
    return best
def ext(p):
    try: return json.load(open(f'{PLUGDIR}/{p}/extension.json'))
    except Exception: return {}
def journey_from_ug(fn):
    """Ordered user actions from the user-manual workflow headings."""
    items=[]
    for l in open(f'{CAT}/{fn}',errors='ignore'):
        m=re.match(r'^#{2,4}\s+(.+)',l.strip())
        if not m: continue
        h=m.group(1).strip()
        if re.match(r'(Overview|User Guide|Table of|Quick Reference|Troubleshooting|Introduction|Conclusion|Index|Key Features|How to Access|Database Tables|Navigation Paths|Session Statuses|Supported File|Descriptive Standards)$',h,re.I): continue
        if h.startswith('+') or len(h)>95: continue
        # turn "Step 2.1: Choose Upload Method" -> "Choose Upload Method"
        h=re.sub(r'^Step\s+[\d.]+:\s*','',h)
        items.append(h)
    return items[:35]

out=["# AHG Plugins — User-Journey Manual Test Checklist","",
 "Walk each plugin **as a user would**, in order. Tick ☐→☑ when the step works; record Pass/Fail + notes. One section per plugin; only user-facing functionality (no internal routes/CLI).","",
 f"{len(plugins)} plugins. Generated 2026-06-27.",""]
n=0
for i,p in enumerate(plugins,1):
    if p in INFRA: continue
    e=ext(p); ug=find_ug(p)
    if p in AUTHORED: steps=AUTHORED[p]
    elif ug: steps=journey_from_ug(ug)
    else: steps=e.get('features',[]) or ["(no user manual — verify the plugin's main screen loads and its primary action works)"]
    if not steps: continue
    n+=1
    out.append(f"\n## {n}. {e.get('name',p)}  ({p})\n")
    desc=e.get('description','')
    if desc: out.append(f"*{desc}*\n")
    out.append("| ✔ | The user can… | Result (Pass/Fail) | Notes |")
    out.append("|---|---|---|---|")
    for s in steps:
        out.append(f"| ☐ | {s.replace('|','/')} | | |")
    out.append("")

dest=f'{CAT}/_inventory/AHG_User_Journey_Test_Checklist.md'
open(dest,'w').write('\n'.join(out))
print(f"wrote {dest}: {n} plugin sections, {sum(1 for l in out if l.startswith('| ☐'))} user-journey steps")
