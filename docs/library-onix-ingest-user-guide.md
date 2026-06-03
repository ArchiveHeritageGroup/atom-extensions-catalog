# ONIX Ingest

## A Guide for Acquisitions / Legal-Deposit Staff

---

## What it does

Ingests **ONIX for Books / ONIX-PL** XML (the EDItEUR standard used for legal-deposit and publisher feeds) through the standard 6-step ingest wizard. Each `<Product>` becomes an ingest row mapped to a bibliographic record, then runs through the same validation, deduplication and review pipeline as CSV/EAD ingest.

---

## Ingesting an ONIX file

1. **Ingest → New Session**, upload your ONIX XML. A file whose root element is `<ONIXMessage>` is detected as ONIX automatically.
2. Each `<Product>` is parsed into a row — **ISBN** (ISBN-13 preferred, then ISBN-10), **title**, **contributor**, **publisher** and **publication date**.
3. **Map & validate** — ISBN/ISSN validation and duplicate detection run as for any other ingest.
4. **Review** the parsed rows in the preview queue, then **commit**.

---

## For Administrators

- The ONIX parser maps ONIX 3.0 reference elements (`ProductIdentifier`, `TitleDetail/TitleElement/TitleText`, `Contributor/PersonName`, `PublishingDetail/Publisher`). It is namespace-agnostic.
- Reuses the existing ingest infrastructure: `ingest_session`/`ingest_file`/`ingest_row`/`ingest_validation`, ISBN validation (`IsbnMetadataMapper`) and dedupe (`ahgDedupePlugin`).
- Detection + parsing live in `IngestService` (`parseRowsFromOnix`).
