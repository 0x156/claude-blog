---
type: hub
title: "Blog Quality Score"
status: active
created: 2026-07-06
updated: 2026-07-08
tags: [quality, scorecard, active]
domain: "Blog Quality"
confidence: verified
related:
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Dual Optimization]]"
  - "[[6-Pillar Dual Optimization]]"
  - "[[E-E-A-T for Blog Content]]"
  - "[[AI Citation Mechanics]]"
  - "[[Blog Schema Stack]]"
  - "[[Research Pack Index]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
---

# Blog Quality Score

## Summary

Blog Quality Score is the gate that turns strategy, writing, E-E-A-T, schema, and AI citation readiness into an auditable review.

This hub defines the five-category 100-point quality score for advisory blog audits.

## Score categories

| Category | Points | Pass evidence |
|---|---:|---|
| Content quality | 30 | Reader task is clear, article answers it directly, original examples or experience are present, no filler sections. |
| SEO and intent alignment | 20 | Primary intent, secondary intents, title, headings, internal links, and canonical target match the query class. |
| E-E-A-T and trust | 20 | Author, reviewer, source quality, evidence dates, conflict disclosures, and YMYL escalation are handled. |
| Technical and schema elements | 15 | Indexability, canonical URL, Core Web Vitals evidence when relevant, visible-content schema, and deprecated feature checks pass. |
| AI citation readiness | 15 | Key passages are source-backed, entity-clear, caveated, and measurable without promising AI inclusion. |

## Thresholds

| Score | Label | Action |
|---:|---|---|
| 90-100 | release candidate | Allowed only if no blocker exists and source claims are current. |
| 75-89 | pass with fixes | Publish only after named fixes are accepted by the owner. |
| 60-74 | revision required | Return to editor with category-level remediation. |
| 0-59 | blocked | Do not publish or ship as a client recommendation. |

Any deprecated schema advice, unsupported ranking guarantee, missing source for a current claim, or YMYL escalation failure is an automatic blocker regardless of point total.

## Current fact anchors

- Google helpful content guidance, retrieved 2026-07-06, is the primary source for people-first content quality.
- QRG stability is anchored to the 2025-09-11 revision with no newer revision recorded as of 2026-07-06.
- Google AI optimization guide, last updated 2026-06-29, says no special AI files or special AI schema are required for AI features.
- Google structured data introduction, retrieved 2026-07-06, recommends JSON-LD and requires markup to describe visible content.
- FAQ rich results retired on 2026-05-07, so schema scoring should not reward FAQ rich result expectations.

## Scope

- Define category weights.
- Define pass, warn, and block thresholds.
- Define evidence requirements.
- Define confidence labels.
- Define rollback notes for recommendations.
- Define citation-readiness checks through [[AI Citation Mechanics]].
- Define schema checks through [[Blog Schema Stack]].
- Define trust checks through [[E-E-A-T for Blog Content]].

## Future spoke notes

- [[Quality Score Rubric]]
- [[Content Quality Subscore]]
- [[SEO Intent Subscore]]
- [[E-E-A-T Trust Subscore]]
- [[Technical Schema Subscore]]
- [[AI Citation Readiness Subscore]]
- [[Quality Gate Failure Modes]]
- [[Recommendation Confidence Labels]]
- [[Rollback Note Patterns]]
- [[Delivery Contract Gate]]
- [[Quality Review Evidence Log]]

## Scoring posture

- Score what can be inspected.
- Separate facts from recommendations.
- Penalize missing source dates on current claims.
- Penalize deprecated schema advice.
- Penalize unsupported AI citation promises.
- Escalate YMYL risks.
- Record unknowns instead of fabricating data.
- Keep final decisions advisory in V1.

## Evidence Requirements

- Every current SEO, schema, AI, policy, or market claim needs a source ID or URL plus retrieval date.
- Market studies can inform context but cannot replace first-party property data where property data exists.
- Practitioner GEO tactics must be labeled advisory.
- Missing GSC, GA4, or generative AI report data must be called out instead of estimated.
- Recommendations need a rollback or refresh trigger.

## Example Scored Audits

| Scenario | Content | SEO | Trust | Technical | AI citation | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| Strong expert refresh with current sources, Article schema, and clear passages | 27 | 18 | 18 | 13 | 12 | 88 | Pass with fixes: add rollback note and missing GSC window. |
| Thin roundup with stale FAQ rich result advice | 12 | 10 | 8 | 4 | 5 | 39 | Blocked: deprecated schema and weak evidence. |
| Good draft with practitioner-only GEO claims | 24 | 16 | 15 | 12 | 7 | 74 | Revision required: downgrade GEO claims and add source map. |

## Source posture

- Use official sources for current Google requirements.
- Use QRG as quality framework context, not a direct ranking-factor claim.
- Use practitioner sources only for workflow heuristics.
- Use first-party data when scoring performance evidence.
- Keep score changes appendable through [[log]].

## Related themes

- [[Dual Optimization]]
- [[6-Pillar Dual Optimization]]
- [[Freshness and Content Decay]]
- [[E-E-A-T for Blog Content]]
- [[AI Citation Mechanics]]
- [[Blog Schema Stack]]
- [[Google Data Integrations]]
- [[Research Pack Index]]

## Sources

- Google helpful content guidance, retrieved 2026-07-06.
- Search Quality Rater Guidelines, 2025-09-11.
- Google AI optimization guide, last updated 2026-06-29.
- Google structured data introduction, retrieved 2026-07-06.

## Next actions

- Fill [[Quality Score Rubric]] before scoring examples.
- Fill [[Delivery Contract Gate]] before report rendering.
- Use [[Quality Review Evidence Log]] when a score must be auditable.
- Link confidence labels to [[CONVENTIONS]].
