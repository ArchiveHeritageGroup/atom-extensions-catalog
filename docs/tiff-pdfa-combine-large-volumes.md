# Large-volume TIFF → PDF/A combine (memory-safe, background, FTP intake)

## What changed and why

Combining many scanned TIFF pages into one PDF/A used to run a single ImageMagick
`convert` over **all** the files at once, in the web request. For large documents
(e.g. 258 TIFFs at ~42 MB each ≈ 11 GB) that ran the server out of memory and timed
out the request — the combine "failed on volumes."

It is now:

- **Memory-safe.** Each page is converted to its own single-page PDF with bounded
  ImageMagick limits (and `-compress JPEG`), the pages are concatenated with `qpdf`
  in batches, then a single Ghostscript pass produces the PDF/A. Peak memory is one
  page's worth (~100 MB) regardless of page count. Output is always **PDF/A** (the
  archival target; pdfa-2b by default).
- **Background.** The web "Process" / "Recreate" buttons only set the job to
  `queued`; a cron worker (`ahg:tiff-pdf-process`) runs the merge and emails the
  job's user on completion/failure.
- **FTP-friendly.** Two intake paths feed the same queue (below).

The combined PDF/A is attached to the record as a master digital object, and the
`ahg:optimize-pdfs` task then generates its fast-loading `.web.pdf` sibling.

## Intake paths

1. **From a record (Link digital object) — auto-link.** Launch the TIFF→PDF merge in
   a record context (`information_object` set). The combined PDF/A is attached to that
   record automatically.

2. **Manual server folder.** POST to `tiffpdfmerge/importFolder` with `folder=<path>`
   (and optional `information_object_id`). The files are referenced **in place** (no
   browser upload, no copy), the job is queued. The folder must sit under the allowed
   base (`app_tiff_combine_import_base`, default = web dir).

3. **FTP drop-folder — create now, link later.** Drop a folder of page TIFFs under the
   watch base named with the target record reference:

   ```
   <watch-base>/<record-ref>/page0001.tif, page0002.tif, ...
   ```

   `ahg:tiff-combine-watch` (cron) detects a ready folder (a `.ready` marker, or no file
   modified for `--stable-minutes`), maps `<record-ref>` → record (slug then identifier),
   queues the combine, and writes a `.queued` marker. If no record matches, the PDF/A is
   still created so it can be linked later. Watch base = `app_tiff_combine_watch_dir`
   (default `<web-dir>/uploads/tiff-combine`).

4. **Recreate / retry.** `tiffpdfmerge/recreate` (job_id) re-queues a completed or failed
   job — use it to regenerate after an upload finishes or after a convert failure.

## Host setup

Needs Ghostscript + qpdf + ImageMagick (`convert`) on PATH (all standard):

```bash
sudo apt-get install -y ghostscript qpdf imagemagick
```

Use a temp dir on real disk with ample free space (intermediate page PDFs are small
with `-compress JPEG`, but the merged + PDF/A copies need room). Configure via the
`temp_directory` job setting (default `/tmp/tiff-pdf-merge`); point it at non-tmpfs
storage if `/tmp` is RAM-backed.

## Cron

```cron
# Process queued combine jobs (memory-safe, notifies on done)
* * * * *      www-data  cd /usr/share/nginx/<instance> && php symfony ahg:tiff-pdf-process >> /var/log/atom-tiff-pdf.log 2>&1
# Auto-queue FTP drop-folders
*/5 * * * *    www-data  cd /usr/share/nginx/<instance> && php symfony ahg:tiff-combine-watch >> /var/log/atom-tiff-pdf.log 2>&1
```

## Backfill / manual run

```bash
cd /usr/share/nginx/<instance>
php symfony ahg:tiff-pdf-process            # process whatever is queued now
php symfony ahg:tiff-combine-watch          # scan the drop-folder once
```

## Notes

- Plugin-only; no AtoM base (`apps/qubit/...`) changes.
- Twin of the Heratio (Laravel) `ahg:optimize-pdfs` / TIFF-PDF tooling.
- Masters/originals are never modified.
