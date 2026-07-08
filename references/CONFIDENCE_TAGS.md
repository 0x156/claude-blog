# Confidence Tags

Use two separate fields in `references/source-ledger.json`:

- `confidence`: `high`, `medium`, or `low`.
- `evidence_tier`: `EVIDENCE-BASED`, `PRACTITIONER`, `CONTESTED`, or `FOLKLORE`.

## Confidence

`high` means the source directly supports the claim, has a clear date, and is
official, primary, standards-based, or a first-party product/API document for
the fact being cited.

`medium` means the source is useful but directional, such as practitioner SEO
research, vendor market analysis, dynamic datasets, or a single non-official
study with methodology limits.

`low` means the claim is weakly supported, stale, contested, missing methodology,
or safe only as a hypothesis for further verification.

## Evidence Tier

`EVIDENCE-BASED` is for official Google documentation, standards bodies,
first-party API docs, primary controlled datasets, and source-owned product
facts.

`PRACTITIONER` is for SEO/GEO studies, vendor benchmarks, market reports,
observational studies, and expert guidance that can inform operations but should
not be presented as guaranteed behavior.

`CONTESTED` is for claims where credible sources disagree, methodology is
unstable, or the observed effect varies materially by site, market, or query
class.

`FOLKLORE` is for unsupported ranking hacks, undocumented AI visibility
promises, copied industry assumptions, or tactics that lack a dated source.

## Operating Rule

Official facts and practitioner analysis must be separate ledger entries or
separate claims with separate limitations. Never attach named-site impact,
traffic loss, or AI citation claims to an official Google URL unless Google
itself documents that exact claim.
