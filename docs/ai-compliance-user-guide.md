---
title: AI Compliance - Article 12 receipts
slug: ai-compliance-user-guide
category: ai
order: 80
---

# AI Compliance user guide

PSIS records every AI inference call in a tamper-evident chain so auditors
(internal or external) can verify the system has not been silently rewritten.
This is how PSIS satisfies EU AI Act Article 12.

## What gets logged

Every call to an AI service - LLM completion, HTR extraction, NER tagging,
OCR, translation, guardrail check - produces one row in the `ai_inference_log`
table. Each row contains:

- the service name, model id and model version
- a SHA-256 fingerprint of the input and of the output (full bodies are not
  retained by default)
- the timestamp, request id, user id (if logged in) and tenant id
- a chain hash that links to the previous row
- an Ed25519 signature

Modifying or deleting a row breaks the chain at a detectable point. The
verifier task walks the chain end-to-end and reports the first tamper site.

## Where to find the public key

The signing public key is published at:

```
https://psis.theahg.co.za/.well-known/ai-inference-pubkey
```

Any external auditor or sibling system can use that key to verify receipts
offline.

## Verifying the log

A site administrator can verify the chain at any time:

```
php symfony ai-compliance:verify-inference-log
```

A successful run prints `PASS - <N> receipts verified in <ms> ms`. A failed
run prints the first broken sequence number and a hint for inspection. Wire
this task into your monitoring (cron + alert on non-zero exit) so any
tampering is surfaced within hours.

## Retention

By default the full payload of each receipt is kept for 7 years (`payload_json`
column). After the retention window, a daily sweep nulls `payload_json` while
preserving the row, its chain hash and its signature - the chain is still
verifiable, the PII-bearing payload is gone.

Change the window in AtoM settings (`ai_compliance_retention_years`) or
override per-run with `--years=N`.

## Rotating the signing key

When you rotate (annually, or on suspected compromise):

```
sudo -u www-data php symfony ai-compliance:install-key --rotate --force
```

The new key becomes active for new receipts; the old key stays in
`ai_inference_key` with `rotated_at` set, so historic receipts continue
to verify under the key that signed them.

## What this does not do

The chain proves the receipts have not been tampered with. It does not
prove the receipts were complete - that depends on the AI services
actually calling the logger after each inference. Once the Phase-2
wire-up ships, every AI service in `ahgAIPlugin` will log to the chain.

## See also

- Plugin README: `plugins/ahgAiCompliancePlugin/README.md`
- Reference doc: `ai-compliance-article-12.md`
- EU AI Act Article 12 (enforcement: 2 August 2026)
