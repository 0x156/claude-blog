---
type: spoke
title: "Delivery Contract Gate"
domain: "Blog Quality"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [quality, scorecard, active]
confidence: advisory
related:
  - "[[Blog Quality Score]]"
  - "[[Quality Gate Failure Modes]]"
  - "[[Quality Review Evidence Log]]"
  - "[[Rollback Note Patterns]]"
---

# Delivery Contract Gate

## Delivery Contract Gate Deliverable Boundary

This gate decides whether a blog draft or audit packet is ready to hand off, needs revision, or must stay blocked. It is the last quality note before delivery, but it does not publish, mutate a CMS, or approve live changes by itself. Its evidence is operational: `g-helpful-content` supports reader-value review, `g-update-2026-06-05-guidance-on-third-party-seo-tools-services-and-advice` blocks vendor certainty, `g-gsc-api` supports first-party query evidence, and `g-genai-reports` covers June 2026 AI Overview and AI Mode reporting.

## Required Inputs And Exclusions

Required inputs are the scored object, owner, score summary, open blockers, source IDs, confidence label, and rollback trigger. Excluded inputs are private credentials, unpublished client system data, and any claim that cannot be cited or explicitly marked unknown. The gate should not infer access to GSC or generative AI reports when the packet does not include `g-gsc-api` or `g-genai-reports` evidence.

## Required Output Sections

- Final status: ready, revise, blocked, or monitor.
- Score summary with one sentence per subscore.
- Open blocker list with owner and due date.
- Evidence source map for current claims.
- Rollback or review note for any recommendation that could affect visibility or trust.

## Delivery Gate Acceptance Table

| Required section | Mandatory fields | Validator | Acceptance condition | Handoff owner |
|---|---|---|---|---|
| Object summary | Title, URL or draft ID, target query, locale | Editor | The reviewed asset is unambiguous. | Content lead |
| Score snapshot | Five subscores, total, lowest confidence | Quality reviewer | No hidden blocker overrides the score. | Quality lead |
| Source map | Source IDs, retrieval dates, claim locations | Evidence owner | Current claims map to ledger-backed IDs. | Research owner |
| Risk flags | YMYL, AI, schema, market-data caveats | Specialist reviewer | High-risk items have an explicit decision. | Assigned specialist |
| Handoff status | Ready, revise, blocked, monitor | Gate owner | Status matches unresolved evidence. | Delivery owner |
| Rollback trigger | Trigger, metric, date, responsible person | Operator | Reversal or review path is written before implementation. | Implementation owner |
| Missing data note | Absent GSC, AI report, crawl, or CWV source | Gate owner | Missing evidence is explicit, not inferred as pass. | Delivery owner |
| Vendor claim screen | Tool promise, source ID, confidence label | SEO reviewer | No vendor certainty conflicts with Google guidance. | SEO owner |

## Field, Validator, Evidence, Owner, And Blocker State

Every accepted packet needs a named person for evidence and a separate person for delivery. If one person owns both, record that explicitly. A blocked state is required when a source is missing for a current claim, when an AI inclusion guarantee appears, or when the draft recommends a Google Search tactic contradicted by the assigned AI guidance sources.

## Delivery Contract Gate Handoff Procedure

1. Confirm all score spokes have current evidence rows.
2. Translate unresolved gaps into revise or blocked items.
3. Attach the confidence label and rollback note.
4. Send ready packets to the human delivery owner.
5. Send blocked packets back to the spoke that owns the failure.

## Gate Decision Example

A draft has 91 points and one AI-reporting claim.
The packet includes GSC export evidence from `g-gsc-api`.
It lacks generative AI reporting evidence from `g-genai-reports`.
Decision: monitor, not ready.
The score remains visible, but the status changes.
The owner adds a missing-data note.
The recommendation avoids vendor certainty using `g-update-2026-06-05-guidance-on-third-party-seo-tools-services-and-advice`.

## Gate-Specific Breaks

- A ready label appears before the rollback owner exists.
- GSC evidence is assumed because the client has Search Console.
- AI Overview reporting is claimed without `g-genai-reports`.
- A vendor tool verdict outranks Google source boundaries.
- A blocked source gap is hidden as a stylistic edit.

## Consuming Deliverables

[[Blog Write Article Contract]] consumes the final gate state.
Inputs provided: score summary, blockers, risk flags, rollback trigger.
Expected output: release, revise, or blocked article package.
[[Blog Analyzer Score Report]] consumes gate language.
It expects action-list status and owner fields.
The gate sends unresolved source gaps back to [[Quality Review Evidence Log]].
