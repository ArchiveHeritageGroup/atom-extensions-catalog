# AHG — Screen-Based Manual Test Checklist

Test the system **the way a user works it** — by screen. Each screen lists the
functions a user can reach *from that screen* (the linked plugins/panels), each
with its own sub-functions. Tick ☐→☑ as you verify; record Pass/Fail + notes.

---

## 1. ISAD(G) — Archival Description (Information Object)

The description view/edit screen (`/informationobject/<slug>` and its edit). From here a user can:

### 1.1 Core ISAD(G) description
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Reference code, title, level of description, dates, extent | | |
| ☐ | Context area | Name of creator, admin/biographical history, archival history, acquisition | | |
| ☐ | Content & structure | Scope & content, appraisal, accruals, system of arrangement | | |
| ☐ | Conditions of access & use | Access conditions, reproduction, language, physical characteristics, finding aids | | |
| ☐ | Allied materials | Originals, copies, related units, publication note | | |
| ☐ | Notes / access points | Subjects, places, names, genres | | |
| ☐ | Description control | Identifier, rules/conventions, status, dates, language, sources | | |
| ☐ | Save / publish | Create → validation fires → save → publish (draft↔published) | | |

### 1.2 Provenance (ahgProvenancePlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | View provenance | Chain-of-custody timeline on the record | | |
| ☐ | Edit provenance record | Acquisition method, certainty, Nazi-era / cultural-property / POPIA fields | | |
| ☐ | Add event | Add a custody/transfer event | | |
| ☐ | Delete event | Remove an event | | |
| ☐ | Documents | Attach / delete a provenance document | | |
| ☐ | Authenticity report | C2PA + AI-inference trust verdict | | |

### 1.3 AI (ahgAIPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | NER | Extract persons / orgs / places / dates → link as access points | | |
| ☐ | Summarize | AI summary of scope & content | | |
| ☐ | Translate | Machine-translate the description | | |
| ☐ | Spellcheck | Spelling / grammar check | | |
| ☐ | Suggest description | LLM description suggestion | | |
| ☐ | Face detection | Detect faces on the digital object, match to authorities | | |

### 1.4 Rights (ahgRightsPlugin / ahgExtendedRightsPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | PREMIS rights | Add a rights statement (act, basis, restriction) | | |
| ☐ | Creative Commons | Apply a CC licence | | |
| ☐ | RightsStatements.org | Apply a rights-statement URI | | |
| ☐ | Embargo | Set an embargo-until date | | |
| ☐ | TK / ICIP labels | Apply Traditional-Knowledge labels | | |
| ☐ | Orphan works | Mark orphan-work status | | |

### 1.5 Digital object (ahgIiifPlugin / ahgDAMPlugin / ahg3DModelPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Upload | Attach a master digital object | | |
| ☐ | Derivatives | Reference + thumbnail generate | | |
| ☐ | IIIF viewer | Open the IIIF/Mirador viewer; deep-zoom | | |
| ☐ | Media | Audio/video player + waveform/transcription | | |
| ☐ | 3D | 3D model viewer, hotspots, AR | | |
| ☐ | Watermark | Apply derivative watermark | | |
| ☐ | Metadata extraction | EXIF / IPTC / XMP pulled into the record | | |

### 1.6 Other linked panels
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Security classification (ahgSecurityClearancePlugin) | Set classification + clearance/embargo gate | | |
| ☐ | Custom fields (ahgCustomFieldsPlugin) | Institution-defined fields render + save | | |
| ☐ | Audit trail (ahgAuditTrailPlugin) | Changes logged + viewable | | |
| ☐ | Version control (ahgVersionControlPlugin) | View versions / restore | | |
| ☐ | Preservation (ahgPreservationPlugin) | Checksum / fixity / PREMIS event | | |
| ☐ | Share link (ahgTimeLimitedShareLinkPlugin) | Create a time-limited public link | | |

---

## 2. ISAAR-CPF — Authority Record (Actor)

The actor view/edit screen (`/actor/<slug>`). From here a user can:

### 2.1 Core ISAAR-CPF
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Type (person/family/corporate), authorised/parallel/other names, dates | | |
| ☐ | Description area | Places, legal status, functions/occupations, history, general context | | |
| ☐ | Relationships | Related actors (hierarchical/associative/temporal) | | |
| ☐ | Control area | Identifier, rules, status, level of detail, sources, maintenance | | |
| ☐ | Save / publish | Create → validate → save → publish | | |

