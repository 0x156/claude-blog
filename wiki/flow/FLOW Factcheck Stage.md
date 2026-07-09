---
type: spoke
title: "FLOW Factcheck Stage"
domain: "Blog Workflow"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [flow, active]
confidence: advisory
related:
  - "[[FLOW Framework]]"
  - "[[FLOW Draft Stage]]"
  - "[[FLOW Confidence Tags]]"
  - "[[Research Pack Index]]"
  - "[[AI Citation Mechanics]]"
---

# FLOW Factcheck Stage

## Factcheck Purpose

FLOW Factcheck Stage verifies current claims, statistics, citations, sensitive language, and source scope before a recommendation is delivered. It is not a copyedit pass. It tests whether the draft's evidence can carry the exact sentence being made and whether the verdict should be confirmed, advisory, contested, or blocked.

## Claim Classes Requiring Checks

Check Search policy, AI feature claims, schema advice, performance language, market statistics, and any recommendation that could alter live content. Use [[Research Pack Index]] for source lookup and [[FLOW Confidence Tags]] for verdict language. AI-file language is checked against Google guidance and the June 2026 ledger entry (source_ids: `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`). Retired FAQ rich-result claims use the schema changelog (source_id: `g-faqpage-sd`). Market statistics remain AS-REPORTED and are checked against the cited study, such as SparkToro (source_id: `sparktoro-zero-click-2026`).

## Verification Register Table

| Check item | Evidence required | Action | Verdict label | Owner | Handoff |
|---|---|---|---|---|---|
| People-first content claim | Source packet with dated retrieval | Confirm the sentence matches guidance | CONFIRMED if direct | Factchecker | [[FLOW Review Stage]] |
| AI optimization instruction | `g-ai-opt-guide` | Remove special-file or special-schema overreach | CONFIRMED for correction | SEO factchecker | [[FLOW Draft Stage]] |
| `llms.txt` mention | June 2026 update source ID | Mark unsupported as a Google requirement | CONFIRMED correction | SEO factchecker | [[2026 Google Update Timeline]] |
| Zero-click statistic or conclusion | `sparktoro-zero-click-2026` with method caveat | Retain only as market context | AS-REPORTED | Strategy reviewer | [[AI Citation Mechanics]] |
| Unsourced new claim | Source packet absent | Block the claim or send to intake | BLOCKED | Editor | [[FLOW Source Intake]] |

## Escalation Rules

Escalate when a draft makes a legal, medical, financial, reputation, or platform policy statement without sufficient evidence. Escalate also when a source is dated but does not prove the operational recommendation. A factcheck can approve wording, request rewrite, or block publication advice, but it does not mutate external systems in V1.

## Exit Packet

The exit packet contains checked claims, rejected claims, source IDs, verdicts, unresolved gaps, and the owner of each correction. Items that affect live content move to [[FLOW Approval Queue]] with a rollback note.
