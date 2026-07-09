---
type: spoke
title: "FLOW Confidence Tags"
domain: "Blog Workflow"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [flow, active]
confidence: advisory
related:
  - "[[FLOW Framework]]"
  - "[[FLOW Source Intake]]"
  - "[[FLOW Factcheck Stage]]"
  - "[[FLOW Approval Queue]]"
  - "[[Research Pack Index]]"
---

# FLOW Confidence Tags

## Confidence Tagging Purpose

FLOW Confidence Tags tells the operator how strongly a recommendation or claim may be used before it reaches a brief, draft, report, or approval queue. It borrows verdict discipline from `references/claim-ledger.md`: CONFIRMED claims can support operating rules, AS-REPORTED studies need scope notes, CONTESTED claims need caution, and FOLKLORE should not be used as advice. The tag is attached to the claim, not to the whole page.

## Tag Assignment Matrix

| Claim or recommendation | Source evidence | Claim-ledger posture | FLOW tag | Owner action | Handoff |
|---|---|---|---|---|---|
| Reader usefulness or people-first review | `g-helpful-content` | CONFIRMED when applied to usefulness guidance | Verified | Use as quality gate | [[FLOW Review Stage]] |
| AI optimization advice based on normal Search fundamentals | `g-ai-opt-guide` | CONFIRMED for Google guidance | Verified | Keep recommendation narrow | [[FLOW Draft Stage]] |
| Statement that Google Search does not require `llms.txt` | `g-ai-opt-guide` | CONFIRMED for current Google guidance | Verified | Remove contrary recommendation | [[2026 Google Update Timeline]] |
| Market or AI Overview click context | `sparktoro-zero-click-2026`, `seer-aio-impact-ctr-2026` | AS-REPORTED with methodology limits | Advisory | Add scope caveat and avoid forecast language | [[AI Citation Mechanics]] |
| Claim that lacks dated source support | None accepted | FOLKLORE until sourced | Blocked | Return to intake | [[FLOW Source Intake]] |

## Source-To-Tag Rules

Official Google documents can still be misused if the note turns guidance into a guarantee. For example, `g-helpful-content` supports evaluating usefulness, but it does not promise ranking results. `g-ai-opt-guide` blocks special-file myths, but it does not prove that a passage will be cited. SparkToro and Seer evidence can inform visibility planning; each needs its method near the recommendation that relies on it.

## Claim Verdict Crosswalk

Use `Verified` for direct official support, `Advisory` for practitioner or market evidence, `Contested` when the ledger says sources conflict, and `Blocked` when the source packet is missing dates, retrieval metadata, or a defensible verdict. A claim can move from `Blocked` to `Advisory` after [[FLOW Factcheck Stage]] records the source and limitation. It moves to [[FLOW Approval Queue]] when the action affects live content.

## Control Checks Before Handoff

Before handoff, confirm that the tag appears beside the claim it qualifies. Do not place one confidence label at the bottom of a report and let it cover unrelated statements. If a source ID is missing, the tag is incomplete.
