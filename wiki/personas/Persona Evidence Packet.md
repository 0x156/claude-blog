---
type: spoke
title: "Persona Evidence Packet"
domain: "Blog Voice"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [personas, voice-style, active]
---

# Persona Evidence Packet

## Persona Evidence Packet Evidence Job

Persona Evidence Packet stores the proof that a persona is real enough to guide content. It captures interviews, support questions, sales notes, query language, survey excerpts, analytics observations, and exclusions. Without this packet, [[Audience Persona Template]] should mark the persona as a hypothesis.

### Persona Facts This Packet Can Own

The packet can own reader jobs, vocabulary, objections, comparison criteria, risk sensitivity, and evidence preferences. It cannot prove market demand or ranking opportunity by itself. Use `g-helpful-content` for audience-usefulness framing, `g-qrg-full` for trust and YMYL caution, `nng-editorial-heuristics` for recognizable wording, and `g-ai-opt-guide` when persona assumptions are used for AI answer readiness. `g-gsc-api` and `g-ga4-data` may support first-party behavioral evidence when exports exist.

### Human Review For Thin Evidence

Escalate when evidence comes from one stakeholder, one anecdote, generated personas, or a sample that excludes the intended reader. Sensitive roles and locales need review through [[YMYL Tone Guardrails]] or [[Locale Voice Adaptation]].

## Persona Evidence Packet Evidence Table

| Evidence type | Required input | Source ID or data route | Verdict discipline | Owner | Next action |
|---|---|---|---|---|---|
| Interview pattern | Date, role, excerpt, consent-safe summary | local evidence plus `g-helpful-content` | advisory until repeated | Research lead | Extract job and objection |
| Search language | Query set, intent note, date range | `g-gsc-api` or keyword source | observed, not persona proof | SEO analyst | Separate wording from need |
| Support or sales theme | Ticket or call theme, count, date | local evidence | stronger if repeated | Customer owner | Add exact pain language |
| Risk flag | Topic sensitivity and reviewer note | `g-qrg-full` | block if unresolved | Editor | Route to tone guardrail |

### Claim, Required Input, Source ID, Verdict, Owner, And Next Action

Each row should say what the evidence proves and what it does not prove. Do not promote a pattern to CONFIRMED unless the evidence is dated, repeated, and appropriate for the content decision.

## Persona Evidence Packet Expiry Check

Refresh evidence when the buyer changes, the product changes, the locale changes, or the draft uses a new risk category. Archive stale persona claims rather than leaving them as quiet assumptions.
