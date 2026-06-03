# COUNTER 5 usage statistics & SUSHI

The library module produces **COUNTER 5** usage reports for your electronic resources and can serve them over **SUSHI** so consortia, funders, and your own analytics can harvest them automatically.

- **COUNTER** (Counting Online Usage of Networked Electronic Resources) is the international standard for consistent, comparable e-resource usage reporting.
- **SUSHI** (Standardized Usage Statistics Harvesting Initiative) is the companion protocol a remote client uses to pull those reports without anyone exporting files by hand.

## Usage dashboard

**Admin → Library → COUNTER usage**, or directly: `/admin/library/counter`

Shows the usage accrued in the catalogue, aggregated for reporting. Usage events are stored in `library_usage_event` and rolled up into the COUNTER report types below.

## COUNTER 5 reports

The module generates the COUNTER 5 standard reports:

| Report | What it covers |
|---|---|
| **TR_J1** | Journal requests (excluding OA_Gold) — the headline "how much were our journals used" report |
| **TR_J3** | Journal usage by access type |
| **PR** | Platform Report — usage across the whole platform |
| **DR** | Database Report — usage per database/resource |
| **IR** | Item Report — usage at the individual item level |

Each report can be emitted as **JSON** (the COUNTER 5 JSON model) or **TSV** (the tabular export auditors and spreadsheets expect).

## SUSHI harvesting

**Admin → Library → SUSHI settings**, or directly: `/admin/library/sushi`

This page configures the credentials a remote SUSHI client presents when harvesting your reports. A harvest request must carry the three standard SUSHI headers:

- `X-Requestor-Id`
- `X-Customer-Id`
- `X-API-Key` — matched against the key set on this page (until a key is set, requests are allowed so you can complete first-time setup)

A missing header or a wrong key is rejected with the relevant COUNTER error (see below). Every harvest request is recorded in `library_sushi_access_log` for audit.

### COUNTER/SUSHI error codes

The endpoint returns COUNTER-standard exception codes:

| Code | Meaning |
|---|---|
| 1000 | No usage available for the requested report/period |
| 2000 | Service busy / timeout |
| 3000 | Invalid or missing request syntax |
| 4000 | Invalid date range |
| 5000 | Report request limit exceeded |
| 6000 | Authentication failed (bad/missing API key) |
| 9000 | Internal error |

## Data

| Table | Purpose |
|---|---|
| `library_usage_event` | Raw usage events that the COUNTER reports aggregate |
| `library_counter_settings` | COUNTER/SUSHI configuration, including the SUSHI API key |
| `library_sushi_access_log` | Audit log of every SUSHI harvest request |

## Related

- **Library catalogue & OPAC** — the activity that generates usage events.
- **KBART e-resource feeds** — for the title-level holdings of the packages whose usage these reports count.

## Excel (XLSX) export (v3.46.0)

COUNTER R5 reports can now be downloaded as **XLSX** in addition to JSON and TSV. On **Admin → Library → COUNTER**, pick a report (PR / TR_J1 / TR_J3 / DR / IR), choose the **Excel** format, and **Download**. The workbook carries a report-header block (Report_ID, institution, reporting period, created) followed by the data rows.
