# AtoM Heratio — Project Briefing

**Version:** Framework 2.11.7 / Plugins 3.21.17
**Date:** 16 March 2026
**Organization:** The Archive and Heritage Group (Pty) Ltd
**Owner:** Johan Pieterse (johan@theahg.co.za)

---

## What Is AtoM Heratio?

AtoM Heratio is a comprehensive modernization of **Access to Memory (AtoM) 2.10** — the world's leading open-source archival management system used by thousands of institutions globally. Heratio transforms AtoM from a single-purpose archival tool into an enterprise-grade **GLAM platform** (Galleries, Libraries, Archives, Museums) and **Digital Asset Management** system.

It adds approximately **300% more functionality** through 80 modular plugins — without modifying a single core AtoM file. All customizations sit in two layers on top of base AtoM, maintaining full backward compatibility and upgrade paths.

### Target Market

GLAM and DAM institutions internationally:
- National archives and government record offices
- University and research libraries
- Museums and cultural heritage institutions
- Art galleries and exhibition spaces
- Digital asset management organizations
- Heritage and conservation bodies

### Competitive Position

| Alternative | Cost | Limitations |
|-------------|------|------------|
| Preservica | $50K+/year | Proprietary, archive-only |
| ArchivesSpace | Free (open source) | Archive-only, no GLAM |
| CollectiveAccess | Free (open source) | Museum-focused, limited |
| ResourceSpace | Free/paid | DAM-only |
| **AtoM Heratio** | **Free (GPL-3.0)** | **All 5 sectors in one platform** |

---

## System at a Glance

| Metric | Value |
|--------|-------|
| Framework version | 2.11.7 |
| Plugin version | 3.21.17 |
| Total plugins | 80 (registered: 79 + ahgMigrationPlugin filesystem-only) |
| Enabled plugins | 108 (incl. base AtoM plugins) |
| Locked core plugins | 16 |
| Database tables | 894 |
| CLI commands | 235 (Symfony) + framework commands |
| Help articles | 201 (published) |
| Settings fields | 200+ across 21 sections |
| Descriptive standards | 5 (ISAD(G), DACS, Dublin Core, MODS, RAD) |
| GLAM sectors | 5 (Archive, Library, Museum, Gallery, DAM) |
| Compliance standards | 12 jurisdictions |
| WCAG conformance | Level AA |
| Voice commands | 100+ in 11 languages |
| GitHub issues | 218 closed, 9 open (7 future/parked) |

### Sample Instance (PSIS)

| Metric | Count |
|--------|-------|
| Archival descriptions | 704 |
| Authority records | 395 |
| Digital objects | 665 |
| Accessions | 4 |
| Repositories | 14 |

---

