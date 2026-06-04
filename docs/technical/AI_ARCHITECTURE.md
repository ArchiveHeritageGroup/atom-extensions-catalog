# AtoM Heratio — AI Architecture & Installation

**Author:** The Archive and Heritage Group (Pty) Ltd
**Applies to:** AtoM Heratio (Symfony/AtoM stack) — `ahgAIPlugin` and companion AI plugins
**Status:** Technical reference

---

## 1. Overview

AI in AtoM Heratio is split into two layers:

1. **In‑app layer (PHP / Symfony)** — the `ahgAIPlugin` plugin and its companions. This layer owns the UI, routing, persistence, governance and orchestration. **It never runs models itself.**
2. **Inference services (outside the web process)** — Python/model services running on the GPU/CPU fleet. The PHP layer reaches them over HTTP.

This separation keeps the web tier light and lets models be swapped, scaled or moved between machines without touching application code.

```
┌─────────────────────────── AtoM (PHP / Symfony) ───────────────────────────┐
│  ahgAIPlugin                                                                 │
│   • module `ai`  (/ai/* actions — NER, summarize, HTR, suggest, DONUT,      │
│                   batch, LLM config, collection assistant)                   │
│   • Services:  NerService · DescriptionService · ahgDonutService ·           │
│                LlmService (provider factory) · CollectionChatbotService      │
│   • DB:  ahg_llm_config · ahg_ai_inference · DONUT tables · ahg_ai_*         │
│  Companions: ahgAiCompliancePlugin · ahgProvenancePlugin · ahgHelpPlugin     │
└───────────────┬───────────────────────────────┬────────────────────────────┘
                │ HTTP                            │ HTTP (LlmService → provider)
   ┌────────────▼────────────┐     ┌─────────────▼───────────────────────────┐
   │ ahg-ai.service  :5004   │     │ LLM providers (pluggable per ahg_llm_    │
   │ (Workhorse, GPU)        │     │ config):                                 │
   │ NER · summarize ·       │     │  • ollama   → e.g. mistral:7b @          │
   │ translate · spellcheck  │     │              192.168.0.78:11434          │
   │ transformers · spaCy ·  │     │  • openai   (fallback)                   │
   │ CTranslate2 · Argos     │     │  • anthropic(fallback)                   │
   └─────────────────────────┘     │ RAG infra: KM :5050 · Qdrant :6333 ·     │
                                    │            embeddings (.112)             │
                                    └──────────────────────────────────────────┘
```

---

## 2. Components

### 2.1 In‑app PHP (`ahgAIPlugin`)

| Piece | Path | Responsibility |
|-------|------|----------------|
| `ai` module actions | `modules/ai/actions/actions.class.php` | Endpoints under `/ai/*` |
| `LlmService` | `lib/Services/LlmService.php` | **Provider factory** — reads `ahg_llm_config`, decrypts the API key, returns an `OllamaProvider` / `OpenAIProvider` / `AnthropicProvider` |
| `LlmProviderInterface` | `lib/Services/LlmProviderInterface.php` | `complete($system,$user,$opts)`, `isAvailable()` |
| `NerService`, `DescriptionService` | `lib/Services/` | NER + description assistance (call `ahg-ai.service`) |
| `ahgDonutService` | `lib/Services/` | DONUT document understanding |
| `CollectionChatbotService` | `lib/Services/` | RAG Q&A over the catalogue (FULLTEXT retrieve → `LlmService` generate) |

### 2.2 Companion plugins

| Plugin | Role |
|--------|------|
| `ahgAiCompliancePlugin` | EU AI Act governance — signed inference receipts (`KeyResolver`, `SignerFactory`, `InferenceLogger`), verifiable via `ai:verify-inference-log` |
| `ahgProvenancePlugin` | AI provenance on records (`InferenceService`) |
| `ahgHelpPlugin` | Help‑desk chatbot (`HelpChatbotService`) — RAG over help articles, reuses `LlmService` |

### 2.3 Inference services (fleet)

| Service | Host / Port | Provides |
|---------|-------------|----------|
| `ahg-ai.service` | Workhorse (GPU), `:5004` (`/ai/v1/`) | NER, summarization, translation, spellcheck — `transformers`, `spaCy`, `CTranslate2`, Argos. Code: `/opt/ahg-ai/api/ai_service.py`; venv `/opt/ahg-ai/.venv`; models `/opt/ahg-ai/models/` |
| Ollama | GPU node, `:11434` | Local LLM generation (the active model is **`mistral:7b`** per `ahg_llm_config`) |
| AI Gateway | `:8002` | (Fleet design) routes LLM/embeddings to whichever GPU node is hot |
| KM + Qdrant | `.112`, `:5050` / `:6333` | Vector RAG knowledge base + embeddings |
| `atom-ahg-python` | package | The Python behind NLP tasks (`ner.py`, `summarize.py`, `translation.py`) |

> The **live default** on this instance is Ollama → `mistral:7b` at `http://192.168.0.78:11434`. OpenAI (`gpt-4o-mini`) and Anthropic (`claude-3-haiku`) rows exist in `ahg_llm_config` but are **inactive** — they are drop‑in fallbacks.

---

## 3. Installation

### 3.1 Application side

1. **Enable the plugin** — `ahgAIPlugin` needs an `atom_plugin` row (`is_enabled=1`) and a symlink in `plugins/`. Enable companions (`ahgAiCompliancePlugin`, `ahgProvenancePlugin`) the same way if used.
2. **Create the schema** — `php symfony ai:install` runs the plugin SQL, creating the AI tables (incl. `ahg_llm_config`, `ahg_ai_inference`, DONUT tables).
3. **Configure a model** — Admin → AHG Settings → AI, or insert into `ahg_llm_config`:
   - `provider` (`ollama` | `openai` | `anthropic`), `model`, `endpoint_url`,
   - `api_key_encrypted` (stored encrypted), `max_tokens`, `temperature`, `timeout_seconds`,
   - `is_active`, `is_default`.
   The active/default row is what `LlmService::getProvider()` selects.
