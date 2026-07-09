---
type: spoke
title: "Intent Fit Writing Pass"
domain: "Blog Writing"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [writing, six-pillar, evergreen]
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://ziptie.dev/blog/google-ai-overviews-source-selection/"
---

# Intent Fit Writing Pass

## Intent Fit Writing Pass Drafting Job

This pass checks whether each article section matches the reader intent the page promised to serve. It happens after the brief and outline exist but before the writer polishes paragraphs. Intent fit is a writing decision here, not a keyword-volume exercise.

### Fit Signals This Note Reviews

The pass compares the target reader job, the page type, the opening promise, the H2 sequence, and the internal links. `g-helpful-content` anchors the people-first requirement. `g-qrg-full` helps identify cases where intent mismatch can become a trust problem. `g-ai-opt-guide` and `ziptie-aio-source-selection` matter when a section is expected to answer a question directly enough for AI citation review.

### Sections This Pass Sends Elsewhere

If the mismatch is caused by a weak topic cluster, use [[Semantic Topic Clusters]]. If the problem is evidence selection, use [[Claim Source Pairing Pattern]]. If the article is trying to answer two different reader jobs, consider merge, split, or repositioning through [[SERP-Informed Briefs and Outlines]].

## Intent Fit Mapping Table

| Page or section | Target intent | Canonical owner | Anchor or handoff | Evidence state | Action |
|---|---|---|---|---|---|
| Article introduction | Confirm the reader job and promise | [[Blog Introduction Patterns]] | First 150 words | `g-helpful-content` | Rewrite if promise is broad |
| Core H2 answer | Resolve the main task | [[Answer First Section Pattern]] | Primary H2 | `g-helpful-content`, `g-ai-opt-guide` | Move answer upward |
| Trust or expertise block | Prove why advice is credible | [[Experience Signal Placement]] | Byline, method, case, reviewer | `g-qrg-full` | Add visible proof |
| Citation candidate passage | Provide extractable answer with source | [[Citation Ready Paragraphs]] | H2 or H3 paragraph | `g-ai-opt-guide`, `ziptie-aio-source-selection` | Tighten entity and claim |
| Next-step link | Continue the reader's task | [[Internal Link Placement Rules]] | Contextual link | `g-helpful-content` | Add or remove link |

## Intent Fit Editing Procedure

1. Write the primary reader intent in one sentence.
2. Label every H2 as answer, proof, example, comparison, caveat, or next step.
3. Delete or move sections that serve a different reader job.
4. Check that AI-facing answer blocks still serve the human task.
5. Add internal links only where the reader would naturally need the next note.
6. Send unresolved page-scope conflicts back to the brief owner.

## Source Handling

This pass cites `g-helpful-content`, `g-ai-opt-guide`, `g-qrg-full`, and `ziptie-aio-source-selection`. Use these IDs to judge fit and boundaries, not to infer demand or traffic.

## Related

- [[SERP-Informed Briefs and Outlines]]
- [[Semantic Topic Clusters]]
- [[Internal Link Placement Rules]]
- [[Reader Satisfaction Test]]
