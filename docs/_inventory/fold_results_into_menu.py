#!/usr/bin/env python3
"""Fold Playwright route results into the menu-driven checklist, producing the
end-to-end test DOCX: every menu item = screen, every link/URL under it,
auto-ticked from the Playwright pass; rest left ☐ for the manual tester."""
import re, json, os

INV = '/usr/share/nginx/archive/atom-extensions-catalog/docs/_inventory'
SRC = f'{INV}/AHG_Menu_Test_Checklist.md'
DEST = f'{INV}/AHG_EndToEnd_Test_Checklist.md'
vmap = json.load(open('/tmp/verdict_map.json')) if os.path.exists('/tmp/verdict_map.json') else {}

# also pull in the latest param results files directly (run2 may have finished after map build)
for f in ['/tmp/param_results.tsv', '/tmp/param_results2.tsv']:
    if os.path.exists(f):
        for l in open(f):
            p = l.rstrip('\n').split('\t')
            if len(p) >= 4 and p[0].startswith('/'):
                vmap[p[0]] = [p[2], p[3]]

lines = open(SRC).read().split('\n')
out = []
counts = {'PASS': 0, 'FAIL': 0, 'N/A': 0, 'SKIP': 0, 'MANUAL': 0}
fails = []
for l in lines:
    m = re.match(r'^\| ☐ \| `(/[^`]+)` \| ([^|]*)\| ([^|]*)\| *\| *\|', l)
    if not m:
        out.append(l)
        continue
    path = m.group(1)
    v = vmap.get(path)
    if v:
        verdict, note = v[0], v[1]
        tick = '☑' if verdict == 'PASS' else '☐'
        if verdict == 'FAIL':
            fails.append(f'{path} ({note})')
        counts[verdict] = counts.get(verdict, 0) + 1
        result = verdict
    else:
        # parameterised/destructive/untested -> leave for manual tester
        tick = '☐'
        result = ''
        note = 'manual'
        counts['MANUAL'] += 1
    parts = l.split('|')
    parts[1] = f' {tick} '
    parts[5] = f' {result} '
    parts[6] = f' {note} '
    out.append('|'.join(parts))

# header summary
hdr_i = next((i for i, x in enumerate(out) if x.startswith('# AHG')), 0)
summary = (f"\n**Playwright auto-test summary (2026-06-28):** "
           f"PASS={counts['PASS']} · FAIL={counts['FAIL']} · "
           f"N/A={counts['N/A']} · destructive/manual={counts['MANUAL']}. "
           f"☑ = passed automated GET; ☐ = awaiting your manual check "
           f"(parameterised, destructive/POST, or button/JS interaction). "
           f"FAIL rows are flagged in the Result column.\n")
out.insert(hdr_i + 1, summary)
open(DEST, 'w').write('\n'.join(out))
print(f"wrote {DEST}")
print('counts:', counts)
if fails:
    print('FAILS:\n  ' + '\n  '.join(sorted(set(fails))))
