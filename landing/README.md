# www.atom-extensions.com

The product page and plugin catalogue for AHG Extensions for AtoM, as static HTML.

`build.py` reads every plugin's `extension.json` and README in `atom-ahg-plugins`, and
the flagship table in its README, and writes the site to `public/`. Run it after a
plugins release so versions and descriptions stay current:

    python3 landing/build.py

nginx serves `public/` (vhost: `stuff/atom-extensions.com.conf` on the PSIS host). www.atom-extensions.com is the main address; atom-extensions.com, atom-extensions.info and atom-extensions.theahg.co.za redirect to it.

## Checks

`build.py` builds into `public.building` and swaps it in only when every check passes, so a refused build leaves the live site as it was. It refuses:

- a plugin without a licence, version or description, or with a licence other than AGPL-3.0-or-later;
- two plugins with the same page address;
- a README "Totals: N plugins" line that disagrees with the number of manifests;
- a `tested_at` date on a plugin outside the README's verified standalone set, or a verified plugin without one;
- an internal link or `#anchor` that does not resolve in the built site.

`python3 landing/build.py --check-external` also checks every packaged download's GitHub release and every walkthrough video link (needs the network).

`python3 landing/test_build.py` proves each refusal: it builds from a copy of the plugin data into a temporary folder, breaks one thing at a time, and confirms the build stops and the previous output is untouched.
