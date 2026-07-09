"""Tests for wiki substance scoring."""
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_brain import check_wiki_substance  # noqa: E402


def write_source_ledger(root: Path, sources: dict[str, str]) -> None:
    references = root / "references"
    references.mkdir(parents=True)
    payload = {
        "sources": [
            {"id": source_id, "url": url}
            for source_id, url in sorted(sources.items())
        ]
    }
    (references / "source-ledger.json").write_text(json.dumps(payload), encoding="utf-8")


def unique_words(seed: str, count: int = 135) -> str:
    return " ".join(f"{seed}-substance-{index}" for index in range(count))


def write_spoke(root: Path, folder: str, title: str, source_url: str, body: str) -> Path:
    path = root / "wiki" / folder / f"{title}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
type: spoke
title: "{title}"
domain: "Fixture Domain"
status: active
created: 2026-07-09
updated: 2026-07-09
tags: [fixture, active]
source_urls:
  - "{source_url}"
---
{body}
""",
        encoding="utf-8",
    )
    return path


def clean_body(title: str, seed: str) -> str:
    return f"""# {title}

## {title} Evidence Table

| Check | Specific action |
|---|---|
| {seed} proof | Record dated evidence before the recommendation is used. |

## {title} Operating Notes

{unique_words(seed)}
"""


def cloned_body(title: str) -> str:
    shared = unique_words("shared-clone", 150)
    return f"""# {title}

## Shared Evidence Table

| Check | Specific action |
|---|---|
| clone proof | Record dated evidence before the recommendation is used. |

## Shared Operating Notes

{shared}
"""


def test_clean_distinct_spoke_set_passes(tmp_path: Path) -> None:
    sources = {
        "source-alpha": "https://example.org/source-alpha",
        "source-beta": "https://example.org/source-beta",
        "source-gamma": "https://example.org/source-gamma",
    }
    write_source_ledger(tmp_path, sources)
    write_spoke(tmp_path, "concepts", "Alpha Note", sources["source-alpha"], clean_body("Alpha Note", "alpha"))
    write_spoke(tmp_path, "writing", "Beta Note", sources["source-beta"], clean_body("Beta Note", "beta"))
    write_spoke(tmp_path, "schema", "Gamma Note", sources["source-gamma"], clean_body("Gamma Note", "gamma"))

    ok, score, notes, critical, details = check_wiki_substance(tmp_path)

    assert ok is True
    assert score == 100
    assert notes == []
    assert critical == []
    assert details["metrics"]["spoke_count"] == 3
    assert details["metrics"]["near_duplicate_pairs"] == 0
    assert details["metrics"]["table_or_procedure_coverage"] == 1.0
    assert details["metrics"]["specific_citation_coverage"] == 1.0
    assert details["metrics"]["density_floor"] >= 120


def test_near_duplicate_spoke_pair_fails_with_critical(tmp_path: Path) -> None:
    sources = {
        "source-alpha": "https://example.org/source-alpha",
        "source-beta": "https://example.org/source-beta",
    }
    write_source_ledger(tmp_path, sources)
    write_spoke(tmp_path, "concepts", "Clone One", sources["source-alpha"], cloned_body("Clone One"))
    write_spoke(tmp_path, "writing", "Clone Two", sources["source-alpha"], cloned_body("Clone Two"))
    write_spoke(tmp_path, "schema", "Distinct Note", sources["source-beta"], clean_body("Distinct Note", "distinct"))

    ok, score, notes, critical, details = check_wiki_substance(tmp_path)

    assert ok is False
    assert score <= 40
    assert details["metrics"]["near_duplicate_pairs"] == 1
    assert critical
    assert "wiki_substance near_duplicate_pairs=1" in critical[0]
    pair_paths = details["offenders"]["near_duplicate_pairs"][0]["paths"]
    assert "wiki/concepts/Clone One.md" in pair_paths
    assert "wiki/writing/Clone Two.md" in pair_paths
    assert any("near duplicate spoke pairs: 1" == note for note in notes)