## Architecture

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 481 276" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="480" height="275" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="18.0" x2="17.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="18.0" x2="13.6" y2="26.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="18.0" x2="20.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="18.0" x2="24.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="18.0" x2="28.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="18.0" x2="31.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="18.0" x2="35.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="18.0" x2="38.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="18.0" x2="42.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="18.0" x2="46.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="18.0" x2="49.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="18.0" x2="53.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="18.0" x2="56.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="18.0" x2="60.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="18.0" x2="64.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="18.0" x2="67.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="18.0" x2="71.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="18.0" x2="74.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="18.0" x2="78.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="18.0" x2="82.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="18.0" x2="85.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="18.0" x2="89.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="18.0" x2="92.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="18.0" x2="96.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="18.0" x2="100.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="18.0" x2="103.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="18.0" x2="107.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="18.0" x2="110.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="18.0" x2="114.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="18.0" x2="118.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="18.0" x2="121.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="18.0" x2="125.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="18.0" x2="128.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="18.0" x2="132.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="18.0" x2="136.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="18.0" x2="139.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="18.0" x2="143.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="18.0" x2="146.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="18.0" x2="150.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="18.0" x2="154.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="18.0" x2="157.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="18.0" x2="161.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="18.0" x2="164.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="18.0" x2="168.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="18.0" x2="172.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="18.0" x2="175.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="18.0" x2="179.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="18.0" x2="182.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="18.0" x2="186.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="18.0" x2="190.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="18.0" x2="193.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="18.0" x2="197.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="18.0" x2="200.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="18.0" x2="204.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="18.0" x2="208.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="18.0" x2="211.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="18.0" x2="215.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="18.0" x2="218.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="18.0" x2="222.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="18.0" x2="226.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="18.0" x2="229.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="18.0" x2="233.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="18.0" x2="236.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="18.0" x2="240.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="18.0" x2="244.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="18.0" x2="247.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="18.0" x2="251.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="18.0" x2="254.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="18.0" x2="258.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="18.0" x2="262.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="18.0" x2="265.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="18.0" x2="269.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="18.0" x2="272.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="18.0" x2="276.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="18.0" x2="280.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="18.0" x2="283.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="18.0" x2="287.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="18.0" x2="290.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="18.0" x2="294.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="18.0" x2="298.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="18.0" x2="301.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="18.0" x2="305.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="18.0" x2="308.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="18.0" x2="312.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="18.0" x2="316.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="18.0" x2="319.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="18.0" x2="323.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="18.0" x2="326.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="18.0" x2="330.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="18.0" x2="334.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="18.0" x2="337.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="18.0" x2="341.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="18.0" x2="344.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="18.0" x2="348.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="18.0" x2="352.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="18.0" x2="355.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="18.0" x2="359.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="18.0" x2="362.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="18.0" x2="366.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="18.0" x2="370.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="18.0" x2="373.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="18.0" x2="377.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="18.0" x2="380.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="18.0" x2="384.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="18.0" x2="388.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="18.0" x2="391.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="18.0" x2="395.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="18.0" x2="398.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="18.0" x2="402.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="18.0" x2="406.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="18.0" x2="409.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="18.0" x2="413.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="18.0" x2="416.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="18.0" x2="420.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="18.0" x2="424.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="18.0" x2="427.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="18.0" x2="431.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="18.0" x2="434.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="18.0" x2="438.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="18.0" x2="442.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="18.0" x2="445.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="18.0" x2="449.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="18.0" x2="452.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="18.0" x2="456.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="18.0" x2="460.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="18.0" x2="460.0" y2="26.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="26.0" x2="467.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="34.0" x2="467.2" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="42.0" x2="467.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="50.0" x2="467.2" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="66.0" x2="35.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="66.0" x2="38.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="66.0" x2="42.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="66.0" x2="46.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="66.0" x2="49.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="66.0" x2="53.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="66.0" x2="56.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="66.0" x2="60.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="66.0" x2="64.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="66.0" x2="67.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="66.0" x2="71.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="66.0" x2="74.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="66.0" x2="78.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="66.0" x2="82.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="66.0" x2="85.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="66.0" x2="89.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="66.0" x2="92.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="66.0" x2="96.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="66.0" x2="100.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="66.0" x2="103.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="66.0" x2="107.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="66.0" x2="110.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="66.0" x2="114.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="66.0" x2="118.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="66.0" x2="121.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="66.0" x2="125.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="66.0" x2="128.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="66.0" x2="132.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="66.0" x2="136.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="66.0" x2="139.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="66.0" x2="143.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="66.0" x2="146.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="66.0" x2="150.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="66.0" x2="154.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="66.0" x2="157.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="66.0" x2="161.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="66.0" x2="164.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="66.0" x2="168.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="66.0" x2="172.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="66.0" x2="175.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="66.0" x2="179.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="66.0" x2="182.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="66.0" x2="186.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="66.0" x2="190.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="66.0" x2="193.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="66.0" x2="197.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="66.0" x2="200.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="66.0" x2="204.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="66.0" x2="208.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="66.0" x2="211.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="66.0" x2="215.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="66.0" x2="218.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="66.0" x2="222.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="66.0" x2="226.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="66.0" x2="229.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="66.0" x2="233.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="66.0" x2="236.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="66.0" x2="240.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="66.0" x2="244.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="66.0" x2="247.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="66.0" x2="251.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="66.0" x2="254.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="66.0" x2="258.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="66.0" x2="262.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="66.0" x2="265.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="66.0" x2="269.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="66.0" x2="272.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="66.0" x2="276.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="66.0" x2="280.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="66.0" x2="283.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="66.0" x2="287.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="66.0" x2="290.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="66.0" x2="294.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="66.0" x2="298.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="66.0" x2="301.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="66.0" x2="305.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="66.0" x2="308.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="66.0" x2="312.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="66.0" x2="316.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="66.0" x2="319.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="66.0" x2="323.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="66.0" x2="326.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="66.0" x2="330.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="66.0" x2="334.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="66.0" x2="337.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="66.0" x2="341.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="66.0" x2="344.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="66.0" x2="348.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="66.0" x2="352.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="66.0" x2="355.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="66.0" x2="359.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="66.0" x2="362.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="66.0" x2="366.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="66.0" x2="370.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="66.0" x2="373.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="66.0" x2="377.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="66.0" x2="380.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="66.0" x2="384.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="66.0" x2="388.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="66.0" x2="391.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="66.0" x2="395.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="66.0" x2="398.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="66.0" x2="402.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="66.0" x2="406.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="66.0" x2="409.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="66.0" x2="413.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="66.0" x2="416.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="66.0" x2="420.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="66.0" x2="424.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="66.0" x2="427.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="66.0" x2="431.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="66.0" x2="434.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="66.0" x2="438.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="66.0" x2="442.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="66.0" x2="445.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="66.0" x2="449.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="66.0" x2="452.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="66.0" x2="456.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="66.0" x2="460.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="58.0" x2="460.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="66.0" x2="460.0" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="74.0" x2="467.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="82.0" x2="467.2" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="98.0" x2="38.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="90.0" x2="35.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="98.0" x2="35.2" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="98.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="90.0" x2="467.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="98.0" x2="467.2" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="114.0" x2="38.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="106.0" x2="35.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="114.0" x2="35.2" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="114.0" x2="42.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="46.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="114.0" x2="49.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="114.0" x2="53.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="106.0" x2="467.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="114.0" x2="467.2" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="130.0" x2="38.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="122.0" x2="35.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="130.0" x2="35.2" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="130.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="46.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="130.0" x2="49.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="130.0" x2="53.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="122.0" x2="467.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="130.0" x2="467.2" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="146.0" x2="38.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="138.0" x2="35.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="146.0" x2="35.2" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="146.0" x2="42.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="46.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="146.0" x2="49.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="146.0" x2="53.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="138.0" x2="467.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="146.0" x2="467.2" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="162.0" x2="38.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="154.0" x2="35.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="162.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="46.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="162.0" x2="49.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="162.0" x2="53.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="154.0" x2="467.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="162.0" x2="467.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="17.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="178.0" x2="20.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="178.0" x2="24.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="178.0" x2="28.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="178.0" x2="31.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="178.0" x2="35.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="178.0" x2="38.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="178.0" x2="42.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="46.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="178.0" x2="49.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="178.0" x2="53.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="178.0" x2="56.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="178.0" x2="60.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="178.0" x2="64.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="178.0" x2="67.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="178.0" x2="71.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="178.0" x2="74.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="178.0" x2="78.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="178.0" x2="82.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="178.0" x2="85.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="178.0" x2="89.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="178.0" x2="92.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="178.0" x2="96.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="178.0" x2="100.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="178.0" x2="103.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="178.0" x2="107.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="178.0" x2="110.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="178.0" x2="114.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="178.0" x2="118.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="178.0" x2="121.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="178.0" x2="125.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="178.0" x2="128.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="178.0" x2="132.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="178.0" x2="136.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="178.0" x2="139.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="178.0" x2="143.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="178.0" x2="146.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="178.0" x2="150.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="178.0" x2="154.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="178.0" x2="157.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="178.0" x2="161.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="178.0" x2="164.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="178.0" x2="168.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="178.0" x2="172.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="178.0" x2="175.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="178.0" x2="179.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="178.0" x2="182.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="178.0" x2="186.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="178.0" x2="190.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="178.0" x2="193.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="178.0" x2="197.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="178.0" x2="200.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="178.0" x2="204.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="178.0" x2="208.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="178.0" x2="211.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="178.0" x2="215.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="178.0" x2="218.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="178.0" x2="222.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="178.0" x2="226.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="178.0" x2="229.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="178.0" x2="233.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="178.0" x2="236.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="178.0" x2="240.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="178.0" x2="244.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="178.0" x2="247.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="178.0" x2="251.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="178.0" x2="254.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="178.0" x2="258.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="178.0" x2="262.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="178.0" x2="265.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="178.0" x2="269.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="178.0" x2="272.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="178.0" x2="276.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="178.0" x2="280.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="178.0" x2="283.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="178.0" x2="287.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="178.0" x2="290.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="178.0" x2="294.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="178.0" x2="298.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="178.0" x2="301.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="178.0" x2="305.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="178.0" x2="308.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="178.0" x2="312.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="178.0" x2="316.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="178.0" x2="319.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="178.0" x2="323.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="178.0" x2="326.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="178.0" x2="330.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="178.0" x2="334.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="178.0" x2="337.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="178.0" x2="341.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="178.0" x2="344.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="178.0" x2="348.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="178.0" x2="352.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="178.0" x2="355.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="178.0" x2="359.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="178.0" x2="362.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="178.0" x2="366.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="178.0" x2="370.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="178.0" x2="373.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="178.0" x2="377.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="178.0" x2="380.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="178.0" x2="384.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="178.0" x2="388.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="178.0" x2="391.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="178.0" x2="395.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="178.0" x2="398.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="178.0" x2="402.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="178.0" x2="406.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="178.0" x2="409.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="178.0" x2="413.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="178.0" x2="416.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="178.0" x2="420.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="178.0" x2="424.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="178.0" x2="427.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="178.0" x2="431.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="178.0" x2="434.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="178.0" x2="438.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="178.0" x2="442.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="178.0" x2="445.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="178.0" x2="449.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="178.0" x2="452.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="178.0" x2="456.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="178.0" x2="460.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="170.0" x2="460.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="178.0" x2="460.0" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="186.0" x2="467.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="194.0" x2="467.2" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="210.0" x2="38.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="202.0" x2="35.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="210.0" x2="35.2" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="210.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="46.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="210.0" x2="49.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="210.0" x2="53.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="202.0" x2="467.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="210.0" x2="467.2" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="13.6" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="226.0" x2="38.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="218.0" x2="35.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="226.0" x2="35.2" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="226.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="46.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="226.0" x2="49.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="226.0" x2="53.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="218.0" x2="467.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="226.0" x2="467.2" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="234.0" x2="13.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="242.0" x2="13.6" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="242.0" x2="38.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="234.0" x2="35.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="242.0" x2="42.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="242.0" x2="46.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="242.0" x2="49.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="242.0" x2="53.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="234.0" x2="467.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="467.2" y1="242.0" x2="467.2" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="258.0" x2="17.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="250.0" x2="13.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="258.0" x2="20.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="258.0" x2="24.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="258.0" x2="28.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="258.0" x2="31.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="258.0" x2="35.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="258.0" x2="38.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="258.0" x2="42.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="258.0" x2="46.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="258.0" x2="49.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="258.0" x2="53.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="258.0" x2="56.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="258.0" x2="60.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="258.0" x2="64.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="258.0" x2="67.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="258.0" x2="71.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="74.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="258.0" x2="78.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="258.0" x2="82.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="258.0" x2="85.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="258.0" x2="89.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="258.0" x2="92.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="258.0" x2="96.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="258.0" x2="100.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="258.0" x2="103.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="258.0" x2="107.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="258.0" x2="110.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="258.0" x2="114.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="258.0" x2="118.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="258.0" x2="121.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="258.0" x2="125.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="258.0" x2="128.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="258.0" x2="132.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="258.0" x2="136.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="258.0" x2="139.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="258.0" x2="143.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="258.0" x2="146.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="258.0" x2="150.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="258.0" x2="154.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="258.0" x2="157.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="258.0" x2="161.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="258.0" x2="164.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="258.0" x2="168.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="258.0" x2="172.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="258.0" x2="175.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="258.0" x2="179.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="258.0" x2="182.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="258.0" x2="186.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="258.0" x2="190.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="258.0" x2="193.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="258.0" x2="197.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="258.0" x2="200.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="258.0" x2="204.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="258.0" x2="208.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="258.0" x2="211.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="258.0" x2="215.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="258.0" x2="218.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="258.0" x2="222.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="258.0" x2="226.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="258.0" x2="229.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="258.0" x2="233.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="258.0" x2="236.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="258.0" x2="240.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="258.0" x2="244.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="258.0" x2="247.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="258.0" x2="251.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="258.0" x2="254.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="258.0" x2="258.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="258.0" x2="262.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="258.0" x2="265.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="258.0" x2="269.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="258.0" x2="272.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="258.0" x2="276.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="258.0" x2="280.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="258.0" x2="283.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="258.0" x2="287.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="258.0" x2="290.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="258.0" x2="294.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="258.0" x2="298.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="258.0" x2="301.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="258.0" x2="305.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="258.0" x2="308.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="258.0" x2="312.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="258.0" x2="316.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="258.0" x2="319.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="258.0" x2="323.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="258.0" x2="326.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="258.0" x2="330.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="258.0" x2="334.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="258.0" x2="337.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="258.0" x2="341.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="258.0" x2="344.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="258.0" x2="348.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="258.0" x2="352.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="258.0" x2="355.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="258.0" x2="359.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="258.0" x2="362.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="258.0" x2="366.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="258.0" x2="370.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="258.0" x2="373.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="258.0" x2="377.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="258.0" x2="380.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="258.0" x2="384.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="258.0" x2="388.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="258.0" x2="391.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="258.0" x2="395.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="258.0" x2="398.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="258.0" x2="402.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="258.0" x2="406.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="258.0" x2="409.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="258.0" x2="413.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="258.0" x2="416.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="258.0" x2="420.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="258.0" x2="424.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="258.0" x2="427.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="258.0" x2="431.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="258.0" x2="434.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="258.0" x2="438.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="258.0" x2="442.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="258.0" x2="445.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="258.0" x2="449.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="258.0" x2="452.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="258.0" x2="456.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="258.0" x2="460.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="250.0" x2="460.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><text x="161.2" y="38.0" font-size="9.5" fill="#10373E">AtoM</text><text x="197.2" y="38.0" font-size="9.5" fill="#10373E">2.10</text><text x="233.2" y="38.0" font-size="9.5" fill="#10373E">BASE</text><text x="269.2" y="38.0" font-size="9.5" fill="#10373E">(Symfony</text><text x="334.0" y="38.0" font-size="9.5" fill="#10373E">1.x)</text><text x="31.6" y="54.0" font-size="9.5" fill="#10373E">Routing</text><text x="89.2" y="54.0" font-size="9.5" fill="#10373E">·</text><text x="103.6" y="54.0" font-size="9.5" fill="#10373E">Templates</text><text x="175.6" y="54.0" font-size="9.5" fill="#10373E">·</text><text x="190.0" y="54.0" font-size="9.5" fill="#10373E">ACL</text><text x="218.8" y="54.0" font-size="9.5" fill="#10373E">·</text><text x="233.2" y="54.0" font-size="9.5" fill="#10373E">Propel</text><text x="283.6" y="54.0" font-size="9.5" fill="#10373E">ORM</text><text x="312.4" y="54.0" font-size="9.5" fill="#10373E">·</text><text x="326.8" y="54.0" font-size="9.5" fill="#10373E">sfPluginAdmin</text><text x="31.6" y="86.0" font-size="9.5" fill="#10373E">LAYER</text><text x="74.8" y="86.0" font-size="9.5" fill="#10373E">1:</text><text x="96.4" y="86.0" font-size="9.5" fill="#10373E">atom-framework</text><text x="204.4" y="86.0" font-size="9.5" fill="#10373E">v2.11.7</text><text x="262.0" y="86.0" font-size="9.5" fill="#10373E">(REQUIRED)</text><text x="60.4" y="102.0" font-size="9.5" fill="#10373E">Laravel</text><text x="118.0" y="102.0" font-size="9.5" fill="#10373E">Query</text><text x="161.2" y="102.0" font-size="9.5" fill="#10373E">Builder</text><text x="218.8" y="102.0" font-size="9.5" fill="#10373E">(Illuminate\Database\Capsule)</text><text x="60.4" y="118.0" font-size="9.5" fill="#10373E">Extension</text><text x="132.4" y="118.0" font-size="9.5" fill="#10373E">Manager</text><text x="190.0" y="118.0" font-size="9.5" fill="#10373E">(CLI</text><text x="240.4" y="118.0" font-size="9.5" fill="#10373E">Service)</text><text x="60.4" y="134.0" font-size="9.5" fill="#10373E">90</text><text x="89.2" y="134.0" font-size="9.5" fill="#10373E">Services</text><text x="60.4" y="150.0" font-size="9.5" fill="#10373E">RouteLoader</text><text x="161.2" y="150.0" font-size="9.5" fill="#10373E">RouteCollector</text><text x="60.4" y="166.0" font-size="9.5" fill="#10373E">Helper</text><text x="110.8" y="166.0" font-size="9.5" fill="#10373E">classes</text><text x="31.6" y="198.0" font-size="9.5" fill="#10373E">LAYER</text><text x="74.8" y="198.0" font-size="9.5" fill="#10373E">2:</text><text x="96.4" y="198.0" font-size="9.5" fill="#10373E">atom-ahg-plugins</text><text x="218.8" y="198.0" font-size="9.5" fill="#10373E">v3.21.17</text><text x="283.6" y="198.0" font-size="9.5" fill="#10373E">(80</text><text x="312.4" y="198.0" font-size="9.5" fill="#10373E">plugins)</text><text x="60.4" y="214.0" font-size="9.5" fill="#10373E">16</text><text x="82.0" y="214.0" font-size="9.5" fill="#10373E">locked</text><text x="132.4" y="214.0" font-size="9.5" fill="#10373E">core</text><text x="168.4" y="214.0" font-size="9.5" fill="#10373E">plugins</text><text x="60.4" y="230.0" font-size="9.5" fill="#10373E">6</text><text x="74.8" y="230.0" font-size="9.5" fill="#10373E">stable</text><text x="125.2" y="230.0" font-size="9.5" fill="#10373E">GLAM</text><text x="161.2" y="230.0" font-size="9.5" fill="#10373E">sector</text><text x="211.6" y="230.0" font-size="9.5" fill="#10373E">plugins</text><text x="60.4" y="246.0" font-size="9.5" fill="#10373E">58</text><text x="82.0" y="246.0" font-size="9.5" fill="#10373E">optional</text><text x="146.8" y="246.0" font-size="9.5" fill="#10373E">feature</text><text x="204.4" y="246.0" font-size="9.5" fill="#10373E">plugins</text></svg></div>

