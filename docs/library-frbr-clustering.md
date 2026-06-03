# FRBR Work-Set Clustering

## Overview

The library module groups items by **work** using FRBR (Functional Requirements for
Bibliographic Records) logic. This means you see one card per work, with all
editions (manifestations) collapsed beneath it — rather than a flat list where
every edition appears separately.

**Default: ON.** The browse page opens in clustered mode. Toggle to flat list any time.

---

## How It Works

### Work Key Algorithm

Each library item receives a stable **work key** computed from its metadata:

```
work_key = SHA-256( isbn13_base10 | issn_base | lccn_normalised | title_normalised | creator_last_name )
          -> first 20 characters
```

The algorithm uses identifiers (ISBN-13, ISSN, LCCN) before falling back to
title + creator, so different editions of the same work reliably share a key.

### Clustering Rules (applied in order)

| Override | Effect |
|----------|--------|
| `force_split` | Item excluded from any work cluster — shown as a singleton |
| `force_group` | Item merged into a specific target work key |
| (none) | Normal clustering by `frbr_work_key` |

---

## Managing Overrides

Go to **Library Reports** → **FRBR Work Override** to:

- **Force-group** an item into another work (e.g. a reprint linked to the original work)
- **Force-split** an item so it never clusters with others (e.g. a summarised edition
  that should not appear alongside the full text)
- **Clear** an override to restore auto-clustering

Each override requires a reason (e.g. "2nd edition is abridged — separate work").

---

## Bulk Re-Indexing

If you import many items at once, or change the algorithm, re-run the work key
generator:

```bash
# On the PSIS server:
cd /usr/share/nginx/archive
php symfony library:frbr-reindex [--batch=500]
```

To backfill keys for items that have none (one-time operation after migration):

```bash
php symfony library:frbr-backfill [--batch=500]
```

To check work counts (useful for analytics):

```bash
php symfony library:frbr-stats
```

---

## Performance Notes

- Clustering fetches up to 5,000 items at a time client-side. For collections
  larger than 5,000 items, consider adding a search filter to limit the browse.
- Items with no identifier and no title cannot receive a work key and appear as
  singletons.
- The `frbr_work_key` column is indexed for fast lookups.

---

## Material Types and Clustering

Items are grouped by work regardless of material type. A work may contain:

- A print monograph
- An ebook
- A large-print edition
- An audio recording

All are shown under one card with a badge: **"5 editions"**.

---

## Example

**Flat list (FRBR OFF):**
- History of South Africa (Book, 2010)
- History of South Africa (Large Print, 2012)
- History of South Africa (E-book, 2014)

**Clustered (FRBR ON):**
- History of South Africa (Book, 2010) **[3 editions]**
  - Large Print, 2012
  - E-book, 2014

---

*Part of the AtoM AHG Framework — Library Module*