### 2.2 Authority resolution (ahgAuthorityResolutionPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Match | Reconcile to ULAN / LCNAF / VIAF / Wikidata / ORCID | | |
| ☐ | Store identifier | Save the external URI on the actor | | |
| ☐ | Merge / dedupe | Merge duplicate authority records | | |

### 2.3 Contact (ahgContactPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Extended contact | Add phones / emails / addresses / web | | |

### 2.4 AI + linked records
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | AI (ahgAIPlugin) | NER / translate / summarize on the history | | |
| ☐ | Linked descriptions | Records created by / related to this actor | | |
| ☐ | Custom fields / audit | Custom fields render + save; changes logged | | |

---

## 3. ISDIAH — Repository (Archival Institution)

The repository view/edit screen (`/repository/<slug>`). From here a user can:

### 3.1 Core ISDIAH
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Identifier, authorised/parallel names, type | | |
| ☐ | Contact area | Address, phone, email, contacts | | |
| ☐ | Description area | History, geo/cultural context, mandates, structure, holdings, finding aids | | |
| ☐ | Access area | Opening times, conditions, accessibility | | |
| ☐ | Services area | Research services, reproduction, public areas | | |
| ☐ | Control area | Identifier, rules, status, sources | | |

### 3.2 Repository extras
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Logo / theme | Upload logo; per-repository branding | | |
| ☐ | Holdings | Linked descriptions for this repository | | |
| ☐ | Uploads path | Digital objects route to the repo's NAS path | | |
| ☐ | Custom fields / audit | Render + save; changes logged | | |

---

## 4. Accession

The accession view/edit screen (`/accession/<slug>`). From here a user can:

### 4.1 Core accession
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity | Accession number, acquisition date, title, scope | | |
| ☐ | Acquisition | Source of acquisition, type, processing status/priority | | |
| ☐ | Appraisal / disposal | Appraisal, accrual, disposal notes | | |
| ☐ | Create description | Generate an information_object from the accession | | |

### 4.2 Donor & agreements (ahgDonorManagePlugin / ahgDonorAgreementPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Donor | Link / create a donor record (contact, PII) | | |
| ☐ | Donor agreement | Attach / generate the donor agreement (SA compliance) | | |

### 4.3 Rights holder & storage
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Rights holder (ahgRightsHolderManagePlugin) | Link / create a rights holder | | |
| ☐ | Physical storage (ahgStorageManagePlugin) | Assign a physical location / container | | |
| ☐ | Deaccession | Record a deaccession | | |
| ☐ | Audit | Changes logged | | |

---

## 5. Term / Taxonomy

The term view/edit + taxonomy browse (`/taxonomy/...`, `/term/<slug>`). From here a user can:

### 5.1 Term management (ahgTermTaxonomyPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Browse taxonomy | Open a taxonomy; navigate terms | | |
| ☐ | View term | Term detail + scope note | | |
| ☐ | Edit term (ACL-gated) | Preferred/alt labels, scope note, code | | |
| ☐ | Relationships | Broader / narrower / related (SKOS) | | |
| ☐ | Delete (ACL-gated) | Remove a non-protected term | | |
| ☐ | SKOS export | `/taxonomy/<id>/skos` export | | |

### 5.2 Semantic / thesaurus (ahgSemanticSearchPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Thesaurus sync | WordNet / Wikidata enrichment | | |
| ☐ | Used-in | Records using this term | | |

---

## 6. Function (ISDF)

The function view/edit screen (ahgFunctionManagePlugin). From here a user can:

| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Identity area | Type, authorised/parallel names, classification | | |
| ☐ | Context area | Dates, description, history, legislation | | |
| ☐ | Relationships | Related functions / actors | | |
| ☐ | Control area | Identifier, rules, status, sources | | |
| ☐ | Linked records | Actors / descriptions performing this function | | |

---

## 7. Digital Object (stand-alone view)

The digital-object view + actions (IIIF/DAM/preservation). From here a user can:

### 7.1 View & derivatives (ahgIiifPlugin / ahgDAMPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | View / stream | IIIF deep-zoom, media player, 3D viewer | | |
| ☐ | Derivatives | Reference + thumbnail; regen-derivatives | | |
| ☐ | DAM metadata | IPTC / XMP / EXIF panel | | |
| ☐ | Watermark | Apply / preview watermark | | |