### Technology Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| PHP | 8.3 | Application runtime |
| MySQL | 8.0 | Database |
| Elasticsearch | 7.10 | Full-text search |
| Bootstrap 5 | 5.3 | Frontend framework |
| Nginx | 1.18+ | Web server |
| Cantaloupe | 5.0.6 | IIIF image server |
| Ollama | 0.17.7 | Local LLM runtime (LLaVA, Mistral) |
| Python 3 | 3.12 | AI services (NER, translation, summarization) |
| Node.js | 18+ | Webpack build |

### Server Infrastructure

| Server | IP | Role | GPU |
|--------|-----|------|-----|
| 112 | 192.168.0.112 | Web/App (AtoM instances) | None |
| 115 | 192.168.0.115 | AI/GPU Workhorse | NVIDIA RTX 3080 10GB |
| 92 | 192.168.0.92 | Future inference | NVIDIA RTX 3060 12GB |
| TrueNAS | /mnt/nas/heratio/ | Digital object storage | — |

---

## Complete Plugin Catalog (80 Plugins)

### Core & Theme (Locked)

| Plugin | Purpose |
|--------|---------|
| ahgCorePlugin | Framework integration bridge |
| ahgThemeB5Plugin | Bootstrap 5 theme with voice commands, WCAG AA, TTS |
| ahgSecurityClearancePlugin | Bell-LaPadula security classification |
| ahgDisplayPlugin | GLAM Browse with dynamic facets, 4 view modes |
| ahgUiOverridesPlugin | Viewer dispatch, UI helpers |
| ahgSettingsPlugin | 21-section settings management (200+ options) |

