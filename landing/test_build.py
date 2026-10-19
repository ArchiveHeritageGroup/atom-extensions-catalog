#!/usr/bin/env python3
"""Negative tests for build.py: each deliberate mistake must stop the build, and a
refused build must leave the previous site untouched. Builds from a copy of the
plugin data into a temporary folder; the live site is never touched.

    python3 landing/test_build.py
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGINS = os.path.normpath(os.path.join(HERE, '..', '..', 'atom-ahg-plugins'))


def copy_plugin_data(dst):
    """Only what build.py reads: manifests, READMEs and the downloads page."""
    for f in glob.glob(os.path.join(PLUGINS, '*', 'extension.json')) + glob.glob(os.path.join(PLUGINS, '*', 'README.md')):
        rel = os.path.relpath(f, PLUGINS)
        os.makedirs(os.path.join(dst, os.path.dirname(rel)), exist_ok=True)
        shutil.copy(f, os.path.join(dst, rel))
    for rel in ('README.md', 'docs/plugins/README.md'):
        os.makedirs(os.path.join(dst, os.path.dirname(rel)), exist_ok=True)
        shutil.copy(os.path.join(PLUGINS, rel), os.path.join(dst, rel))


def build(plugins, out):
    env = {**os.environ, 'AHG_PLUGINS_DIR': plugins, 'AHG_SITE_OUT': out}
    r = subprocess.run([sys.executable, os.path.join(HERE, 'build.py')], env=env, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def edit_json(path, change):
    data = json.load(open(path))
    change(data)
    json.dump(data, open(path, 'w'), indent=4)


def main():
    tmp = tempfile.mkdtemp(prefix='atom-ext-test-')
    base = os.path.join(tmp, 'plugins')
    out = os.path.join(tmp, 'site')
    copy_plugin_data(base)
    failures = 0

    code, log = build(base, out)
    if code != 0:
        print('FAIL baseline build should pass:\n' + log)
        return 1
    marker = os.path.join(out, 'index.html')
    good = open(marker).read()
    print('ok   baseline build passes')

    def readme_total(d):
        p = os.path.join(d, 'README.md')
        s = open(p).read()
        open(p, 'w').write(s.replace('Totals: 122 plugins', 'Totals: 120 plugins'))

    def broken_link(d):
        p = os.path.join(d, 'ahgAIPlugin', 'README.md')
        s = open(p).read()
        open(p, 'w').write(s.replace('## Requirements\n', '## Requirements\n\n<a href="/plugins/no-such-page.html">gone</a>\n', 1))

    cases = [
        ('missing licence', lambda d: edit_json(os.path.join(d, 'ahgAIPlugin', 'extension.json'), lambda j: j.pop('license')),
         'no license'),
        ('wrong licence', lambda d: edit_json(os.path.join(d, 'ahgAIPlugin', 'extension.json'), lambda j: j.update(license='GPL-3.0')),
         'is not AGPL-3.0-or-later'),
        ('stale README total', readme_total, 'README.md says 120 plugins'),
        ('unjustified test status', lambda d: edit_json(os.path.join(d, 'ahgAIPlugin', 'extension.json'), lambda j: j.update(tested_at='2026-08-18')),
         'tested_at set but not in the README verified standalone set'),
        ('verified plugin missing its date', lambda d: edit_json(os.path.join(d, 'ahgBackupPlugin', 'extension.json'), lambda j: j.pop('tested_at')),
         'in the README verified standalone set but has no tested_at'),
        ('broken internal link', broken_link, 'link to /plugins/no-such-page.html has no page'),
    ]
    for name, mutate, expect in cases:
        case = os.path.join(tmp, 'case')
        shutil.rmtree(case, ignore_errors=True)
        shutil.copytree(base, case)
        mutate(case)
        code, log = build(case, out)
        untouched = os.path.exists(marker) and open(marker).read() == good and not os.path.exists(out + '.building')
        if code != 0 and expect in log and untouched:
            print(f'ok   {name}: refused, site untouched')
        else:
            failures += 1
            print(f'FAIL {name}: exit {code}, expected "{expect}", site untouched={untouched}\n{log[-400:]}')

    shutil.rmtree(tmp)
    print('all passed' if not failures else f'{failures} failed')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
