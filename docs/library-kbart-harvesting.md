# KBART e-resource feeds (vendor harvesting)

KBART (**K**nowledge **B**ases **A**nd **R**elated **T**ools, a NISO recommended practice) is the standard tab-separated format vendors use to publish the title lists and date coverage of the e-resource packages you subscribe to. The library module can register one or more vendor KBART feeds, download and parse them, and keep an audit log of every harvest — so your catalogue knows which electronic titles a package covers and for which date ranges.

## Where it lives

**Library → KBART vendors**, or directly: `/library/kbart/vendors`

The vendors page lists every registered feed with its name, source URL, active flag, and the time of its last fetch.

## Adding a vendor feed

`/library/kbart/vendor/add`

Provide:

- **Name** — a label for the package/provider (e.g. "ProQuest Ebook Central", "JSTOR Arts & Sciences").
- **URL** — the HTTPS address of the vendor's KBART `.txt`/`.tsv` file.
- **Active** — marks the vendor as one you intend to keep harvesting (see *Scheduling* below).

Edit an existing vendor at `/library/kbart/vendor/edit/:id`, enable/disable it at `/library/kbart/vendor/toggle/:id`, and remove it at `/library/kbart/vendor/delete/:id`.

## Fetching a feed

`/library/kbart/vendor/fetch/:id` — the **Fetch now** action.

Fetching downloads the vendor's KBART file (30-second timeout) and parses it as tab-separated values keyed by the KBART column names, including the standard fields:

- `publication_title`
- `print_identifier` / `online_identifier` (ISSN/ISBN)
- `date_first_issue_online`, `num_first_vol_online`, `num_first_issue_online`
- `date_last_issue_online`, `num_last_vol_online`, `num_last_issue_online`
- `title_url`, `first_author`, `title_id`
- `embargo_info`, `coverage_depth`, `coverage_notes`

Each fetch records how many rows were read and any parse/validation problems.

## Import log

`/library/kbart/vendor/log/:id`

Every fetch writes an entry you can review here: when it ran, how many rows the feed contained, and any errors (unreachable URL, malformed TSV, missing required columns). Use it to confirm a harvest succeeded and to diagnose a feed a vendor has changed or broken.

## Scheduling

Harvesting is currently **manual** — open a vendor and click **Fetch now** to pull the latest feed. The **Active** flag marks vendors you want kept up to date; automatic, scheduled harvesting of all active vendors is not yet enabled, so re-fetch feeds by hand (or after a vendor notifies you of a holdings change) until scheduled harvesting ships.

## Data

KBART harvesting uses two tables:

- `library_kbart_vendor` — one row per registered feed (name, URL, active flag, last-fetch timestamp).
- `library_kbart_import_log` — one row per fetch (timestamp, row count, error detail).

## Prerequisites

- The server must be able to reach the vendor URL over outbound HTTPS.
- The feed must be a valid KBART tab-separated file with the standard header row; non-KBART or HTML responses are rejected and recorded in the import log.

## Related

- **Z39.50 / SRU Integration** — for harvesting bibliographic (MARC) records from remote catalogues.
- **MARC Import/Export** — for loading and exporting catalogue records directly.
