---
type: spoke
title: "Audience Persona Template"
domain: "Blog Voice"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [personas, voice-style, active]
---

# Audience Persona Template

## Audience Persona Template Voice Job

Audience Persona Template turns scattered audience notes into a usable writing constraint before [[SERP-Informed Briefs and Outlines]] or [[FLOW Framework]] asks for a draft. The output is a one-page persona card with the reader's job, trigger, decision stage, topic knowledge, objections, risk sensitivity, and preferred proof type. It should stop writers from assuming that every reader wants the same depth, examples, or CTA.

### Persona Or Brand Constraint Owned Here

This spoke owns reader context, not brand slogans. Use `g-helpful-content` for the people-first test, `g-qrg-full` for purpose and trust sensitivity, `nng-editorial-heuristics` for recognition and error-prevention cues, and `g-ai-opt-guide` when the persona work mentions AI Search visibility. Query language from `g-ads-kw` can inform vocabulary, but it is not proof of a persona by itself.

### Situations That Require Human Editorial Review

Escalate when the persona includes legal, medical, financial, civic, or safety pressure; when the only evidence is a stakeholder guess; or when the draft changes advice for a vulnerable reader. Route YMYL sensitivity to [[YMYL Tone Guardrails]], brand limits to [[Brand Voice Inventory]], and phrase restrictions to [[Banned Claims And Phrases]].

## Audience Persona Template Decision Table

| Decision | Required input | Source IDs | Evidence state | Owner | Next action |
|---|---|---|---|---|---|
| Reader job | Interview note, support ticket, SERP intent, or sales call summary | `g-helpful-content`, `g-ads-kw` | advisory until first-party evidence exists | Strategist | Write one task the article must help complete |
| Knowledge level | Draft topic, glossary, known questions | `nng-editorial-heuristics` | editorial heuristic | Editor | Set vocabulary and explanation depth |
| Risk sensitivity | Topic category, claim list, reviewer note | `g-qrg-full` | high for trust-sensitive subjects | Reviewer | Mark cautious tone or expert review need |
| AI-facing context | Request mentions AI answers, snippets, or llms.txt | `g-ai-opt-guide` | official Google guidance | SEO lead | Link to [[AI Citation Mechanics]] without promising citation |

### Constraint, Example, Allowed Variant, Banned Variant, And Scope

The persona card should include an approved example sentence and a forbidden version. "Compare two payroll options without assuming legal expertise" is useful. "Write for busy founders" is too vague unless it names the decision, evidence, and risk. A persona may adjust example order, vocabulary, and proof density; it may not expand a claim past its source.

## Audience Persona Template Drift Check

Refresh the card when the product, target locale, buyer role, regulatory risk, or source packet changes. If a persona has no evidence after review, mark it as a hypothesis and block it from driving tone or examples.
