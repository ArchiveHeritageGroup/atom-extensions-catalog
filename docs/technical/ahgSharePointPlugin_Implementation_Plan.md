# ahgSharePointPlugin — Implementation Plan

**Status:** Planning complete, decisions locked, ready to scaffold Phase 1.
**Author:** The Archive and Heritage Group (Pty) Ltd
**Date:** 2026-05-10
**Targets (must achieve 100% feature parity):**
- AtoM Heratio (Symfony 1.x + atom-framework) at `/usr/share/nginx/archive` → `atom-ahg-plugins/ahgSharePointPlugin/`
- Heratio standalone (Laravel 12 monorepo) at `/usr/share/nginx/heratio` → `packages/ahg-sharepoint/`
**Namespaces:** `AtomExtensions\SharePoint` (AtoM plugin) / `AhgSharePoint` (Heratio package)

---

## 1. Purpose

Integrate Microsoft 365 SharePoint Online with AtoM Heratio so that:

1. **Records management handoff** — when documents in SharePoint are tagged for disposition (Microsoft Purview retention labels) or change relevant content, they are ingested into AtoM as archival descriptions with attached digital objects.
2. **Staff discovery in M365** — staff working in SharePoint, Teams, or M365.com search can discover archival records held in AtoM without leaving the M365 surface.
3. **Federated search** — AtoM users (gated to staff roles) can run a single search that returns AtoM hits and SharePoint hits side-by-side.

Direction is one-way (SharePoint → AtoM). No data flows out of AtoM into SharePoint at the data level; only search queries do.

---

## 2. Locked Decisions (2026-05-10)

| # | Area | Decision | Rationale |
|---|------|----------|-----------|
| 1 | Graph client | Hand-rolled via framework `HttpClientService` | ~10 endpoints needed; reuses existing SSRF protection, timeouts, blocked-host checks; no transitive deps |
| 2 | Settings UI | Add `sharepoint` section to `ahgSettingsPlugin` (precedented edit to locked plugin) | 12 sections already added by other plugins; keeps unified Admin > AHG Settings UX |
| 3 | `ingest_session` schema | Add nullable `source VARCHAR(20) DEFAULT 'wizard'` column | Lets webhook ingest reuse `IngestCommitService` cleanly; additive, safe |
| 4 | JWT validation | `firebase/php-jwt` composer dep (added to `atom-framework/composer.json`) | Phase 3 connector feed needs inbound AAD JWT validation; small, well-maintained, JWKS support |
| 5 | Webhook URL | `psis.theahg.co.za/sharepoint/webhook` direct, path-based nginx rate limit | Simplest; existing TLS cert; no new DNS or subdomain |
| 6 | Federated search permissions | Gate AtoM-side federated tab to staff (editor/admin) only | App-only Graph token returns un-trimmed; honest mitigation without OBO complexity in v1 |
| 7 | Purview disposition events | Half-day verification spike at start of Phase 2 | Need to confirm whether `driveItem updated` notifications fire on retention-label changes, or whether O365 Activity API is required |

---

## 3. Architecture

### Design principle — thin SharePoint adapter

The plugin delegates everything heavy to existing AtoM Heratio services:

| SharePoint plugin concern | Delegates to |
|---------------------------|--------------|
| Ingest pipeline (validation, AI processing, OAIS packages, DB inserts) | `ahgIngestPlugin` `IngestCommitService` |
| Background jobs, retry, backoff, batching | `atom-framework` `QueueService` + `ahg_queue_*` tables |
| Encrypted secret storage | `atom-framework` `EncryptionService` (XChaCha20-Poly1305) |
| Settings UI | `ahgSettingsPlugin` (new `sharepoint` section) |
| Audit trail | `ahgAuditTrailPlugin` `AuditService` |
| Webhook patterns (HMAC, retry, status enum, delivery log) | Mirror `ahgAPIPlugin` `WebhookService` |
| Outbound HTTP | `atom-framework` `HttpClientService` |

SharePoint-specific code is limited to:

- Graph OAuth2 client-credentials token flow + token cache
- Graph delta query handling (sync state, cursors)
- Graph webhook subscription lifecycle (create / validate / renew / delete)
- SP item → AtoM field projection (column mapping)
- Purview retention label → AtoM disposition mapping
- AtoM-side federated search wrapper around Graph Search API
- M365-facing connector OData feed (Phase 3)

