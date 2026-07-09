---
type: spoke
title: "Source Confidence Labels"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [sources, research-pack, active]
domain: "Source Evidence"
confidence: verified
related:
  - "[[Research Pack Index]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Google Algorithm Update Ledger]]"
  - "[[Google Data Integrations]]"
  - "[[Evidence Gap Register]]"
  - "[[Source URL Canonicalization]]"
  - "[[Research Release Gate Notes]]"
  - "[[Source Ledger Reading Guide]]"
  - "[[Current Requirements Digest]]"
  - "[[Claim To Source Mapping]]"
  - "[[Source Refresh Cadence]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/fundamentals/third-party-seo"
  - "https://blog.google/products-and-platforms/products/search/search-io-2026/"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://ziptie.dev/blog/google-ai-overviews-source-selection/"
---

# Source Confidence Labels

## Summary
This spoke defines claim-level confidence labels for wiki notes. The label belongs to the weakest evidence needed for the actual recommendation, not the strongest source in the bibliography.

The source ledger has separate `confidence` values such as high, medium, and low. This wiki uses operational labels below because a high-quality source can still support only a narrow claim.

## Allowed Labels

| Label | Use when | Downgrade when | Example |
|---|---|---|---|
| verified | A current official, primary, standards, government, regulator, API, or first-party source directly supports the exact claim, date, and surface. | The claim generalizes beyond the source, source date fields are mixed, raw provenance is missing for a release claim, or the source is outside the affected platform. | Google AI optimization guide last updated 2026-06-29 says Google Search does not use llms.txt. |
| evidence-based | Multiple trustworthy sources or one strong primary source supports an observed pattern, but it is not an official requirement for the local site. | The evidence is market-average only, property-specific without access to the property, or methodologically narrow. | First-party GSC data plus a market study show AIO exposure affects a content class. |
| practitioner | A practitioner source describes a workflow, test, heuristic, or observed tactic without official confirmation. | It is presented as a durable rule, ranking factor, traffic guarantee, or AI citation guarantee. | ZipTie passage-format guidance for AI Overviews source selection. |
| advisory | The recommendation combines verified facts with judgment, market context, practitioner heuristics, or local policy. | Any required claim is missing a source ID, URL, retrieval date, confidence label, or refresh trigger. | AI citation readiness checklist using Google facts plus GEO heuristics. |
| contested | Trustworthy sources conflict, or studies disagree because of different samples, periods, surfaces, or methods. | One source is later found irrelevant, or first-party property data resolves the practical decision. | AIO CTR effect estimates from separate market studies. |
| gap | Evidence is missing, stale, date-mismatched, source-mismatched, raw-provenance-missing, or outside the source coverage. | A dated trustworthy source is recorded in [[Claim To Source Mapping]] and, for release use, the machine ledger and raw provenance are corrected. | `g-product-sd` date mismatch for the July 7 merchant listing update. |

## Downgrade Rules

- A note with any practitioner-only operational claim cannot be `confidence: verified` unless verified facts and practitioner guidance are split into separate claim rows.
- A note that mixes verified Google facts with market studies or workflow heuristics should use `confidence: advisory` at note level even if individual rows are verified.
- Market-study statistics stay advisory until first-party property data confirms the local pattern.
- Official Google Search documentation supports Google Search claims only; it does not prove behavior for ChatGPT, Perplexity, Copilot, or other non-Google assistants.
- Google AI developer documentation supports model and provenance claims about Google AI products only; it does not clear rights, consent, or client publication policy.
- A source URL without source ID, retrieval date, and refresh trigger cannot support a release-gate claim.
- A live source whose page date conflicts with the machine ledger becomes `gap` until the date model is repaired.
- Confidence follows the weakest source needed for the recommendation.

## Label Examples

| Claim | Label | Why |
|---|---|---|
| Google Search does not use llms.txt for Search visibility. | verified | Directly stated in Google AI optimization guide, retrieved 2026-07-09. |
| Keep important answer passages concise and source-near. | practitioner | Useful GEO workflow, but supported by practitioner guidance rather than an official Google rule. |
| AIO citation increases clicks by a fixed percent for this client. | gap | Market studies cannot be applied to a client without first-party data. |
| Generated images need model, rights, consent, disclosure, and provenance review. | advisory | Combines Google AI docs, C2PA provenance standard, and local publication policy. |
| The Product intro page was updated on 2026-07-07. | gap | Live Product intro page shows 2025-12-10; July 7 applies to merchant listing documentation. |

## Audit Checks

- Every current claim has a row in [[Claim To Source Mapping]] or a gap in [[Evidence Gap Register]].
- Every `pending:` source ID has a corresponding gap owner and due date.
- Current claims include exact dates such as 2026-07-09 instead of relative wording.
- Deprecated features are not scored as current tactics.
- Advisory or practitioner evidence is never phrased as a guarantee.

## Related
- [[Research Pack Index]]
- [[index|Index]]
- [[hot|Hot]]
- [[Google Algorithm Update Ledger]]
- [[Google Data Integrations]]
- [[Evidence Gap Register]]
- [[Source URL Canonicalization]]
- [[Research Release Gate Notes]]
- [[Source Ledger Reading Guide]]
- [[Current Requirements Digest]]
- [[Claim To Source Mapping]]
- [[Source Refresh Cadence]]

## Source URLs
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
- https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf
- https://developers.google.com/search/docs/fundamentals/third-party-seo
- https://blog.google/products-and-platforms/products/search/search-io-2026/
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://ziptie.dev/blog/google-ai-overviews-source-selection/
