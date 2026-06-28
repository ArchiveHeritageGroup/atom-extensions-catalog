# ahgAiCompliancePlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). EU AI Act Article 12 record-keeping (PSIS port of ahg/ai-compliance). Tamper-evident receipt chain over every AI inference call using the ahg/inference-receipts library (SHA-256 chain + RFC 8785 JCS + Ed25519).

## Overview

- **Name:** AI Compliance
- **Machine name:** `ahgAiCompliancePlugin`
- **Version:** 0.1.0
- **Category:** ahg
- **Dependencies:** `ahgCorePlugin`
- **License:** AGPL-3.0-or-later

## Database tables

- `ai_act_attestation`
- `ai_act_model`
- `ai_act_risk`
- `ai_act_system`
- `ai_inference_key`
- `ai_inference_log`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ahg_ai_compliance_well_known_pubkey` | `/.well-known/ai-inference-pubkey` | wellKnownPubkey |
| `ai_act_index` | `/admin/ai-act` | index |
| `ai_act_systems` | `/admin/ai-act/systems` | systems |
| `ai_act_system_edit` | `/admin/ai-act/system/edit` | systemEdit |
| `ai_act_models` | `/admin/ai-act/models` | models |
| `ai_act_model_edit` | `/admin/ai-act/model/edit` | modelEdit |
| `ai_act_risks` | `/admin/ai-act/risks` | risks |
| `ai_act_risk_edit` | `/admin/ai-act/risk/edit` | riskEdit |
| `ai_act_attestations` | `/admin/ai-act/attestations` | attestations |
| `ai_act_attestation_edit` | `/admin/ai-act/attestation/edit` | attestationEdit |

## Module actions

**`aiActGovernance`** — `index`, `systems`, `systemEdit`, `models`, `modelEdit`, `risks`, `riskEdit`, `attestations`, `attestationEdit`
**`aiCompliance`** — `wellKnownPubkey`

## CLI tasks

- `php symfony ai-compliance:install-key` — Generate the Ed25519 signing keypair for the AI inference log
- `php symfony ai-compliance:prune` — Null payload_json on inference-log rows older than the retention window
- `php symfony ai-compliance:verify-inference-log` — Walk the ai_inference_log chain and validate hashes + signatures

## Service layer

### `AiActGovernanceService`  
`lib/Services/AiActGovernanceService.php`

Public methods: `listSystems()`, `getSystem()`, `systemOptions()`, `saveSystem()`, `deleteSystem()`, `listModels()`, `getModel()`, `saveModel()`, `deleteModel()`, `listRisks()`, `getRisk()`, `saveRisk()`, `deleteRisk()`, `riskBand()`, `listAttestations()`, `getAttestation()`, `saveAttestation()`, `deleteAttestation()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
