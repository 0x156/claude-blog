---
type: spoke
title: "SERP Observation Ledger"
domain: "Blog Briefs"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [briefs-outlines, serp-briefs, active]
---

# SERP Observation Ledger

## SERP Observation Ledger Record Scope

This ledger records dated observations that informed a brief: visible result types, source categories, AI features, freshness cues, media formats, competing page types, and gaps. It does not declare ranking factors. It gives later reviewers enough context to understand why a brief made a structural choice and when that choice should be revisited.

Use dated SERP capture or a provider source such as `dfs-api` for visible-result facts. Cite `g-ai-features` when the observation involves Google AI surfaces or preview controls, and use `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` when a visible page claims llms.txt has Google Search impact. Use `sparktoro-zero-click-2026` only as market context for measurement caveats.

### Captured Events

Capture query, date, locale, device, signed-in state if known, result features, top source types, visible dates, and notable absence of expected source types. Screenshots or exports can support the observation, but the note itself must summarize the finding.

### Routed Elsewhere

Send source-validation work to [[Brief Source Pack]], claim approval to [[Evidence Block Requirements]], and SERP-pattern interpretation to [[Competitive Pattern Notes]]. This ledger stores observations so those notes do not treat memory as evidence.

## Observation Register Table

| Observation item | Source ID or evidence | Owner | Confidence | Status | Next review date | Rollback trigger |
| --- | --- | --- | --- | --- | --- | --- |
| AI Overview appears for query variant | `g-ai-features` plus dated SERP capture | SEO lead | medium unless repeated | active | 2026-08-09 | Feature disappears or query intent changes |
| Competitor promotes llms.txt as Google tactic | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | source steward | high for caveat | do-not-copy | 2026-08-06 | Google publishes different guidance |
| Results favor comparison tables | Dated SERP capture via `dfs-api` or manual log | strategist | medium | observe | next brief refresh | New dominant format appears |
| Low-click planning affects metric choice | `sparktoro-zero-click-2026` | analyst | medium, practitioner | advisory | 2026-08-06 | First-party GSC contradicts market framing |
| Page-quality gap is visible across competitors | Observation plus [[Evidence Block Requirements]] | editor | medium | action candidate | next outline QA | Better source pack changes the angle |

## SERP Observation Ledger Review Loop

1. Record the observation before it is used in the brief.
2. Label the observation as visual, source-type, feature, freshness, or gap.
3. Decide whether it can influence structure, evidence, risk, or metric framing.
4. Add a review date when the observation is volatile or tied to a live feature.
5. Roll back brief assumptions when the observation disappears, contradicts first-party data, or gains a stronger source.

## Sources

- `dfs-api`
- `g-ai-features`
- `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`
- `sparktoro-zero-click-2026`

## Handoff

Send current observations to [[Competitive Pattern Notes]] for interpretation and to [[Search Intent Classification]] when the observation changes the intent label. Keep raw source decisions out of this ledger unless they are linked back to [[Brief Source Pack]].
