---
type: spoke
title: "Information Gain Checklist"
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

# Information Gain Checklist

## Information Gain Checklist Review Scope

This checklist decides whether the draft adds useful content beyond what a competent reader would already find in common SERP summaries. Information gain can come from original examples, sharper distinctions, data interpretation, field constraints, decision rules, or clearer caveats. It cannot be simulated by longer prose.

### Checks Unique To This Gate

This gate looks for new reader value inside the draft, not just accurate sourcing. `g-helpful-content` supports the standard that content should be helpful and reliable. `g-qrg-full` raises the trust burden for topics where weak advice can harm the reader. `ziptie-aio-source-selection` is relevant only after a distinct answer exists; it cannot create the substance itself.

### Inputs Required Before Review

Before using this checklist, gather the target reader job, the outline, competitor or SERP observations, approved source IDs, and any first-party examples. AI-facing claims must stay inside `g-ai-opt-guide`, and broad AI visibility context should link to [[AI Citation Mechanics]] rather than repeat a market line.

## Information Gain Pass Fail Table

| Check | Pass evidence | Fail signal | Source evidence | Severity | Fix owner |
|---|---|---|---|---|---|
| Distinct answer | The article states a position or decision rule | It paraphrases common summaries | `g-helpful-content` | Major | Writer |
| Original proof | Example, method, data, or field note is visible | Claims are true but interchangeable | `g-qrg-full` | Major | Editor |
| Useful caveat | Limitation changes reader action | Caveat is generic or absent | `g-helpful-content`, `g-qrg-full` | Blocker for sensitive claims | Reviewer |
| Extractable substance | Self-contained answer contains real evidence | Passage is concise but empty | `g-ai-opt-guide`, `ziptie-aio-source-selection` | Advisory to major | GEO reviewer |
| Reader advancement | The reader can decide next step | Post ends with awareness only | `g-helpful-content` | Major | Strategist |

## Information Gain Handoff Rules

1. If no row passes, send the article back to brief or research instead of editing style.
2. If only the extractable-substance row fails, route to [[Citation Ready Paragraphs]].
3. If proof exists but is misplaced, route to [[Experience Signal Placement]].
4. If the missing value is strategic positioning, return to [[SERP-Informed Briefs and Outlines]].
5. If the topic is trust-sensitive, require editor approval before the draft enters [[Blog Quality Score]].

## Source Handling

This note cites `g-helpful-content`, `g-ai-opt-guide`, `g-qrg-full`, and `ziptie-aio-source-selection`. It does not cite market benchmarks because this pass measures draft substance, not search behavior.

## Related

- [[6-Pillar Dual Optimization]]
- [[Experience Signal Placement]]
- [[SERP-Informed Briefs and Outlines]]
- [[Blog Quality Score]]
