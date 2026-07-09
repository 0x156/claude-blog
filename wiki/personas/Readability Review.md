---
type: spoke
title: "Readability Review"
domain: "Blog Voice"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [personas, voice-style, active]
---

# Readability Review

## Readability Review Clarity Job

Readability Review checks whether a draft can be scanned, understood, and acted on by the intended reader. It is not a grammar-only pass. It inspects the answer order, heading jobs, sentence load, example placement, source proximity, and whether caveats appear before the reader could misapply the advice.

### Reader Burden Owned Here

Use `g-helpful-content` to test whether the page satisfies a reader purpose, `g-qrg-full` when trust or YMYL sensitivity raises the clarity bar, `nng-editorial-heuristics` for recognition and error-prevention heuristics, and `g-ai-opt-guide` when a readability change is proposed for AI answer surfaces. `g-ai-features` is relevant only when the draft discusses Google's documented AI feature behavior.

### Human Review For Meaning Changes

Escalate if simplifying a sentence changes the claim, removes a condition, drops a source date, or changes who the advice applies to. If the problem is tone, send it to [[Brand Voice Inventory]]; if it is a forbidden promise, use [[Banned Claims And Phrases]].

## Readability Review Inspection Table

| Check | Evidence | Fix | Owner | Exit signal |
|---|---|---|---|---|
| Lead answer | Reader job and draft intro | Move answer before context | Editor | First paragraph states the usable answer |
| Heading scan | H2 and H3 outline | Rename headings by section job | Strategist | A skimmer can predict section value |
| Sentence load | Dense paragraphs and caveats | Split condition, action, and limit | Editor | No key caveat is buried |
| Source proximity | Claim and citation distance | Place source cue near the claim | Factchecker | Claim remains verifiable outside the paragraph |

### Check, Evidence, Fix, Owner, And Exit Signal

The reviewer should mark pass, revise, or block for each check. A draft can pass readability while still failing evidence; in that case [[Research Pack Index]] owns the blocker.

## Readability Review Regression Check

Run this pass after major edits, localization, repurposing, and schema rewrites. If a later edit improves fluency but weakens source accuracy, revert the sentence and reopen the relevant voice note.
