"""Adapter tests for the Claude Blog Brain domain pipeline."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from ingest_blog_input import ValidationError, load_blog_input  # noqa: E402
from render_blog_report import render_markdown  # noqa: E402
from synthesize_blog_plan import load_ingested, synthesize  # noqa: E402


FIXTURE = ROOT / "tests" / "fixtures" / "sample-blog-post.json"
PY = sys.executable


def run_cli(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=False)


def test_blog_adapter_happy_path() -> None:
    record = load_blog_input(FIXTURE)
    plan = synthesize(record)
    report = render_markdown(plan)

    assert record["schema"] == "claude-blog-brain.ingested-blog-post.v1"
    assert record["input"]["target_keyword"] == "AI citation ready blog"
    assert record["provenance"]["source_count"] == 3
    assert plan["schema"] == "claude-blog-brain.blog-optimization-plan.v1"
    assert set(plan["scores"]) >= {"overall", "content", "seo", "eeat", "technical", "ai_citation"}
    assert plan["geo_ai_citation_readiness"]["checks"][0]["name"] == "Passage extractability"
    assert any(item["schema_type"] == "FAQPage caveat" for item in plan["schema_recommendations"])
    assert "<table>" in report
    assert "## Prioritized Recommendations" in report
    assert "`g-helpful-content`" in report
    assert "`g-faqpage-sd`" in report


def test_blog_adapter_determinism() -> None:
    first_record = load_blog_input(FIXTURE)
    second_record = load_blog_input(FIXTURE)
    assert first_record == second_record

    first_plan = synthesize(first_record)
    second_plan = synthesize(second_record)
    assert first_plan == second_plan

    first_report = render_markdown(first_plan)
    second_report = render_markdown(second_plan)
    assert first_report == second_report
    assert "--" not in first_report
    assert "\u2014" not in first_report
    assert "\u2013" not in first_report


def test_blog_adapter_invalid_input_error(tmp_path: Path) -> None:
    bad_input = tmp_path / "bad-blog-post.json"
    bad_input.write_text(
        json.dumps(
            {
                "url": "not a url",
                "target_keyword": "AI citation ready blog",
                "locale": "english",
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError) as excinfo:
        load_blog_input(bad_input)

    message = str(excinfo.value)
    assert "missing required key: title" in message
    assert "one of body_markdown or body_html is required" in message
    assert "url must be an absolute URI" in message


def test_blog_adapter_rejects_invalid_iso_dates(tmp_path: Path) -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload["published_at"] = "June 10, 2026"
    bad_input = tmp_path / "bad-iso-date-blog-post.json"
    bad_input.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValidationError) as excinfo:
        load_blog_input(bad_input)

    assert "published_at" in str(excinfo.value)
    assert "ISO date or date-time" in str(excinfo.value)


def test_blog_adapter_rejects_non_http_url(tmp_path: Path) -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload["url"] = "ftp://example.org/post"
    bad_input = tmp_path / "bad-url-blog-post.json"
    bad_input.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValidationError) as excinfo:
        load_blog_input(bad_input)

    assert "url must be an absolute URI" in str(excinfo.value) or "does not match" in str(excinfo.value)


def test_blog_adapter_rejects_wrong_typed_dates(tmp_path: Path) -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload["published_at"] = 20260610
    bad_input = tmp_path / "bad-date-blog-post.json"
    bad_input.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValidationError) as excinfo:
        load_blog_input(bad_input)

    assert "published_at must be a string" in str(excinfo.value)


def test_blog_synthesis_rejects_missing_nested_fields(tmp_path: Path) -> None:
    record = load_blog_input(FIXTURE)
    del record["input"]["title"]
    bad_record = tmp_path / "bad-ingested.json"
    bad_record.write_text(json.dumps(record), encoding="utf-8")

    with pytest.raises(ValidationError) as excinfo:
        load_ingested(bad_record)

    assert "ingested record missing key: input.title" in str(excinfo.value)


def test_unknown_audit_source_is_operator_supplied_uncited(tmp_path: Path) -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload["audit_findings"][0]["source"] = "operator-note"
    bad_source_input = tmp_path / "operator-source-blog-post.json"
    bad_source_input.write_text(json.dumps(payload), encoding="utf-8")

    plan = synthesize(load_blog_input(bad_source_input))
    recommendation = next(item for item in plan["prioritized_recommendations"] if item["id"] == "audit-geo-source-context")

    assert recommendation["source_ids"] == []
    assert recommendation["recommendation"].startswith("operator-supplied (unverified):")
    assert "operator-note" not in {source["id"] for source in plan["source_citations"]}


def test_blog_adapter_script_clis_write_outputs(tmp_path: Path) -> None:
    ingested = tmp_path / "ingested.json"
    plan = tmp_path / "plan.json"
    report = tmp_path / "report.md"

    ingest_proc = run_cli([PY, "scripts/ingest_blog_input.py", str(FIXTURE), "-o", str(ingested)])
    assert ingest_proc.returncode == 0, ingest_proc.stderr
    assert json.loads(ingested.read_text(encoding="utf-8"))["schema"] == "claude-blog-brain.ingested-blog-post.v1"

    synth_proc = run_cli([PY, "scripts/synthesize_blog_plan.py", str(ingested), "-o", str(plan)])
    assert synth_proc.returncode == 0, synth_proc.stderr
    assert json.loads(plan.read_text(encoding="utf-8"))["schema"] == "claude-blog-brain.blog-optimization-plan.v1"

    render_proc = run_cli([PY, "scripts/render_blog_report.py", str(plan), "-o", str(report), "--json-errors"])
    assert render_proc.returncode == 0, render_proc.stderr
    assert "## Prioritized Recommendations" in report.read_text(encoding="utf-8")


def test_blog_adapter_cli_json_error_envelope(tmp_path: Path) -> None:
    bad_input = tmp_path / "bad.json"
    bad_input.write_text('{"url":"ftp://example.org"}', encoding="utf-8")

    proc = run_cli([PY, "scripts/ingest_blog_input.py", str(bad_input)])
    assert proc.returncode == 2
    payload = json.loads(proc.stdout)
    assert payload["ok"] is False
    assert payload["errors"]

    bad_plan = tmp_path / "bad-plan.json"
    bad_plan.write_text("{}", encoding="utf-8")
    render_proc = run_cli([PY, "scripts/render_blog_report.py", str(bad_plan), "--json-errors"])
    assert render_proc.returncode == 2
    render_payload = json.loads(render_proc.stdout)
    assert render_payload["ok"] is False


def test_installed_cli_blog_pipeline(tmp_path: Path) -> None:
    out_dir = tmp_path / "pipeline"
    proc = run_cli([PY, "-m", "claude_blog_brain", "blog-pipeline", "--input", str(FIXTURE), "--out-dir", str(out_dir)])
    assert proc.returncode == 0, proc.stderr
    assert (out_dir / "ingested-blog-post.json").exists()
    assert (out_dir / "blog-optimization-plan.json").exists()
    assert (out_dir / "blog-optimization-report.md").exists()
