---
type: spoke
title: "Channel Asset Inventory"
domain: "Blog Distribution"
status: active
created: 2026-07-06
updated: 2026-07-09
tags:
  - distribution
  - assets
  - inventory
  - active
confidence: advisory
related:
  - "[[Distribution and Repurposing]]"
  - "[[Canonical Attribution Rules]]"
  - "[[Repurposing Source Fidelity]]"
  - "[[Distribution Measurement Plan]]"
  - "[[Images Audio and Charts]]"
  - "[[Google Data Integrations]]"
  - "[[Voice and Style]]"
  - "[[Zero Click Planning Baseline]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://developers.google.com/analytics/devguides/reporting/data/v1"
  - "https://developers.google.com/search/docs/appearance/google-images"
---

# Channel Asset Inventory

## Channel Asset Inventory Channel Job

Channel Asset Inventory is the distribution control sheet for derivative assets created from one canonical blog post. It answers four questions before publication: what asset exists, which channel owns it, whether the asset still matches the source post, and how performance will be measured. The inventory should be opened before a team creates a thread, email, video, community post, podcast brief, or image card.

### Canonical Post Signals To Preserve

Every row should preserve the canonical URL, the article's main claim, publication or refresh date, source IDs used in the derivative asset, and any caveat that changes interpretation. Use `g-helpful-content` when the asset changes reader value, `g-ai-opt-guide` for Google AI setup statements, and `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` when someone asks whether an AI file is mandatory.

### Channel-Specific Adaptations Allowed

Allowed adaptations include changing the hook, shortening evidence, replacing a chart with alt text or a thumbnail, and shifting the call to action to fit the channel. The asset owner must not turn market context from `sparktoro-zero-click-2026` into a property forecast; point the context to [[Zero Click Planning Baseline]]. Image or thumbnail handling can cite `g-google-images` when visual search eligibility or descriptive alt text matters.

## Channel Asset Inventory Asset Table

| Inventory field | Required decision | Source ids | Evidence state | Owner | Next action |
|---|---|---|---|---|---|
| Canonical source | URL, title, publish date, refresh date | `g-helpful-content` | Confirmed from post | Content owner | Add canonical link to row |
| Asset format | Thread, newsletter, video, community post, podcast, image | [[Distribution and Repurposing]] | Draft until channel selected | Distribution lead | Assign one format per row |
| Source fidelity | Exact claims reused and caveats retained | `g-helpful-content`, [[Repurposing Source Fidelity]] | Needs reviewer signoff | Factcheck owner | Compare against source block |
| AI claim hygiene | No Google AI-only file requirement inserted | `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | Confirmed after copy review | SEO reviewer | Remove unsupported setup tasks |
| Visual provenance | Thumbnail, chart, or screenshot origin and alt text | `g-google-images`, [[Images Audio and Charts]] | Pending until asset file exists | Media owner | Record license or source path |
| Measurement route | Metric, tool, and date window | `g-ga4-data`, [[Distribution Measurement Plan]] | Blocked without access | Analytics owner | Attach report link or gap note |

## Asset, Channel, Source Link, Owner, Status, And Measurement

An inventory row should be boring enough to audit. The status values are planned, drafted, reviewed, shipped, measured, and retired. Measurement belongs in the row only after the metric definition is known; otherwise the row records an evidence gap rather than a speculative target. If a derivative asset is deleted, keep the row and mark the reason so later reporting does not treat missing data as a performance change.

## Channel Asset Inventory Fidelity Checks

1. Open the canonical post and highlight claims reused in the derivative asset.
2. Add the source ID beside each claim that leaves the original page.
3. Verify the channel adaptation changes framing without broadening the claim.
4. Confirm owner, status, and measurement field before the asset is marked shipped.
5. Send unresolved visual, voice, or attribution issues to [[Images Audio and Charts]], [[Voice and Style]], or [[Canonical Attribution Rules]].

## Source IDs Wired

This note cites `g-helpful-content`, `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`, `sparktoro-zero-click-2026`, `g-ga4-data`, and `g-google-images`.