4. **Navigation** — `php symfony ai:install-menu` adds the **Collection assistant** link under *Manage* (idempotent; nested‑set safe). *(As of the latest build this also runs automatically at the end of `ai:install`.)*
5. **Clear cache + restart** — `rm -rf cache/qubit/prod/* && sudo systemctl restart php8.3-fpm` so new routes and the menu appear.

### 3.2 Service side (fleet)

- Run **`ahg-ai.service`** (systemd) on the GPU host — venv `/opt/ahg-ai/.venv`, models in `/opt/ahg-ai/models/`.
- Run **Ollama** with the configured model pulled (`ollama pull mistral:7b`), reachable at the `endpoint_url`.
- For vector RAG: **Qdrant** + **KM** on `.112`; the **AI Gateway** for fleet routing.
- Ensure the web host can reach those host:port endpoints (firewall/routes).

---

## 4. Runtime request flow

```
user → /ai/<action>                         (ahgAIPlugin action)
     → Service  (NerService | LlmService | CollectionChatbotService | …)
     → HTTP     (ahg-ai:5004  OR  provider endpoint via getProvider())
     → model inference → JSON
     → log to ahg_ai_inference  (+ signed receipt via ahgAiCompliancePlugin)
     → render in the UI
```

Example — the **Collection assistant** (`/ai/assistant`):
1. Retrieve: MySQL FULLTEXT over **published** `information_object` titles + scope.
2. Augment: build a context block from the top matches.
3. Generate: `LlmService` provider `complete()` with a grounding system prompt.
4. Return: a catalogue‑grounded answer + cited record links; fail‑open to a record list if the LLM is offline.

---

## 5. Endpoints (selected)

| Route | Purpose |
|-------|---------|
| `/ai/ner/extract/:id`, `/ai/ner/review`, `/ai/ner/health` | Named‑entity recognition + review |
| `/ai/summarize/:id` | Summarisation |
| `/ai/htr/:id` | Handwritten‑text recognition |
| `/ai/suggest/:id`, `/ai/suggest/review` | LLM description suggestions |
| `/ai/donut/*` | DONUT document understanding |
| `/ai/batch/*` | Batch AI jobs |
| `/ai/llm/configs`, `/ai/llm/health` | LLM model configuration + health |
| `/ai/assistant`, `/ai/assistant/ask` | Collection chatbot (page + JSON) |

---

## 6. CLI tasks

```
php symfony ai:install              # create AI tables (and the nav link)
php symfony ai:install-menu         # add the Collection assistant nav link (idempotent)
php symfony ai:ner-extract          # extract named entities
php symfony ai:ner-sync             # sync NER training data
php symfony ai:htr-extract          # handwritten-text recognition
php symfony ai:summarize            # summarise records
php symfony ai:translate            # machine translation
php symfony ai:spellcheck           # spelling/grammar
php symfony ai:suggest-description  # LLM description suggestions
php symfony ai:process-pending      # process queued AI work
php symfony ai:sync-entity-cache    # refresh entity cache
php symfony ai:uninstall            # remove AI tables
```

---

## 7. Governance, logging & safety

- **Inference log** — every call is recorded in `ahg_ai_inference` (model, confidence, timing; issue #140).
- **EU AI Act compliance** — `ahgAiCompliancePlugin` produces **cryptographically signed inference receipts** (chain of who/what/when), verifiable with `ai:verify-inference-log`.
- **Provenance** — `ahgProvenancePlugin` records AI provenance on affected descriptions.
- **Fail‑safe** — every AI call is wrapped so an unreachable service degrades gracefully (the assistant returns records instead of a generated answer; NER/summarise report "AI unavailable" rather than a 500).
- **Secrets** — provider API keys are stored encrypted (`api_key_encrypted`) and never logged.

---

## 8. Health & verification

- **In‑app:** the provider's `isAvailable()`, `/ai/llm/health`, `/ai/ner/health`, and the **"AI ready / offline"** badge on the assistant page.
- **Service:** `systemctl status ahg-ai.service`; `curl http://<host>:5004/ai/v1/health`; `curl http://<host>:11434/api/tags` (Ollama models).
- **DB:** `SELECT provider, model, endpoint_url, is_active FROM ahg_llm_config WHERE is_default = 1;`

---

## 9. Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Assistant badge "AI offline" / `mode:"fallback"` | No active `ahg_llm_config` row, or endpoint unreachable | Check the default row + that the host can reach `endpoint_url`; confirm Ollama is up and the model pulled |
| NER/summarise "AI unavailable" | `ahg-ai.service` down | `systemctl restart ahg-ai.service`; check `:5004/ai/v1/health` |
| New AI route 404 / menu link missing | Cache not cleared | `rm -rf cache/qubit/prod/*` + restart php‑fpm; run `ai:install-menu` |
| Generation slow/timeouts | GPU node cold or model large | Warm the node / smaller model; raise `timeout_seconds` in `ahg_llm_config` |

---

## 10. The two app stacks

This document describes the **AtoM/Symfony (PSIS)** implementation (`ahgAIPlugin`). The **Heratio Laravel** stack has equivalent packages (`ahg-ai-services`, `ahg-ai-chatbot`, `ahg-ai-compliance`) that call the **same fleet services**. Parity work tracked on the AHG issue trackers keeps the two feature sets aligned.
