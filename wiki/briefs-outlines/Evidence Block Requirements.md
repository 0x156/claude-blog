---
type: spoke
title: "Evidence Block Requirements"
domain: "Blog Briefs"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [briefs-outlines, serp-briefs, active]
---

# Evidence Block Requirements

## Evidence Block Requirements Claim Gate

Evidence blocks decide what a draft may assert and what proof must sit beside the assertion. The unit is the claim, not the whole article. A claim can be accepted, caveated, narrowed, escalated, or removed. This note prevents the common failure where a brief has a source list but no mapping from source to claim.

Use `g-helpful-content` for people-first quality recommendations, `g-qrg-full` when a claim has trust or YMYL sensitivity, and `g-ai-opt-guide` for Google AI-feature constraints. Use `g-update-2026-06-05-guidance-on-third-party-seo-tools-services-and-advice` when a source or tool claim drifts toward a ranking, AEO, or GEO guarantee.

### Claim Classes Owned Here

This note owns source requirements for definitions, statistics, workflow recommendations, Google-policy statements, AI-feature statements, YMYL claims, and competitor observations that are about to become prose.

### Escalations Out Of This Note

Send legal, medical, financial, or reputation advice to a qualified reviewer. Send unresolved market forecasts to [[Google Data Integrations]] if first-party data exists. Send SERP-only observations to [[SERP Observation Ledger]] until a source supports the claim.

## Evidence Requirement Table

| Claim type | Minimum evidence | Required caveat | Owner | Verdict discipline | Draft action |
| --- | --- | --- | --- | --- | --- |
| Google Search or AI feature rule | Official Google source such as `g-ai-opt-guide` | State what the source does not promise | SEO lead | CONFIRMED only when the source directly says it | Allow with source ID |
| People-first quality recommendation | `g-helpful-content` plus topic expertise when needed | Do not imply E-E-A-T is a single direct ranking factor | editor | CONFIRMED for guidance, not for guaranteed outcome | Allow with scoped wording |
| Market behavior statistic | Primary study source from [[Brief Source Pack]] | Geography, sample, date, and "not property data" | analyst | AS-REPORTED | Allow as context |
| llms.txt Google tactic | `g-ai-opt-guide` | May be relevant outside Google, but not a Google visibility lever | source steward | CONFIRMED for Google Search stance | Remove unsupported tactic |
| Live SERP pattern | Dated observation plus corroborating source if it becomes a claim | A visible pattern is not a ranking factor | brief owner | SINGLE-SOURCE or lower until supported | Hold or rewrite |

## Approval And Caveat Procedure

1. Rewrite the claim in one plain sentence before choosing evidence.
2. Ask what the source proves and what it leaves unproven.
3. Assign CONFIRMED, AS-REPORTED, CONTESTED, SINGLE-SOURCE, or FOLKLORE from [[Claim To Source Mapping]] practice.
4. Add the caveat beside the claim in the brief, not in a hidden reviewer note.
5. Remove any claim that cannot be sourced or safely narrowed.

## Sources

- `g-helpful-content`
- `g-qrg-full`
- `g-ai-opt-guide`
- `g-update-2026-06-05-guidance-on-third-party-seo-tools-services-and-advice`

## Handoff

Accepted blocks go to [[Brief To Draft Handoff]]. Rejected blocks return to [[Brief Source Pack]] for replacement sources or to [[Brief Risk Notes]] when the issue is approval risk rather than missing evidence.
