# AHG Plugins — Manual Test Checklist (PILOT)

Manual end-to-end test checklist. Tick ☐→☑ per functionality. Record Pass/Fail + notes. Source: each plugin's user + technical manual.

**PILOT — 2 plugins shown to lock the format before generating all 111.**


## ahgIngestPlugin — Data Ingestion Manager

### User-facing functionality (from user guide)

| ✔ | Functionality | Source | Result (P/F) | Notes |
|---|---|---|---|---|
| ☐ | Step 1.1: Open a New Ingestion | UG step | | |
| ☐ | Step 1.2: Fill In Session Details | UG step | | |
| ☐ | Step 1.3: Configure Parent Placement | UG step | | |
| ☐ | Step 1.4: Configure Output Options | UG step | | |
| ☐ | Step 1.5: Configure AI Processing (Optional) | UG step | | |
| ☐ | Step 2.1: Choose Upload Method | UG step | | |
| ☐ | Step 2.2: File Auto-Detection | UG step | | |
| ☐ | Step 2.3: Preview Data (First 10 Rows) | UG step | | |
| ☐ | Step 2.4: ZIP File Extraction (if applicable) | UG step | | |
| ☐ | Step 3.1: Two-Column Mapping Interface | UG step | | |
| ☐ | Step 3.2: Default Value Assignment | UG step | | |
| ☐ | Step 3.3: Digital Object Matching Strategy | UG step | | |
| ☐ | Step 3.4: Metadata Extraction Panel | UG step | | |
| ☐ | Saved Mapping Profiles | UG step | | |
| ☐ | Step 4.1: Automatic Validation Runs | UG step | | |
| ☐ | Step 4.2: Validation Summary | UG step | | |
| ☐ | Step 4.3: Review Issues | UG step | | |
| ☐ | Step 4.4: Inline Fix or Exclude Rows | UG step | | |
| ☐ | Duplicate Detection Methods | UG step | | |
| ☐ | Step 5.1: Hierarchical Tree Visualization | UG step | | |
| ☐ | Step 5.2: SIP/DIP Package Preview (if enabled) | UG step | | |
| ☐ | Step 5.3: Approval Actions | UG step | | |
| ☐ | Step 6.1: Live Progress Bar | UG step | | |
| ☐ | Step 6.2: Completion Report | UG step | | |
| ☐ | Manifest CSV Format | UG step | | |
| ☐ | Session Dashboard | UG | | |
| ☐ | Rollback | UG | | |
| ☐ | CSV Templates | UG | | |
| ☐ | Supported File Formats | UG | | |

### Technical surface (routes — from technical manual)

| ✔ | Functionality | Source | Result (P/F) | Notes |
|---|---|---|---|---|
| ☐ | Route /ingest → action index | TECH route | | |
| ☐ | Route /ingest/new → action configure | TECH route | | |
| ☐ | Route /ingest/:id/configure → action configure | TECH route | | |
| ☐ | Route /ingest/:id/upload → action upload | TECH route | | |
| ☐ | Route /ingest/:id/map → action map | TECH route | | |
| ☐ | Route /ingest/:id/validate → action validate | TECH route | | |
| ☐ | Route /ingest/:id/preview → action preview | TECH route | | |
| ☐ | Route /ingest/:id/commit → action commit | TECH route | | |
| ☐ | Route /ingest/ajax/search-parent → action searchParent | TECH route | | |
| ☐ | Route /ingest/ajax/auto-map → action autoMap | TECH route | | |
| ☐ | Route /ingest/ajax/extract-metadata → action extractMetadata | TECH route | | |
| ☐ | Route /ingest/ajax/job-status → action jobStatus | TECH route | | |
| ☐ | Route /ingest/ajax/preview-tree → action previewTree | TECH route | | |
| ☐ | Route /ingest/:id/cancel → action cancel | TECH route | | |
| ☐ | Route /ingest/:id/rollback → action rollback | TECH route | | |
| ☐ | Route /ingest/:id/manifest → action downloadManifest | TECH route | | |
| ☐ | Route /ingest/template/:sector → action downloadTemplate | TECH route | | |
| ☐ | CLI: php symfony ingest:commit --job-id=N | TECH CLI | | |
| ☐ | CLI: php symfony ingest:commit --session-id=N | TECH CLI | | |


## ahgRdmPlugin — Research Data Management (authored; no manual yet)

### User-facing functionality

| ✔ | Functionality | Source | Result (P/F) | Notes |
|---|---|---|---|---|
| ☐ | Create a dataset (title, description, optional project) | UG | | |
| ☐ | Deposit files into a dataset (each → child IO + master digital object) | UG | | |
| ☐ | Run POPIA scan (deterministic SA-ID/email/phone/passport + lexicon + gateway NER + scanned-PDF OCR) | UG | | |
| ☐ | View masked scan findings + dataset verdict (CLEAR/PERSONAL/SPECIAL_CATEGORY) | UG | | |
| ☐ | Human gate: confirm/dismiss each finding with a note | UG | | |
| ☐ | Open release BLOCKED while any PERSONAL/SPECIAL finding pending/confirmed | UG | | |
| ☐ | Apply disposition: restrict / embargo / de-identify / release | UG | | |
| ☐ | Restricted files relocated off /uploads; raw URL 404s; download via ODRL-gated controller | UG | | |
| ☐ | DOI minted (test-prefix off-prod) on disposition | UG | | |
| ☐ | Public citable landing page (metadata + DOI + access badge; binaries gated) | UG | | |
| ☐ | Link / create-and-link a Data Management Plan (DMP) to a dataset | UG | | |
| ☐ | Compliance scoreboard (filter by institution/verdict/disposition) — admin | UG | | |
| ☐ | Roll-up dashboard (8 KPIs + 5 Chart.js charts + date/faculty filters) — admin | UG | | |
| ☐ | CLI demo: php symfony rdm:demo --fresh (full synthetic pipeline) | TECH CLI | | |

### Access-control checks (ACL)

| ✔ | Functionality | Source | Result (P/F) | Notes |
|---|---|---|---|---|
| ☐ | Mutations (deposit/scan/resolve/disposition/DMP) deny non-owner non-admin | TECH ACL | | |
| ☐ | Index scoped to depositor for non-admins; admin sees all | TECH ACL | | |
| ☐ | Dashboard + compliance require admin | TECH ACL | | |
| ☐ | Public landing reachable without login; binaries not | TECH ACL | | |
