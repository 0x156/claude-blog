---
type: spoke
title: "Six Pillar Editing Rubric"
domain: "Blog Writing"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [writing, six-pillar, evergreen]
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
---

# Six Pillar Editing Rubric

## Six Pillar Editing Rubric Scoring Job

This rubric turns the six writing pillars into an editing score that can block handoff. It is a draft-readiness tool, not an attempt to model Google's ranking systems. The score should expose what to fix, who owns the fix, and which source boundary controls the judgment.

### Criteria This Score Owns

The rubric owns intent fit, information gain, experience placement, answer-first structure, evidence proximity, and reader satisfaction. `g-helpful-content` supports the people-first quality baseline. `g-qrg-full` adds a quality-evaluator lens for expertise and trust. `g-ai-opt-guide` and `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` keep AI-readiness scoring from rewarding unsupported special files or hidden tactics.

### Criteria Delegated To Other Scores

Technical structured data belongs to [[Blog Schema Stack]]. Performance data belongs to [[Google Data Integrations]]. Freshness triage belongs to [[Freshness and Content Decay]]. The rubric may point to those notes, but it should not score what it cannot inspect in the draft.

## Rubric Evidence Table

| Criterion | Points or severity | Required proof | Blocking failure | Source IDs |
|---|---|---|---|---|
| Intent fit | 20 points | Reader job matches intro, H2s, and conclusion | Article serves a different task than the brief | `g-helpful-content` |
| Information gain | 20 points | Original example, method, data interpretation, or decision rule | Draft repeats common summaries without new value | `g-helpful-content`, `g-qrg-full` |
| Experience and trust | 20 points | Visible author, method, reviewer, or field evidence | Trust-sensitive claim lacks responsible proof | `g-qrg-full` |
| Answer and passage clarity | 15 points | Important sections answer before expanding | Core answer is buried or fragmented | `g-ai-opt-guide` |
| Source proximity | 15 points | Claim, source ID, date, and caveat stay near each other | Current claim has no nearby source | `g-helpful-content`, `g-ai-opt-guide` |
| AI boundary discipline | Blocker control | AI-facing advice stays within documented Google guidance | Draft recommends llms.txt for Google Search visibility | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` |
| Reader satisfaction | 10 points | Reviewer can state answer, evidence, and next step | Reader needs another search to complete the task | `g-helpful-content` |

## Rubric Review Procedure

1. Score the draft after source pairing and paragraph edits, not before.
2. Mark any blocker first; do not average a blocker into a passing score.
3. Assign a fix owner for each criterion below full credit.
4. Record the weakest evidence source that affected the score.
5. Send schema, freshness, or analytics defects to their owner notes.
6. Re-score only the changed sections unless the article promise moved.

## Source Handling

This rubric wires `g-helpful-content`, `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`, and `g-qrg-full`. It intentionally excludes broad market studies because this score is about draft quality, not market demand.

## Related

- [[6-Pillar Dual Optimization]]
- [[Blog Quality Score]]
- [[Reader Satisfaction Test]]
- [[Claim Source Pairing Pattern]]
