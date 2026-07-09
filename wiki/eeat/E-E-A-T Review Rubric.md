---
type: spoke
title: "E-E-A-T Review Rubric"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [eeat, evergreen]
domain: "Blog Trust"
confidence: verified
related:
  - "[[E-E-A-T for Blog Content]]"
  - "[[Author Bio Requirements]]"
  - "[[Experience Evidence Checklist]]"
  - "[[Source Quality Ladder]]"
  - "[[Editorial Transparency Checklist]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/essentials/spam-policies"
  - "https://www.nngroup.com/articles/ten-usability-heuristics/"
---
# E-E-A-T Review Rubric

## E-E-A-T Review Rubric Scoring Job

This rubric turns E-E-A-T review into a scored editorial decision. It is used after a draft, refresh candidate, or content audit has a defined reader task. The score is not a Google ranking prediction. It is a practical way to decide whether the page can move forward, needs expert review, or should be rewritten. Source IDs `g-helpful-content` and `g-qrg-full` set the quality frame, `g-spam-policies` identifies abuse boundaries, and `nng-editorial-heuristics` supports clear review feedback.

### Criteria This Score Owns

The rubric owns page purpose, first-hand evidence, expertise fit, authority support, trust transparency, and AI or scaled-content risk. It also records blockers that override a numeric score.

### Criteria Routed To Sibling Scores

Do not score schema implementation, Core Web Vitals, AI citation likelihood, or traffic impact here. Send those to [[Blog Schema Stack]], [[Google Data Integrations]], [[AI Citation Mechanics]], or [[Blog Quality Score]] as appropriate.

## Rubric Evidence And Blocker Table

| Criterion | Points or severity | Required proof | Blocking failure | Source ids |
|---|---:|---|---|---|
| Clear useful purpose | 20 points | Reader task, article promise, and answer path are aligned | Page cannot say who it helps or why | g-helpful-content |
| Experience signal | 20 points | Examples, tests, observations, or operational notes are visible | Experience is claimed but not shown | g-qrg-full, nng-editorial-heuristics |
| Expertise and review fit | 20 points | Author or reviewer evidence matches the claim risk | Sensitive claim lacks qualified review | g-qrg-full |
| Source and authority support | 20 points | Claims map to strong, dated sources or reputation evidence | High-stakes claim rests on weak citation | g-helpful-content, g-qrg-full |
| Trust and transparency | 10 points | Byline, update context, limitations, and ownership are clear | Material limitation is hidden | g-qrg-full, nng-editorial-heuristics |
| Scaled or low-value risk | Blocker | Draft shows original contribution and avoids mass-produced sameness | Mostly copied, paraphrased, or generic AI output | g-spam-policies, g-qrg-full |

## Point Weights, Required Proof, And Blockers

Treat any blocker as more important than the total. A page with a high score but missing expert review on a risky claim is not ready. A page below 70 should enter a rewrite queue. A page from 70 to 84 can proceed only with named fixes. A page at 85 or above can move forward if no blocker exists and all source IDs are current.

## E-E-A-T Rubric Review Procedure

1. Write the reader task in one sentence and confirm that the draft actually serves it.
2. Fill each row with page evidence, not intent from the content brief.
3. Link weak rows to the owning spoke: [[Author Bio Requirements]], [[Source Quality Ladder]], [[Experience Evidence Checklist]], or [[Editorial Transparency Checklist]].
4. Mark blocker rows before calculating the score.
5. Add a confidence label based on the weakest source required for the recommendation.
6. Attach the rubric result to the audit or rewrite plan without promising search outcomes.