### Plugin directory structure

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 654 676" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="653" height="675" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="46.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="74.0" x2="42.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="82.0" x2="49.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="82.0" x2="53.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="82.0" x2="56.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="60.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="17.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="98.0" x2="20.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="98.0" x2="24.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="98.0" x2="28.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="98.0" x2="31.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="46.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="106.0" x2="42.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="42.4" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="114.0" x2="49.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="114.0" x2="53.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="114.0" x2="56.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="114.0" x2="60.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="122.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="130.0" x2="56.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="130.0" x2="60.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="146.0" x2="74.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="138.0" x2="71.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="146.0" x2="78.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="146.0" x2="82.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="146.0" x2="85.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="146.0" x2="89.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="17.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="162.0" x2="20.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="162.0" x2="24.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="162.0" x2="28.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="162.0" x2="31.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="46.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="170.0" x2="42.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="42.4" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="178.0" x2="49.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="178.0" x2="53.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="178.0" x2="56.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="178.0" x2="60.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="186.0" x2="42.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="42.4" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="194.0" x2="74.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="186.0" x2="71.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="194.0" x2="71.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="194.0" x2="78.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="194.0" x2="82.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="194.0" x2="85.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="194.0" x2="89.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="202.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="42.4" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="74.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="202.0" x2="71.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="71.2" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="210.0" x2="78.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="210.0" x2="82.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="210.0" x2="85.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="210.0" x2="89.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="13.6" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="218.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="42.4" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="74.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="218.0" x2="71.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="71.2" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="226.0" x2="78.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="226.0" x2="82.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="226.0" x2="85.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="226.0" x2="89.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="234.0" x2="13.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="242.0" x2="13.6" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="234.0" x2="42.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="242.0" x2="42.4" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="242.0" x2="74.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="234.0" x2="71.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="242.0" x2="71.2" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="242.0" x2="78.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="242.0" x2="82.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="242.0" x2="85.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="242.0" x2="89.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="250.0" x2="13.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="258.0" x2="13.6" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="250.0" x2="42.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="258.0" x2="42.4" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="74.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="250.0" x2="71.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="71.2" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="258.0" x2="78.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="258.0" x2="82.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="258.0" x2="85.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="258.0" x2="89.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="266.0" x2="13.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="274.0" x2="13.6" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="266.0" x2="42.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="274.0" x2="42.4" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="274.0" x2="74.8" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="266.0" x2="71.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="274.0" x2="71.2" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="274.0" x2="78.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="274.0" x2="82.0" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="274.0" x2="85.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="274.0" x2="89.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="282.0" x2="13.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="290.0" x2="13.6" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="282.0" x2="42.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="290.0" x2="42.4" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="290.0" x2="74.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="282.0" x2="71.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="290.0" x2="71.2" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="290.0" x2="78.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="290.0" x2="82.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="290.0" x2="85.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="290.0" x2="89.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="298.0" x2="13.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="306.0" x2="13.6" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="298.0" x2="42.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="306.0" x2="42.4" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="306.0" x2="74.8" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="298.0" x2="71.2" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="306.0" x2="71.2" y2="314.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="306.0" x2="78.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="306.0" x2="82.0" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="306.0" x2="85.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="306.0" x2="89.2" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="314.0" x2="13.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="322.0" x2="13.6" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="314.0" x2="42.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="322.0" x2="42.4" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="322.0" x2="74.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="314.0" x2="71.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="322.0" x2="71.2" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="322.0" x2="78.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="322.0" x2="82.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="322.0" x2="85.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="322.0" x2="89.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="330.0" x2="13.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="338.0" x2="13.6" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="330.0" x2="42.4" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="338.0" x2="42.4" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="338.0" x2="74.8" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="330.0" x2="71.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="338.0" x2="78.4" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="338.0" x2="82.0" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="338.0" x2="85.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="338.0" x2="89.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="346.0" x2="13.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="354.0" x2="13.6" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="354.0" x2="46.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="346.0" x2="42.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="354.0" x2="42.4" y2="362.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="354.0" x2="49.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="354.0" x2="53.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="354.0" x2="56.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="354.0" x2="60.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="362.0" x2="13.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="370.0" x2="13.6" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="362.0" x2="42.4" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="370.0" x2="42.4" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="370.0" x2="74.8" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="362.0" x2="71.2" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="370.0" x2="71.2" y2="378.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="370.0" x2="78.4" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="370.0" x2="82.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="370.0" x2="85.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="370.0" x2="89.2" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="378.0" x2="13.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="386.0" x2="13.6" y2="394.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="378.0" x2="42.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="386.0" x2="42.4" y2="394.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="386.0" x2="74.8" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="378.0" x2="71.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="386.0" x2="71.2" y2="394.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="386.0" x2="78.4" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="386.0" x2="82.0" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="386.0" x2="85.6" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="386.0" x2="89.2" y2="386.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="394.0" x2="13.6" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="402.0" x2="13.6" y2="410.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="394.0" x2="42.4" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="402.0" x2="42.4" y2="410.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="402.0" x2="74.8" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="394.0" x2="71.2" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="402.0" x2="71.2" y2="410.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="402.0" x2="78.4" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="402.0" x2="82.0" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="402.0" x2="85.6" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="402.0" x2="89.2" y2="402.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="410.0" x2="13.6" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="418.0" x2="13.6" y2="426.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="410.0" x2="42.4" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="418.0" x2="42.4" y2="426.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="418.0" x2="74.8" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="410.0" x2="71.2" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="418.0" x2="71.2" y2="426.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="418.0" x2="78.4" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="418.0" x2="82.0" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="418.0" x2="85.6" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="418.0" x2="89.2" y2="418.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="426.0" x2="13.6" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="434.0" x2="13.6" y2="442.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="426.0" x2="42.4" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="434.0" x2="42.4" y2="442.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="434.0" x2="74.8" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="426.0" x2="71.2" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="434.0" x2="71.2" y2="442.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="434.0" x2="78.4" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="434.0" x2="82.0" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="434.0" x2="85.6" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="434.0" x2="89.2" y2="434.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="442.0" x2="13.6" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="450.0" x2="13.6" y2="458.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="442.0" x2="42.4" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="450.0" x2="42.4" y2="458.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="450.0" x2="74.8" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="442.0" x2="71.2" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="450.0" x2="78.4" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="450.0" x2="82.0" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="450.0" x2="85.6" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="450.0" x2="89.2" y2="450.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="458.0" x2="13.6" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="466.0" x2="13.6" y2="474.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="466.0" x2="46.0" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="458.0" x2="42.4" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="466.0" x2="49.6" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="466.0" x2="53.2" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="466.0" x2="56.8" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="466.0" x2="60.4" y2="466.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="474.0" x2="13.6" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="482.0" x2="13.6" y2="490.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="482.0" x2="74.8" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="474.0" x2="71.2" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="482.0" x2="71.2" y2="490.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="482.0" x2="78.4" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="482.0" x2="82.0" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="482.0" x2="85.6" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="482.0" x2="89.2" y2="482.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="490.0" x2="13.6" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="498.0" x2="13.6" y2="506.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="498.0" x2="74.8" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="490.0" x2="71.2" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="498.0" x2="71.2" y2="506.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="498.0" x2="78.4" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="498.0" x2="82.0" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="498.0" x2="85.6" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="498.0" x2="89.2" y2="498.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="506.0" x2="13.6" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="514.0" x2="13.6" y2="522.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="514.0" x2="74.8" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="506.0" x2="71.2" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="514.0" x2="71.2" y2="522.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="514.0" x2="78.4" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="514.0" x2="82.0" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="514.0" x2="85.6" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="514.0" x2="89.2" y2="514.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="522.0" x2="13.6" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="530.0" x2="13.6" y2="538.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="530.0" x2="74.8" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="522.0" x2="71.2" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="530.0" x2="71.2" y2="538.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="530.0" x2="78.4" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="530.0" x2="82.0" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="530.0" x2="85.6" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="530.0" x2="89.2" y2="530.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="538.0" x2="13.6" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="546.0" x2="13.6" y2="554.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="546.0" x2="74.8" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="538.0" x2="71.2" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="546.0" x2="71.2" y2="554.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="546.0" x2="78.4" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="546.0" x2="82.0" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="546.0" x2="85.6" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="546.0" x2="89.2" y2="546.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="554.0" x2="13.6" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="562.0" x2="13.6" y2="570.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="562.0" x2="74.8" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="554.0" x2="71.2" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="562.0" x2="71.2" y2="570.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="562.0" x2="78.4" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="562.0" x2="82.0" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="562.0" x2="85.6" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="562.0" x2="89.2" y2="562.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="570.0" x2="13.6" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="578.0" x2="13.6" y2="586.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="578.0" x2="74.8" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="570.0" x2="71.2" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="578.0" x2="78.4" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="578.0" x2="82.0" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="578.0" x2="85.6" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="578.0" x2="89.2" y2="578.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="594.0" x2="17.2" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="586.0" x2="13.6" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="594.0" x2="13.6" y2="602.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="594.0" x2="20.8" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="594.0" x2="24.4" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="594.0" x2="28.0" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="594.0" x2="31.6" y2="594.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="602.0" x2="13.6" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="610.0" x2="13.6" y2="618.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="610.0" x2="46.0" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="602.0" x2="42.4" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="610.0" x2="49.6" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="610.0" x2="53.2" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="610.0" x2="56.8" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="610.0" x2="60.4" y2="610.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="618.0" x2="13.6" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="626.0" x2="13.6" y2="634.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="626.0" x2="74.8" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="618.0" x2="71.2" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="626.0" x2="71.2" y2="634.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="626.0" x2="78.4" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="626.0" x2="82.0" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="626.0" x2="85.6" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="626.0" x2="89.2" y2="626.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="634.0" x2="13.6" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="642.0" x2="13.6" y2="650.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="642.0" x2="74.8" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="634.0" x2="71.2" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="642.0" x2="78.4" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="642.0" x2="82.0" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="642.0" x2="85.6" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="642.0" x2="89.2" y2="642.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="658.0" x2="17.2" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="650.0" x2="13.6" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="658.0" x2="20.8" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="658.0" x2="24.4" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="658.0" x2="28.0" y2="658.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="658.0" x2="31.6" y2="658.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">atom-ahg-plugins/ahgSharePointPlugin/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">extension.json</text><text x="38.8" y="54.0" font-size="9.5" fill="#10373E">README.md</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">config/</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">ahgSharePointPluginConfiguration.class.php</text><text x="38.8" y="102.0" font-size="9.5" fill="#10373E">database/</text><text x="67.6" y="118.0" font-size="9.5" fill="#10373E">install.sql</text><text x="67.6" y="134.0" font-size="9.5" fill="#10373E">migrations/</text><text x="96.4" y="150.0" font-size="9.5" fill="#10373E">20260510_add_source_to_ingest_session.sql</text><text x="38.8" y="166.0" font-size="9.5" fill="#10373E">lib/</text><text x="67.6" y="182.0" font-size="9.5" fill="#10373E">Services/</text><text x="96.4" y="198.0" font-size="9.5" fill="#10373E">GraphClientService.php</text><text x="96.4" y="214.0" font-size="9.5" fill="#10373E">GraphTokenCache.php</text><text x="96.4" y="230.0" font-size="9.5" fill="#10373E">GraphTokenValidatorService.php</text><text x="384.4" y="230.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="230.0" font-size="9.5" fill="#10373E">Phase</text><text x="442.0" y="230.0" font-size="9.5" fill="#10373E">3</text><text x="456.4" y="230.0" font-size="9.5" fill="#10373E">(inbound</text><text x="521.2" y="230.0" font-size="9.5" fill="#10373E">JWTs)</text><text x="96.4" y="246.0" font-size="9.5" fill="#10373E">SharePointSyncService.php</text><text x="96.4" y="262.0" font-size="9.5" fill="#10373E">SharePointSubscriptionService.php</text><text x="384.4" y="262.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="262.0" font-size="9.5" fill="#10373E">Phase</text><text x="442.0" y="262.0" font-size="9.5" fill="#10373E">2</text><text x="96.4" y="278.0" font-size="9.5" fill="#10373E">SharePointWebhookHandler.php</text><text x="384.4" y="278.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="278.0" font-size="9.5" fill="#10373E">Phase</text><text x="442.0" y="278.0" font-size="9.5" fill="#10373E">2</text><text x="96.4" y="294.0" font-size="9.5" fill="#10373E">SharePointIngestAdapter.php</text><text x="96.4" y="310.0" font-size="9.5" fill="#10373E">SharePointMappingService.php</text><text x="96.4" y="326.0" font-size="9.5" fill="#10373E">SharePointFederatedSearchService.php</text><text x="384.4" y="326.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="326.0" font-size="9.5" fill="#10373E">Phase</text><text x="442.0" y="326.0" font-size="9.5" fill="#10373E">3</text><text x="96.4" y="342.0" font-size="9.5" fill="#10373E">SharePointRetentionMapper.php</text><text x="384.4" y="342.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="342.0" font-size="9.5" fill="#10373E">Phase</text><text x="442.0" y="342.0" font-size="9.5" fill="#10373E">2</text><text x="67.6" y="358.0" font-size="9.5" fill="#10373E">Repositories/</text><text x="96.4" y="374.0" font-size="9.5" fill="#10373E">SharePointTenantRepository.php</text><text x="96.4" y="390.0" font-size="9.5" fill="#10373E">SharePointDriveRepository.php</text><text x="96.4" y="406.0" font-size="9.5" fill="#10373E">SharePointMappingRepository.php</text><text x="96.4" y="422.0" font-size="9.5" fill="#10373E">SharePointSubscriptionRepository.php</text><text x="96.4" y="438.0" font-size="9.5" fill="#10373E">SharePointSyncStateRepository.php</text><text x="96.4" y="454.0" font-size="9.5" fill="#10373E">SharePointEventRepository.php</text><text x="67.6" y="470.0" font-size="9.5" fill="#10373E">task/</text><text x="96.4" y="486.0" font-size="9.5" fill="#10373E">sharepointInstallTask.class.php</text><text x="96.4" y="502.0" font-size="9.5" fill="#10373E">sharepointTestConnectionTask.class.php</text><text x="96.4" y="518.0" font-size="9.5" fill="#10373E">sharepointSubscribeTask.class.php</text><text x="384.4" y="518.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="518.0" font-size="9.5" fill="#10373E">Phase</text><text x="442.0" y="518.0" font-size="9.5" fill="#10373E">2</text><text x="96.4" y="534.0" font-size="9.5" fill="#10373E">sharepointRenewSubscriptionsTask.class.php</text><text x="406.0" y="534.0" font-size="9.5" fill="#10373E">#</text><text x="420.4" y="534.0" font-size="9.5" fill="#10373E">Phase</text><text x="463.6" y="534.0" font-size="9.5" fill="#10373E">2</text><text x="96.4" y="550.0" font-size="9.5" fill="#10373E">sharepointSyncTask.class.php</text><text x="96.4" y="566.0" font-size="9.5" fill="#10373E">sharepointIngestEventTask.class.php</text><text x="384.4" y="566.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="566.0" font-size="9.5" fill="#10373E">Phase</text><text x="442.0" y="566.0" font-size="9.5" fill="#10373E">2</text><text x="96.4" y="582.0" font-size="9.5" fill="#10373E">sharepointStatusTask.class.php</text><text x="38.8" y="598.0" font-size="9.5" fill="#10373E">modules/</text><text x="67.6" y="614.0" font-size="9.5" fill="#10373E">sharepoint/</text><text x="96.4" y="630.0" font-size="9.5" fill="#10373E">actions/</text><text x="96.4" y="646.0" font-size="9.5" fill="#10373E">templates/</text><text x="384.4" y="646.0" font-size="9.5" fill="#10373E">#</text><text x="398.8" y="646.0" font-size="9.5" fill="#10373E">both</text><text x="434.8" y="646.0" font-size="9.5" fill="#10373E">.php</text><text x="470.8" y="646.0" font-size="9.5" fill="#10373E">(Symfony)</text><text x="542.8" y="646.0" font-size="9.5" fill="#10373E">and</text><text x="571.6" y="646.0" font-size="9.5" fill="#10373E">.blade.php</text><text x="38.8" y="662.0" font-size="9.5" fill="#10373E">docs/</text></svg></div>

