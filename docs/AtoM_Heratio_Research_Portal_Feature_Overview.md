# AtoM Heratio Research Portal — Feature Overview

**Product:** AtoM Heratio Research Portal (ahgResearchPlugin)
**Version:** 3.3.0 (Research Enhancements release, 2026-05-16)
**Vendor:** The Archive and Heritage Group (Pty) Ltd
**Contact:** johan@theahg.co.za
**Date:** May 2026

---

## What Is It?

The AtoM Heratio Research Portal is a comprehensive research support module built into the AtoM Heratio archival management platform. It transforms AtoM from a catalogue-only system into a full-service research environment — covering everything from researcher registration and reading room bookings through to material retrieval, chain-of-custody tracking, reproduction requests, and collaborative research tools.

The Research Portal is designed for GLAM institutions (Galleries, Libraries, Archives, Museums) and Digital Asset Management organisations that need to manage researcher access, track physical material movements, and provide self-service research tools to their users.

---

## Key Feature Areas

### 1. Researcher Registration and Access Control

| Feature | Description |
|---------|-------------|
| Self-registration | Researchers register online with institutional affiliation, research purpose, and ID verification |
| Admin approval workflow | Staff review, approve, or reject applications with full audit trail |
| Researcher types | Configurable types (Academic, Government, Public, Institutional) with per-type booking limits |
| Profile management | Researchers maintain their profile, ORCID integration, and contact details |

### 2. Reading Room and Bookings

| Feature | Description |
|---------|-------------|
| Room management | Configure reading rooms with capacity, opening hours, and available equipment |
| Seat assignment | Assign specific seats within rooms; track occupancy in real time |
| Online booking | Researchers book reading room sessions online, subject to type-based limits |
| Equipment booking | Book specialised equipment (microfilm readers, scanners, laptops) alongside room bookings |
| Walk-in registration | Quick registration for unbooked visitors arriving at the reading room |

### 3. Material Retrieval Queue

| Feature | Description |
|---------|-------------|
| Queue-based workflow | Requests flow through named queues: New, Rush, Retrieval, Transit, Delivery, Curatorial, Return |
| Priority management | Rush and high-priority requests are visually flagged and can be filtered |
| Call slip printing | Generate printable call slips with item details, shelf location, and researcher information |
| Batch status updates | Select multiple requests and update their status in one action |
| Automatic location tracking | The system automatically tracks each item's current location as it moves through the workflow |
| Scheduled retrieval runs | Configure scheduled retrieval windows with cutoff times |

### 4. Chain-of-Custody Tracking

A full physical chain-of-custody system that records every handoff of archival materials:

| Feature | Description |
|---------|-------------|
| Custody checkout | Record who received materials, when, in what condition, with optional barcode scanning |
| Custody check-in | Record material returns with condition-before and condition-after assessments |
| Return verification | A second staff member verifies the returned material's condition before re-shelving |
| Staff-to-staff transfer | Record handoffs between staff members (e.g., shift changes) |
| Batch checkout | Check out multiple items to researchers in a single operation |
| Batch return | Process multiple returns with per-item condition assessment |
| Full custody chain view | A unified timeline combining custody handoffs, Spectrum movement records, and provenance events |
| Spectrum 5.1 integration | Every custody event auto-generates a Spectrum-compliant movement record |

### 4a. Equipment Management

| Feature | Description |
|---------|-------------|
| Equipment inventory | Track equipment per reading room with type, brand, model, serial number, and condition |
| Equipment types | Managed via Dropdown Manager — admin-configurable (Microfilm Reader, Scanner, Computer, etc.) |
| Equipment booking | Researchers book equipment alongside reading room sessions |
| Maintenance logging | Log maintenance actions with condition before/after, performer, and next maintenance date |
| Maintenance history | Full audit trail of all maintenance per equipment item with AJAX-loaded history viewer |

### 5. Request Lifecycle and SLA

End-to-end lifecycle management for material and reproduction requests:

| Feature | Description |
|---------|-------------|
| Requests dashboard | Combined view of all material and reproduction requests with SLA status badges |
| Triage workflow | Every request is triaged (approve, deny, needs information) before processing begins |
| SLA tracking | Configurable SLA policies with warning, due, and escalation thresholds |
| Staff assignment | Assign requests to specific staff members for fulfilment |
| Correspondence | Built-in threaded messaging between staff and researchers, with internal staff-only notes |
| Request closure | Close requests with a reason (fulfilled, cancelled, duplicate, unable to fulfil) |
| Audit trail | Every status change, triage decision, assignment, and correspondence entry is logged |
| "Request this item" button | Researchers can request materials directly from catalogue description pages |

