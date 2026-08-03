# Cantaloupe IIIF Image Server - Setup Guide

**Version:** Cantaloupe 5.0.6
**Last Updated:** 2026-04-09
**Required By:** ahgIiifPlugin (optional but recommended for deep zoom tiling)

---

## Overview

Cantaloupe is a standalone Java-based IIIF image server that provides deep zoom tiling for high-resolution images. It runs as a separate service alongside AtoM and is proxied via Nginx.

AtoM Heratio uses Cantaloupe with a **Ruby delegate script** (`delegates.rb`) that provides:
1. **Multi-instance path routing** — a single Cantaloupe instance serves multiple AtoM instances based on the `Host` header
2. **IIIF Auth enforcement** — calls back to AtoM's internal auth endpoint to check access permissions per image

---

## Architecture

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 603 212" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="602" height="211" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="42.4" y1="26.0" x2="42.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="34.0" x2="42.4" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="66.0" x2="71.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="66.0" x2="74.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="66.0" x2="78.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="66.0" x2="82.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="66.0" x2="85.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="66.0" x2="89.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="66.0" x2="157.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="66.0" x2="161.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="66.0" x2="164.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="66.0" x2="168.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="66.0" x2="265.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="66.0" x2="269.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="66.0" x2="272.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="66.0" x2="276.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="74.0" x2="330.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="82.0" x2="330.4" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="106.0" x2="294.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="114.0" x2="294.4" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="106.0" x2="366.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="114.0" x2="366.4" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="130.0" x2="204.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="130.0" x2="200.8" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="130.0" x2="208.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="130.0" x2="211.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="130.0" x2="215.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="130.0" x2="218.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="130.0" x2="222.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="130.0" x2="226.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="130.0" x2="229.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="130.0" x2="233.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="130.0" x2="236.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="130.0" x2="240.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="130.0" x2="244.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="130.0" x2="247.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="130.0" x2="251.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="130.0" x2="254.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="130.0" x2="258.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="130.0" x2="262.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="130.0" x2="265.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="130.0" x2="269.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="130.0" x2="272.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="130.0" x2="276.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="130.0" x2="280.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="130.0" x2="283.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="130.0" x2="287.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="130.0" x2="290.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="130.0" x2="294.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="122.0" x2="294.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="130.0" x2="370.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="122.0" x2="366.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="130.0" x2="373.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="130.0" x2="377.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="130.0" x2="380.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="130.0" x2="384.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="130.0" x2="388.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="130.0" x2="391.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="130.0" x2="395.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="130.0" x2="398.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="130.0" x2="402.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="130.0" x2="406.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="130.0" x2="409.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="130.0" x2="413.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="130.0" x2="416.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="130.0" x2="420.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="420.4" y1="130.0" x2="424.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="130.0" x2="427.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="427.6" y1="130.0" x2="431.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="130.0" x2="434.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="434.8" y1="130.0" x2="438.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="438.4" y1="130.0" x2="442.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="442.0" y1="130.0" x2="445.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="445.6" y1="130.0" x2="449.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="449.2" y1="130.0" x2="452.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="452.8" y1="130.0" x2="456.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="456.4" y1="130.0" x2="460.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="460.0" y1="130.0" x2="460.0" y2="138.0" stroke="#10373E" stroke-width="1.3"/><path d="M38.4 45.0 L42.4 52.0 L46.4 45.0 Z" fill="#10373E"/><path d="M196.8 141.0 L200.8 148.0 L204.8 141.0 Z" fill="#10373E"/><path d="M463.2 141.0 L467.2 148.0 L471.2 141.0 Z" fill="#10373E"/><path d="M217.4 174.0 L224.4 178.0 L217.4 182.0 Z" fill="#10373E"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">Browser</text><text x="67.6" y="22.0" font-size="9.5" fill="#10373E">Request</text><text x="24.4" y="70.0" font-size="9.5" fill="#10373E">Nginx</text><text x="96.4" y="70.0" font-size="9.5" fill="#10373E">/iiif/*</text><text x="168.4" y="70.0" font-size="9.5" fill="#10373E">►</text><text x="182.8" y="70.0" font-size="9.5" fill="#10373E">proxy_pass</text><text x="276.4" y="70.0" font-size="9.5" fill="#10373E">►</text><text x="290.8" y="70.0" font-size="9.5" fill="#10373E">Cantaloupe</text><text x="370.0" y="70.0" font-size="9.5" fill="#10373E">(port</text><text x="413.2" y="70.0" font-size="9.5" fill="#10373E">8182)</text><text x="276.4" y="102.0" font-size="9.5" fill="#10373E">delegates.rb</text><text x="132.4" y="166.0" font-size="9.5" fill="#10373E">filesystemsource_pathname()</text><text x="398.8" y="166.0" font-size="9.5" fill="#10373E">authorize()</text><text x="132.4" y="182.0" font-size="9.5" fill="#10373E">Host</text><text x="168.4" y="182.0" font-size="9.5" fill="#10373E">header</text><text x="233.2" y="182.0" font-size="9.5" fill="#10373E">file</text><text x="269.2" y="182.0" font-size="9.5" fill="#10373E">path</text><text x="398.8" y="182.0" font-size="9.5" fill="#10373E">HTTP</text><text x="434.8" y="182.0" font-size="9.5" fill="#10373E">callback</text><text x="499.6" y="182.0" font-size="9.5" fill="#10373E">to</text><text x="521.2" y="182.0" font-size="9.5" fill="#10373E">AtoM</text><text x="132.4" y="198.0" font-size="9.5" fill="#10373E">(INSTANCE_PATHS</text><text x="247.6" y="198.0" font-size="9.5" fill="#10373E">map)</text><text x="398.8" y="198.0" font-size="9.5" fill="#10373E">/iiif/auth/cantaloupe-check</text></svg></div>

