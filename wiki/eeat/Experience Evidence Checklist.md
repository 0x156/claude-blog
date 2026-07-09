---
type: spoke
title: "Experience Evidence Checklist"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [eeat, evergreen]
domain: "Blog Trust"
confidence: verified
related:
  - "[[E-E-A-T for Blog Content]]"
  - "[[Author Bio Requirements]]"
  - "[[Reviewer And Expert Review Rules]]"
  - "[[Trust Signal Inventory]]"
  - "[[Source Quality Ladder]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/essentials/spam-policies"
  - "https://www.nngroup.com/articles/ten-usability-heuristics/"
---
# Experience Evidence Checklist

## Experience Evidence Checklist Review Scope

This checklist asks whether the page shows experience a reader can inspect. It is useful for tutorials, reviews, comparisons, operational guides, and case-based posts where the claim depends on having done the work. The QRG and helpful-content sources support experience as part of useful and trustworthy content (source_ids: g-qrg-full, g-helpful-content). Spam-policy evidence matters when many pages reuse the same surface-level claims without new value (source_id: g-spam-policies). NN/g supports placing evidence where the reader needs it, not burying proof in a process note (source_id: nng-editorial-heuristics).

### Evidence Types This Gate Accepts

Accepted evidence includes original photos or screenshots, tested steps, field observations, client or internal anonymized learnings, comparison notes, failed attempts, constraints, and dated update notes. Unsupported adjectives such as "expert", "proven", or "battle-tested" do not count.

### Inputs Required Before Experience Review

Bring the draft, author notes, source pack, product or process artifacts, screenshots if available, and any claim list from [[E-E-A-T Review Rubric]].

## Experience Evidence Pass Fail Table

| Evidence check | Pass condition | Fail condition | Source evidence | Severity | Fix owner |
|---|---|---|---|---|---|
| First-hand claim | Page shows what was observed, tested, used, or implemented | Claim says experience exists but gives no artifact | g-qrg-full, g-helpful-content | High | Author |
| Process specificity | Steps, settings, environment, or constraints are concrete | Advice could apply to any product or case | g-helpful-content, nng-editorial-heuristics | Medium | Editor |
| Example originality | Examples are produced by the team or clearly attributed | Examples are generic paraphrases of common SERP copy | g-spam-policies, g-qrg-full | High | SEO lead |
| Limitations | Page says what the experience does not prove | One case is framed as universal | g-helpful-content, g-qrg-full | High | Reviewer |
| Placement | Evidence appears near the claim it supports | Proof is detached from the section that needs it | nng-editorial-heuristics | Medium | Editor |

## Placement Rules For Experience Signals

Put experience evidence beside the decision it changes. A screenshot belongs near the setup step, a failed-test note belongs near the warning, and a limitation belongs before the reader acts. If the evidence would distract the reader, summarize it in the body and store the detail in the audit record.

## Experience Review Procedure

1. Highlight every claim that asks the reader to trust the author's direct experience.
2. Attach a visible proof type to each highlighted claim.
3. Remove or soften claims that cannot be supported.
4. Escalate expertise-sensitive claims to [[Reviewer And Expert Review Rules]].
5. Record any missing artifacts as next actions in the content brief or rewrite queue.
