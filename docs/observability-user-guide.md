# Observability & Metrics

## A Guide for Technical Staff

---

## What is it?

The Observability plugin (`ahgObservabilityPlugin`) exposes a single,
auth-gated **Prometheus-format `/metrics` endpoint** for AtoM Heratio. It lets
your monitoring stack scrape application, HTTP-request, database-query and
queue-depth metrics without any external Composer dependency — the Prometheus
client and text renderer are self-contained, and a metrics fault never returns a
500 to a user.

## Key features

- **Prometheus text exposition (format 0.0.4)** at `GET /metrics`.
- **Fail-closed authentication** — bearer token **or** IP allow-list; an
  unconfigured endpoint denies all scrapes (401).
- **Auto-selecting counter storage** — Redis (phpredis) → APCu → in-memory,
  degrading silently if a backend is unavailable.
- **Per-request instrumentation** of request count and latency, labelled by
  method / route (`module/action`) / status, with bounded cardinality.
- **Queue-depth gauge** sampled from `ahg_queue_job`.
- **node_exporter textfile emitter** for environments that can't scrape
  `/metrics` directly (atomic write-then-rename).

## How to use it

### The endpoint

```
GET /metrics
Authorization: Bearer <obs_token>
```

Metrics are namespaced `atom_`:

| Metric | Type | Labels |
|--------|------|--------|
| `atom_http_requests_total` | counter | method, route, status |
| `atom_http_request_duration_seconds` | histogram | method, route, status |
| `atom_queue_depth` | gauge | queue |

`route` is always the `module/action` pair (never the raw URL) to keep label
cardinality bounded.

### CLI commands (`php bin/atom`)

```bash
# Sample the ahg_queue_job backlog into the atom_queue_depth gauge
php bin/atom observability:record-queue-depth

# Write a registry snapshot to the node_exporter textfile directory
php bin/atom observability:emit-textfile
php bin/atom observability:emit-textfile --dry-run
```

Recommended cron: run `record-queue-depth` every minute. Only run
`emit-textfile` when Prometheus cannot reach `/metrics` directly but can scrape
node_exporter.

## Administration / setup

Settings are seeded idempotently by `database/install.sql` into `ahg_settings`
(group `observability`):

| Setting | Purpose |
|---------|---------|
| `obs_token` | Bearer token required for scrapes |
| `obs_allowed_ips` | IP allow-list (default `127.0.0.1,::1`) |
| `obs_storage_driver` | `auto` / `redis` / `apcu` / `inmemory` |
| `obs_textfile_dir` | node_exporter textfile output directory |
| `obs_redis_host` / `obs_redis_port` / `obs_redis_database` | Redis backend |

The `/metrics` route is registered **without** the AtoM ACL/login filter so
Prometheus can scrape without a session cookie — the action performs its own
authentication. **Set `obs_token` or `obs_allowed_ips` before enabling**, or the
endpoint denies everyone by design.

Add a scrape target to your Prometheus config pointing at `https://<host>/metrics`
with the bearer token.

## Tips & FAQ

- **Which storage backend should I use?** `redis` for multi-host setups (shared
  across php-fpm and queue workers), `apcu` for a single host, `inmemory` only
  for tests/CLI. `auto` picks the best available.
- **Counters reset on deploy?** With in-memory or APCu storage, counters are
  process/host-local; Prometheus handles counter resets natively.
- **Will a Redis outage break the site?** No — the plugin degrades to in-memory
  and never 500s a request on a metrics fault.
