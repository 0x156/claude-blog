# References

This folder is the evidence spine for Claude Blog Brain.

- `source-ledger.json` records dated sources, retrieval dates, confidence,
  evidence tier, limitations, and supported claims.
- `claim-ledger.md` records high-impact claims, verdicts, second-source status,
  and usage limits.
- `CONFIDENCE_TAGS.md` defines the confidence enum and evidence-tier policy.
- `current-requirements.md` summarizes volatile operating requirements after
  they are supported by ledger entries.
- `market-research.md` summarizes buyer and market evidence with practitioner
  caveats where appropriate.
- `canon/` contains stable source-led notes for recurring policy and workflow
  claims.
- `adapter-manifest.json` records adapter maturity truth. It is generic-only
  until the implementation and test gates are release-verified.

## Rules

- Do not add a source to prose only. Add it to `source-ledger.json` first.
- Do not reuse an official source URL for third-party impact, named-site, CTR,
  or traffic claims.
- Do not promote a practitioner study to high-confidence official evidence.
- Do not use a month-only or year-only date without `date_precision`.
- Do not call the brain market-ready until raw snapshots, hashes, citations,
  adapter tests, and the release audit all pass.