### GLAM Sectors (Stable)

| Plugin | Sector | Key Features |
|--------|--------|-------------|
| ahgLibraryPlugin | Library | MARC cataloguing, ISBN lookup, circulation, fines, patron management |
| ahgMuseumPlugin | Museum | CCO, Collections Procedures, Getty AAT (1,057 cached terms), condition assessment |
| ahgGalleryPlugin | Gallery | VRA Core, exhibitions, artist tracking, loans, valuations |
| ahgDAMPlugin | DAM | IPTC metadata extraction, watermarking, batch processing |

### Browse/Manage Plugins

| Plugin | Entity |
|--------|--------|
| ahgAccessionManagePlugin | Accessions with numbering, priority, intake workflow |
| ahgAccessRequestPlugin | Researcher access requests with triage |
| ahgActorManagePlugin | Authority records + autocomplete |
| ahgDonorManagePlugin | Donors |
| ahgRepositoryManagePlugin | Repositories |
| ahgRightsHolderManagePlugin | Rights holders |
| ahgStorageManagePlugin | Physical storage locations |
| ahgTermTaxonomyPlugin | Terms + taxonomies |
| ahgUserManagePlugin | User accounts |
| ahgJobsManagePlugin | Background jobs |
| ahgMenuManagePlugin | Navigation menus |
| ahgStaticPagePlugin | Static pages |
| ahgFunctionManagePlugin | ISDF functions |