---

## 4. Database Schema

All tables `InnoDB` + `utf8mb4`. `VARCHAR + COMMENT` for enumerations (no MySQL ENUM). FKs to AtoM core use `ON DELETE SET NULL` to avoid breaking core cascade chains. All six tables created by `database/install.sql`.

### 4.1 `sharepoint_tenant`

Stores Azure AD tenant binding. One row per institution (most installs = 1).

| Column | Type | Notes |
|--------|------|-------|
| id | INT AI PK | |
| name | VARCHAR(255) NOT NULL | Friendly label |
| tenant_id | VARCHAR(64) NOT NULL | Azure AD tenant GUID |
| client_id | VARCHAR(64) NOT NULL | App registration GUID |
| client_secret_ref | VARCHAR(255) NOT NULL | Reference to encrypted blob in `ahg_settings` |
| graph_endpoint | VARCHAR(255) | Default `https://graph.microsoft.com/v1.0` |
| default_site_id | VARCHAR(255) NULL | Graph site identifier |
| webhook_client_state | VARCHAR(64) NOT NULL | Random secret echoed by Graph for validation |
| status | VARCHAR(20) DEFAULT 'active' | `active, disabled, error` |
| last_token_at | DATETIME NULL | |
| last_error | TEXT NULL | |
| created_at, updated_at | DATETIME | |

### 4.2 `sharepoint_drive`

Registered SP sites + document libraries available for ingest. Site and drive collapsed into a single table since ingest always operates at drive level.

| Column | Type | Notes |
|--------|------|-------|
| id | INT AI PK | |
| tenant_id | INT NOT NULL | FK → `sharepoint_tenant.id` |
| site_id | VARCHAR(255) NOT NULL | Graph site identifier |
| site_url | VARCHAR(1000) NOT NULL | |
| site_title | VARCHAR(500) | |
| drive_id | VARCHAR(255) NOT NULL | |
| drive_name | VARCHAR(500) | |
| ingest_enabled | TINYINT(1) DEFAULT 0 | |
| sector | VARCHAR(50) DEFAULT 'archive' | `archive, museum, library, gallery, dam` |
| default_repository_id | INT NULL | AtoM repository for ingested records |
| default_parent_id | INT NULL | AtoM info_object for placement |
| default_parent_placement | VARCHAR(51) DEFAULT 'top_level' | matches `ingest_session.parent_placement` values |
| ai_processing_inherit | TINYINT(1) DEFAULT 1 | inherit AI flags from ingest defaults |
| content_type_filter | VARCHAR(500) NULL | comma list of SP content type IDs |
| last_full_sync_at | DATETIME NULL | |
| created_at, updated_at | DATETIME | |
| | UNIQUE (tenant_id, drive_id) | |

### 4.3 `sharepoint_mapping`

Per-drive column mapping. Persistent profiles per drive/content-type. Kept separate from `ingest_mapping` (which is keyed on `session_id` for per-run mappings).

| Column | Type | Notes |
|--------|------|-------|
| id | INT AI PK | |
| drive_id | INT NOT NULL | FK → `sharepoint_drive.id` |
| content_type_id | VARCHAR(255) NULL | NULL = applies to all CTs in drive |
| source_field | VARCHAR(255) NOT NULL | SP column internal name |
| target_field | VARCHAR(255) NOT NULL | AtoM field name |
| target_standard | VARCHAR(47) DEFAULT 'isadg' | |
| transform | VARCHAR(100) NULL | `date_iso, taxonomy_lookup, html_strip`, etc. |
| default_value | VARCHAR(500) NULL | |
| is_required | TINYINT(1) DEFAULT 0 | |
| sort_order | INT DEFAULT 0 | |

### 4.4 `sharepoint_sync_state`

Delta token (per-drive cursor) for Graph delta queries. Used by `sharepoint:sync` and as fallback when webhooks miss events.

| Column | Type | Notes |
|--------|------|-------|
| id | INT AI PK | |
| drive_id | INT NOT NULL | FK → `sharepoint_drive.id` |
| delta_link | TEXT NULL | opaque Graph delta URL |
| last_run_at | DATETIME NULL | |
| last_status | VARCHAR(20) NULL | `ok, error, in_progress` |
| last_error | TEXT NULL | |
| items_processed | INT DEFAULT 0 | |
| | UNIQUE (drive_id) | |

### 4.5 `sharepoint_subscription` (Phase 2)

Graph webhook subscription state. SharePoint driveItem subscriptions expire — must be renewed before expiry (conservative: 24h before).

| Column | Type | Notes |
|--------|------|-------|
| id | INT AI PK | |
| drive_id | INT NOT NULL | FK → `sharepoint_drive.id` |
| subscription_id | VARCHAR(64) NOT NULL UNIQUE | Graph-issued GUID |
| resource | VARCHAR(500) NOT NULL | e.g. `/sites/{id}/drives/{id}/root` |
| change_type | VARCHAR(50) DEFAULT 'updated' | `created, updated, deleted` |
| notification_url | VARCHAR(1000) NOT NULL | |
| client_state | VARCHAR(64) NOT NULL | secret echoed back for validation |
| expires_at | DATETIME NOT NULL | |
| status | VARCHAR(20) DEFAULT 'active' | `active, expired, renewing, error, deleted` |
| created_at, last_renewed_at | DATETIME | |

### 4.6 `sharepoint_event` (Phase 2)

Inbound webhook events. Idempotency table — rejects duplicate `(drive_id, sp_item_id, sp_etag)` within window.

| Column | Type | Notes |
|--------|------|-------|
| id | BIGINT AI PK | |
| subscription_id | INT NOT NULL | FK → `sharepoint_subscription.id` |
| drive_id | INT NOT NULL | FK → `sharepoint_drive.id` |
| sp_item_id | VARCHAR(255) NULL | |
| sp_etag | VARCHAR(255) NULL | |
| change_type | VARCHAR(50) NOT NULL | |
| raw_payload | JSON NOT NULL | as received from Graph |
| status | VARCHAR(20) DEFAULT 'received' | `received, queued, processing, completed, failed, skipped_duplicate` |
| attempts | INT DEFAULT 0 | |
| last_error | TEXT NULL | |
| queue_job_id | INT NULL | FK → `ahg_queue_job.id` |
| ingest_job_id | INT NULL | FK → `ingest_job.id` |
| information_object_id | INT NULL | the AtoM IO created/updated |
| received_at | DATETIME DEFAULT CURRENT_TIMESTAMP | |
| processed_at | DATETIME NULL | |

### 4.7 Migration: `ingest_session.source`

Additive migration in `database/migrations/20260510_add_source_to_ingest_session.sql`:

```sql
ALTER TABLE ingest_session
    ADD COLUMN source VARCHAR(20) DEFAULT 'wizard'
    COMMENT 'wizard, sharepoint, api',
    ADD COLUMN source_id INT DEFAULT NULL
    COMMENT 'Origin record id (e.g., sharepoint_event.id)';
```

Existing rows default to `wizard`. New SP-driven rows set `source='sharepoint'`, `source_id=<sharepoint_event.id>`.

### 4.8 Reuse — no new queue tables

All background jobs use existing `ahg_queue_*` tables via `QueueService`. Dedicated queue name `integrations` keeps SP traffic from drowning out `ingest:commit`.

### 4.9 Reporting view (Phase 2 deliverable)

Add `v_report_sharepoint_events` to `atom-framework/database/views/reporting_views.sql` joining `sharepoint_event + sharepoint_drive + information_object` for BI tools.

### 4.10 ERD registry

Append a row for `ahgSharePointPlugin` to `registry_erd.tables_json` describing the 6 tables, so the live ERD on the registry site picks them up.

---

## 5. Authentication & Secret Handling

**Flow:** Azure AD client-credentials (server-to-server). No user delegation in v1.

**Endpoints:**
- Token: `POST https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token`
- Scope: `https://graph.microsoft.com/.default`