### 7.2 Preservation (ahgPreservationPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Checksum / fixity | Generate checksum; verify fixity | | |
| ☐ | Format ID | Siegfried / PRONOM identification | | |
| ☐ | PREMIS event | Event recorded per action | | |
| ☐ | Replication | Replicate to a configured target | | |

### 7.3 Text & rights
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | OCR / HTR | Extract text from image/PDF | | |
| ☐ | Rights / ODRL | Access policy on the object (download gated) | | |

---

## 8. Research Portal

The researcher-facing area (`/research/...`). From here a user can:

### 8.1 Researcher & reading room (ahgResearchPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Registration / profile | Register; set experience level | | |
| ☐ | Booking | Reading-room booking; seat map; retrieval queue | | |
| ☐ | Projects | Create a research project / evidence set | | |
| ☐ | Journal & annotations | Research journal; annotation studio | | |
| ☐ | Bibliographies | Build / export a bibliography (citation formats) | | |
| ☐ | DMP | Author a Data Management Plan | | |

### 8.2 Requests & datasets
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Request to publish (ahgRequestToPublishPlugin) | Submit a publication request; receipt token; curator inbox | | |
| ☐ | Cart (ahgCartPlugin) | Add reproductions; checkout; pay (PayFast); download | | |
| ☐ | Favorites (ahgFavoritesPlugin) | Bookmark records | | |
| ☐ | RDM datasets (ahgRdmPlugin) | Deposit → POPIA scan → gate → DOI → landing (see RDM) | | |

---

## 9. GLAM Browse & Search

The public discovery surface. From here a user can:

### 9.1 Browse & display (ahgDisplayPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | GLAM browse | Display modes; grid/list | | |
| ☐ | Guest published-only | Logged-out users see published records only | | |
| ☐ | Landing page (ahgLandingPagePlugin) | Visual landing blocks render | | |

### 9.2 Search (ahgSearchPlugin / ahgSemanticSearchPlugin / ahgDiscoveryPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Global search | Query + autocomplete | | |
| ☐ | Facets | Filter by repository / level / date / subject | | |
| ☐ | Semantic / discovery | Natural-language query; semantic results | | |

### 9.3 Sector browse
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Library (ahgLibraryPlugin) | OPAC search; FRBR clusters; export (CSV/BibTeX/RIS); MARC | | |
| ☐ | Museum (ahgMuseumPlugin) | Museum browse; Spectrum; CIDOC-CRM | | |
| ☐ | Gallery (ahgGalleryPlugin) | Gallery browse / show | | |
| ☐ | DAM (ahgDAMPlugin) | DAM browse; rights/technical metadata | | |

---

## 10. Reports & Dashboards

The reporting/admin surface (`/reports`). From here a user (admin) can:

### 10.1 Reports (ahgReportsPlugin / ahgReportBuilderPlugin)
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Central reports | Descriptions / authorities / repositories / accessions reports | | |
| ☐ | Report builder | Sections, rich text, SQL queries, templates | | |
| ☐ | Export | Word / PDF / XLSX / CSV | | |
| ☐ | Sharing / scheduling | Time-limited share link; scheduled run | | |

### 10.2 Statistics, audit & compliance
| ✔ | Function | Sub-function | Result | Notes |
|---|---|---|---|---|
| ☐ | Statistics (ahgStatisticsPlugin) | Usage stats | | |
| ☐ | Audit reports (ahgAuditTrailPlugin) | Logs; statistics; seal/chain | | |
| ☐ | Privacy / data protection (ahgPrivacyPlugin / ahgCDPAPlugin) | PII scan; DPIA/ROPA; POPIA/GDPR/CDPA | | |
| ☐ | Heritage accounting (ahgHeritageAccountingPlugin / ahgIPSASPlugin) | GRAP 103 / IPSAS asset reports | | |
| ☐ | RDM compliance / dashboard (ahgRdmPlugin) | Scoreboard + roll-up dashboard | | |

---

*Coverage: the central GLAM entity screens + the cross-cutting panels and surfaces. Add institution-specific screens (Zimbabwe NAZ/NMMZ/CDPA, exhibitions, loans, heritage discovery) as needed.*
