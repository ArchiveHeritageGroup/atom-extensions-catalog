# ahgAiConditionPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). AI-powered condition assessment using YOLOv8 damage detection and EfficientNet classification. Companion to ahgConditionPlugin.

## Overview

- **Name:** AI Condition Assessment
- **Machine name:** `ahgAiConditionPlugin`
- **Version:** 1.0.0
- **Category:** ai
- **Dependencies:** `ahgCorePlugin`, `ahgConditionPlugin`
- **License:** AGPL-3.0

## Database tables

- `ahg_ai_condition_assessment`
- `ahg_ai_condition_config`
- `ahg_ai_condition_damage`
- `ahg_ai_condition_history`
- `ahg_ai_service_client`
- `ahg_ai_service_usage`
- `ahg_ai_training_contribution`

See `database/install.sql` for the schema (sidecar tables only; no Qubit base-table changes).

## Routes

| Route name | URL | Action |
|---|---|---|
| `ai_condition_index` | `/ai-condition` | index |
| `ai_condition_dashboard` | `/ai-condition/dashboard` | dashboard |
| `ai_condition_browse` | `/ai-condition/browse` | browse |
| `ai_condition_assess` | `/ai-condition/assess` | assess |
| `ai_condition_view` | `/ai-condition/view/:id` | view |
| `ai_condition_history` | `/ai-condition/history/:slug` | history |
| `ai_condition_settings` | `/ai-condition/settings` | settings |
| `ai_condition_bulk` | `/ai-condition/bulk` | bulk |
| `ai_condition_clients` | `/ai-condition/clients` | clients |
| `ai_condition_manual_assess` | `/ai-condition/manual-assess` | manualAssess |
| `ai_condition_training` | `/ai-condition/training` | training |
| `ai_condition_api_test` | `/ai-condition/api/test` | apiTest |
| `ai_condition_api_submit` | `/ai-condition/api/submit` | apiSubmit |
| `ai_condition_api_confirm` | `/ai-condition/api/confirm` | apiConfirm |
| `ai_condition_api_history_data` | `/ai-condition/api/history-data` | apiHistoryData |
| `ai_condition_api_bulk_status` | `/ai-condition/api/bulk-status` | apiBulkStatus |
| `ai_condition_api_client_save` | `/ai-condition/api/client-save` | apiClientSave |
| `ai_condition_api_client_revoke` | `/ai-condition/api/client-revoke` | apiClientRevoke |
| `ai_condition_api_object_search` | `/ai-condition/api/object-search` | apiObjectSearch |
| `ai_condition_api_manual_save` | `/ai-condition/api/manual-save` | apiManualSave |
| `ai_condition_api_training_model_info` | `/ai-condition/api/training/model-info` | apiTrainingModelInfo |
| `ai_condition_api_training_status` | `/ai-condition/api/training/status` | apiTrainingStatus |
| `ai_condition_api_training_upload` | `/ai-condition/api/training/upload` | apiTrainingUpload |
| `ai_condition_api_training_datasets` | `/ai-condition/api/training/datasets` | apiTrainingDatasets |
| `ai_condition_api_training_start` | `/ai-condition/api/training/start` | apiTrainingStart |
| `ai_condition_api_contribute` | `/ai-condition/api/contribute` | apiContribute |
| `ai_condition_api_contributions` | `/ai-condition/api/contributions` | apiContributions |
| `ai_condition_api_client_training_toggle` | `/ai-condition/api/client-training-toggle` | apiClientTrainingToggle |
| `ai_condition_api_client_approve_training` | `/ai-condition/api/client-approve-training` | apiClientApproveTraining |
| `ai_condition_api_client_upload_consent` | `/ai-condition/api/client-upload-consent` | apiClientUploadConsent |
| `ai_condition_api_client_contributions` | `/ai-condition/api/client-contributions` | apiClientContributions |
| `ai_condition_api_contribution_review` | `/ai-condition/api/contribution-review` | apiContributionReview |
| `ai_condition_api_push_training_data` | `/ai-condition/api/push-training-data` | apiPushTrainingData |

## Module actions

**`aiCondition`** — `index`, `assess`, `dashboard`, `browse`, `view`, `history`, `settings`, `bulk`, `apiBulkStatus`, `clients`, `apiTest`, `apiSubmit`, `apiConfirm`, `apiHistoryData`, `apiClientSave`, `apiClientRevoke`, `apiObjectSearch`, `manualAssess`, `apiManualSave`, `training`, `apiTrainingModelInfo`, `apiTrainingStatus`, `apiTrainingUpload`, `apiTrainingDatasets`, `apiTrainingStart`, `apiContribute`, `apiContributions`, `apiClientTrainingToggle`, `apiClientApproveTraining`, `apiClientUploadConsent`, `apiClientContributions`, `apiContributionReview`, `apiPushTrainingData`

## CLI tasks

- `php symfony ai-condition:bulk-scan` — Bulk scan digital objects for condition assessment
- `php symfony ai-condition:install` — Install AI Condition Assessment tables
- `php symfony ai-condition:status` — Check AI Condition Service health

## Service layer

### `AiConditionService`  
`lib/Services/AiConditionService.php`

Public methods: `healthCheck()`, `assess()`, `assessFile()`, `getReport()`, `getUsage()`, `proxyGet()`, `proxyPost()`, `proxyDelete()`, `proxyFileUpload()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
