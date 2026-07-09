---
type: spoke
title: "Recommendation Confidence Labels"
domain: "Blog Quality"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [quality, scorecard, active]
confidence: advisory
related:
  - "[[Blog Quality Score]]"
  - "[[Quality Review Evidence Log]]"
  - "[[Quality Gate Failure Modes]]"
  - "[[Delivery Contract Gate]]"
---

# Recommendation Confidence Labels

## Recommendation Confidence Labels Distinct Job

This note standardizes the confidence language used in quality reviews. Its job is to stop advisory SEO and GEO recommendations from sounding more certain than the evidence allows. It follows the verdict discipline from `references/claim-ledger.md`: confirmed, as-reported, single-source, contested, folklore, blocked, and unknown must not be collapsed into one generic "verified" label. The source IDs wired here are `g-ai-opt-guide`, `g-update-2026-06-05-guidance-on-third-party-seo-tools-services-and-advice`, `g-gsc-api`, and `seer-aio-impact-ctr-2026`.

## Inputs Specific To Recommendation Confidence Labels

Inputs are the claim text, source IDs, source type, retrieval date, evidence tier, methodology limit, owner, and whether first-party data exists. A recommendation about people-first content can often be confirmed from Google guidance. A recommendation about zero-click behavior should usually be as-reported unless client data independently supports it.

## Decisions Recommendation Confidence Labels Must Record

- Whether the claim is confirmed, advisory, blocked, unknown, or contested.
- Whether a practitioner source is being used as context or as proof.
- Whether the recommendation can ship as written.
- Which owner can refresh or downgrade the label later.

## Recommendation Confidence Labels Scorecard Evidence Table

| Label | Required inputs | Source IDs | Evidence state | Owner | Next action |
|---|---|---|---|---|---|
| Confirmed | Official or primary source, current date, matching claim. | `g-ai-opt-guide`; `g-gsc-api`; `g-update-2026-06-05-guidance-on-third-party-seo-tools-services-and-advice`. | Source directly supports the recommendation. | Research owner | Allow use with refresh date. |
| Advisory | Useful evidence with limits or missing property data. | `seer-aio-impact-ctr-2026` when used for AIO context. | Source informs decision but does not prove outcome. | Strategy owner | Add caveat and measurement plan. |
| Blocked | Source contradicts the recommendation. | `g-ai-opt-guide` for required special-file claims, or `g-update-2026-06-05-guidance-on-third-party-seo-tools-services-and-advice` for vendor certainty. | Recommendation cannot ship. | SEO reviewer | Rewrite or remove. |
| Unknown | No adequate ledger source or property evidence. | None until logged. | Evidence gap remains open. | Assigned reviewer | Move to [[Quality Review Evidence Log]]. |

## Source IDs, Evidence, Owner, Confidence, And Next Action

The label belongs beside the recommendation, not at the bottom of the packet. Do not use "verified" for a claim that is only as-reported. Do not use "blocked" as a style preference. The label should tell the delivery owner whether to publish, caveat, revise, or hold.

## Recommendation Confidence Labels Operating Procedure

1. Rewrite the claim in one inspectable sentence.
2. Match it to a source ID or mark a gap.
3. Apply the strictest valid label.
4. Add owner, refresh date, and next action.
5. Send blocked items to [[Quality Gate Failure Modes]].
