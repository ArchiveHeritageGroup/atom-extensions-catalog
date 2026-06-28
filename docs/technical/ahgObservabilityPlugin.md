# ahgObservabilityPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Prometheus-format /metrics exporter for AtoM. Exposes app, HTTP request, DB query and queue-depth metrics through a lightweight, auth-gated (bearer token OR IP allow-list) endpoint. Auto-selecting APCu/Redis/in-memory counter storage with graceful fallback. CLI commands sample queue depth and emit node_exporter textfiles.

## Overview

- **Name:** AHG Observability Plugin
- **Machine name:** `ahgObservabilityPlugin`
- **Version:** 1.0.0
- **Category:** integration
- **Dependencies:** none
- **License:** GPL-3.0

### Features

- Prometheus text exposition (version 0.0.4) /metrics endpoint
- Bearer-token OR IP allow-list authentication (fail-closed by default)
- Auto-selecting metric storage: Redis (phpredis) -> APCu -> in-memory
- HTTP request count + latency histogram per method/route/status
- Queue backlog gauge sampled from ahg_queue_job
- node_exporter textfile emitter (atomic write-then-rename)
- Zero external composer dependency, never 500s on a metrics fault

## Routes

| Route name | URL | Action |
|---|---|---|
| `observability_metrics` | `/metrics` | metrics |

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