---

## Installation

### Prerequisites

- Java 11+ (OpenJDK recommended)
- AtoM with ahgIiifPlugin enabled

### 1. Download and Install

```bash
cd /opt
wget https://github.com/cantaloupe-medimaging/cantaloupe/releases/download/v5.0.6/cantaloupe-5.0.6.zip
unzip cantaloupe-5.0.6.zip
chown -R www-data:www-data /opt/cantaloupe-5.0.6
```

### 2. Create systemd Service

```bash
cat > /etc/systemd/system/cantaloupe.service << 'EOF'
[Unit]
Description=Cantaloupe IIIF Image Server
After=network.target

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/opt/cantaloupe-5.0.6
Environment="JAVA_OPTS=-Xmx2g"
ExecStart=/usr/bin/java -Dcantaloupe.config=/opt/cantaloupe-5.0.6/cantaloupe.properties -Xmx2g -jar /opt/cantaloupe-5.0.6/cantaloupe-5.0.6.jar
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable cantaloupe
systemctl start cantaloupe
```

### 3. Verify

```bash
systemctl status cantaloupe
curl -s http://127.0.0.1:8182/ | head -5
```

---

## Configuration

### Key Files

| File | Purpose |
|------|---------|
| `/opt/cantaloupe-5.0.6/cantaloupe.properties` | Main configuration (ports, caching, processors) |
| `/opt/cantaloupe-5.0.6/delegates.rb` | Ruby delegate script (path routing, auth) |

### cantaloupe.properties — Required Settings

These settings must be present at the **end** of `cantaloupe.properties` (they override any earlier defaults):

```properties
# Enable delegate script
delegate_script.enabled = true
delegate_script.pathname = /opt/cantaloupe-5.0.6/delegates.rb
delegate_script.class = CustomDelegate

# Use delegate for file path resolution (multi-instance support)
FilesystemSource.ScriptLookupStrategy.script = /opt/cantaloupe-5.0.6/delegates.rb
source.static = FilesystemSource
source.delegate = true
FilesystemSource.lookup_strategy = ScriptLookupStrategy
```