### 6. Reproduction Requests

| Feature | Description |
|---------|-------------|
| Online submission | Researchers submit reproduction requests with purpose, format, quality, and delivery preferences |
| Inline first item | Add the first archive item (with TomSelect autocomplete) directly on the creation form — type, format, specifications |
| ODRL enforcement | Reproduction requests are checked against ODRL policies before creation |
| Item-level detail | Add specific items with page/section requirements and per-item notes |
| Pricing engine | Costs calculated based on item count, format, quality, and urgency |
| Invoice generation | Staff generate invoices attached to reproduction requests |
| File delivery | Completed reproductions are uploaded with unique download tokens |
| Download audit | Every download is logged for compliance |

### 7. Collections and Discovery

| Feature | Description |
|---------|-------------|
| Personal collections | Researchers create and manage personal groupings of archival items |
| Saved searches | Save search queries and receive notifications when new results appear |
| Search result diffing | Compare search results over time using snapshots |
| Citation generation | Generate citations in 6 academic styles (APA, MLA, Chicago, Harvard, Turabian, IEEE) |

### 8. Annotations and Knowledge Management

| Feature | Description |
|---------|-------------|
| W3C Web Annotations | Standards-compliant annotations on archival items with IIIF import/export |
| Annotation Studio | Rich text editor for creating and managing annotations |
| Research journal | Personal research journal with dated entries |
| Hypotheses | Formal hypothesis tracking with evidence linking |
| Assertions | Subject-Predicate-Object triples for building knowledge graphs |
| Source assessment | Trust scoring and source credibility evaluation |

### 9. Collaboration

| Feature | Description |
|---------|-------------|
| Research projects | Create projects with collaborators, shared collections, and milestones |
| Ethics milestones | Track ethics review steps with type (IRB, consent, risk assessment), status, due date, and inline editing |
| Workspaces | Shared workspaces with discussions, shared resources, member management, and role-based access |
| Workspace CRUD | Full edit/delete for workspace details, discussions, resources (with TomSelect search), and members (role change, remove) |
| Shared collections | Workspace-linked collections with item counts and owner display |
| Peer review | Invite peers to review and comment on research outputs |
| Institutional sharing | Share research across partner institutions |

### 10. Publishing and Reproducibility

| Feature | Description |
|---------|-------------|
| Bibliographies | Manage bibliographies with RIS, BibTeX, and Zotero export |
| Reports | Generate research reports in PDF and DOCX format with rich text editing |
| Reproducibility pack | Comprehensive pack with summary cards (milestones, snapshots, resources, assertions, hypotheses, extraction jobs), computed integrity hash, and JSON download |
| Immutable snapshots | Create hash-verified snapshots of research state for reproducibility |
| RO-Crate packaging | Package research outputs as Research Object Crates |
| DOI minting | Mint DOIs for published research outputs via DataCite |
| ORCID integration | Link researcher profiles to ORCID identifiers |

### 11. AI-Powered Tools

| Feature | Description |
|---------|-------------|
| Entity extraction | AI-powered Named Entity Recognition from archival documents |
| Summarisation | Automatic text summarisation of archival descriptions |
| Validation queue | Staff review and validate AI-generated extractions |
| Entity resolution | Disambiguate and link extracted entities to authority records |

### 12. Visualisation

| Feature | Description |
|---------|-------------|
| Timeline builder | Interactive timeline of research events and archival dates |
| Geographic map | Plot archival items and events on interactive maps |
| Network graph | Visualise relationships between entities and assertions |
| Knowledge graph | Explore assertions and hypotheses as an interactive graph |

### 13. ODRL Policy Enforcement

| Feature | Description |
|---------|-------------|
| Policy management | Create, edit, and delete ODRL policies via a full-featured admin UI |
| Target types | Policies can target archival descriptions, collections, projects, snapshots, annotations, and assertions |
| Target autocomplete | TomSelect-powered search for all target types — shows names, not IDs |
| Policy types | Permission, Prohibition, and Obligation with constraint support |
| Constraints | Researcher whitelist (multi-select), date windows (from/to), and usage limits (max uses) |
| Enforcement layer | Policies enforced at 6 access points: view project, view collection, view snapshot, share project, reproducibility pack, reproduction requests |
| Default-allow | Resources with no policies are accessible by default — only explicit prohibitions block access |
| Audit logging | Every access evaluation is logged to `research_access_decision` with rationale |