### Descriptive Standard CRUD

| Plugin | Standard |
|--------|----------|
| ahgInformationObjectManagePlugin | ISAD(G) |
| ahgDacsManagePlugin | DACS |
| ahgDcManagePlugin | Dublin Core |
| ahgModsManagePlugin | MODS |
| ahgRadManagePlugin | RAD |

### AI & Automation

| Plugin | Features |
|--------|----------|
| ahgAIPlugin | NER (spaCy), Translation (Argos), Summarization, Spellcheck, Face Detection, LLM Description Suggestions |
| ahgDiscoveryPlugin | Natural language search, query expansion, 3-strategy search |
| ahgSemanticSearchPlugin | Thesaurus, WordNet/Wikidata sync, vector embeddings |
| ahgSearchPlugin | Global search, autocomplete, search/replace |
| ahgDedupePlugin | Duplicate detection with merge workflow |
| ahgTranslationPlugin | Machine translation (LibreTranslate) |

### Data Ingest & Import/Export

| Plugin | Features |
|--------|----------|
| ahgIngestPlugin | OAIS-aligned 6-step batch ingest wizard with 9 AI processing options |
| ahgDataMigrationPlugin | Field mapping between GLAM sectors |
| ahgExportPlugin | CSV, EAD, bulk export |
| ahgMetadataExportPlugin | GLAM metadata export (JSON-LD, Schema.org, RIC-O, BIBFRAME) |
| ahgPortableExportPlugin | Standalone offline catalogue viewer (CD/USB/ZIP) |
| ahgLabelPlugin | Label generation with barcodes |
| ahgFormsPlugin | Configurable metadata entry forms per repository |
| ahgMetadataExtractionPlugin | EXIF, IPTC, XMP extraction from digital objects |