**Secret storage:**
- Plaintext `client_secret` is **never** stored. On admin save, encrypt via `EncryptionService::encrypt($plain, 'sharepoint')` and store ciphertext in `ahg_settings` under group `sharepoint`, key `tenant_{id}_client_secret`.
- `sharepoint_tenant.client_secret_ref` holds the setting key.
- Encryption master key lives in `/etc/atom/encryption.key` outside the repo (existing framework convention).
- Rotation: UI affords "Replace secret"; keep last two `client_secret_ref`s with overlap window (`previous_secret_until` column on tenant) so in-flight token requests don't fail during rotation.

**Token cache (`GraphTokenCache`):**
- In-memory + database. Token + expiry stored in `ahg_settings` group `sharepoint_runtime`, key `access_token_{tenant_id}`. Read from cache when ≥60s lifetime remains.
- Client-credentials flow has no refresh tokens — re-acquire when expired.
- Access token at-rest encryption is not applied (short-lived, 60-min lifetime); justified in technical doc.

**Graph SDK choice — none.** `HttpClientService::request()` is used directly. ~300 LOC for the ~10 endpoints needed (token, sites, drives, listItem, driveItem, content, delta, subscriptions, search, validateSubscription).

---

## 6.0 Two-mode ingest (Phase 2 architecture)

Phase 2 ships **two complementary ingest modes**, both using the same backend pipeline (`SharePointIngestAdapter` → `IngestCommitService`):

| | Mode A — Manual push | Mode B — Auto/declare |
|---|---------------------|------------------------|
| Trigger | User clicks "Send to Archive" on a SP doc / folder | Retention label change fires Graph webhook |
| Surface | SPFx command set in the SP doc library command bar | Webhook receiver at `/sharepoint/webhook` |
| Selection | One or more user-selected items | Items with `_ComplianceTag` in the configured allowlist |
| Targeting | User picks repo + parent IO + edits metadata in a dialog | Drive default repo / parent / sector |
| Auth boundary | User's AAD bearer token (AAD JWT validated by AtoM) | App-only client-credentials |
| Audit actor | Mapped AtoM user (via `sharepoint_user_mapping`) | "SharePoint Auto-Ingest" service identity |
| Failure surface | SPFx dialog shows error inline | `sharepoint_event` log + retry queue |

**Both modes share:**
- Mapping rules (`sharepoint_mapping` per drive)
- Retention mapper (`SharePointRetentionMapper` reads `_ComplianceTag` regardless of trigger)
- Backend pipeline (`IngestCommitService` via synthetic `ingest_session`)
- File fetch path (Graph) with user-perm validation (see §6.5.4)

**Phasing within Phase 2:**
- **Phase 2.A** ships Mode B (auto/declare). Reuses the work already scaffolded.
- **Phase 2.B** ships Mode A (manual push). SPFx command set + push endpoint + AAD SSO bridge.
- Both can ship together at end of Phase 2; ordering is implementation convenience.

**Schema additions for two-mode (additive, both targets):**

1. `sharepoint_drive.auto_ingest_labels TEXT NULL COMMENT 'JSON array of compliance tag names that trigger auto-ingest in mode B'` — empty/null = no auto ingest (drive is manual-push only).
2. New table `sharepoint_user_mapping`:
   ```
   id INT AI PK
   aad_object_id VARCHAR(64) NOT NULL UNIQUE  -- AAD oid claim
   aad_upn VARCHAR(255) NULL                  -- audit-only readable id
   atom_user_id INT NOT NULL                  -- FK to user.id (AtoM user)
   created_at, last_seen_at DATETIME
   created_by VARCHAR(20) DEFAULT 'auto'      -- auto, manual
   ```
3. Extend `sharepoint_event.source` (the column we add to `ingest_session`) values: `wizard, sharepoint_auto, sharepoint_push, api`.

---

## 6. Mode B — Auto/Declare Ingest (Phase 2.A)

### 6.1 Subscription lifecycle

| Step | Implementation |
|------|----------------|
| **Create** | `sharepoint:subscribe --drive=<id>` calls Graph `POST /subscriptions` with `resource=/sites/{site}/drives/{drive}/root`, `changeType=updated`, `notificationUrl=https://psis.theahg.co.za/sharepoint/webhook`, `clientState=<random>`, `expirationDateTime=now+2d23h`. Persist response in `sharepoint_subscription`. |
| **Validate** | Graph immediately GETs the notificationUrl with `?validationToken=…`. Receiver MUST echo the token as `text/plain` 200 within 10s. Implemented in `webhook` action. |
| **Renew** | Cron `sharepoint:renew-subscriptions` (hourly) finds subs where `expires_at < NOW() + INTERVAL 12 HOUR AND status='active'`, calls Graph `PATCH /subscriptions/{id}`. Cron entry added to `ahgSettingsPlugin` cron jobs page under "SharePoint Integration". |
| **Delete** | Plugin disable / drive disable / `sharepoint:install --uninstall` calls Graph `DELETE /subscriptions/{id}`. |

### 6.2 Webhook receiver

Route `POST /sharepoint/webhook` (also handles validation GET). **Public, must bypass CSRF** — extends a base action class that skips form-token CSRF (mirror `ahgAPIPlugin` webhook receiver pattern).

```
1. If query param `validationToken` present → echo as text/plain 200. Done.
2. Read JSON body, iterate value[]:
   a. Match clientState against sharepoint_subscription.client_state.
      Mismatch → drop request 401. (Auth boundary.)
   b. INSERT into sharepoint_event (status='received').
   c. QueueService::dispatch('sharepoint:ingest-event', ['event_id' => $eventId], 'integrations').
3. Return 202.
```

Rate limit: per-IP token bucket via `ahg_queue_rate_limit`. Microsoft IPs are well-known; optionally allowlist.

### 6.3 Event → ingest pipeline

Queue handler `sharepoint:ingest-event` registered via `QueueJobRegistry::register()`:

1. Load event row, set status `processing`.
2. **Idempotency check** — `SELECT 1 FROM sharepoint_event WHERE drive_id=? AND sp_item_id=? AND sp_etag=? AND status='completed' AND id<>?`. If exists, set `skipped_duplicate`, return.
3. Resolve `sharepoint_drive` config, fetch the changed item via Graph `GET /sites/{site}/drives/{drive}/items/{item}` (full metadata + content stream URL).
4. **Retention-label branch** — read `listItem.fields.{_ComplianceTag, _ComplianceTagWrittenTime}`. `SharePointRetentionMapper` looks up the AtoM disposition (configured in settings: SP label → level_of_description, parent IO, security clearance, embargo).
5. Project SP item JSON through `SharePointMappingService` into the same shape `ingest_row.data` uses.
6. Create synthetic `ingest_session` (status=`commit`, source=`sharepoint`, source_id=event.id, AI flags inherited from drive config or ingest defaults), one `ingest_row`, one `ingest_file` pointing to downloaded blob (cached under `uploads/sharepoint/{event_id}/`).
7. Call `IngestCommitService::startJob($sessionId)` which dispatches `ingest:commit`. Existing pipeline handles validation → info_object insert → digital_object insert → AI processing → SIP/AIP/DIP if enabled.
8. On success: `sharepoint_event.status='completed'`, link `information_object_id`, audit-log via `AuditService::log('sharepoint.ingest', ...)`.
9. On failure: `failed`, increment `attempts`, schedule retry via `QueueService` exponential backoff. Cap `MAX_RETRIES=5`.

### 6.4 Purview spike outcome (research-mode, 2026-05-10)

Run as a docs-driven spike rather than a live tenant test (no Azure tenant available to this scaffold). Findings from Microsoft Graph change-notifications reference + Purview retention-label documentation:

**Confirmed:**
- driveItem subscriptions support **only `updated` changeType** on `/drives/{id}/root` and `/users/{id}/drive/root`.
- list subscriptions also exist under SharePoint sites: `/sites/{site-id}/lists/{list-id}` — also `updated` only.
- driveItem `updated` notifications fire for **content-level** changes (file added/modified/deleted within the folder hierarchy).
- `_ComplianceTag` (the retention label name) is exposed via listItem.fields and via dedicated retentionLabel methods on driveItem.
- Graph exposes basic metadata (`complianceTag`, `isRecord`) but **NOT** `retentionEventType`, `retentionTriggerDate`, `expirationDateTime` — even in beta.

**Limitations:**
- Microsoft does NOT explicitly document whether listItem-only metadata changes (e.g., setting `_ComplianceTag` via Purview without changing file content) reliably trigger driveItem `updated` events. Field reports are mixed.
- Purview retention-driven **disposition events** (e.g., "label triggered disposition review") are NOT in Graph webhooks at all. They surface via the **Office 365 Management Activity API** — separate auth scope, separate SDK pattern.

**Architectural decision (locks the Phase 2 implementation):**

1. **Subscribe to BOTH resources per ingest-enabled drive:**
   - `/sites/{site-id}/drives/{drive-id}/root` (changeType=updated) → catches content-level changes
   - `/sites/{site-id}/lists/{list-id}` (changeType=updated) → catches metadata-only changes (label set/changed)

   Each ingest-enabled drive therefore creates 2 rows in `sharepoint_subscription`. No per-tenant quota concern (driveItem and list have no documented organizational quota cap).

2. **Read retention label state from listItem.fields:** `_ComplianceTag` (label name), `_ComplianceTagWrittenTime`, `_IsRecord`. Pull listItem alongside driveItem on every ingest-event handler invocation.

3. **`SharePointRetentionMapper`** does straightforward lookup: tag-name → AtoM disposition (level_of_description, parent_id, security_classification_id, embargo flag). Map is configurable per tenant in `ahg_settings` group `sharepoint`, key `retention_label_map`.