### 14. API Keys and Research API

| Feature | Description |
|---------|-------------|
| API key management | Generate, list, and revoke API keys from the researcher profile |
| Scope-based permissions | Keys support Read, Write, and Search scopes — enforced by the API middleware |
| Unified key system | Research API keys are stored in the central `ahg_api_key` table with full scope enforcement |
| REST endpoints | Profile, projects, collections, bookings, bibliographies, annotations, statistics, citations |
| Rate limiting | Per-key rate limits with usage tracking |

### 15. Admin Tools

| Feature | Description |
|---------|-------------|
| Researcher management | Status tabs (All, Pending, Approved, Suspended, Expired) with live counts |
| Researcher types | CRUD with delete protection (cannot delete types assigned to researchers) |
| Statistics dashboard | Summary cards, registrations chart, bookings by room chart, breakdown by status |
| Activity log | All research actions logged and viewable with type filtering |
| Compliance dashboard | Ethics milestones, ODRL policies, security classification, trust scores per project |
| Dropdown Manager integration | Seat types, equipment types, ID types managed via Dropdown Manager |
| Seed data | All dropdown taxonomies included in `install.sql` for new installations |

---

## What's New in 3.3.0 — Research Enhancements (May 2026)

This release adds thirteen new researcher-facing features under a single bundled
update. They were ported from the Laravel Heratio reference implementation
(`docs/research-enhancements-roadmap.md`) into the Symfony 1.4 AtoM Heratio
fork to give cross-instance researchers the same workflow on both platforms.

### Studio — grounded AI artefact generator

Every research project now has a **Studio** tab. Researchers drop in items
from their evidence sets, pick an output type, and the platform generates an
LLM-grounded artefact with `[N]` citation markers tied to the source list.
Eight output types are supported:

| Type | Output |
|---|---|
| Briefing | 400–700 word markdown brief with overview, key facts, people, themes, open questions |
| Study guide | 600–1 000 word guide for graduate students with reading guide and discussion questions |
| FAQ | 6–10 Q&A pairs, each citing the supporting source |
| Timeline | Chronological event list with year-precision dates and source citations |
| Diagram | Mermaid graph showing entity relationships, plus a citation legend |
| Video script | Two-voice (Host/Expert) script for short documentary segments |
| Spreadsheet | Strict-JSON tabular extraction rendered to a downloadable `.xlsx` (via PhpSpreadsheet) |
| Audio | Two-voice podcast script; posted to a configurable TTS endpoint for `.mp3` rendering |

All AI calls flow through the existing AHG AI gateway via the `ahgAIPlugin`
`LlmService` — no new provider keys, no new infrastructure. Generation status,
token usage, model name, and elapsed time are tracked on each artefact.

### Citation hover popovers

Any `[N]` marker in a Studio artefact, report, or research output now renders
as a hover popover: source title, a 220-character snippet, and an "Open
source" link. Clicking the marker scrolls to the matching source list entry.
Implemented as a single vanilla-JS file (`citation-popover.js`) with no build
step; uses Bootstrap 5 popovers (already in the theme).

### Researcher notebooks

A new researcher-owned scratchpad. Each notebook collects:

- **Saved queries** (search expressions worth re-running)
- **AI outputs** (raw model responses worth keeping)
- **Source pins** (information objects to revisit)
- **Freeform notes**

Items can be pinned to the top, reordered, and removed. A one-click
**Promote to project** action turns a notebook into a public research
project: it creates the `research_project` row, the owner-collaborator
record, a new collection seeded with the pinned sources, and marks the
notebook as promoted (idempotent — re-promotion returns the original
project id).

### Cross-fonds reasoning queries

A single query is fanned out across N selected fonds in parallel. Each
fonds is queried via its `lft`/`rgt` MPTT range; per-fonds top-K hits are
merged and reranked by score; a single ranked list is returned. Optional
thesaurus expansion via `SemanticSearchService::expandQuery()` widens
queries when enabled.

