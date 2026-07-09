---
type: spoke
title: "Reader Satisfaction Test"
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

# Reader Satisfaction Test

## Reader Satisfaction Test Drafting Job

This test asks whether the target reader could stop searching after reading the article. It is the human outcome check for [[6-Pillar Dual Optimization]]. Passing extraction, schema, or keyword checks is not enough if the article leaves the reader without a clear answer, useful proof, or next step.

### Satisfaction Signals This Note Measures

The reader should see the main answer early, understand the conditions where it changes, trust the source path, and know what to do next. `g-helpful-content` is the primary source for people-first review. `g-qrg-full` supports stronger scrutiny where trust and expertise affect the reader's decision. `g-ai-opt-guide` keeps AI-facing advice inside normal Search guidance rather than making a separate hidden objective.

### What Counts As A Failed Reader Outcome

The article fails when it answers a keyword but not the task, cites sources without explaining what they prove, adds caveats that are too late to matter, or optimizes passages in a way that fragments the reading experience. A post can also fail by turning a dated Google clarification, such as the llms.txt stance in `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`, into a broad recommendation that the source does not support.

## Reader Satisfaction Test Table

| Review point | Required input | Source IDs | Evidence state | Owner | Next action |
|---|---|---|---|---|---|
| Main answer visibility | Intro and first H2 | `g-helpful-content` | Official people-first baseline | Editor | Move answer up |
| Decision completeness | Reader task and article promise | `g-helpful-content`, `g-qrg-full` | Official quality lens | Strategist | Add missing criterion |
| Trust clarity | Byline, reviewer, sources, dates | `g-qrg-full` | Official quality-evaluator source | Lead editor | Add proof or caveat |
| AI boundary honesty | AI-facing claims and caveats | `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | Official Google Search boundary | GEO reviewer | Remove unsupported AI task |
| Next step usefulness | Conclusion and internal links | `g-helpful-content` | Editorial judgment | Writer | Add or simplify handoff |

## Reader Satisfaction Editing Procedure

1. Give the draft to a reviewer who has not seen the brief.
2. Ask them to state the answer, evidence, and next step in three sentences.
3. Mark every place where they had to infer missing context.
4. Rewrite sections that require another search for the basic answer.
5. Confirm that internal links deepen the task instead of replacing the answer.
6. Score the revised draft through [[Six Pillar Editing Rubric]].

## Source Handling

This note cites `g-helpful-content`, `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`, and `g-qrg-full`.

## Related

- [[6-Pillar Dual Optimization]]
- [[Blog Conclusion Patterns]]
- [[Intent Fit Writing Pass]]
- [[Six Pillar Editing Rubric]]