### Compliance & Regulatory

| Plugin | Jurisdiction | Standard |
|--------|-------------|----------|
| ahgPrivacyPlugin | Multi (7) | POPIA, GDPR, CCPA, PIPEDA, NDPA, DPA, UK GDPR |
| ahgCDPAPlugin | Zimbabwe | Cyber & Data Protection Act |
| ahgNAZPlugin | Zimbabwe | National Archives Act (25-year rule) |
| ahgNMMZPlugin | Zimbabwe | National Museums & Monuments Act |
| ahgAuditTrailPlugin | Universal | Full audit logging |
| ahgExtendedRightsPlugin | Multi | RightsStatements.org, TK Labels, embargo enforcement |
| ahgICIPPlugin | Indigenous | Indigenous Cultural & Intellectual Property |

### Heritage Accounting & Finance

| Plugin | Standard |
|--------|----------|
| ahgHeritageAccountingPlugin | GRAP 103 / IPSAS 45 |
| ahgIPSASPlugin | International Public Sector Accounting |
| ahgSpectrumPlugin | Collections Procedures |

### Digital Preservation

| Plugin | Features |
|--------|----------|
| ahgPreservationPlugin | Checksums, fixity, PREMIS events, format registry, PRONOM sync, migration pathways |
| ahgBackupPlugin | Full/incremental/scheduled backups, restore, email notifications |
| ahgTiffPdfMergePlugin | TIFF and PDF merge jobs |

