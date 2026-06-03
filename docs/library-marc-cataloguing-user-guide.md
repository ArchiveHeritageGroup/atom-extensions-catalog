# MARC Cataloguing

## A Guide for Cataloguers

---

## What it does

- **MARC21 import** — both **binary ISO 2709** (`.mrc`) and **MARCXML**.
- **Copy cataloguing** — search a Z39.50 target, preview the returned records, and import the chosen one.
- **Validation** — checks the leader, indicators and required subfields before import.
- **Round-trip preservation** — the original leader, `005` (last transaction) and `008` (fixed-length data) are kept and re-emitted on export, instead of being regenerated.
- **Conflict detection** — incoming records are checked against existing holdings by ISBN (020), ISSN (022), OCLC (035) and LCCN (010) so duplicates are flagged rather than silently created.

---

## Importing MARC

1. **Cataloguing → Import MARC**, upload a `.mrc` (binary) or MARCXML file.
2. Records are **validated** — leader length, indicator values, mandatory `245` and required `$a` subfields. Issues are reported per record.
3. **Conflicts** against existing holdings (by standard identifier) are surfaced for review before commit.
4. On import, the leader / `005` / `008` are stored so a later **export** reproduces them.

## Copy cataloguing (Z39.50)

**Cataloguing → Copy Cataloguing**: pick a target, run a CCL search (e.g. `ti=appraisal` or `isbn=…`), preview the results, and **Import** the record you want — it is decoded and added to the catalogue.

---

## For Administrators

- Services: `MarcService` (import/export, `parseMarc21`, `findConflicts`), `Marc21DecoderService` (ISO 2709 + `validate()`); copy cataloguing reuses `Z3950Service`.
- New `library_item` columns: `marc_leader`, `marc_005`, `marc_008` (round-trip preservation).
- MARCXML export is also available via the metadata-export module (`marc21` format).
