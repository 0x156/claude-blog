---
type: spoke
title: "Terminology Control List"
domain: "Blog Voice"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [personas, voice-style, active]
---

# Terminology Control List

## Terminology Control List Naming Job

Terminology Control List keeps preferred terms, forbidden terms, acronyms, synonyms, product names, and definitions consistent across the blog. It prevents a cluster from calling the same concept by five names or using a keyword variant that changes the meaning. It supports [[Semantic Topic Clusters]], [[Voice and Style]], and [[SERP-Informed Briefs and Outlines]].

### Terms Owned By This Control

Use `g-helpful-content` for reader clarity, `g-qrg-full` for trust-sensitive wording, `nng-editorial-heuristics` for consistency, and `g-ai-opt-guide` when terminology touches AI Search features. `g-nlp` can support entity extraction workflows, but an API label is not a brand definition.

### Human Review For Risky Names

Escalate regulated terms, competitor names, legal entity names, medical claims, financial terms, and product names that conflict with source evidence. Send prohibited phrasing to [[Banned Claims And Phrases]] and localized naming to [[Locale Voice Adaptation]].

## Terminology Control List Governance Table

| Term | Preferred use | Forbidden use | Source or basis | Owner | Action |
|---|---|---|---|---|---|
| AI citation readiness | Editorial review state | Guaranteed inclusion in AI answers | `g-ai-opt-guide`, [[AI Citation Mechanics]] | GEO reviewer | Keep caveat in templates |
| Helpful content | Reader-usefulness standard | A magic ranking label | `g-helpful-content` | Editor | Tie to concrete reader outcome |
| YMYL | Higher-risk topic class | Generic seriousness label | `g-qrg-full` | Reviewer | Require source and expert check |
| Brand product name | Exact approved capitalization | Keyword-stuffed variant | Brand source plus glossary | Brand owner | Update cluster references |

### Term, Preferred Use, Forbidden Use, Source, Owner, And Action

Each row should include an example sentence and the contexts where the term applies. A synonym is allowed only when it helps the reader and does not break entity clarity.

## Terminology Control List Drift Scan

Scan new briefs, rewritten intros, title tags, schema names, and localized variants. If multiple names are already indexed, record the cleanup plan before changing published copy.
