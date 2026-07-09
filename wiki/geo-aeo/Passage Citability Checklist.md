---
type: spoke
title: "Passage Citability Checklist"
domain: "GEO and AEO"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [geo-aeo, ai-citation, evergreen]
---

# Passage Citability Checklist

## Passage Citability Checklist Review Scope

This checklist is the pre-flight gate for a single passage before it enters an AI Overview, AI Mode, or assistant-answer review. It checks whether the passage is useful to a reader, clear outside its surrounding article, and tied to source evidence. Google sources `g-ai-opt-guide` and `g-ai-features` support the general AI feature and content-foundation posture. `ziptie-aio-source-selection` is advisory passage-craft evidence, while `sparktoro-zero-click-2026` and `seer-aio-impact-ctr-2026` provide market context that must not be turned into a claim of citation or click lift.

### Checks Unique To This Gate

The gate focuses on answer structure, entity naming, nearby evidence, scope limits, and whether a reader would still understand the claim if the passage appeared outside the article.

### Inputs Required Before Review

Bring the passage text, page URL, target query, source IDs for claims, date-sensitive numbers, and any preview-control constraints.

## Passage Citability Checklist Pass Fail Table

| Check | Pass state | Source evidence | Severity | Fix owner | Status |
|---|---|---|---|---|---|
| Answer sentence | The first sentence directly answers the reader job | `ziptie-aio-source-selection` | blocker | Editor | pass, fix, or defer |
| Entity clarity | The target entity is named inside the passage | `g-ai-opt-guide`, `g-ai-features` | blocker | GEO reviewer | pass, fix, or defer |
| Source proximity | The supporting source sits next to the claim | `seer-aio-impact-ctr-2026`, article source IDs | high | Researcher | pass, fix, or defer |
| Market caveat | Broad click behavior is clearly labeled as market context | `sparktoro-zero-click-2026` | medium | Strategist | pass, fix, or defer |
| Measurement path | A later citation check has a metric or explicit missing-data note | `g-genai-reports` | medium | Analyst | pass, fix, or defer |

## Passage Citability Checklist Procedure

1. Read only the candidate passage and mark any missing entity, date, source, or limitation.
2. Compare each claim with its source ID and remove unsupported generalizations.
3. Decide whether the passage is ready for surface-specific review or needs a rewrite.
4. Send failed answer structure to [[Answer Block Extraction Test]] and failed source placement to [[Source Proximity Pattern]].

## Passage Citability Checklist Handoff Rules

A passage passes this checklist only when it is accurate, self-contained, source-adjacent, and clear to a human reader. Passing the checklist means "ready to review", not "likely to be cited".
