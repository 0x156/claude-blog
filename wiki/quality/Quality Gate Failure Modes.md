---
type: spoke
title: "Quality Gate Failure Modes"
domain: "Blog Quality"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [quality, scorecard, active]
confidence: advisory
related:
  - "[[Blog Quality Score]]"
  - "[[Delivery Contract Gate]]"
  - "[[Recommendation Confidence Labels]]"
  - "[[Rollback Note Patterns]]"
---

# Quality Gate Failure Modes

## Quality Gate Failure Modes Review Scope

This note defines the defects that stop or slow a delivery packet even when the total score looks acceptable. The scope is severity classification, not rewriting. Use `g-helpful-content` for people-first and source-backed content concerns, `g-spam-policies` for abuse-pattern blockers, `g-ai-opt-guide` for supposed Google AI file requirements, and `seer-aio-impact-ctr-2026` only as AS-REPORTED AIO context.

## Checks Unique To This Gate

- Blockers that override numerical scores.
- Warnings that permit handoff only with named fixes.
- Advisory issues that can be monitored after delivery.
- Unknowns that need source work before a recommendation can be verified.

## Inputs Required Before Review

The reviewer needs the scored asset, subscore evidence, source IDs, confidence label, rollback trigger, and owner list. Missing inputs should be recorded as unknown rather than converted into assumed facts. This is especially important for property data, AI visibility, and technical validation claims.

## Quality Gate Failure Modes Pass Fail Table

| Check | Pass state | Source evidence | Severity | Fix owner |
|---|---|---|---|---|
| Current claim sourcing | Each current claim has a source ID and date. | `g-helpful-content` or other relevant ledger ID. | Blocker when absent. | Research owner |
| AI-file requirement language | Draft rejects required `llms.txt` or AI-only schema myths. | `g-ai-opt-guide`. | Blocker when contradicted. | SEO reviewer |
| Market statistic use | Third-party study is caveated and not a property forecast. | `seer-aio-impact-ctr-2026`; [[AI Citation Mechanics]]. | Warning or blocker by impact. | Strategy owner |
| Reader usefulness | Article has a reader job and direct answer. | `g-helpful-content`. | Blocker for thin content. | Editor |
| Rollback readiness | Live-impact recommendation has a trigger and owner. | [[Rollback Note Patterns]]. | Warning unless risk is high. | Delivery owner |

## Evidence, Severity, Owner, And Fix Status

Severity should describe the operational consequence, not the reviewer mood. A blocker prevents delivery. A warning allows delivery only after the named owner accepts the risk or fix. An advisory item stays in the packet as a monitoring note. Unknown means the team lacks evidence and must not rewrite the gap as a fact.

## Quality Gate Failure Modes Handoff Rules

1. Start with blockers, then warnings, then advisory items.
2. Assign one fix owner to each row.
3. Move evidence gaps to [[Quality Review Evidence Log]].
4. Apply [[Recommendation Confidence Labels]] before handoff.
5. Send unresolved blockers to [[Delivery Contract Gate]] as blocked.