Per-fonds K is 10; final K is 30 — both configurable. Query history is
persisted to `research_cross_fonds_query` for analytics and audit.

### Research analytics dashboard

A new date-filtered dashboard at `/research/analytics` aggregates the
already-logged `research_activity_log` and `research_citation_log` tables
into:

- **Eight KPI tiles**: total events, researchers, objects, views, searches, citations, downloads, annotations
- **Daily volume bar chart** (inline divs — no Chart.js dependency)
- **Top researchers**, **popular descriptions**, **popular collections**
- **Top search terms**, **citations by style/format**
- **Day-of-week distribution**

No new audit tables; the data is already being logged by existing actions.
New activity types added: `ai_studio`, `search_cross_fonds`,
`notebook_item_added`, `cite_export`.

### Real-time collaboration (polling)

Project-scoped live collaboration without a WebSocket broker:

- **Presence indicators** — each active collaborator gets a distinct colour
  and appears in the "Online now" list. Stale entries (90 s without a
  heartbeat) are dropped automatically.
- **Threaded project comments** with **resolve** workflow. Reuses the
  existing `research_comment` polymorphic table (`entity_type='project'`).
- **3 s polling cadence** with a comment-id cursor; both presence and new
  comments come back in a single round-trip.
- **Shared IIIF annotations** — `research_annotation` already has `project_id`
  + `visibility` (`private` / `shared` / `public`), so collaborators on the
  same project see each other's shared annotations on the same canvas.

The polling architecture allows a Reverb/Pusher swap-in later if a broker
becomes available.

### Per-record citation manager export

In addition to the existing styled citation card (Chicago / MLA / Turabian
/ APA / Harvard / UNISA), each record now has a **Copy in citation
manager format** card with six file-format downloads:

| Format | Use case |
|---|---|
| RIS | Zotero, Mendeley, EndNote import |
| BibTeX | LaTeX, JabRef |
| EndNote XML | EndNote desktop |
| APA 7 | Plain-text APA citation for paste-into-essay |
| MLA 9 | Plain-text MLA citation |
| Chicago 17 | Plain-text Chicago Notes-Bibliography |

Each download is a real file with the correct MIME type
(`application/x-research-info-systems`, `application/x-bibtex`,
`application/xml`, `text/plain`) and a slug-derived filename.

### ORCID Works push and pull

The existing ORCID OAuth flow now supports two new operations:

- **Pull works** — fetch the researcher's complete works list from ORCID
  with put-codes, titles, years, journals, DOIs, types.
- **Push work** — create a new ORCID Work record from a local citation,
  returning the new put-code.

Access tokens are persisted to `research_orcid_link` with AES-256-CBC
encryption keyed off `sf_app_secret`. The "Connect / linked / unlinked"
status page mirrors the Laravel side.

### Mobile / PWA shell

A phone-first researcher home at `/research/mobile` with:

- **Reading list** — most-recent 50 collection items
- **4-button grid** — Search, Notebooks, Bibliographies, Journal
- **Quick journal entry** form that works offline
- **Online / offline badge** that reacts to `navigator.onLine`

A new `manifest.webmanifest` + `sw.js` at the AtoM web root let the
researcher install the portal as a standalone app on their phone
("Add to home screen" → standalone mode).

### Offline mode and sync

When the device is offline, journal entries are buffered to
`localStorage` under the key `heratio_offline_queue_v1`. When the
device comes back online, the queue is POSTed to
`/research/sync/offline` and applied to either
`research_journal_entry` or `research_annotation` depending on the
entry's `kind`. Sync metadata (queued count, applied count,
conflicts, payload hash) is persisted to a new
`research_offline_sync_log` table for audit.

### ResearcherView consolidated JSON endpoint

A single round-trip endpoint at `/research/researcher-view/:id`
returns a researcher's public projects, recent shared annotations,
and ORCID-link summary in one JSON document. Designed for external
tools (Zotero, Tropy, LMS) that need to compose a researcher
dashboard without making 5+ separate calls.

### Schema additions

Eight new tables (all `IF NOT EXISTS`-idempotent in
`database/migrations/2026_05_16_research_enhancements.sql`):

