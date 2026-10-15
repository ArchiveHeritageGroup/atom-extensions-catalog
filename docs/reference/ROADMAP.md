# Product Roadmap - AHG Extensions for AtoM 2.10

**The Archive and Heritage Group (Pty) Ltd**
**Owner:** Dr Johan Pieterse
**atom-framework:** v2.19.10 (14 October 2026) | **atom-ahg-plugins:** v3.121.12 (15 October 2026) | **Plugins:** 121, plus the generated runtime | **Updated:** 15 October 2026

The AHG extensions add preservation, provenance, Records in Contexts, AI-assisted description and discovery, museum, library and DAM workflows, rights, privacy and governance to [Access to Memory (AtoM)](https://www.accesstomemory.org/) 2.10. There are two parts. `atom-framework` supplies the shared services, the `bin/atom` command line and the generated `ahgRuntimePlugin`; `atom-ahg-plugins` holds the plugins themselves. Base AtoM is not modified. Every capability is a plugin an institution can install or leave out.

This roadmap covers those two repositories only. Heratio, the Laravel platform that runs on the same data model, is a separate product with its own roadmap.

## Where things stand

| Item | Value |
|------|-------|
| atom-framework | v2.19.8, released 12 October 2026 |
| atom-ahg-plugins | v3.121.1, released 13 October 2026 |
| Plugins in the repository | 121 (`ahg*Plugin` directories with an `extension.json`) |
| Runtime | `ahgRuntimePlugin`, generated from atom-framework since v2.14.0 (4 August 2026) |
| Reference instance | PSIS (psis.theahg.co.za): 114 AHG plugins enabled; `ahgMultiTenantPlugin` installed but switched off |
| Supported AtoM | 2.8 to 2.10, PHP 8.1 or later |
| Licence | AGPL-3.0 |

Plugin maturity is uneven, and the catalogue says so. A handful ship as packaged bundles with screenshots and install notes; IIIF, Seadragon, Mirador, Preservation, Provenance, Backup, Favourites and Feedback are among them. Several newer plugins still carry a 0.x version number: GIS, SharePoint, RDM, Records management, Archaeology, AI compliance, Authority resolution, Version control, C2PA, NARSSA and Time-limited share links. Treat those as early releases.

## Shipped since February 2026

The previous roadmap was written against plugins v3.9.30 (27 February 2026). Since then the plugins repository has moved through roughly 1,300 commits to v3.121.1, and the framework from v2.10.24 to v2.19.8. The larger pieces, roughly in the order they landed:

| Capability | Plugin(s) | Release | Date |
|-----------|-----------|---------|------|
| Image similarity search (CLIP vectors in Qdrant), HTR command, GIS spatial search | ahgDiscoveryPlugin, ahgAIPlugin, ahgGISPlugin 0.1.0 | plugins v3.9.34 | 27 Feb 2026 |
| Linked data sync; workflow v2.0 | ahgAuthorityPlugin, ahgWorkflowPlugin | plugins v3.10.0 | 28 Feb 2026 |
| Accessioning v2: intake queue, appraisal, containers, rights inheritance | ahgAccessionManagePlugin | plugins v3.14.0 | 28 Feb 2026 |
| Dropdown Manager and removal of ENUM columns | atom-framework | framework v2.11.0 | 8 Mar 2026 |
| Wikidata auto-verification and ISNI search for authorities | ahgAuthorityPlugin | plugins v3.22.0 | 10 Apr 2026 |
| SharePoint ingest and push | ahgSharePointPlugin 0.1.0 | plugins v3.28.0 to v3.31.0 | 10 May 2026 |
| Research portal 3.1: studio outputs, notebooks, ORCID, offline PWA | ahgResearchPlugin 3.1.0 | plugins v3.33.0 | 16 May 2026 |
| Retention schedules, disposal workflow, NARSSA transfer manifests | ahgExtendedRightsPlugin, ahgNARSSAPlugin 0.1.0 | plugins v3.34.0 | 17 May 2026 |
| Authority resolution engine | ahgAuthorityResolutionPlugin 0.1.0 | plugins v3.35.0 | 19 May 2026 |
| AI inference provenance and grounding guardrails | ahgProvenancePlugin, ahgAIPlugin | plugins v3.36.0 to v3.38.0 | 22 May 2026 |
| OCFL, scanning, ResourceSync, observability, C2PA (first cut) | ahgOcflPlugin, ahgScanPlugin, ahgResourceSyncPlugin, ahgObservabilityPlugin, ahgC2paPlugin | plugins v3.48.0 | 1 Jun 2026 |
| DPIA and structured redaction | ahgPrivacyPlugin | plugins v3.50.0, v3.51.0 | 3 Jun 2026 |
| Records-management file plan | ahgRecordsManagePlugin 0.1.0 | plugins v3.52.0 | 3 Jun 2026 |
| OpenAPI 3.1 specification and Swagger UI for REST API v2 | atom-framework, ahgAPIPlugin | framework v2.12.0 | 3 Jun 2026 |
| Passkey (WebAuthn) MFA, per-role MFA, tamper-evident audit chain | ahgSecurityClearancePlugin, ahgAuditTrailPlugin | plugins v3.56.0 | 4 Jun 2026 |
| W3C Web Annotations, image AR, functions documentation | ahgAnnotationsPlugin, ahgImageArPlugin, ahgFunctionsDocsPlugin | plugins v3.60.0 | 10 Jun 2026 |
| EU AI Act register: systems, models, risks, attestations | ahgAiCompliancePlugin 0.1.0 | plugins v3.64.0 | 14 Jun 2026 |
| Cross-domain knowledge graph view; federated union catalogue | ahgRicExplorerPlugin, ahgFederationPlugin | plugins v3.70.0, v3.71.0 | 15 Jun 2026 |
| Research data management, with ODRL enforcement on files | ahgRdmPlugin 0.1.0 | plugins v3.73.0 to v3.79.0 | 27 Jun 2026 |
| SAHRA heritage-permit workflow | ahgSAHRAPlugin | plugins v3.80.0 | 22 Jul 2026 |
| Records in Contexts as a selectable descriptive standard | ahgRicManagePlugin | plugins v3.82.0 to v3.87.0 | 23 Jul 2026 |
| Seadragon and Mirador as separate viewer plugins, with a viewer switcher | ahgSeadragonPlugin, ahgMiradorPlugin | plugins v3.89.0 to v3.95.0 | 4 to 10 Aug 2026 |
| Site records for archaeology and rock art; excavation contexts with Harris Matrix | ahgSiteRecordPlugin, ahgArchaeologyPlugin 0.1.0 | plugins v3.100.0, v3.104.0 | 15 and 23 Aug 2026 |
| Nonce-only CSP: inline handlers and style attributes removed from templates | all plugins | plugins v3.105.0 to v3.113.0 | 23 Aug to 30 Sep 2026 |
| Storage locations: movement log, bulk relocation, capacity counted down the tree | ahgStorageManagePlugin | plugins v3.111.0 to v3.116.0 | 28 Sep to 8 Oct 2026 |
| Ask the Archive, a public chatbot that re-checks every record against access rules | ahgChatbotPlugin 1.3.0 | plugins v3.114.0 | 6 Oct 2026 |
| Restricted descriptions enforced in record pages, browse, exports and OAI-PMH | ahgExtendedRightsPlugin, ahgAPIPlugin, atom-framework | plugins v3.114.4, v3.115.2; framework v2.19.1 | 7 and 8 Oct 2026 |
| Session timeout warning | ahgThemeB5Plugin | plugins v3.117.0 | 8 Oct 2026 |
| CAAIS 1.0 accessions and export; OpenID Connect sign-in; custom fields in EAD, PDF, CSV, REST and GraphQL; batch edit and rename; child sorting; Excel import and grid entry; preservation triage dashboard | several, see the release note | plugins v3.118.0; framework v2.19.0 | 8 Oct 2026 |
| Tenant isolation | ahgMultiTenantPlugin 1.3.0 | plugins v3.118.1 | 8 Oct 2026 |
| Hierarchical CSV import with correct nested sets | ahgIngestPlugin 1.1.0 | plugins v3.119.0 | 8 Oct 2026 |
| REST API key management page | ahgAPIPlugin 1.2.0 | plugins v3.119.12 | 10 Oct 2026 |
| C2PA content credentials signed on upload | ahgC2paPlugin 0.2.0 | plugins v3.120.0 | 12 Oct 2026 |
| Provenance chain checked link by link | ahgProvenancePlugin 1.2.3 | plugins v3.121.1 | 13 Oct 2026 |

Everything the February roadmap listed as completed is still in the repository. Two of those plugins have since grown their own version histories: ahgAIPlugin is now 2.3.0 and ahgPortableExportPlugin 3.0.0.

## What happened to the February plan

None of the February "In Progress" or "Planned" rows carried a date that held, and several of them shipped in a different shape from the one described. The status of each, as of today:

| February item | Status | Evidence |
|---------------|--------|----------|
| Voice command interface (speech recognition) | Shipped | Browser speech recognition and synthesis in ahgThemeB5Plugin (`voiceCommands.js`, first commit 15 Feb 2026); image and object description through the AHG AI gateway since plugins v3.113.4 (5 Oct 2026) |
| Intelligent cataloguing: LLM suggestions, image similarity, HTR | Shipped | `ai:suggest-description` in ahgAIPlugin; image similarity and the `ai:htr-extract` task in plugins v3.9.34 (27 Feb 2026); the HTR task routes through the gateway since plugins v3.35.9 |
| Linked data: Wikidata, VIAF, Getty | Largely shipped | Linked data sync in v3.10.0; Wikidata verification in v3.22.0; local Getty AAT cache in ahgMuseumPlugin (16 Mar 2026); Wikidata links on description and authority pages in v3.118.0; VIAF search and record lookup working again in October 2026, after OCLC retired the old VIAF API |
| Multi-tenant architecture | Built; not yet switched on in production | ahgMultiTenantPlugin 1.3.0 with tenant isolation (v3.118.1); disabled on PSIS. Next step is a check on a separate test instance |
| Enterprise authentication: LDAP, SAML, OIDC, MFA | Mostly shipped | LDAP through base AtoM; passkey MFA in v3.56.0; OpenID Connect in v3.118.0. SAML is built but cannot run until its PHP library is added to atom-framework |
| REST API v2 | Shipped | ahgAPIPlugin 1.2.0: CRUD, API keys with scopes, rate limiting, HMAC-signed webhooks, OpenAPI 3.1 (framework v2.12.0); OAI-PMH filtered by the same access rules (v3.115.2) |
| Handwritten text recognition | Shipped (command and gateway route) | See intelligent cataloguing above. The vision-model OCR port from Heratio (#194) is deferred |
| Image similarity search | Shipped | ahgDiscoveryPlugin `ImageSearchStrategy`, plugins v3.9.34 |
| GIS and spatial heritage | Early release | ahgGISPlugin 0.1.0: geospatial search and GeoJSON export. Site locality is recorded in ahgSiteRecordPlugin |
| SaaS deployment | Not built as a hosted service | Docker and Ansible installers have been in atom-framework since January 2026 and the Docker nginx template was hardened in August |
| Mobile field app | Not built as a native app | The research portal has an offline PWA (v3.33.0, v3.79.56); site and excavation recording are web forms |
| Extended standards: CIDOC-CRM, public SPARQL, BIBFRAME, PBCore | Partly shipped | BIBFRAME, PBCore, LIDO, MODS, METS, PREMIS, EBUCore, VRA Core, RiC-O and schema.org exporters in ahgMetadataExportPlugin; CIDOC-CRM export in ahgMuseumPlugin; SPARQL through the RiC triplestore. Further CIDOC-CRM joins (#150) are deferred |
| Multilingual NER (Afrikaans, isiZulu, Sesotho) | Not started | Only interface translations exist (framework v2.13.37 added glossaries for the remaining official South African languages) |
| Platform evolution: Symfony 1.4 to Laravel | Moved to Heratio | AtoM 2.10 keeps Symfony 1.4 and its nested sets. The migration became Heratio, a separate product |
| Collaboration tools | Partly shipped | W3C annotations (ahgAnnotationsPlugin, v3.60.0); real-time collaboration in the research portal (v3.33.0). Discussion threads on records have not been built |

## Open work

What follows is open, with no committed dates. Items move into a release when they are built and tested on PSIS, not before.

**Finishing current work.** SAML sign-on needs its PHP library added to atom-framework before it can be switched on (#200). The WCAG 2.1 AA audit has fixed its first blocker, on the physical storage pages, and the remaining findings are still to be worked through (#201). Multi-tenancy needs its isolation check on a test instance before any production tenant is enabled.

**Still wanted, not yet built.** A self-service hosted platform (today each client is hosted and installed by hand, with the Docker and Ansible installers), a mobile app, named-entity recognition in Afrikaans, isiZulu and Sesotho, and discussion threads on records.

**Platform hardening.** Issue #198 (public portal, multi-tenancy and hardening) is closed, and much of it shipped: upload validation, unserialize and path hardening, batch edit with preview and audit, tenant branding and tenant isolation for descriptions. What it asked for and has not been built: isolation of uploads, search indices and caches per tenant; an explainable ranking panel; rollback of bulk edits; an outbound-HTTP (SSRF) policy; and automated tests for cross-tenant leakage.

**Deferred ports from Heratio.** These were deferred on 8 October 2026 and stay on the list:

| Issue | Work |
|-------|------|
| #194 | Vision-model OCR as an optional engine, with Tesseract kept as a cross-check |
| #195 | Rebuilding a PDF or PDF/A text layer from a corrected transcript |
| #196 | Collection cross-referencing: same-story links, name grounding, duplicate checks |
| #150 | Knowledge graph: CIDOC-CRM and knowledge-base joins |
| #151 | Federation: loans between institutions |
| #152 | C2PA: content credentials are now signed on upload (v3.120.0); what remains is open on the issue |
| #153 | Compliance drafting: DPIA, records of processing, retention |
| #155 | Storytelling: trails, posts, school packs |

## Parked

| Item | Note |
|------|------|
| JSON-LD export | Low demand in the South African market |
| Keyword search for the chatbot | Plan written on 7 October 2026; not started until it is taken off hold |

## Answered by Heratio, not here

Two long-standing community requests can only be met by changing AtoM itself: replacing nested sets for performance, and moving to a framework with long-term support. The extensions do not change base AtoM, so both are answered by Heratio rather than by these plugins.

## Contributing

Feedback and feature requests are welcome. Open an issue on [atom-ahg-plugins](https://github.com/ArchiveHeritageGroup/atom-ahg-plugins/issues) or [atom-extensions-catalog](https://github.com/ArchiveHeritageGroup/atom-extensions-catalog/issues).

**Contact:** Dr Johan Pieterse, [The Archive and Heritage Group](https://theahg.co.za)
**Licence:** AGPL-3.0