4. **Defer Purview disposition events to Phase 2.5.** Office 365 Management Activity API integration is a separate effort:
   - Different scope: `https://manage.office.com/.default`
   - Different endpoint pattern: subscriptions on content types like `Audit.SharePoint`
   - Separate event log table or shared `sharepoint_event` with a `source` column
   - Will cover scenarios like "retention period expired → disposition reviewer notified" that v1 won't catch.

5. **Document the gap honestly in user-facing docs:** "Phase 2 v1 catches all SharePoint content changes and label-set events that propagate as driveItem updates. Pure-metadata Purview disposition triggers may take up to one hour (the cron-driven `sharepoint:sync` delta poll fallback). Full Purview disposition event coverage is Phase 2.5."

**This decision UPDATES the locked scope:** the Phase 2 plan in §17 includes dual-resource subscriptions and the listItem.fields read path. The Activity API extension is now formally Phase 2.5, not "if needed".

**Sources:**
- [Graph change-notifications overview](https://learn.microsoft.com/en-us/graph/api/resources/change-notifications-api-overview?view=graph-rest-1.0)
- [Set up notifications for changes in resource data](https://learn.microsoft.com/en-us/graph/change-notifications-overview)
- [Webhook delivery](https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks)
- [CSOM methods for retention labels](https://learn.microsoft.com/en-us/sharepoint/dev/apis/csom-methods-for-applying-retention-labels)
- [Auto-apply retention labels in SharePoint](https://learn.microsoft.com/en-us/purview/auto-apply-retention-labels-scenario)
- [Reduce missing change notifications](https://learn.microsoft.com/en-us/graph/change-notifications-lifecycle-events)

---

## 6.5 Mode A — Manual Push via SPFx (Phase 2.B)

### 6.5.1 SPFx command set

Lives outside the AtoM/Heratio packages, in `atom-extensions-catalog/spfx/atom-archive-push/`. Standard SPFx scaffold:

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 726 260" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="725" height="259" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="17.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="82.0" x2="20.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="82.0" x2="24.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="82.0" x2="28.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="82.0" x2="31.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="90.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="98.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="17.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="114.0" x2="20.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="114.0" x2="24.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="114.0" x2="28.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="114.0" x2="31.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="122.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="42.4" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="130.0" x2="56.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="130.0" x2="60.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="46.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="138.0" x2="42.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="42.4" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="146.0" x2="49.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="146.0" x2="53.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="146.0" x2="56.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="146.0" x2="60.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="154.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="42.4" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="162.0" x2="74.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="154.0" x2="71.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="162.0" x2="71.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="162.0" x2="78.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="162.0" x2="82.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="162.0" x2="85.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="162.0" x2="89.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="170.0" x2="42.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="42.4" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="74.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="170.0" x2="71.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="71.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="178.0" x2="78.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="178.0" x2="82.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="178.0" x2="85.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="178.0" x2="89.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="186.0" x2="42.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="42.4" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="194.0" x2="74.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="186.0" x2="71.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="194.0" x2="71.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="194.0" x2="78.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="194.0" x2="82.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="194.0" x2="85.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="194.0" x2="89.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="202.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="42.4" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="74.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="202.0" x2="71.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="210.0" x2="78.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="210.0" x2="82.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="210.0" x2="85.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="210.0" x2="89.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="46.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="218.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="226.0" x2="49.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="226.0" x2="53.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="226.0" x2="56.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="226.0" x2="60.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="242.0" x2="74.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="234.0" x2="71.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="242.0" x2="78.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="242.0" x2="82.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="242.0" x2="85.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="242.0" x2="89.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">atom-extensions-catalog/spfx/atom-archive-push/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">package.json</text><text x="38.8" y="54.0" font-size="9.5" fill="#10373E">tsconfig.json</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">gulpfile.js</text><text x="38.8" y="86.0" font-size="9.5" fill="#10373E">config/</text><text x="67.6" y="102.0" font-size="9.5" fill="#10373E">package-solution.json</text><text x="38.8" y="118.0" font-size="9.5" fill="#10373E">src/extensions/atomArchivePush/</text><text x="67.6" y="134.0" font-size="9.5" fill="#10373E">AtomArchivePushCommandSet.ts</text><text x="326.8" y="134.0" font-size="9.5" fill="#10373E">#</text><text x="341.2" y="134.0" font-size="9.5" fill="#10373E">SPFx</text><text x="377.2" y="134.0" font-size="9.5" fill="#10373E">command-set</text><text x="463.6" y="134.0" font-size="9.5" fill="#10373E">entry</text><text x="67.6" y="150.0" font-size="9.5" fill="#10373E">components/</text><text x="96.4" y="166.0" font-size="9.5" fill="#10373E">PushDialog.tsx</text><text x="326.8" y="166.0" font-size="9.5" fill="#10373E">#</text><text x="341.2" y="166.0" font-size="9.5" fill="#10373E">Fluent</text><text x="391.6" y="166.0" font-size="9.5" fill="#10373E">UI</text><text x="413.2" y="166.0" font-size="9.5" fill="#10373E">dialog</text><text x="96.4" y="182.0" font-size="9.5" fill="#10373E">RepositoryPicker.tsx</text><text x="326.8" y="182.0" font-size="9.5" fill="#10373E">#</text><text x="341.2" y="182.0" font-size="9.5" fill="#10373E">autocomplete</text><text x="434.8" y="182.0" font-size="9.5" fill="#10373E">from</text><text x="470.8" y="182.0" font-size="9.5" fill="#10373E">AtoM</text><text x="506.8" y="182.0" font-size="9.5" fill="#10373E">/api/v2/repositories</text><text x="96.4" y="198.0" font-size="9.5" fill="#10373E">ParentPicker.tsx</text><text x="326.8" y="198.0" font-size="9.5" fill="#10373E">#</text><text x="341.2" y="198.0" font-size="9.5" fill="#10373E">autocomplete</text><text x="434.8" y="198.0" font-size="9.5" fill="#10373E">from</text><text x="470.8" y="198.0" font-size="9.5" fill="#10373E">AtoM</text><text x="506.8" y="198.0" font-size="9.5" fill="#10373E">/api/v2/informationobjects?q=</text><text x="96.4" y="214.0" font-size="9.5" fill="#10373E">MetadataForm.tsx</text><text x="326.8" y="214.0" font-size="9.5" fill="#10373E">#</text><text x="341.2" y="214.0" font-size="9.5" fill="#10373E">editable</text><text x="406.0" y="214.0" font-size="9.5" fill="#10373E">ISAD(G)</text><text x="463.6" y="214.0" font-size="9.5" fill="#10373E">form,</text><text x="506.8" y="214.0" font-size="9.5" fill="#10373E">prefilled</text><text x="67.6" y="230.0" font-size="9.5" fill="#10373E">services/</text><text x="96.4" y="246.0" font-size="9.5" fill="#10373E">AtomClient.ts</text><text x="326.8" y="246.0" font-size="9.5" fill="#10373E">#</text><text x="341.2" y="246.0" font-size="9.5" fill="#10373E">AAD-authed</text><text x="420.4" y="246.0" font-size="9.5" fill="#10373E">HTTP</text><text x="456.4" y="246.0" font-size="9.5" fill="#10373E">client</text></svg></div>

Build: `npm install && gulp bundle --ship && gulp package-solution --ship` produces `atom-archive-push.sppkg`. SP admin uploads it once to the tenant App Catalog. The command appears as a button in every SP document library.

### 6.5.2 Push flow

1. User selects one or more files in a SP doc library.
2. Clicks "Send to Archive" → `AtomArchivePushCommandSet.onExecute` opens the React dialog.
3. SPFx obtains an AAD bearer token via `aadHttpClientFactory.getClient(<our AtoM app id URI>)`. This token is for the user's identity, scoped to AtoM's API.
4. Dialog calls `GET /api/v2/sharepoint/push/projection` with the SP item refs to retrieve a prefilled metadata form (the same projection the auto mode does).
5. User picks repository (autocomplete) → parent IO (autocomplete) → reviews/edits metadata fields → submits.
6. Dialog `POST /api/v2/sharepoint/push` with bearer token + payload (item refs, repo, parent, edited metadata).
7. AtoM validates token, resolves user, ingests, returns 201 + ingest job id.
8. Dialog polls job status; shows success toast or error detail.

### 6.5.3 AtoM-side push endpoint

| Route | Method | Auth | Purpose |
|-------|--------|------|---------|
| `/api/v2/sharepoint/push/projection` | POST | AAD JWT | Given SP item refs, return prefilled metadata payload (uses `SharePointMappingService::project`). |
| `/api/v2/sharepoint/push` | POST | AAD JWT | Submit a push: SP refs + edited metadata + target repo/parent. Creates synthetic `ingest_session` (source=`sharepoint_push`), returns ingest job id. |
| `/api/v2/sharepoint/push/jobs/{id}` | GET | AAD JWT | Poll ingest job status for the dialog. |

All three routes mounted under `ahgAPIPlugin` apiv2 module (AtoM target) and `ahg-api` package (Heratio target). Validated via the same `GraphTokenValidatorService` used in Phase 3 connector feed. JWT validation moves from Phase 3 to Phase 2.B as a result.

### 6.5.4 File fetch — user permission preservation

Issue: app-only Graph token would let any SP user push any file in the tenant. Fix:

**Use OBO (On-Behalf-Of) flow** for manual-push file reads:

1. AtoM receives the user's AAD bearer token (audience = AtoM API).
2. AtoM calls AAD token endpoint with `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`, `requested_token_use=on_behalf_of`, `assertion=<user_token>`, `scope=https://graph.microsoft.com/Files.Read`.
3. AAD returns a Graph token impersonating the user (subject to their consent + the AAD app's delegated permissions).
4. AtoM fetches the file via Graph using the OBO token. If the user lacks SP read access, Graph returns 403 — AtoM rejects the push.
5. The OBO token is short-lived; re-acquired per push.

**AAD app registration changes for OBO:**
- Add **delegated** API permission: `Microsoft Graph / Files.Read.All` (or scoped down)
- Configure the AtoM API as an "Expose an API" with a scope (e.g., `api://<our-app-id>/SharePointPush.Submit`)
- The SPFx code requests THAT scope when getting the bearer token
- The user (or admin on their behalf) consents to both the AtoM scope and the Graph delegated permission

**Fallback (simpler, weaker):**
- Skip OBO. Have SPFx fetch the file blob client-side using its own Graph token (in the user's session) and POST it directly in the request body. AtoM never calls Graph for manual push.
- Drawback: large files (>50 MB) become problematic for browser POSTs; SPFx aadHttpClientFactory has practical body-size limits.

**Recommendation:** OBO for v1. Document the AAD app registration setup carefully. Keep client-side blob fallback as a Phase 2.B.1 follow-on if file-size friction shows up.

### 6.5.5 User mapping

`sharepoint_user_mapping` table (defined in §6.0) maps AAD `oid` → AtoM `user.id`. Three lookup behaviors, configurable per tenant in `ahg_settings`:

1. **Strict** — only pre-existing mappings work. New AAD users get 403. Admins must pre-provision via the user mapping admin UI.
2. **Auto-create** (default) — first push from an unmapped AAD user creates an AtoM user (username = UPN, email = email claim, role = configurable default e.g. `editor`), inserts the mapping, proceeds with the push.
3. **Match by email** — if an AtoM user already exists with the AAD email, link to it; else fall back to strict or auto-create.

Auto-create is gated by setting `sharepoint_push_user_create_enabled` (default `false` in production, `true` for dev). Admin UI at `/sharepoint/user-mappings` lists, edits, removes mappings.

### 6.5.6 Audit trail

Every push records via `AuditService::log`:
- action: `sharepoint.push`
- entity: `informationobject`
- entity_id: the created IO id
- actor: the resolved AtoM user (NOT the service identity)
- metadata: `{aad_oid, aad_upn, sp_drive_id, sp_item_id, sp_etag, push_dialog_session_id}`

Audit row is the source of truth for "who pushed what from SP, when".

### 6.5.7 Dependencies summary (added in Phase 2.B)

- AAD app registration: delegated `Files.Read.All` permission, "Expose an API" scope for AtoM, redirect/reply URLs for SPFx
- composer dep `firebase/php-jwt` (already locked) — moves from Phase 3 to Phase 2.B
- New schema: `sharepoint_user_mapping` table
- New routes under apiv2 / ahg-api: `push`, `push/projection`, `push/jobs/{id}`
- New SPFx project: `atom-extensions-catalog/spfx/atom-archive-push/`
- Settings additions: `sharepoint_push_*` flags

---

## 7. Use Case B — Staff Discovery in M365 (Phase 3)

### 7.1 Approach: Microsoft Search vertical (Graph connector)

Recommended over SPFx web part / Teams tab for v1. Server-to-server: AtoM exposes a connector OData feed; M365 indexes AtoM content periodically; users see archive results in their normal M365 search experience. No client build pipeline, no separate repo.

### 7.2 AtoM-side connector endpoints (extend `ahgAPIPlugin`)

| Route | Purpose |
|-------|---------|
| `GET /api/v2/sharepoint/connector/items?$skiptoken=…` | Paged item feed for indexing. Returns IO id, slug, title, scope_and_content, repository, sector, level, public URL, lastModifiedDateTime. |
| `GET /api/v2/sharepoint/connector/items/{id}` | Single item, used for refresh. |
| `GET /api/v2/sharepoint/connector/schema` | Schema descriptor per Graph connector spec. |

### 7.3 Auth from M365 → AtoM

- AAD app registration (same as outbound) gets a delegated-or-app-only client-credentials token.
- AtoM validates inbound JWT against AAD JWKS (`https://login.microsoftonline.com/{tenant}/discovery/v2.0/keys`), confirms `iss`, `aud`, `tid`, signature.
- Implementation: `GraphTokenValidatorService` using `firebase/php-jwt` library.
- Connector routes gated on this validator middleware.

### 7.4 SPFx / Teams as Phase 3.5 follow-on

If an institution wants a richer in-context UI (preview pane in Teams), a separate SPFx project lives in `atom-extensions-catalog/spfx/atom-archive-search/` (NOT in this plugin). Out-of-scope for v1.

---

## 8. Use Case C — Federated Search (Phase 3)

### 8.1 Backend

`GET /sharepoint/federated-search?q=…` AJAX endpoint. `SharePointFederatedSearchService::search($q, $tenantId)` wraps Graph `POST /search/query` with `entityTypes: [driveItem, listItem]`, scoped to configured sites. Normalize response into `[{title, url, snippet, lastModified, site, drive, mimeType}, ...]` and render a card list.

### 8.2 UI integration

Mount via `ahgDisplayPlugin` search-results page. Use `extension.json` `display_panels` declaration (existing pattern, see `ahgCustomFieldsPlugin`). Pane appears as a "From SharePoint" tab next to AtoM results.

### 8.3 Caching

- Cache key = `sha256(q + tenant_id + scope)`, TTL 5min, stored in `ahg_cache` via existing `CacheService`.
- Frontend debounces 300ms (matches AtoM autocomplete debounce in `ahgSemanticSearchPlugin`).
- Lazy load: only fire SP query when user clicks the "From SharePoint" tab, not on every keystroke.

### 8.4 Permission trimming — gated by AtoM role

App-only Graph token returns un-trimmed results. Mitigation: federated search tab only visible to AtoM users with `editor` or `administrator` role. Anonymous and researcher users do not see the tab at all. The technical manual documents this tradeoff explicitly.

OBO/SSO flow is a Phase 3.5 follow-on for institutions that want per-user trimming — requires AtoM auth delegated to AAD via OIDC.

---

## 9. CLI Tasks

| Task | Purpose | Cron? |
|------|---------|-------|
| `sharepoint:install` | Create tables (idempotent), seed `ahg_dropdown` codes, validate config | No (manual) |
| `sharepoint:test-connection --tenant=<id>` | Acquire token, list sites, fail-fast diagnostics | No |
| `sharepoint:subscribe --drive=<id>` | Create Graph subscription (Phase 2) | No |
| `sharepoint:renew-subscriptions` | Renew any sub expiring in next 12h | **Yes — hourly** (Phase 2) |
| `sharepoint:sync --drive=<id> [--full]` | Delta poll fallback / initial backfill | **Yes — hourly per drive** |
| `sharepoint:ingest-event --event-id=<id>` | Queue handler invocation; not normally manual | No |
| `sharepoint:status` | Print active tenants, drives, subscription expiries, last sync, queue depth | No |

All registered via `lib/task/*.class.php`. Each task is also a queue handler target via `QueueCliTaskHandler`.

---

## 10. Settings Section

Modifications to `ahgSettingsPlugin` (locked, but section-add is precedented):

- `sectionAction.class.php` `$sections` array — add `'sharepoint' => ['label' => 'SharePoint Integration', 'icon' => 'fa-cloud', 'description' => 'Microsoft 365 SharePoint integration: tenant config, drives, webhooks, federated search']`.
- `$checkboxFields['sharepoint']` — `sharepoint_enabled, sharepoint_federated_search_enabled, sharepoint_records_handoff_enabled, sharepoint_m365_search_enabled, sharepoint_inherit_ai_defaults`.
- `$sectionPluginMap['sharepoint'] = 'ahgSharePointPlugin'`.
- Add `case 'sharepoint':` block in **BOTH** `section.blade.php` AND `sectionSuccess.php` (dual template requirement).

Fields exposed:
- tenant_id, client_id, client_secret (write-only password field — empties on display, only updates on submit if non-empty, encrypted on write)
- default site/drive dropdown (populated from `sharepoint_drive`)
- federated-search toggle, records-handoff toggle, M365-search toggle
- webhook public URL (display-only, derived from server config)
- retention-label → AtoM disposition mapping (table editor)
- AI processing inheritance toggle

---

## 11. Admin UIs (`modules/sharepoint/`)

| Route | Action | Purpose | Phase |
|-------|--------|---------|-------|
| `/sharepoint` | `index` | Dashboard: tenants, drives, subscriptions, recent events | 1 |
| `/sharepoint/tenants` | `tenants` | List/edit tenants | 1 |
| `/sharepoint/tenants/:id` | `tenantEdit` | Tenant detail (test connection button) | 1 |
| `/sharepoint/drives` | `drives` | Browse SP sites/drives via Graph, register for ingest | 1 |
| `/sharepoint/drives/:id/mapping` | `mapping` | Column → AtoM field editor | 1 |
| `/sharepoint/subscriptions` | `subscriptions` | Active subs, expiry countdown, manual renew/delete | 2 |
| `/sharepoint/events` | `events` | Event log (paged, filter by status) | 2 |
| `/sharepoint/events/:id` | `eventDetail` | Raw payload, retry button | 2 |
| `/sharepoint/webhook` | `webhook` | **Public, no auth, no CSRF** — Graph notification endpoint | 2 |
| `/sharepoint/federated-search` | `federatedSearch` | AJAX, JSON response | 3 |
| `/api/v2/sharepoint/connector/*` | (in apiv2 module) | M365 connector feed | 3 |

Templates: every action gets BOTH `xxxSuccess.php` (Symfony) and `xxx.blade.php` (Heratio). Per project rule, dispatcher auto-detection handles the routing; Blade is source of truth going forward.

---

## 12. Queue Handler Registration

In `ahgSharePointPluginConfiguration::initialize()`:

```php
if (class_exists('\AtomFramework\Services\QueueJobRegistry')) {
    \AtomFramework\Services\QueueJobRegistry::register('sharepoint:ingest-event',         \AtomFramework\Services\QueueCliTaskHandler::class);
    \AtomFramework\Services\QueueJobRegistry::register('sharepoint:sync',                 \AtomFramework\Services\QueueCliTaskHandler::class);
    \AtomFramework\Services\QueueJobRegistry::register('sharepoint:renew-subscriptions',  \AtomFramework\Services\QueueCliTaskHandler::class);
}
```

Dispatch shape (matches existing `ingest:commit` usage):

```php
\AtomFramework\Services\QueueService::dispatch(
    'sharepoint:ingest-event',
    ['event_id' => $eventId],
    'integrations',
    priority: 5
);
```

---

## 13. Composer Dependencies

Added to `atom-framework/composer.json` (NOT root `composer.json`):

```json
{
    "require": {
        "firebase/php-jwt": "^6.10"
    }
}
```

Run `composer update firebase/php-jwt --no-dev -d /usr/share/nginx/archive/atom-framework`.

No other new dependencies. Microsoft Graph SDK explicitly NOT taken — hand-rolled HTTP via `HttpClientService`.

---

## 14. Security

- **Webhook clientState** — Graph does not sign webhook payloads. The `clientState` echoed in every notification IS the auth — keep 64+ char random, store in `sharepoint_subscription.client_state`, reject mismatches with HTTP 401. Rotate on tenant secret rotation.
- **Rate limit receiver** — per-IP token bucket via `ahg_queue_rate_limit`. Log unexpected source IPs.
- **TLS** — `HttpClientService` enforces SSL verification and blocks private IPs.
- **Client-secret rotation** — UI affords "Replace secret" with overlap window.
- **Audit trail** — `AuditService::log('sharepoint.ingest', 'informationobject', $ioId, ['source'=>'sharepoint', 'sp_item_id'=>…, 'sp_drive'=>…, 'event_id'=>…])` on every successful ingest.
- **PII handling** — SP documents may contain PII. Run `ahgPrivacyPlugin` PII scan as part of the ingest pipeline (`ingest_session.process_ner=1` extracts personal names into authority records with appropriate flags).
- **Webhook URL** — `psis.theahg.co.za/sharepoint/webhook` over HTTPS only. Path-based nginx rate limit.
- **Secret in URLs** — never. All secrets in headers/body.

---

## 15. Testing

### Unit tests (PHPUnit, framework test harness)

`atom-framework/test/SharePoint/`:
- `SharePointMappingServiceTest` — transforms (date_iso, taxonomy_lookup, html_strip)
- `SharePointRetentionMapperTest` — label → disposition resolution
- `GraphClientServiceTest` — HTTP mocking via hand-rolled `HttpClientServiceMock`
- `SharePointIngestAdapterTest` — projection logic

### Webhook end-to-end

Fixture posts simulated Graph payloads to `/sharepoint/webhook`, asserts queue job enqueued, runs `php symfony queue:work --once`, asserts `information_object` row materializes. Mock outbound Graph fetch.

### Playwright tests at `testing/playwright/sharepoint/`

| Spec | Phase |
|------|-------|
| `tenant-config.spec.ts` | 1 |
| `drive-registration.spec.ts` | 1 |
| `mapping-editor.spec.ts` | 1 |
| `event-log.spec.ts` | 2 |
| `federated-search.spec.ts` | 3 |

### Live integration (gated)

Subscription lifecycle test (gated behind `SHAREPOINT_LIVE_TESTS=1`) creates / renews / deletes a real subscription against a test tenant. Skip in CI unless creds present.

---

## 16. Documentation Deliverables

Per project rule (CLAUDE.md): all User and Technical Manuals in BOTH `.md` AND `.docx`.

**Phase 1:**
- `atom-extensions-catalog/docs/AtoM_Heratio_SharePointPlugin_Feature_Overview.md` + `.docx`
- This implementation plan: `atom-extensions-catalog/docs/technical/ahgSharePointPlugin_Implementation_Plan.md`

**Phase 2:**
- `atom-extensions-catalog/docs/sharepoint-user-guide.md` (admin walkthrough, screenshots)
- `atom-extensions-catalog/docs/technical/ahgSharePointPlugin.md` (architecture, schema, API reference)

**Phase 3:**
- `atom-extensions-catalog/docs/sharepoint-flow-guide.docx` (records handoff + federated search flows)

Update `DATABASE_ERD.md` with section for SP tables. Update `registry_erd.tables_json` row.

pandoc command (per project rule):

```bash
pandoc input.md -o output.docx --from=markdown --to=docx \
    --metadata title="..." \
    --metadata author="The Archive and Heritage Group (Pty) Ltd"
```

---

## 17. Phasing

Each phase is independently shippable.

### Phase 1 — Foundation (~2 weeks)

- Schema (all 6 tables) + `ingest_session.source` migration
- Repositories
- `GraphClientService`, `GraphTokenCache`
- Encrypted secret storage via `EncryptionService`
- `sharepoint:install`, `sharepoint:test-connection`, `sharepoint:sync` CLI tasks
- Tenant config admin UI
- Drive registration UI (browse SP sites via Graph)
- Mapping editor (per drive)
- Settings section in `ahgSettingsPlugin`
- Audit-trail integration
- Phase 1 docs (Feature Overview, this plan)
- Playwright: tenant-config, drive-registration, mapping-editor

**Shippable** as "manual SharePoint ingest." Institutions get value without webhook infra.

### Phase 2 — Two-mode ingest (~3 weeks, split into 2.A and 2.B)

#### Phase 2.A — Mode B: Auto/Declare (~1.5 weeks)

- Purview verification spike (DONE 2026-05-10, see §6.4)
- `sharepoint_subscription` + `sharepoint_event` tables (DONE in Phase 1 install.sql)
- `sharepoint_drive.auto_ingest_labels` schema addition (additive migration)
- `sharepoint:subscribe`, `sharepoint:renew-subscriptions` (cron), `sharepoint:ingest-event` (queue handler) tasks
- Webhook receiver action (public, no CSRF) with clientState validation
- Dual-resource subscriptions (driveItem + list per drive)
- `SharePointWebhookHandler`, `SharePointMappingService`, `SharePointRetentionMapper`, `SharePointSubscriptionService` services
- Label-allowlist filter (only ingest items whose `_ComplianceTag` is in the configured list)
- Idempotency, retry/backoff
- Subscription dashboard + event log UI
- Cron entries for renewal added to `ahgSettingsPlugin`
- Reporting view `v_report_sharepoint_events`
- Playwright: event-log
- **Shippable** as "real-time records handoff via Graph webhooks."

#### Phase 2.B — Mode A: Manual Push (~1.5 weeks)

- New schema: `sharepoint_user_mapping` table
- AAD app registration changes documented (delegated Files.Read.All, "Expose an API" scope)
- `firebase/php-jwt` composer dep added to `atom-framework` (and `ahg/sharepoint` for Heratio)
- `GraphTokenValidatorService` — validates inbound AAD JWTs against AAD JWKS (also serves Phase 3)
- OBO flow client method on `GraphClientService` (`acquireOboToken`)
- AtoM-side push endpoints in apiv2 module (and `ahg-api` package for Heratio):
  - `POST /api/v2/sharepoint/push/projection`
  - `POST /api/v2/sharepoint/push`
  - `GET /api/v2/sharepoint/push/jobs/{id}`
- User mapping admin UI at `/sharepoint/user-mappings`
- New SPFx project `atom-extensions-catalog/spfx/atom-archive-push/`:
  - SPFx command set (TypeScript, Fluent UI React)
  - PushDialog with repository/parent pickers + editable metadata form
  - AAD-authed AtoM API client
  - Build via `gulp bundle --ship && gulp package-solution --ship` → `.sppkg`
- Documentation: SP admin SPFx install guide, AAD app registration guide
- Playwright: push-dialog spec (mocked SPFx context)
- **Shippable** as "manual push with per-user accountability."

**Phase 2 retro:** confirm both modes share backend; verify no duplicate audit rows when a manual push and auto-ingest race on the same item (idempotency check in `SharePointEventRepository::isDuplicate` covers this).

### Phase 3 — Discovery Surfaces (~2 weeks)

- AtoM-side federated search (`SharePointFederatedSearchService`, /sharepoint/federated-search)
- "From SharePoint" tab in search UI (gated to staff roles)
- M365-side connector feed (`/api/v2/sharepoint/connector/*`)
- `firebase/php-jwt` dependency added
- `GraphTokenValidatorService` (inbound AAD JWT validation against JWKS)
- Caching layer for federated search
- Permission-trimming policy implemented + documented
- Phase 3 docs update
- Playwright: federated-search

**Shippable** as "M365 + federated discovery."

### Phase 3.5 (optional follow-on)

- SPFx web part / Teams tab in separate `atom-extensions-catalog/spfx/atom-archive-search/` repo
- OBO/SSO flow for per-user permission trimming on federated search (requires AtoM AAD OIDC delegation)

---

## 18. Risks & Open Questions Resolved

All seven open questions from the planning round were resolved on 2026-05-10 (see §2). Remaining risk surface:

1. **Purview disposition coverage** — gating Phase 2 on the verification spike. Worst case: add Activity API integration as Phase 2.5.
2. **Multi-tenant install** — `ahgMultiTenantPlugin` is currently disabled. `sharepoint_tenant` rows are scoped per AtoM repository to be future-safe.
3. **Graph subscription expiry windows** — current docs say up to 30 days for SharePoint driveItem; we renew at 24h-before-expiry to be conservative if Microsoft reduces it again.
4. **Permission trimming on federated search** — staff-only gate is honest mitigation. OBO is Phase 3.5.

---

## 19. Portability — Dual-Target Implementation

**Hard requirement: 100% feature parity between AtoM Heratio (Symfony 1.x) and Heratio standalone (Laravel 12).** Established codebase pattern (every plugin in `atom-ahg-plugins/` has a matching package in `heratio/packages/`, e.g., `ahgIngestPlugin` ↔ `ahg-ingest`, `ahgAPIPlugin` ↔ `ahg-api`). The schemas of `ahg-ingest` were ported from `ahgIngestPlugin` on 2026-04-30 with transforms documented inline — same approach applies here.

### 19.1 Two implementations, mirrored schema

| | AtoM target | Heratio target |
|---|-------------|----------------|
| Path | `/usr/share/nginx/archive/atom-ahg-plugins/ahgSharePointPlugin/` | `/usr/share/nginx/heratio/packages/ahg-sharepoint/` |
| Framework | Symfony 1.x plugin + Capsule (Illuminate\Database) | Laravel 12 package, Eloquent, service provider |
| Manifest | `extension.json` | `composer.json` (with `extra.laravel.providers`) |
| Namespace | `AtomExtensions\SharePoint\…` | `AhgSharePoint\…` |
| Entry point | `ahgSharePointPluginConfiguration::initialize()` | `AhgSharePoint\Providers\AhgSharePointServiceProvider::register/boot` |
| Routes | `RouteLoader` in plugin config | `routes/web.php` + `routes/api.php` per Laravel convention |
| Controllers | `modules/sharepoint/actions/…Action.class.php` (sfActions) | `src/Controllers/…Controller.php` (Laravel) |
| Templates | `modules/sharepoint/templates/…Success.php` + `.blade.php` | `resources/views/…blade.php` (Blade only — Heratio is Blade-native) |
| CLI | `lib/task/sharepoint…Task.class.php` (`php symfony sharepoint:*`) | `src/Console/Commands/…Command.php` (`php artisan sharepoint:*`) |
| Queue | `QueueService::dispatch()` + `QueueJobRegistry::register()` | Laravel queue jobs (`Queue::push()` / `dispatch(new Job)`) |
| DB layer | Capsule `DB::table('sharepoint_*')` | Eloquent models + migrations |
| Encryption | framework `EncryptionService` | Laravel `Crypt::encryptString()` (or shared `EncryptionService` facade in `ahg-core`) |
| HTTP | framework `HttpClientService` | Laravel `Http::` facade or Guzzle |
| Audit | `ahgAuditTrailPlugin` `AuditService::log()` | Heratio `ahg-audit-trail` package's logger |
| Settings | `ahgSettingsPlugin` `sharepoint` section + `ahg_settings` table | Heratio `ahg-settings` package + same `ahg_settings` table |

### 19.2 Schema parity

Both targets create the **same six tables** (`sharepoint_tenant`, `sharepoint_drive`, `sharepoint_mapping`, `sharepoint_sync_state`, `sharepoint_subscription`, `sharepoint_event`) and the **same `ingest_session.source` migration**. Schema is the source of truth; install.sql is byte-identical between targets except for the header comment block and the SQL transforms documented in `ahg-ingest/database/install.sql` (DROP-stripping, IF NOT EXISTS, COMMENT placement for MySQL 8 strict).

Heratio uses Laravel migrations (`database/migrations/2026_05_10_000001_create_sharepoint_tables.php`) backed by the same install.sql for parity.

### 19.3 Feature parity matrix

Every feature in §6, §7, §8, §9, §11 must exist in BOTH targets. Drift between implementations is the bug that this requirement exists to prevent.

| Feature | AtoM | Heratio |
|---------|------|---------|
| Schema (6 tables + ingest_session migration) | ✓ | ✓ |
| Tenant config UI | sfActions + Symfony+Blade dual templates | Laravel controller + Blade |
| Drive registration UI | ✓ | ✓ |
| Mapping editor | ✓ | ✓ |
| `sharepoint:install` / `:test-connection` / `:sync` (Phase 1) | Symfony task | Artisan command |
| `sharepoint:subscribe` / `:renew-subscriptions` / `:ingest-event` (Phase 2) | Symfony task | Artisan command |
| Webhook receiver | sfAction at `/sharepoint/webhook` | Laravel route at `/sharepoint/webhook` |
| Federated search backend (Phase 3) | sfAction + AJAX | Laravel controller + AJAX |
| M365 connector feed (Phase 3) | extends `ahgAPIPlugin` apiv2 routes | extends `ahg-api` package routes |
| Settings section | edits `ahgSettingsPlugin` (locked plugin precedent) | adds section to Heratio `ahg-settings` package |
| Audit trail integration | `AuditService::log()` | Heratio audit logger |

### 19.4 Optional shared core library — DEFERRED

A shared `ahg/sharepoint-core` PHP package (containing pure-PHP Graph client, mapping logic, retention mapper, DTOs) would reduce drift, but no existing plugin uses this pattern. Defer until both targets are built and a real drift problem appears. Document as a future refactor opportunity in the Phase 1 retro.

### 19.4.1 SPFx project — single-source

The SPFx command set lives ONCE at `atom-extensions-catalog/spfx/atom-archive-push/`. It is platform-independent — it talks to whichever AtoM/Heratio API is configured at install time via the SPFx solution's tenant property. The same `.sppkg` works against either target. This is the only Phase 2 component that does not have a dual-target implementation.

### 19.5 Portability rules for code (both targets)

- **No hardcoded absolute paths.** Use config keys: `sfConfig::get('sf_root_dir')` / `sfConfig::get('sf_upload_dir')` (AtoM) and `base_path()` / `storage_path()` / `config('filesystems.disks.uploads.root')` (Heratio).
- **No instance-specific URLs in code.** Webhook URL is a setting (read from `ahg_settings.sharepoint.webhook_public_url`), not hardcoded to `psis.theahg.co.za`. Default fallback derives from request host.
- **No instance-specific tenant IDs in code.** Tenant config is per-row in `sharepoint_tenant`.
- **Encryption key path is configurable.** AtoM reads from `/etc/atom/encryption.key`, Heratio reads from `config/key` or `APP_KEY`. The plugin must NOT read either path directly — it goes through the framework's encryption service.
- **Database connection is framework-provided.** Plugin code never instantiates a connection — uses `DB::table()` (Capsule in AtoM, Eloquent/QB in Heratio).
- **Plugin must work standalone in either install.** No cross-instance assumptions, no shared state outside the database.

### 19.6 Release & version tracking

- **AtoM target:** version bumped via `cd /usr/share/nginx/archive/atom-ahg-plugins && ./bin/release patch "..."` per project rule.
- **Heratio target:** version bumped via `cd /usr/share/nginx/heratio && ./bin/release patch "..."` per Heratio's own bin/release (note: Heratio has locked-paths enforcement via `.locked-paths` and pre-commit hooks — confirm the SP package is not in a locked path before adding code).
- Versions kept in lock-step: same patch number on both releases when both are touched.

---

## 20. Critical Files for Implementation

### AtoM target

| Purpose | File |
|---------|------|
| Pipeline we hand off to from webhook events | `atom-ahg-plugins/ahgIngestPlugin/lib/Services/IngestCommitService.php` |
| Queue dispatch / chain / batch / retry signatures | `atom-framework/src/Services/QueueService.php` |
| HMAC, retry, status enum, delivery log patterns to mirror | `atom-ahg-plugins/ahgAPIPlugin/lib/Services/WebhookService.php` |
| Settings section dual-template (must edit both) | `atom-ahg-plugins/ahgSettingsPlugin/modules/ahgSettings/actions/handlers/sectionAction.class.php` + `section.blade.php` + `sectionSuccess.php` |
| Encrypted client_secret at rest | `atom-framework/src/Core/Security/EncryptionService.php` |
| Outbound Graph HTTP | `atom-framework/src/Services/HttpClientService.php` |
| Cron registration pattern | `atom-ahg-plugins/ahgSettingsPlugin/modules/ahgSettings/actions/cronJobsAction.class.php` |
| Reporting views | `atom-framework/database/views/reporting_views.sql` |

### Heratio target

| Purpose | File |
|---------|------|
| Schema porting reference (transforms documented inline) | `heratio/packages/ahg-ingest/database/install.sql` (header) |
| Pipeline we hand off to from webhook events | `heratio/packages/ahg-ingest/src/Services/…` (port equivalent of IngestCommitService) |
| Service provider pattern | `heratio/packages/ahg-api/src/Providers/AhgApiServiceProvider.php` |
| Webhook controller pattern (CSRF-exempt) | `heratio/packages/ahg-api-plugin/src/Controllers/…` |
| Settings package (mirror section-add pattern) | `heratio/packages/ahg-settings/` |
| Audit logger | `heratio/packages/ahg-audit-trail/` |
| Locked-paths manifest (confirm SP package not locked) | `heratio/.locked-paths` |
| Release tooling | `heratio/bin/release` |

---

*End of plan.*