| Table | Purpose |
|---|---|
| `research_studio_artefact` | LLM-generated artefacts with body, citations JSON, model + tokens + timing |
| `research_notebook` | Researcher scratchpad metadata + promote-to-project tracking |
| `research_notebook_item` | Notebook items (saved_query, ai_output, source_pin, note) |
| `research_cross_fonds_query` | Cross-fonds query history with elapsed time + result count |
| `research_collaboration_session` | Live session bookkeeping (start/end times per project) |
| `research_collaboration_presence` | Per-researcher presence row with cursor target + colour + last-seen |
| `research_orcid_link` | Encrypted ORCID tokens + scope + last-sync metadata |
| `research_offline_sync_log` | Sync run audit (queued / applied / conflicts / payload hash) |

The polymorphic `research_comment` and `research_annotation` tables
already had the columns needed for collaboration and shared
annotations, so no new comment or annotation tables were added.

### Operational notes

- **TTS endpoint** is operator-configurable via `app_ahg_tts_endpoint`
  in `apps/qubit/config/app.yml`. When unset, audio artefacts fall
  back to script-only with the transcript persisted for manual TTS
  hand-off — never a 500.
- **ORCID** is operator-configurable via `app_orcid_client_id` /
  `app_orcid_client_secret` / `app_orcid_redirect_uri`. When unset,
  the ORCID page shows a clean "not configured" alert listing the
  exact ENV keys.
- **php-fpm** must include `ReadWritePaths=/usr/share/nginx/archive/cache`
  and `ReadWritePaths=/usr/share/nginx/archive/log` in its drop-in
  when `ProtectSystem=full` is set (the host-level requirement is
  documented in the project CLAUDE.md).

---

## Accessibility (WCAG 2.1 AA)

The Research Portal is designed for accessibility compliance across all screens:

- **Skip navigation** on every page for keyboard and screen reader users
- **ARIA live regions** announce dynamic content changes to screen readers
- **Data tables** with proper headers, captions, and scope attributes
- **Status badges** use icons and text alongside colour (never colour alone)
- **Keyboard navigation** for all interactive elements with visible focus indicators
- **Form validation** with programmatic error association and alert roles
- **Decorative icons** hidden from screen readers via `aria-hidden`

---

## Compliance and Standards

| Standard | Coverage |
|----------|----------|
| WCAG 2.1 Level AA | All screens |
| Spectrum 5.1 | Object Location and Movement Control (via custody/movement integration) |
| W3C Web Annotation | Annotation data model |
| IIIF | Manifest and annotation interoperability |
| RO-Crate | Research object packaging |
| DataCite | DOI minting |
| ODRL | Digital rights policy language |

---

## Technical Requirements

| Requirement | Specification |
|-------------|---------------|
| Platform | AtoM 2.10 with AtoM Heratio Framework v2.8.2+ |
| PHP | 8.3+ |
| Database | MySQL 8.0+ |
| Browser | Chrome 90+, Firefox 90+, Safari 14+, Edge 90+ |
| Dependencies | Bootstrap 5 (included), Font Awesome 6 (included) |

---

## Database Footprint

The Research Portal uses 80+ dedicated database tables (no modifications to core AtoM tables). Key tables include:

- Researcher management (registration, types, audit)
- Reading room configuration (rooms, seats, bookings, equipment, equipment maintenance)
- Material requests (retrieval queue, scheduling, status history)
- Custody tracking (handoff records, Spectrum movement integration)
- Reproduction workflow (requests, items, files, invoices)
- Correspondence (threaded messaging with internal notes)
- Collections, annotations, projects, workspaces
- AI extraction, validation, entity resolution
- Reports, snapshots, bibliographies
- ODRL policies and access decisions (enforcement audit trail)
- API keys (integrated with central ahg_api_key table)
- Notification preferences and activity log
- Dropdown Manager seed data (7 taxonomies: seat_type, booking_status, researcher_status, researcher_type, material_request_status, reproduction_type, reproduction_request_status, equipment_type)

---

## Getting Started

1. **Install** the ahgResearchPlugin via the AtoM Heratio Extension Manager
2. **Run** the database migration (`database/install.sql` + migration files)
3. **Configure** reading rooms, researcher types, and SLA policies via Admin > AHG Settings
4. **Enable** the "Research" menu in Admin > Menus
5. **Test** by registering a researcher account and creating a booking

For detailed setup instructions, see the full Training Manual (included).

---

*The Archive and Heritage Group (Pty) Ltd — Preserving Heritage Through Technology*
*https://theahg.co.za*
