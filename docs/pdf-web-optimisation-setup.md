# PDF web optimisation (fast document loading) - AtoM-AHG setup

## Why

Large PDFs - especially scanned ones (e.g. 8 pages at ~26 MB/page = 200 MB+) -
open slowly because the master is not linearized ("fast web view" off) and each
page is a full-resolution scan image. On a digital-object show page the page-1
thumbnail links straight to the master, so clicking it makes the browser pull
the whole 200 MB file before showing anything.

The AHG plugins fix this by generating a **web-optimized sibling** next to the
master on disk: the embedded scan images are downsampled to a screen-sensible DPI
and the file is linearized. A 200 MB scan typically becomes a few MB and opens
page-1-fast. The viewer's click-through link points at the sibling when it
exists.

This is the twin of the Heratio (Laravel) `ahg:optimize-pdfs` feature. It is
**plugin-only** - no AtoM base (`apps/qubit/...`) changes - and the **master is
never modified** (it stays the download / preservation copy).

## How it works

- `ahgWebPdf` (in `ahgCorePlugin/lib/`) runs Ghostscript (downsample) + qpdf
  (linearize) and resolves the sibling URL for the viewer.
- The sibling is written as `<master-basename>.web.pdf` in the same upload
  directory as the master. **No database row is added** - it is detected by
  filename.
- `ahgCorePlugin/.../digitalobject/templates/_showText.php` (an AHG override of
  the base PDF thumbnail template) redirects its click-through link to the
  sibling when present; otherwise behaviour is unchanged.

## One-time host setup

Install Ghostscript and qpdf:

```bash
sudo apt-get install -y ghostscript qpdf      # Debian/Ubuntu
```

Verify (the helper resolves them via `command -v`):

```bash
gs --version
qpdf --version
```

If they are missing, the task and the viewer no-op cleanly - nothing breaks.

## Backfill existing documents

Dry-run first (touches nothing):

```bash
cd /usr/share/nginx/<atom-instance>
php symfony ahg:optimize-pdfs --min-mb=20
```

Apply (run as www-data so siblings land with the right ownership - never as
root):

```bash
sudo -u www-data php symfony ahg:optimize-pdfs --commit --min-mb=20 --dpi=200
```

Options: `--commit`, `--min-mb=20`, `--dpi=200` (150 = smallest, 300 = crisp),
`--max-ratio=0.8` (keep only if the sibling is at most this fraction of the
master), `--limit=0`, `--id=<digital_object id>`. Idempotent - a master that
already has a `.web.pdf` sibling is skipped, so it is safe to re-run.

## Scheduling (optional)

AtoM uses system cron for tasks. Add an off-peak daily pass, e.g.:

```cron
10 3 * * *  www-data  cd /usr/share/nginx/<atom-instance> && php symfony ahg:optimize-pdfs --commit --min-mb=20 --dpi=200 >> /var/log/atom-optimize-pdfs.log 2>&1
```

## Reversibility

Masters are never touched. To undo, delete the `*.web.pdf` files in the uploads
tree - the viewer falls straight back to the master.