Other notable settings:

```properties
# Server
http.port = 8182

# IIIF endpoints
endpoint.iiif.2.enabled = true
endpoint.iiif.3.enabled = true

# Slash substitute (used in IIIF identifiers for path separators)
slash_substitute = _SL_
```

---

## Multi-Instance Routing (delegates.rb)

### How It Works

Cantaloupe is a standalone Java process — it has no access to AtoM's PHP config or database. The `delegates.rb` script is a Ruby extension point that Cantaloupe calls for each request.

The `INSTANCE_PATHS` hash maps hostnames to AtoM instance root directories. When a IIIF request arrives:

1. Cantaloupe calls `filesystemsource_pathname()` in delegates.rb
2. The delegate extracts the `Host` (or `X-Forwarded-Host`) header
3. It looks up the host in `INSTANCE_PATHS` to get the base path
4. The IIIF identifier (with `_SL_` decoded back to `/`) is appended to the base path
5. The resulting absolute path is returned to Cantaloupe for image processing

### Adding a New AtoM Instance

Edit `/opt/cantaloupe-5.0.6/delegates.rb` and add the hostname mapping:

```ruby
INSTANCE_PATHS = {
  'psis.theahg.co.za' => '/usr/share/nginx/archive/',
  'atom.theahg.co.za' => '/usr/share/nginx/atom/',
  'dam.theahg.co.za' => '/usr/share/nginx/dam/',
  'heratio.theahg.co.za' => '/usr/share/nginx/heratio/',
  # Add new instances here:
  # 'newsite.example.com' => '/usr/share/nginx/newsite/',
}.freeze
```

Then restart Cantaloupe:

```bash
sudo systemctl restart cantaloupe
```

**Note:** The `DEFAULT_PATH` fallback (`/usr/share/nginx/archive/`) is used when no hostname match is found.

### Current Instance Mappings

| Hostname | AtoM Root Path | Instance |
|----------|---------------|----------|
| `nahlisa.theahg.co.za` | `/usr/share/nginx/archive/` | PSIS (alias) |
| `archives.theahg.co.za` | `/usr/share/nginx/archive/` | PSIS (alias) |
| `psis.theahg.co.za` | `/usr/share/nginx/archive/` | PSIS (primary) |
| `heratio.theahg.co.za` | `/usr/share/nginx/heratio/` | Heratio |
| `atom.theahg.co.za` | `/usr/share/nginx/atom/` | ANC |
| `dam.theahg.co.za` | `/usr/share/nginx/dam/` | DAM |

---

## IIIF Auth Integration

### How Auth Works

The `authorize()` method in delegates.rb enforces access control by calling back to AtoM:

1. Cantaloupe calls `authorize()` for each image request
2. The delegate extracts auth credentials from cookies (`iiif_auth_token`) and/or `Authorization: Bearer` header
3. It makes an HTTP GET to `http://127.0.0.1/iiif/auth/cantaloupe-check` with the identifier and credentials
4. AtoM's ahgIiifPlugin checks access rights and responds:
   - `{"allowed": true}` — full access
   - `{"degraded": true, "max_scale": N}` — degraded access (reduced resolution)
   - `{"allowed": false}` — denied
5. Results are cached for 60 seconds (`AUTH_CACHE_TTL`)

### Fail-Open Behavior

If the auth callback fails (AtoM is down, timeout, network error), Cantaloupe **allows access** (fail-open). This is intentional — IIIF tile serving should not break if AtoM is temporarily unavailable. The auth endpoint runs on `127.0.0.1` (loopback), so external access is not possible without going through Nginx/AtoM first.

### Auth Cache

- Cache TTL: 60 seconds
- Max cache size: 1000 entries (auto-evicts expired entries)
- Cache key: `identifier:cookie:bearer` (per-user, per-image)

