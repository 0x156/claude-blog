---
type: hub
title: "Blog Quality Score"
status: active
created: 2026-07-06
updated: 2026-07-09
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

## Point Rubric

| Category | Subcheck | Points | Full-credit evidence | Zero-credit condition |
|---|---|---:|---|---|
| Content quality | Reader job and answer | 8 | The first screen states the reader job and gives a direct, useful answer. | The article delays the answer, changes topic, or has no clear reader task. |
| Content quality | Originality and information gain | 8 | Includes first-hand experience, examples, data, screenshots, expert review, or original synthesis. | Mostly repeats common SERP claims or generic definitions. |
| Content quality | Completeness without padding | 6 | Covers necessary subquestions and caveats without filler sections. | Inflated word count, thin subsections, or unsupported superlatives. |
| Content quality | Source integration | 5 | Important factual claims have nearby source IDs, dates, and visible caveats. | Current claims are unsourced or sources are separated from claims. |
| Content quality | Editorial clarity | 3 | Headings, paragraphs, and examples are scan-friendly and reader-centered. | Unclear structure, vague pronouns, or confusing transitions. |
| SEO and intent alignment | Intent match | 6 | Primary and secondary intent are named and mapped to sections. | Query class is guessed or contradicted by the content. |
| SEO and intent alignment | Title and heading fit | 4 | Title, H1, H2s, and intro match the canonical target without stuffing. | Headings chase keywords but do not serve the reader. |
| SEO and intent alignment | Internal link logic | 4 | Links support topic depth and cluster coverage without irrelevant anchors. | No useful internal links or links are only promotional. |
| SEO and intent alignment | Freshness and decay | 3 | Dates, screenshots, and claims are refreshed or marked stale. | Old data is presented as current. |
| SEO and intent alignment | Measurement plan | 3 | GSC, GA4, or missing-data notes define how performance will be checked. | Performance claims rely only on market averages. |
| E-E-A-T and trust | Author and reviewer | 5 | Author, reviewer, and qualification evidence match topic sensitivity. | Anonymous or unqualified advice on sensitive topics. |
| E-E-A-T and trust | Evidence quality | 5 | Uses official, primary, first-party, or clearly caveated practitioner sources. | Low-quality roundups or generated summaries support important claims. |
| E-E-A-T and trust | Transparency | 4 | Discloses affiliations, generated assistance, review date, and limitations when relevant. | Material conflicts or generated content are hidden. |
| E-E-A-T and trust | YMYL escalation | 4 | YMYL-adjacent content has expert review or a defer/decline path. | Sensitive guidance is published without review. |
| E-E-A-T and trust | Reputation and corrections | 2 | Notes reputation evidence and correction path. | No owner for corrections or reputation risk. |
| Technical and schema elements | Indexability and canonical | 4 | Canonical URL, indexability, redirects, and crawl blockers are checked or marked unavailable. | Basic indexability facts are unknown. |
| Technical and schema elements | Structured data fit | 4 | Markup describes visible content and uses current Google-supported features. | Markup invents facts or uses deprecated rich-result promises. |
| Technical and schema elements | Media and accessibility | 3 | Images, video, charts, alt text, captions, and source data are reviewed. | Media carries unsupported claims or inaccessible text. |
| Technical and schema elements | Performance evidence | 2 | Core Web Vitals, page experience, or missing-data caveat is recorded when relevant. | Performance is guessed. |
| Technical and schema elements | Validation trail | 2 | Validation tools, warnings, and unresolved issues are recorded. | No reproducible validation record. |
| AI citation readiness | Answer block quality | 4 | Important passages are self-contained, date-aware, entity-clear, and source-backed. | Passages are vague or unsupported. |
| AI citation readiness | Google AI guidance compliance | 4 | No llms.txt, chunking, AI-only schema, or inauthentic mention advice is sold as a Google requirement. | GEO tactic is framed as official Google guidance without source. |
| AI citation readiness | Entity and source proximity | 3 | Entities, authors, dates, and citations are close to claims. | Claims cannot be extracted without losing context. |
| AI citation readiness | Measurement caveat | 2 | AI Overview, AI Mode, and assistant exposure are measured only where supported. | AI citation or traffic uplift is promised. |
| AI citation readiness | Risk controls | 2 | Advisory confidence, rollback, and refresh triggers are present. | No path to revise stale AI-surface guidance. |

## Current fact anchors

- Google helpful content guidance, retrieved 2026-07-09, is the primary source for people-first content quality.
- QRG stability is anchored to the 2025-09-11 revision with no newer revision recorded as of 2026-07-09.
- Google AI optimization guide, last updated 2026-06-29, says no special AI files or special AI schema are required for AI features.
- Google structured data introduction, retrieved 2026-07-09, recommends JSON-LD and requires markup to describe visible content.
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
- A score cannot pass if the evidence table contains `gap` for a claim that affects the recommendation.
- A score must name the weakest confidence label used in the recommendation.

## Example Scored Audits

| Scenario | Content | SEO | Trust | Technical | AI citation | Total | Decision | Required fix |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Expert refresh with current Google sources, visible Article schema, and clear answer blocks | 27 | 18 | 18 | 13 | 12 | 88 | Pass with fixes | Add rollback note and missing GSC comparison window before publication. |
| Thin roundup with stale FAQ rich result advice and no author evidence | 12 | 10 | 8 | 4 | 5 | 39 | Blocked | Remove deprecated schema promise, rebuild source map, add qualified review. |
| Good draft with practitioner-only GEO claims but no first-party measurement | 24 | 16 | 15 | 12 | 7 | 74 | Revision required | Downgrade GEO claims, add source map, and add missing-data note. |
| Ecommerce blog post with valid Product content but missing July 7 merchant listing review | 25 | 17 | 16 | 9 | 10 | 77 | Pass with fixes | Review `Product.category`, sale duration fields, and ledger gap before final schema advice. |

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

- `g-helpful-content`: Google helpful content guidance, retrieved 2026-07-09.
- Search Quality Rater Guidelines, 2025-09-11.
- `g-ai-opt-guide`: Google AI optimization guide, last updated 2026-06-29.
- `g-intro-sd`: Google structured data introduction, retrieved 2026-07-09.
- `g-update-2026-05-07-faq-rich-results-retired`: FAQ rich result retirement, event date 2026-05-07.
- `g-search-docs-updates-2026-07-07-product-structured-data`: merchant listing documentation update, event date 2026-07-07.

## Next actions

- Fill [[Quality Score Rubric]] before scoring examples.
- Fill [[Delivery Contract Gate]] before report rendering.
- Use [[Quality Review Evidence Log]] when a score must be auditable.
- Link confidence labels to [[CONVENTIONS]].
