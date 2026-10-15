# atom-extensions.theahg.co.za

The product page and plugin catalogue for AHG Extensions for AtoM, as static HTML.

`build.py` reads every plugin's `extension.json` and README in `atom-ahg-plugins`, and
the flagship table in its README, and writes the site to `public/`. Run it after a
plugins release so versions and descriptions stay current:

    python3 landing/build.py

nginx serves `public/` (vhost: `stuff/atom-extensions.theahg.co.za.conf` on the PSIS host).