---

## Nginx Proxy Configuration

Cantaloupe must be proxied through Nginx so that IIIF requests on your domain reach port 8182.

### Option A: Use the Framework's extensions.conf

In `atom-framework/config/nginx/extensions.conf`, uncomment the Cantaloupe proxy block:

```nginx
location /iiif/ {
    proxy_pass http://127.0.0.1:8182/iiif/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    add_header Access-Control-Allow-Origin "*" always;
}
```

Then include it in your server block:

```nginx
server {
    server_name psis.theahg.co.za;
    # ... other config ...

    # BEFORE the main PHP handler:
    include /usr/share/nginx/archive/atom-framework/config/nginx/extensions.conf;

    # ... PHP handler ...
}
```

### Option B: Add Directly to Server Block

Add the `location /iiif/` block directly to your site's Nginx config.

**Important:** The `Host` header (`proxy_set_header Host $host`) is critical — delegates.rb uses it to determine which AtoM instance to serve files from.

After editing Nginx config:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

---

## IIIF Identifier Format

IIIF identifiers use `_SL_` as a slash substitute (configured in `cantaloupe.properties`). This is because IIIF URIs encode the identifier in the URL path, where `/` would be ambiguous.

Example for a file at `/usr/share/nginx/archive/uploads/r/123/doc.jpg`:

```
IIIF URL:  https://psis.theahg.co.za/iiif/2/uploads_SL_r_SL_123_SL_doc.jpg/full/max/0/default.jpg
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                 identifier (decoded to uploads/r/123/doc.jpg)
```

The delegate script decodes `_SL_` → `/` and prepends the instance base path.

---

## Troubleshooting

### Cantaloupe Won't Start

```bash
# Check Java is installed
java -version

# Check logs
journalctl -u cantaloupe -n 50

# Check port is free
ss -tlnp | grep 8182
```

### Images Not Loading (404)

1. Check the delegate is active:
   ```bash
   grep "delegate_script.enabled" /opt/cantaloupe-5.0.6/cantaloupe.properties
   # Should be: delegate_script.enabled = true
   ```

2. Check the hostname mapping exists in `delegates.rb`

3. Check the file path resolves correctly:
   ```bash
   # Look for delegate log output
   journalctl -u cantaloupe | grep "Identifier="
   ```

4. Verify the file exists on disk at the resolved path

### Images Blocked (403 / Auth Failure)

1. Check AtoM is running and reachable on loopback:
   ```bash
   curl -s http://127.0.0.1/iiif/auth/cantaloupe-check?identifier=test
   ```

2. Check delegate logs for auth errors:
   ```bash
   journalctl -u cantaloupe | grep "Auth check"
   ```

3. Remember: auth is fail-open — if you're getting 403s, Cantaloupe itself may be blocking (check `cantaloupe.properties` for access restrictions)

### Memory Issues

Cantaloupe runs with `-Xmx2g` by default. For large collections with many concurrent users, increase the heap:

```bash
# Edit /etc/systemd/system/cantaloupe.service
# Change: -Xmx2g → -Xmx4g
systemctl daemon-reload
systemctl restart cantaloupe
```

---

## Maintenance

### Restart After Config Changes

```bash
# delegates.rb changes require restart
sudo systemctl restart cantaloupe

# Most cantaloupe.properties changes take effect without restart
# (marked with !! in the properties file if restart is needed)
```

### Log Monitoring

```bash
journalctl -u cantaloupe -f          # Follow logs
journalctl -u cantaloupe --since today  # Today's logs
```

### Upgrading Cantaloupe

1. Download new version to `/opt/cantaloupe-X.Y.Z/`
2. Copy over `delegates.rb` and `cantaloupe.properties`
3. Update the service file `ExecStart` path
4. Review release notes for config key changes
5. `systemctl daemon-reload && systemctl restart cantaloupe`
