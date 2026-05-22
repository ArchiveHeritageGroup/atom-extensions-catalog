# AI Inventory & Governance

The AHG plugins run several AI services - named-entity recognition (NER), handwriting transcription (HTR), summarisation, translation and condition assessment. The **AI Inventory & Governance** dashboard is the single place to see which models are in use, how they are configured, what they have produced, and whether each result can be cryptographically verified.

Open it from the AI menu at **AI Governance** (`/ai/governance`). The page is admin-gated.

## Why this page exists

An archive that lets AI touch its catalogue records has to be able to answer three questions for any auditor, funder or freedom-of-information request:

1. **What model produced this?** Name, version and the full runtime configuration in force at the time.
2. **Has the result been tampered with since?** A recorded inference can carry a cryptographic signature over a canonical manifest of its inputs, outputs and model identity.
3. **Who configured the AI, and how?** The model inventory shows every LLM endpoint the system is wired to, minus the secrets.

The dashboard answers all three from one screen. It reads only - nothing on this page changes a record or re-runs a model.

## What the dashboard shows

The page is served by the `executeGovernance` action in the AI module and rendered by `governanceSuccess.php`. It has three regions.

**Stat cards** along the top: total inferences recorded, count of distinct models seen, how many inferences are signed, and the share of inferences carrying a model manifest.

**Model inventory table** - one row per configured LLM (from `ahg_llm_config`): the model name, its endpoint, the service it backs, and a manifest badge. API keys are **never** rendered on this page or returned by its JSON endpoints; only their presence is indicated.

**Recent inferences table** - the latest rows from `ahg_ai_inference`: service, model name and version, target record, confidence, a manifest key-count badge, and a **signed** column that reads the real `signer_key_id` column.

Two JSON endpoints back the page for scripted audits:

- `GET /ai/governance/models` - the model inventory as JSON (keys redacted).
- `GET /ai/governance/inferences` - recent inferences as JSON.

All three are Capsule queries over `ahg_llm_config` and `ahg_ai_inference`.

## The model inventory

Every AI endpoint the AHG plugins can call is described by a row in `ahg_llm_config`: a friendly model name, the HTTP endpoint, the service it serves, and an optional operator-curated **model manifest**. The API key for each endpoint is stored in that table but is never exposed through the dashboard or its JSON endpoints.

## Model manifest

A **model manifest** is a small JSON object that captures the identity and material configuration of a model at the moment it ran: model name, version, endpoint, decoding parameters, and any operator notes. It exists so that a result can be reproduced and audited even years later, after the live model has been upgraded or retired.

- **Operator-curated manifest** - an optional JSON blob maintained on the `ahg_llm_config` row. Use it for things the system cannot discover automatically: licence terms, training-data provenance, a model card URL, an internal approval reference.
- **Per-inference manifest** - a snapshot stored on the `ahg_ai_inference.model_manifest` column when an inference is recorded.

The dashboard shows a key-count badge for each inference's manifest. The `model_manifest` columns exist on both `ahg_llm_config` and `ahg_ai_inference`.

## Inference recording and signing

The AHG plugins record every AI inference they perform - NER, summarisation and HTR - into the `ahg_ai_inference` table, through the `InferenceService` in `ahgProvenancePlugin`. Each row captures the model identity, sha256 hashes of the input and output, confidence, the target record and field, and a per-inference model manifest.

Each recorded inference is **Ed25519-signed**: `InferenceService` builds a canonical, key-sorted manifest of the inference and signs it with libsodium. The signature and the signing key's identifier are stored on the `ahg_ai_inference.signature` and `signer_key_id` columns, and the dashboard's **signed** column reads them directly. Verifying a signature deterministically proves the manifest has not changed since it was recorded.

Signing is opt-in. Generate the operator keypair once:

```
php symfony ai-provenance:keygen
```

The private key is written to the AtoM install's `data/ahg-ai-signing/` directory - never in the database, never in git. Until the keypair exists, inferences are recorded unsigned. Two companion tasks support audits:

- `php symfony ai-provenance:verify` - re-checks recorded signatures against the public key.
- `php symfony ai-provenance:replay` - retries any deferred Fuseki provenance writes; run it from cron every few minutes.

Reviewer corrections are recorded into `ahg_ai_override` without ever overwriting the original inference.

## RAG guardrails

Every LLM call the AHG plugins make passes through a policy guardrail before the prompt is dispatched, with the generated text checked for grounding afterwards. The guardrails enforce three things:

- **Data-scope policy.** A cloud provider may only receive data scopes on the allow-list; local providers carry any scope because the data never leaves the trust domain. Out-of-scope data to a cloud provider is blocked, and email addresses and long number sequences in cloud-bound prompts are masked.
- **Purpose limitation.** Each request declares a purpose, which must be in the operator-sanctioned set, else it is blocked or flagged.
- **Grounding / hallucination check.** When a call supplies its retrieved sources, the generated output is scored against them; ungrounded output is flagged as a possible hallucination.

One setting, `rag_guardrail_mode` (`off` / `warn` / `mask` / `block`, default `warn` - compute and flag, but never block or alter), sets the enforcement strength. The five `rag_*` settings live in `ahg_ai_settings` under `feature = guardrails`, with the same keys and defaults as the Heratio side. The guardrail verdict is returned on every LLM result. The guardrail layer is fail-open: a bug in the policy code never denies the AI service, though a deliberate block always blocks.

## How AI requests are routed

All AI traffic flows through one place: the **AI gateway** at `https://ai.theahg.co.za/ai/v1/...`. The gateway authenticates each request with a bearer token, routes it to whichever GPU worker is healthy, and logs it.

Handwriting transcription (HTR) is routed through the gateway:

- The HTR endpoint is resolved from the **`app_htr_url`** configuration value (the gateway HTR endpoint) - no hostnames are hardcoded in the action code.
- Every HTR call carries an `Authorization: Bearer` token rather than the older `X-API-Key` header.

This keeps HTR requests authenticated and visible in the gateway's audit trail alongside NER, translation and summarisation.

## Frequently asked questions

**Does opening this page run any models or change records?** No. It is entirely read-only.

**Where are API keys?** Stored in `ahg_llm_config`, never shown here. The dashboard only reports whether a key is present.

**Can I export this for an audit?** Yes - the `/ai/governance/models` and `/ai/governance/inferences` JSON endpoints give you the inventory and the inference log in machine-readable form.

## See also

- **AI Tools** - using NER, HTR, summarisation and translation day to day.
- **Provenance Tracking** - provenance for catalogue records generally.
