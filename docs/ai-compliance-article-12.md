# AI Compliance - EU AI Act Article 12 (tamper-evident inference receipts)

PSIS / AtoM-AHG ships `ahgAiCompliancePlugin` to satisfy EU AI Act Article 12's
"automatic event logs across the lifecycle ... in a form that ensures
traceability and cannot be silently modified" obligation for AI inference calls.

Same byte format as the Heratio sibling, so receipts from either stack can be
cross-verified by any consumer of the standalone `ahg/inference-receipts`
Composer library.

## Why

Plain database rows do not meet the Article 12 bar. The plugin layers three
primitives on top of an append-only table:

1. **SHA-256 hash chain** - each receipt embeds the hash of its predecessor, so
   modifying or deleting an entry breaks the chain at a detectable point.
2. **RFC 8785 JCS (JSON Canonicalization Scheme)** - deterministic byte
   serialization, so any verifier agrees on what was hashed and signed.
3. **Ed25519 detached signatures** - each entry is signed under a per-server
   key. Auditors verify off-host using the public key served at
   `/.well-known/ai-inference-pubkey`.

EU AI Act enforcement: **2 August 2026**.

## Architecture

```
+--------------------+         +-------------------------+
|  AI service call   |  --->   |  InferenceLogger::log() |
|  (NER / HTR / LLM) |         +-----------+-------------+
+--------------------+                     |
                                           v
                              +-----------------------------+
                              |  ReceiptChain::append()     |
                              |  (ahg/inference-receipts)   |
                              +-----------+-----------------+
                                          |
                                          v
                              +-----------------------------+
                              |  PropelChainStore           |
                              |    -> ai_inference_log row  |
                              +-----------+-----------------+
                                          |
                                          v
                              +-----------------------------+
                              |  ai_inference_log (chain)   |
                              |  ai_inference_key (kids)    |
                              +-----------------------------+

External auditor:  curl /.well-known/ai-inference-pubkey
                   -> verifies offline against any exported receipt
```

## Tables

- `ai_inference_log` - one row per inference. Columns: seq (monotonic, UNIQUE),
  ts (millisecond precision), prev_hash, entry_hash, signature, kid, service,
  model_id, model_version, input_fingerprint (SHA-256 of input body),
  output_fingerprint, request_id, user_id, tenant_id, latency_ms, tokens_in/out,
  payload_json (canonical JSON used for hashing), payload_pruned_at.
- `ai_inference_key` - per-kid public key registry. Rotation appends a new row
  and demotes the old to `active=0` with `rotated_at` stamped, so old receipts
  remain verifiable against their original key.

Both tables live alongside the existing `ahg_*` sidecar tables; no
AtoM/Qubit base tables are altered.

## Operator workflow

```bash
# 1. Back up the database before schema changes
mysqldump archive > /var/backups/archive-before-ai-compliance.sql

# 2. Apply the schema
mysql archive < /usr/share/nginx/archive/atom-ahg-plugins/ahgAiCompliancePlugin/database/install.sql

# 3. Add the composer dep and install
( cd /usr/share/nginx/archive && composer require ahg/inference-receipts:^0.1 --no-scripts )

# 4. Generate the signing key
sudo -u www-data php symfony ai-compliance:install-key

# 5. Clear cache so the new module + route load
php symfony cc

# 6. Verify the public-key endpoint
curl -s https://psis.theahg.co.za/.well-known/ai-inference-pubkey | jq .

# 7. Schedule weekly verification (cron / systemd timer)
#    php symfony ai-compliance:verify-inference-log --quiet-pass

# 8. Schedule the retention sweep (daily / weekly)
#    php symfony ai-compliance:prune
```

## Verifying a receipt off-host

Any external party can verify a receipt by:

1. Pulling `/.well-known/ai-inference-pubkey` to obtain the public key
   matching the receipt's `kid`.
2. JCS-encoding the receipt's signing view (everything except `entry_hash`
   and `signature`).
3. SHA-256 over the JCS bytes - must equal the stored `entry_hash`.
4. Ed25519 verify the `signature` against the `entry_hash` bytes under the
   public key from step 1.

Test vectors that pass against PSIS receipts must also pass against
Heratio receipts and against the `nobulex` reference - this is the
cross-verification contract.

## Retention

Default 7 years (configurable via the AtoM setting
`ai_compliance_retention_years` or `--years=N` on `ai-compliance:prune`).
Prune nulls `payload_json` past the retention window while preserving seq /
prev_hash / entry_hash / signature, so the chain stays structurally
verifiable indefinitely even when the PII-bearing payload has been wiped.

## Phase-2 follow-up

Wiring the actual AtoM AI service classes (`ahgAIPlugin/lib/Services/*`) to
call `InferenceLogger::log()` after each inference is a separate phase.
This phase ships:

- the plugin scaffold + tables
- the `ai-compliance:install-key`, `verify-inference-log`, `prune` tasks
- the `/.well-known/ai-inference-pubkey` endpoint
- the reference / help docs

Once Phase 2 lands, the existing observability instrumentation in
`ahgProvenancePlugin` and `ahgAIPlugin` will route through the same chain.

## See also

- Standalone library: `ahg/inference-receipts` on Packagist
- Heratio sibling: `packages/ahg-ai-compliance/`
- Plugin README: `ahgAiCompliancePlugin/README.md`