### Rights Management

| Plugin | Features |
|--------|----------|
| ahgRightsPlugin | PREMIS rights, Creative Commons |
| ahgExtendedRightsPlugin | Embargo (4 types: full, metadata_only, digital_only, partial), TK Labels |
| ahgICIPPlugin | Indigenous Cultural & Intellectual Property |

### Research & Public Access

| Plugin | Features |
|--------|----------|
| ahgResearchPlugin | Reading room booking, researcher registration, workspace, custody chain |
| ahgRequestToPublishPlugin | Publication requests for archival images |
| ahgCartPlugin | Shopping cart for reproduction requests |
| ahgFavoritesPlugin | User bookmarks |
| ahgFeedbackPlugin | User feedback management |

### Collection Management

| Plugin | Features |
|--------|----------|
| ahgConditionPlugin | Condition assessment with AI (LLaVA), photo annotation, Collections Procedures |
| ahgProvenancePlugin | Chain of custody tracking |
| ahgDonorAgreementPlugin | Donor/institution agreements (SA compliance) |
| ahgLoanPlugin | Shared loan management |
| ahgVendorPlugin | Vendor/supplier management |
| ahgContactPlugin | Extended contact information |

### Exhibitions & Public Engagement

| Plugin | Features |
|--------|----------|
| ahgExhibitionPlugin | Exhibition management, storylines, media, loans |
| ahgLandingPagePlugin | Drag-drop visual landing page builder |
| ahgHeritagePlugin | Heritage discovery platform, contributor system |

### Integration & API

| Plugin | Features |
|--------|----------|
| ahgIiifPlugin | IIIF manifests, viewer, collections, OCR, Auth API 1.0 |
| ahg3DModelPlugin | 3D viewing, Google Model Viewer, AR, hotspots |
| ahgRicExplorerPlugin | Records in Context (RiC), Fuseki SPARQL triplestore |
| ahgGraphQLPlugin | GraphQL API endpoint |
| ahgAPIPlugin | REST API, webhooks |
| ahgDoiPlugin | DOI minting via DataCite |
| ahgFederationPlugin | OAI-PMH federated search |

### Reporting & Admin

| Plugin | Features |
|--------|----------|
| ahgCustomFieldsPlugin | Admin-configurable EAV custom fields (7 types, 6 entity types) |
| ahgReportsPlugin | Reporting dashboard |
| ahgReportBuilderPlugin | Enterprise report builder (Quill.js, Word/PDF/XLSX export, templates, scheduling) |
| ahgStatisticsPlugin | Usage statistics |
| ahgWorkflowPlugin | Configurable approval workflows |
| ahgAuthorityPlugin | Authority enhancement: Wikidata, VIAF, ULAN, LCNAF, ISNI linking, completeness scoring, merge/dedup |

---

## Key Features Delivered (2026)

### WCAG 2.1 Level AA Accessibility (March 2026)
- Global ARIA landmarks, live regions, focus management on every page
- Auto table scoping, form validation ARIA, keyboard navigation
- Colour contrast AA, prefers-reduced-motion, forced-colors
- Automated axe-core testing (10 Playwright tests)
- Built-in accessibility statement page

### Voice Command System
- 100+ commands in 11 languages (English, Afrikaans, Zulu, Xhosa, Sesotho, French, Portuguese, Spanish, German, Dutch)
- Navigation, search, dictation, AI image description, PDF reading
- Enable/disable toggle, continuous listening, hover-read TTS
- Right-click type input for manual command entry

### AI Services (Local — No Cloud Required)
- **NER** — Named entity extraction (spaCy, server 115)
- **Translation** — Offline via Argos Translate (10 languages)
- **Summarization** — BART-based seq2seq (server 115)
- **Spellcheck** — aspell CLI
- **Image Description** — LLaVA:7b via Ollama (server 115 GPU, 0.2s/image)
- **Condition Assessment** — AI damage detection with Collections Procedures vocabulary (15 damage types)
- **LLM Suggestions** — Description generation via Ollama/Anthropic Claude
- **Face Detection** — OpenCV local, AWS/Azure cloud options

