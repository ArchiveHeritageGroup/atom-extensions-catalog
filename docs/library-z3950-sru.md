# Z39.50 / SRU Integration

## Overview

The library module can harvest bibliographic records from external Z39.50 servers
and expose its own catalog via the SRU (Search/Retrieve via URL) HTTP protocol.

- **Z39.50 Client** — query remote Z39.50 targets and import results into the catalog
- **SRU Server** — allow other systems to search the Heratio library via CQL over HTTP

---

## Z39.50 Client

### Adding a Target

Go to **GLAM/DAM** → **Library** → **Z39.50 Targets** → **Add Target**.

| Field | Description |
|-------|-------------|
| Name | Human-readable label (e.g. "Library of Congress") |
| Host | Z39.50 hostname or SRU base URL |
| Port | Default: 210 for Z39.50; 80/443 for SRU-over-HTTP |
| Database | Target database name |
| Record Syntax | MARC-21 (default), USMARC, or MARCXML |
| Timeout | Connection timeout in seconds (default: 15) |
| Username / Password | Optional authentication |

### Testing a Target

Click **Test** on the target row or within the edit form. The system will:

1. Attempt to connect (Z39.50 via YAZ extension, or HTTP SRU fallback)
2. Run a sample query
3. Report the number of hits and response time

> **Note:** If the YAZ PHP extension is not installed, the Z39.50 client falls back
> to HTTP SRU (Z39.50-over-HTTP / WC3) where supported.

### Installing YAZ

```bash
# Ubuntu / Debian:
sudo apt install php-yaz
sudo systemctl restart php-fpm   # or: apache2ctl restart
```

Verify installation:
```bash
php -m | grep yaz
```

### Supported Query Syntax

| Qualifier | Index | Example |
|-----------|-------|---------|
| `ti:` | Title | `ti=warcraft` |
| `au:` | Author | `au=blizzard` |
| `su:` | Subject | `su=fantasy` |
| `ib:` | ISBN/ISSN | `ib=978-0-306` |
| `yr:` | Year | `yr=2020` |
| `all:` | All fields | `all=programming` |

Combine with AND / OR: `ti=warcraft and au=blizzard`

---

## SRU HTTP Server

The SRU endpoint is available at:

```
/api/sru?version=1.1&operation=searchRetrieve&query=dc.title%3Dhistory
```

### Authentication

Include your API key as a header:

```
X-API-Key: <your-sru-api-key>
```

The key must have the `sru` scope.

### Supported Operations

| Operation | Description |
|-----------|-------------|
| `searchRetrieve` | Run a CQL query and return XML results |
| `explain` | Server capability document |

### CQL Indexes

| Index | Maps to |
|-------|---------|
| `dc.title` | Item title |
| `dc.creator` | Author / creator |
| `dc.subject` | Material type |
| `dc.identifier` | ISBN / ISSN |
| `dc.publisher` | Publisher name |
| `dc.date` | Publication year |

### Example Requests

**Search by title:**
```
GET /api/sru?version=1.1&operation=searchRetrieve&query=dc.title%3Dhistory&recordPacking=xml
```

**Search with result limit:**
```
GET /api/sru?version=1.1&operation=searchRetrieve&query=dc.creator%3Dsmith&maximumRecords=50
```

**Server diagnostics:**
```
GET /api/sru?version=1.1&operation=explain
```

### SRU Explain Response

Returns a diagnostic document listing:
- Available indexes and their Dublin Core mappings
- Supported record schemas (Dublin Core, CQL)
- Default settings (maximum records: 20)

---

## Query Log

All SRU queries are logged to `library_sru_log` with:
- Query string
- Parsed CQL
- Result count
- Duration (ms)
- Remote IP address
- API key hint (first 8 chars of the SHA-256 of the key used)

Logs are used for audit and analytics. Rotate logs via the standard AtoM log rotation.

---

## Import Log

Z39.50 import operations are logged to `library_z3950_import_log` with:
- Target used
- Query executed
- Records received / imported / skipped / errored
- Duration and any errors

---

## Prerequisites

| Component | Required for |
|-----------|-------------|
| YAZ PHP extension | Z39.50 client (native Z39.50 protocol) |
| HTTP allow_url_fopen | SRU fallback (when YAZ absent) |
| SRU API key with `sru` scope | SRU server access |

---

*Part of the AtoM AHG Framework — Library Module*