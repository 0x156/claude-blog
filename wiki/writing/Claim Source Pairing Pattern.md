---
type: spoke
title: "Claim Source Pairing Pattern"
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

# Claim Source Pairing Pattern

## Claim Source Pairing Pattern Evidence Job

This note owns the pairing of a claim in draft prose to the source type that can support it. It is a gate before paragraphs become citation-ready. The output is a source pairing row, not a rewritten article section.

### Source Types This Note Owns

Official Google sources can support claims about Google Search guidance, AI feature documentation, and quality principles when the claim matches the page. The QRG source (`g-qrg-full`) supports quality-evaluator concepts, not a direct ranking formula. Practitioner sources may guide tactics only when labeled as practitioner evidence. For the assigned writing set, this note uses `g-helpful-content`, `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`, and `g-qrg-full`.

### Claims This Note Must Not Validate Alone

Do not validate traffic lift, AI citation probability, ranking recovery, or click-through impact from these four sources. Do not use the llms.txt update as proof that non-Google assistants ignore the file. Do not use QRG language to imply that raters directly alter rankings for the reviewed page. Escalate broad market statistics to [[Claim To Source Mapping]] and AI-search caveats to [[AI Citation Mechanics]].

## Source Pairing Table

| Source ID | URL | Date basis | Claim coverage | Limitation | Refresh cadence |
|---|---|---|---|---|---|
| `g-helpful-content` | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | last updated 2025-12-10, retrieved 2026-07-09 | People-first content checks and E-E-A-T framing | Does not score a page or guarantee performance | Monthly or Search Central change |
| `g-ai-opt-guide` | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | last updated 2026-06-15, retrieved 2026-07-08 | AI feature optimization stays on normal Search foundations | Does not promise AI Overview or AI Mode inclusion | Monthly plus changelog watch |
| `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 2026-06-15 documentation event | Google Search does not use llms.txt for visibility | Does not settle other AI systems | Recheck on [[2026 Google Update Timeline]] update |
| `g-qrg-full` | https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf | published 2025-09-11, retrieved 2026-07-08 | Quality evaluator terminology and trust lens | Not an operational ranking API | Monthly revision watch |

## Claim Source Pairing Refresh Procedure

1. Rewrite the draft claim without marketing language.
2. Name the source ID that can actually prove the claim.
3. Add the verdict discipline from `references/claim-ledger.md`: CONFIRMED, CONTESTED, AS-REPORTED, SINGLE-SOURCE, or FOLKLORE.
4. Record the date that makes the claim refreshable.
5. If the source only partly supports the claim, weaken the claim before editing the paragraph.
6. Send unresolved pairs to [[Evidence Gap Register]] rather than filling gaps with inference.

## Related

- [[Citation Ready Paragraphs]]
- [[Evidence Density For Blog Posts]]
- [[Research Pack Index]]
- [[AI Citation Mechanics]]