### Smart Media Handling
- PDF detection with OCR transcript reading
- Video/audio detection with transcript playback
- TIFF deep zoom via IIIF/Cantaloupe
- 3D model viewing with AR support

### Backup Strategy
- Full, incremental, and scheduled backups
- Hourly/daily/weekly/monthly scheduling with admin UI
- Per-schedule retention policies
- Email notifications on success/failure
- CLI: `php symfony backup:run-scheduled`

### Embargo Enforcement
- 4 embargo types: full, metadata_only, digital_only, partial
- Browse/search filtering (embargoed records hidden from public)
- User/group/IP range exceptions
- Auto-lift on expiry with notifications

### Wikidata/VIAF Authority Linking
- 5 external sources: Wikidata, VIAF, Getty ULAN, LCNAF, ISNI
- Live API search and auto-linking
- EAC-CPF export enrichment
- Completeness scoring and dedup pipeline

### Queue Engine
- Background job queue with dispatch, chain, batch, retry
- 5 CLI commands, admin UI, systemd workers
- Rate limiting, exponential backoff

### Custom Fields (EAV)
- Admin-configurable per entity type (7 field types, 6 entity types)
- Repeatable fields, validation, import/export

---

## Open Issues (9)

| # | Issue | Status | Priority |
|---|-------|--------|----------|
| 220 | IIIF AI Extract | Parked | P2 |
| 168 | HTR Vital Records POC | Parked (separate dev) | P2 |
| 124 | Scan + Active Directory | Parked | P3 |
| 77 | Preservica Converter | Future | P3 |
| 72 | Auto-update cron | Ready (script built, needs deploy) | P2 |
| 47 | Mobile PWA | Future | P3 |
| 42 | Archivematica Integration | Future | P3 |
| 30 | SAML/SSO | Future | P3 |
| 29 | LDAP Integration | Future | P3 |

**218 issues closed.**

---

## Roadmap

### Near Term (Q2 2026)
- SAMAB 2026 paper submission (deadline: 30 May 2026)
- HTR vital records pipeline (in progress on 115)
- LLaVA fine-tuning for conservation (training data export, LoRA on 115)
- Auto-update deployment to client servers (#72)

### Medium Term (Q3-Q4 2026)
- Full Laravel AtoM Heratio (replace Symfony entirely)
- IIIF AI extraction pipeline (#220)
- Mobile PWA wrapper (#47)
- SAML/SSO authentication (#30)

### Long Term (2027+)
- Archivematica integration (#42)
- LDAP/Active Directory (#29, #124)
- Preservica migration tool (#77)
- Multi-tenant SaaS offering

---

## Documentation

| Document | Type | Location |
|----------|------|----------|
| User Manual | .md + .docx | atom-extensions-catalog/docs/ |
| Admin Manual | .md + .docx | atom-extensions-catalog/docs/ |
| Technical Manual | .md + .docx | atom-extensions-catalog/docs/ |
| LLaVA Fine-Tuning Guide | .md + .docx | atom-extensions-catalog/docs/technical/ |
| AI Condition Assessment | .md + .docx | atom-extensions-catalog/docs/ |
| Accessibility Feature Overview | .md + .docx | atom-extensions-catalog/docs/ |
| Accessibility Statement | .md + .docx | atom-extensions-catalog/docs/ |
| Backup Strategy Feature Overview | .md + .docx | atom-extensions-catalog/docs/ |
| Database ERD | .md | atom-extensions-catalog/docs/technical/ |
| SAMAB 2026 Paper | .md + .doc | atom-extensions-catalog/docs/samab/ |
| Help Center | 201 articles | https://psis.theahg.co.za/index.php/help |
| Docs Site | MkDocs | https://docs.theahg.co.za |

---

## Instances

| Instance | URL | Database | Purpose |
|----------|-----|----------|---------|
| PSIS | https://psis.theahg.co.za | archive | Primary development/demo |
| ANC | https://atom.theahg.co.za | atom | African National Congress archives |
| KM | https://km.theahg.co.za | — | AI Knowledge Management Q&A |
| Registry | https://registry.theahg.co.za | — | Plugin registry site |
| Docs | https://docs.theahg.co.za | — | MkDocs documentation |
| AI Gateway | https://ai.theahg.co.za | — | AI service admin |

---

## GitHub Repositories

| Repository | Purpose |
|------------|---------|
| ArchiveHeritageGroup/atom-framework | Core Laravel foundation, CLI tools, services |
| ArchiveHeritageGroup/atom-ahg-plugins | All 80 AHG plugins |
| ArchiveHeritageGroup/atom-extensions-catalog | Documentation, issues, registry |

---

*The Archive and Heritage Group (Pty) Ltd — Johan Pieterse*
*AtoM Heratio Framework v2.11.7 / Plugins v3.21.17*
