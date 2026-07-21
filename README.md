<div align="center">

# 🏛️ AtoM Extensions

**Extending Access to Memory for Modern Archives**

[![AtoM Version](https://img.shields.io/badge/AtoM-2.8.x--2.10.x-blue.svg)](https://www.accesstomemory.org/)
[![PHP Version](https://img.shields.io/badge/PHP-8.3-purple.svg)](https://php.net/)
[![License](https://img.shields.io/badge/License-GPL--3.0-green.svg)](LICENSE)
[![Extensions](https://img.shields.io/badge/Extensions-79-orange.svg)](#-available-extensions)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952b3.svg)](https://getbootstrap.com/)
[![Laravel](https://img.shields.io/badge/Laravel-Query%20Builder-red.svg)](https://laravel.com/)

**The most comprehensive extension suite for AtoM archival software**

[Installation](#-installation) • [Feature Comparison](#-feature-comparison) • [Extensions](#-available-extensions) • [Compliance](#-compliance-support) • [Documentation](#-documentation)

---

**Built by [The Archive And Heritage Digital Commons Group](https://theahg.co.za)**

</div>

---

## 🎯 What is AtoM?

**AtoM (Access to Memory)** is an open-source, web-based archival description application developed by Artefactual Systems. It's trusted by national archives, universities, and cultural institutions worldwide.

---

## 📊 Feature Comparison

### Base AtoM Features (Native)

| Feature | Description | Status |
|---------|-------------|:------:|
| **Archival Description** | | |
| ISAD(G) Templates | International Standard Archival Description | ✅ |
| RAD Templates | Rules for Archival Description (Canadian) | ✅ |
| DACS Templates | Describing Archives: A Content Standard (US) | ✅ |
| Dublin Core Templates | Simple metadata standard | ✅ |
| MODS Templates | Metadata Object Description Schema | ✅ |
| Multi-level Descriptions | Fonds → Series → Files → Items | ✅ |
| Hierarchical Browse | Tree-view navigation | ✅ |
| | | |
| **Authority Records** | | |
| ISAAR(CPF) | Corporate bodies, Persons, Families | ✅ |
| Actor Relations | Relationships between authorities | ✅ |
| Maintenance History | Track changes to authorities | ✅ |
| | | |
| **Archival Institutions** | | |
| ISDIAH | Repository descriptions | ✅ |
| Contact Information | Address, phone, email, hours | ✅ |
| Holdings Statistics | Collection counts | ✅ |
| | | |
| **Functions** | | |
| ISDF | Functions/activities descriptions | ✅ |
| Function Relations | Link functions to records | ✅ |
| | | |
| **Access Points** | | |
| Subject Terms | Controlled vocabulary subjects | ✅ |
| Place Terms | Geographic access points | ✅ |
| Name Access Points | Link to authority records | ✅ |
| Genre Terms | Material types | ✅ |
| | | |
| **Digital Objects** | | |
| File Upload | Images, PDFs, audio, video | ✅ |
| Thumbnail Generation | Automatic derivatives | ✅ |
| Compound Objects | Multi-page documents | ✅ |
| External Links | URI references | ✅ |
| | | |
| **Import/Export** | | |
| CSV Import | Bulk data loading | ✅ |
| EAD 2002 Import/Export | Encoded Archival Description | ✅ |
| EAD3 Export | Latest EAD version | ✅ |
| Dublin Core Export | Simple XML | ✅ |
| MODS Export | Library metadata | ✅ |
| SKOS Export | Taxonomy terms | ✅ |
| Clipboard Export | Select and export | ✅ |
| | | |
| **Search & Discovery** | | |
| Elasticsearch | Full-text search | ✅ |
| Faceted Search | Filter by repository, date, subject | ✅ |
| Advanced Search | Boolean operators | ✅ |
| Browse by Repository | Institution grouping | ✅ |
| | | |
| **User Management** | | |
| User Accounts | Login/registration | ✅ |
| User Groups | Role-based permissions | ✅ |
| LDAP Integration | Enterprise authentication | ✅ |
| Two-Factor Auth | OTP security | ✅ |
| | | |
| **Administration** | | |
| Taxonomy Management | Edit controlled vocabularies | ✅ |
| Static Pages | Custom content pages | ✅ |
| Theming | Customize appearance | ✅ |
| Multi-language | Interface translation | ✅ |
| OAI-PMH | Harvesting protocol | ✅ |
| Accessions | Acquisition records | ✅ |
| Deaccessions | Disposal records | ✅ |
| Physical Storage | Location tracking | ✅ |
| Jobs | Background processing | ✅ |

---

### AtoM Extensions Adds

| Feature | Base AtoM | + Extensions |
|---------|:---------:|:------------:|
| **User Interface** | | |
| Modern Bootstrap 5 UI | ❌ | ✅ |
| Responsive Mobile Design | Partial | ✅ Full |
| Dark Mode Support | ❌ | ✅ |
| Drag-and-Drop Landing Pages | ❌ | ✅ |
| Display Profile System | ❌ | ✅ |
| | | |
| **Architecture** | | |
| Laravel Query Builder | ❌ | ✅ |
| Extension Manager CLI | ❌ | ✅ |
| Database-driven Plugin System | ❌ | ✅ |
| PHP 8.3 Optimized | Partial | ✅ Full |
| | | |
| **Security & Compliance** | | |
| Security Classification (5 levels) | ❌ | ✅ |
| GDPR Compliance Tools | ❌ | ✅ |
| POPIA Compliance Tools | ❌ | ✅ |
| CCPA Compliance Tools | ❌ | ✅ |
| PIPEDA Compliance Tools | ❌ | ✅ |
| LGPD Compliance Tools | ❌ | ✅ |
| PAIA Request Management | ❌ | ✅ |
| DSAR Management | ❌ | ✅ |
| Data Breach Register | ❌ | ✅ |
| Consent Management | ❌ | ✅ |
| Comprehensive Audit Trail | ❌ | ✅ |
| | | |
| **GLAM Sector Support** | | |
| Archives (ISAD/EAD) | ✅ | ✅ Enhanced |
| Libraries (RDA/MARC) | Partial | ✅ Full |
| Museums (Collections Procedures) | ❌ | ✅ |
| Museums (CCO) | ❌ | ✅ |
| Galleries (CCO/CDWA) | ❌ | ✅ |
| Digital Asset Management | ❌ | ✅ |
| Unified GLAM Browse | ❌ | ✅ |
| | | |
| **Heritage & Finance** | | |
| GRAP 103 Heritage Accounting | ❌ | ✅ |
| IPSAS 17 (International) | ❌ | ✅ |
| FRS 102 (UK) | ❌ | ✅ |
| GASB 34 (USA) | ❌ | ✅ |
| FASAB (USA Federal) | ❌ | ✅ |
| AASB 116 (Australia) | ❌ | ✅ |
| PSAB/PS 3150 (Canada) | ❌ | ✅ |
| Asset Valuation & Depreciation | ❌ | ✅ |
| Insurance Management | ❌ | ✅ |
| 10 Accounting Standards | ❌ | ✅ |
| | | |
| **Research & Access** | | |
| Research Portal | ❌ | ✅ |
| Researcher Workspace | ❌ | ✅ |
| Reading Room Booking | ❌ | ✅ |
| Access Request Workflow | ❌ | ✅ |
| Embargo Management | ❌ | ✅ |
| | | |
| **Collection Management** | | |
| Donor Agreement Tracking | ❌ | ✅ |
| Donor Reminders | ❌ | ✅ |
| Condition Assessment | ❌ | ✅ |
| Conservation Tracking | ❌ | ✅ |
| Condition Annotator | ❌ | ✅ |
| Provenance Research | ❌ | ✅ |
| Vendor/Supplier Management | ❌ | ✅ |
| | | |
| **Advanced Features** | | |
| IIIF Deep Zoom Viewer | ❌ | ✅ |
| 3D Model Viewer | ❌ | ✅ |
| 3D Thumbnail Generation | ❌ | ✅ |
| Records in Contexts (RiC) | ❌ | ✅ |
| Graph Visualization | ❌ | ✅ |
| AI Entity Extraction (NER) | ❌ | ✅ |
| Automated Backups | ❌ | ✅ |
| TIFF to PDF/A Merge | ❌ | ✅ |
| Metadata Extraction (EXIF/IPTC/XMP) | ❌ | ✅ |

---

### Why Both Together?

**AtoM** = Rock-solid archival foundation trusted by national archives, universities, and cultural institutions worldwide.

**AtoM Extensions** = Enterprise features, multi-sector support, regulatory compliance, modern UI, and AI capabilities.

---

## 📊 Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                     AtoM 2.10 BASE (Symfony 1.x)                │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 1: atom-framework (REQUIRED)                             │
│  ├── Laravel Query Builder (Illuminate\Database)                │
│  ├── Extension Manager CLI                                      │
│  ├── Base Repository/Service Classes                            │
│  └── Helper Utilities                                           │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: atom-ahg-plugins (79 plugins)                         │
│  ├── ahgThemeB5Plugin (Required - Locked)                       │
│  ├── ahgSecurityClearancePlugin (Required - Locked)             │
│  └── [34 Optional Plugins...]                                   │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: SDKs & AI Services (Optional)                         │
│  ├── atom-ahg-python - Python SDK for AtoM API                  │
│  ├── atom-client-js - TypeScript SDK for AtoM API               │
│  └── Provenance AI - Entity extraction service                  │
└─────────────────────────────────────────────────────────────────┘
```

### Repository Structure

| Repository | Purpose | Type |
|------------|---------|------|
| [atom-framework](https://github.com/ArchiveHeritageGroup/atom-framework) | Core Laravel foundation, CLI, services | Required |
| [atom-ahg-plugins](https://github.com/ArchiveHeritageGroup/atom-ahg-plugins) | All 79 AHG plugins | Plugin Collection |
| [atom-ahg-python](https://github.com/ArchiveHeritageGroup/atom-ahg-python) | Python SDK for API integration | SDK |
| [atom-client-js](https://github.com/ArchiveHeritageGroup/atom-client-js) | TypeScript/JavaScript SDK | SDK |
| [atom-extensions-catalog](https://github.com/ArchiveHeritageGroup/atom-extensions-catalog) | Documentation & plugin registry | Catalog |

> **Note:** This catalog repository contains documentation and the plugin registry manifest (`catalog.json`).
> All code lives in the respective repositories above.

---

## ⚡ Installation

### Quick Install (APT Repository)

The easiest way to install on Ubuntu 22.04+ / Debian 12+:

```bash
# Add the APT repository (one-time setup)
curl -fsSL https://archiveheritagegroup.github.io/atom-framework/gpg.key \
  | sudo gpg --dearmor -o /usr/share/keyrings/atom-heratio.gpg

echo "deb [signed-by=/usr/share/keyrings/atom-heratio.gpg] https://archiveheritagegroup.github.io/atom-framework stable main" \
  | sudo tee /etc/apt/sources.list.d/atom-heratio.list

sudo apt update

# Install AtoM Heratio (recommended)
sudo apt install atom-heratio

# Or install vanilla AtoM 2.10.1 (no Heratio)
sudo apt install atom
```

The installer launches an **interactive TUI wizard** that configures your database, web server, SSL, Elasticsearch, and admin account automatically.

### Quick Install (One-Liner)

```bash
curl -fsSL https://archiveheritagegroup.github.io/atom-framework/install.sh | sudo bash
sudo apt install atom-heratio
```

### Direct Download (DEB Packages)

Download from [GitHub Releases](https://github.com/ArchiveHeritageGroup/atom-framework/releases) or the [download page](https://archiveheritagegroup.github.io/atom-framework/):

| Package | Description | Size |
|---------|-------------|------|
| **[atom-heratio.deb](https://github.com/ArchiveHeritageGroup/atom-framework/releases/latest)** | AtoM 2.10 + Heratio framework + 79 plugins | ~45 MB |
| **[atom.deb](https://github.com/ArchiveHeritageGroup/atom-framework/releases/latest)** | Vanilla AtoM 2.10.1 with guided TUI wizard | ~25 MB |

Both packages include bundled tarballs for **air-gapped / offline installations** (no internet required during install).

```bash
# Download and install directly
wget https://github.com/ArchiveHeritageGroup/atom-framework/releases/latest/download/atom-heratio_2.10.20-1_all.deb
sudo apt install ./atom-heratio_2.10.20-1_all.deb
```

### What Happens When You Install

1. **TUI Wizard** launches in your terminal (via debconf) asking:
   - Installation mode (complete / atom-only / heratio-only)
   - Installation path, database credentials, site title
   - SSL configuration (none / self-signed / Let's Encrypt)
   - Elasticsearch install (optional)
   - Web wizard enable (for browser-based plugin configuration)

2. **Automated Setup** runs after answering:
   - Extracts bundled AtoM 2.10 tarball
   - Installs Heratio framework + 79 plugins
   - Configures MySQL database, Nginx, PHP-FPM, systemd worker
   - Sets file permissions, clears caches
   - Runs initial database migration

3. **Web Wizard** starts on port 9090 (if enabled) for advanced configuration:
   - System status dashboard
   - Plugin selection by category
   - GLAM sector configuration
   - AI & automation settings
   - Compliance module setup
   - Digital preservation settings

#### AtoM Heratio - Installation Modes

| Mode | Description |
|------|-------------|
| **complete** | Fresh AtoM 2.10 + Heratio framework + all plugins (recommended) |
| **atom-only** | Vanilla AtoM 2.10 only (no Heratio) |
| **heratio-only** | Overlay Heratio onto existing AtoM >= 2.8 |

#### AtoM Heratio - CLI Management Tool

After install, use the `atom-heratio` command:

```bash
atom-heratio status              # Show status + service health
atom-heratio plugins             # List available plugins
atom-heratio enable <plugin>     # Enable a plugin
atom-heratio disable <plugin>    # Disable a plugin
atom-heratio wizard start        # Launch web configuration wizard
atom-heratio wizard stop         # Stop web wizard
atom-heratio reconfigure         # Re-run TUI wizard
atom-heratio version             # Show version info
atom-heratio upgrade             # Pull latest updates
```

#### Reconfigure / Upgrade

```bash
# Re-run the TUI wizard to change settings
sudo dpkg-reconfigure atom-heratio

# Upgrade to latest version (if using APT repository)
sudo apt update && sudo apt upgrade atom-heratio
```

#### Building Packages from Source

```bash
cd atom-framework/packaging

# Build AtoM Heratio package
bash build.sh                    # With bundled AtoM tarball (~45 MB)
bash build.sh --no-tarball       # Without tarball (~21 MB)

# Build vanilla AtoM package
cd atom-vanilla
bash build.sh                    # => dist/atom_2.10.1-1_all.deb (~25 MB)

# Publish to all channels (GitHub Releases + APT repo + download page)
cd ..
bash publish-all.sh
```

---

### Git Clone (Manual Install)

For development or custom deployments:

---

### Prerequisites

#### Core (Required)

| Component | Minimum | Recommended | Purpose |
|-----------|---------|-------------|---------|
| **AtoM** | 2.8.0 | 2.10.x | Base archival software |
| **PHP** | 8.1 | 8.3 | Runtime (with extensions: mysql, xml, mbstring, curl, gd, zip, intl, xsl, opcache, apcu) |
| **MySQL** | 8.0 | 8.0+ | Database |
| **Elasticsearch** | 5.x | 6.x / 8.x | Search engine (or OpenSearch) |
| **Nginx** | 1.18+ | latest | Web server |
| **Gearman** | 1.1+ | latest | Job server for background tasks |
| **Composer** | 2.x | latest | PHP dependency manager |
| **Node.js** | 16.x | LTS (20.x+) | Asset building |
| **Git** | 2.x | latest | Version control |
| **Python** | 3.10 | 3.12 | AI features, scripting |

#### Media Processing (Required)

| Component | Purpose |
|-----------|---------|
| **ImageMagick** | Image processing, thumbnail generation |
| **FFmpeg** | Audio/video processing, derivatives |
| **Ghostscript** | PDF rendering, conversion |
| **Poppler-utils** | PDF text extraction (pdftotext) |

#### AI & Processing (Optional — needed by AI plugins)

| Component | Purpose | Used By |
|-----------|---------|---------|
| **Tesseract OCR** | Optical character recognition | ahgAIPlugin, ahgIngestPlugin |
| **GNU Aspell** | Spell checking | ahgAIPlugin |
| **PyMuPDF** (pip) | PDF redaction, manipulation | ahgPrivacyPlugin |
| **spaCy** (pip) | Named Entity Recognition | ahgAIPlugin |
| **Argos Translate** (pip) | Offline machine translation | ahgAIPlugin, ahgTranslationPlugin |
| **Pillow** (pip) | Image processing | ahgAIPlugin |
| **OpenCV** (pip) | Face detection, image analysis | ahgAIPlugin |

#### Digital Preservation (Optional — needed by preservation plugins)

| Component | Purpose | Used By |
|-----------|---------|---------|
| **Siegfried** | Format identification (PRONOM) | ahgPreservationPlugin |
| **ClamAV** | Virus scanning | ahgPreservationPlugin, ahgIngestPlugin |
| **BagIt** (pip) | Archival packaging | ahgPreservationPlugin |

#### 3D Processing (Optional — needed by 3D plugin)

| Component | Purpose |
|-----------|---------|
| **Blender** | 3D rendering, thumbnail generation |
| **MeshLab** | 3D mesh processing, conversion |

#### Optional Services

| Component | Purpose |
|-----------|---------|
| **Redis** | Caching (recommended for production) |
| **Memcached** | Caching (alternative to Redis) |
| **Cantaloupe** | IIIF image tile server |
| **Ollama** | Local LLM for AI suggestions |

📖 **[See INSTALLATION.md for complete step-by-step instructions →](INSTALLATION.md)**

---

### Git Clone
```bash
cd /path/to/your/atom

# 1. Clone repositories
git clone https://github.com/ArchiveHeritageGroup/atom-framework.git
git clone https://github.com/ArchiveHeritageGroup/atom-ahg-plugins.git

# 2. Install system dependencies (requires sudo)
sudo bash atom-framework/bin/install-deps          # Required only
sudo bash atom-framework/bin/install-deps --all    # Required + optional (AI, preservation, 3D)

# 3. Install PHP dependencies
cd atom-framework && composer install && cd ..

# 4. Check all dependencies are satisfied
bash atom-framework/bin/check-dependencies

# 5. Install framework (DB tables, symlinks, plugins)
bash atom-framework/bin/install

# 6. Restart and verify
sudo systemctl restart php8.3-fpm
php bin/atom framework:version
php bin/atom extension:discover
```

> **Selective install:** You can install optional dependency groups individually:
> ```bash
> sudo bash atom-framework/bin/install-deps --ai         # AI/NLP: spaCy, PyMuPDF, Tesseract, etc.
> sudo bash atom-framework/bin/install-deps --preserve   # Siegfried, ClamAV, BagIt
> sudo bash atom-framework/bin/install-deps --3d         # Blender, MeshLab
> ```

---

## 📦 Available Extensions

### Required (Core - Locked) 

| Extension | Description |
|-----------|-------------|
| **ahgThemeB5Plugin** | Bootstrap 5 responsive theme |
| **ahgSecurityClearancePlugin** | Security classification (Public to Top Secret) |

### GLAM Sector Plugins

| Extension | Description | Standards |
|-----------|-------------|-----------|
| **ahgLibraryPlugin** | Library cataloging | RDA, MARC21 |
| **ahgMuseumPlugin** | Museum cataloging | CCO, Collections Procedures |
| **arGalleryPlugin** | Visual arts/gallery | CCO, CDWA |
| **ahgDAMPlugin** | Digital Asset Management | Dublin Core, IPTC |

### Research & Access

| Extension | Description |
|-----------|-------------|
| **ahgResearchPlugin** | Researcher portal, workspace, reading room booking |
| **ahgAccessRequestPlugin** | Access request workflow management |

### Compliance & Governance

| Extension | Description |
|-----------|-------------|
| **ahgPrivacyPlugin** | Multi-jurisdiction privacy (GDPR, POPIA, CCPA, PIPEDA, LGPD) |
| **ahgHeritageAccountingPlugin** | Heritage asset accounting (10 standards) |
| **ahgExtendedRightsPlugin** | Rights statements & embargo management |

### Utilities

| Extension | Description |
|-----------|-------------|
| **ahgBackupPlugin** | Automated backup & restore |
| **ahgAuditTrailPlugin** | Comprehensive audit logging |
| **ahgDisplayPlugin** | Display profiles & viewing modes |
| **ahgDonorAgreementPlugin** | Donor agreements with reminders |
| **ahgVendorPlugin** | Vendor/supplier management |
| **ahgConditionPlugin** | Condition assessment & conservation |
| **ahgLandingPagePlugin** | Drag-and-drop landing page builder |

### AI & Advanced Features

| Extension | Description |
|-----------|-------------|
| **ahgNerPlugin** | Named Entity Recognition (Python/spaCy) |
| **ahgSemanticSearchPlugin** | Semantic search, thesaurus, WordNet/Wikidata sync, embeddings |
| **ahgMetadataExtractionPlugin** | EXIF/IPTC/XMP metadata extraction |
| **ahg3DModelPlugin** | 3D model viewer & thumbnails |
| **IiifViewerFramework** | IIIF deep zoom image viewer |
| **ahgRicExplorerPlugin** | Records in Contexts graph viewer |

### API & Integration

| Extension | Description |
|-----------|-------------|
| **ahgAPIPlugin** | Extended REST API endpoints |
| **ahgMigrationPlugin** | Data migration tools |
| **ahgReportBuilderPlugin** | Custom report generation |
| **ahgLoanPlugin** | Object loan management |

---

## 🌍 Compliance Support

### Privacy Regulations

| Jurisdiction | Regulation | Status |
|--------------|------------|--------|
| 🇿🇦 South Africa | POPIA, PAIA, NARSSA | ✅ Full |
| 🇪🇺 European Union | GDPR | ✅ Full |
| 🇺🇸 California | CCPA | ✅ Full |
| 🇨🇦 Canada | PIPEDA | ✅ Full |
| 🇧🇷 Brazil | LGPD | ✅ Full |
| 🇳🇬 Nigeria | NDPA | ✅ Full |
| 🇰🇪 Kenya | DPA | ✅ Full |

### Heritage Accounting Standards

| Standard | Region |
|----------|--------|
| **GRAP 103** | South Africa |
| **IPSAS 17** | International |
| **FRS 102** | United Kingdom |
| **FASAB** | USA Federal |
| **GASB 34** | USA State/Local |
| **AASB 116** | Australia |
| **PSAB/PS 3150** | Canada |
| **NZ PBE IPSAS 17** | New Zealand |
| **mGAAP** | Germany |
| **Custom** | Configurable |

---

## 🔧 CLI Reference
```bash
# Extension Management
php bin/atom extension:discover          # List available
php bin/atom extension:enable <name>     # Enable
php bin/atom extension:disable <name>    # Disable

# Framework Management
php bin/atom framework:version           # Version
php bin/atom update                      # Update
php bin/atom migrate run                 # Migrations

# Maintenance
php bin/atom backup:create               # Backup
php bin/atom cc                          # Clear cache
php bin/atom help                        # Help
```

---

## 🤖 Provenance AI

AI-powered entity extraction for archivists:

- **People** - Names, roles, relationships
- **Places** - Locations, coordinates
- **Organizations** - Companies, institutions
- **Dates** - Events, periods

[Learn more →](https://theahg.co.za/provenance-ai)

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| **[INSTALLATION.md](INSTALLATION.md)** | Complete installation guide (7 methods) |
| **[catalog.json](catalog.json)** | Plugin registry manifest (machine-readable) |
| [docs/](docs/) | User guides for each plugin |
| [docs/technical/](docs/technical/) | Technical documentation |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

---

## 🏢 About

Developed by **The Archive And Heritage Digital Commons Group**

| | |
|---|---|
| 🌐 Website | [theahg.co.za](https://theahg.co.za) |
| 📧 Email | [info@theahg.co.za](mailto:info@theahg.co.za) |
| 🐙 GitHub | [ArchiveHeritageGroup](https://github.com/ArchiveHeritageGroup) |
| 📦 Releases | [Download](https://github.com/ArchiveHeritageGroup/atom-framework/releases) |

---

## 📄 License

GPL-3.0 - see [LICENSE](LICENSE) for details.

---

<div align="center">

**Made with ❤️ for the archival community**

[![Powered by AtoM](https://img.shields.io/badge/Powered%20by-AtoM-blue.svg)](https://www.accesstomemory.org/)
[![by TAHDCG](https://img.shields.io/badge/by-TAHDCG-green.svg)](https://theahg.co.za)

</div>
