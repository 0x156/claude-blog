#!/usr/bin/env python3
"""Detect content decay from two Google Search Console page exports.

The default path is offline: pass a current-period JSON export and a matching
previous-period JSON export. Each export may be either a JSON list of rows or a
GSC helper result with a top-level ``rows`` list. Rows should include a page or
url field plus clicks and impressions.

Optional live export path:
    python3 skills/blog-google/scripts/run.py gsc_query --property sc-domain:example.com --dimensions page --json

Usage:
    python content_decay.py current.json previous.json
    python content_decay.py current.json previous.json --threshold 0.20 --metric clicks
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SEVERITY_RANK = {
    "critical": 3,
    "high": 2,
    "warning": 1,
}


class ContentDecayError(ValueError):
    """Raised when an export cannot be used for content decay analysis."""


def _as_number(value: Any) -> float:
    """Return value as a nonnegative float, using 0 for missing values."""
    if value is None:
        return 0.0
    try:
        number = float(value)
    except (TypeError, ValueError):
        return 0.0
    return max(number, 0.0)


def _row_page(row: dict[str, Any]) -> str | None:
    """Extract a page URL from common GSC row shapes."""
    for key in ("page", "url", "URL", "landingPage", "landing_page"):
        value = row.get(key)
        if value:
            return str(value)

    keys = row.get("keys")
    if isinstance(keys, list):
        for value in keys:
            if not value:
                continue
            text = str(value)
            if text.startswith(("http://", "https://", "/")):
                return text
    return None


def load_export(path: str | Path) -> list[dict[str, Any]]:
    """Load a GSC export from a JSON file and return its row list."""
    export_path = Path(path)
    try:
        raw = export_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ContentDecayError(f"Could not read {export_path}: {exc}") from exc

    if not raw.strip():
        raise ContentDecayError(f"{export_path} is empty.")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ContentDecayError(f"{export_path} is not valid JSON: {exc.msg}") from exc

    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict) and isinstance(data.get("rows"), list):
        rows = data["rows"]
    else:
        raise ContentDecayError(
            f"{export_path} must be a JSON list or an object with a rows list."
        )

    if not rows:
        raise ContentDecayError(f"{export_path} contains no rows.")

    if not all(isinstance(row, dict) for row in rows):
        raise ContentDecayError(f"{export_path} rows must be JSON objects.")

    return rows


def aggregate_pages(rows: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    """Aggregate GSC rows by page and sum clicks and impressions."""
    pages: dict[str, dict[str, float]] = {}
    for row in rows:
        page = _row_page(row)
        if not page:
            continue
        if page not in pages:
            pages[page] = {"clicks": 0.0, "impressions": 0.0}
        pages[page]["clicks"] += _as_number(row.get("clicks"))
        pages[page]["impressions"] += _as_number(row.get("impressions"))
    return pages


def classify_severity(decline: float) -> str:
    """Classify decline severity using fixed content decay thresholds."""
    if decline >= 0.60:
        return "critical"
    if decline >= 0.40:
        return "high"
    return "warning"


def _decline(previous: float, current: float) -> float:
    if previous <= 0:
        return 0.0
    return max((previous - current) / previous, 0.0)


def recommend_action(
    *,
    metric: str,
    threshold: float,
    severity: str,
    dropped_out: bool,
    current: dict[str, float],
    previous: dict[str, float],
) -> tuple[str, str]:
    """Return a recommended action and a short reason."""
    previous_clicks = previous.get("clicks", 0.0)
    previous_impressions = previous.get("impressions", 0.0)
    current_metric = current.get(metric, 0.0)
    previous_metric = previous.get(metric, 0.0)

    if previous_clicks <= 3 and previous_impressions <= 100:
        return (
            "prune",
            "The page had low prior demand, so pruning may be better than a rewrite.",
        )

    if dropped_out:
        return (
            "consolidate/redirect",
            "The page disappeared from the current export, so merge or redirect it if a stronger page exists.",
        )

    if metric == "clicks" and previous_impressions > 0:
        impression_decline = _decline(
            previous_impressions, current.get("impressions", 0.0)
        )
        if impression_decline < threshold:
            return (
                "investigate query shift",
                "Clicks fell while impressions held up, which can point to ranking, CTR, or query mix changes.",
            )

    if severity == "critical" and current_metric <= max(1.0, previous_metric * 0.10):
        return (
            "consolidate/redirect",
            "The loss is severe enough that consolidation may recover value faster than a light refresh.",
        )

    return (
        "refresh/update content",
        "The page still has measurable demand, so update the content, title, internal links, and freshness signals.",
    )


def analyze_decay(
    current_rows: list[dict[str, Any]],
    previous_rows: list[dict[str, Any]],
    *,
    threshold: float = 0.20,
    metric: str = "clicks",
) -> dict[str, Any]:
    """Compare two GSC exports and return a structured content decay report."""
    if metric not in {"clicks", "impressions"}:
        raise ContentDecayError("Metric must be clicks or impressions.")
    if threshold < 0 or threshold > 1:
        raise ContentDecayError("Threshold must be between 0 and 1.")

    current_pages = aggregate_pages(current_rows)
    previous_pages = aggregate_pages(previous_rows)

    if not current_pages:
        raise ContentDecayError("Current export has no usable page rows.")
    if not previous_pages:
        raise ContentDecayError("Previous export has no usable page rows.")

    decays: list[dict[str, Any]] = []

    for page, previous in previous_pages.items():
        current = current_pages.get(page, {"clicks": 0.0, "impressions": 0.0})
        previous_metric = previous.get(metric, 0.0)
        current_metric = current.get(metric, 0.0)
        dropped_out = page not in current_pages

        if previous_metric <= 0:
            continue

        decline = _decline(previous_metric, current_metric)
        if decline < threshold and not dropped_out:
            continue

        severity = classify_severity(decline)
        action, reason = recommend_action(
            metric=metric,
            threshold=threshold,
            severity=severity,
            dropped_out=dropped_out,
            current=current,
            previous=previous,
        )
        decays.append(
            {
                "page": page,
                "severity": severity,
                "decline": round(decline, 4),
                "decline_percent": round(decline * 100, 1),
                "metric": metric,
                "current_metric": round(current_metric, 2),
                "previous_metric": round(previous_metric, 2),
                "current_clicks": round(current.get("clicks", 0.0), 2),
                "previous_clicks": round(previous.get("clicks", 0.0), 2),
                "current_impressions": round(current.get("impressions", 0.0), 2),
                "previous_impressions": round(previous.get("impressions", 0.0), 2),
                "dropped_out": dropped_out,
                "recommended_action": action,
                "action_reason": reason,
            }
        )

    decays.sort(
        key=lambda row: (
            SEVERITY_RANK[row["severity"]],
            row["decline"],
            row["previous_metric"],
        ),
        reverse=True,
    )

    return {
        "metric": metric,
        "threshold": threshold,
        "summary": {
            "current_pages": len(current_pages),
            "previous_pages": len(previous_pages),
            "flagged_pages": len(decays),
            "dropped_out_pages": sum(1 for row in decays if row["dropped_out"]),
            "total_current_metric": round(
                sum(page.get(metric, 0.0) for page in current_pages.values()), 2
            ),
            "total_previous_metric": round(
                sum(page.get(metric, 0.0) for page in previous_pages.values()), 2
            ),
        },
        "decays": decays,
    }


def format_markdown(report: dict[str, Any]) -> str:
    """Render a content decay report as markdown."""
    summary = report["summary"]
    metric = report["metric"]
    threshold = report["threshold"] * 100
    lines = [
        "# Content Decay Report",
        "",
        f"Metric: `{metric}`",
        f"Threshold: {threshold:.0f}%",
        f"Flagged pages: {summary['flagged_pages']}",
        f"Dropped out pages: {summary['dropped_out_pages']}",
        "",
    ]

    if not report["decays"]:
        lines.append("No pages met the decay threshold.")
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            "| Severity | Page | Previous | Current | Decline | Dropped out | Recommendation |",
            "| --- | --- | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in report["decays"]:
        dropped = "yes" if row["dropped_out"] else "no"
        lines.append(
            "| {severity} | {page} | {previous:g} | {current:g} | {decline:.1f}% | {dropped} | {action} |".format(
                severity=row["severity"],
                page=row["page"],
                previous=row["previous_metric"],
                current=row["current_metric"],
                decline=row["decline_percent"],
                dropped=dropped,
                action=row["recommended_action"],
            )
        )

    return "\n".join(lines) + "\n"


def write_output(text: str, output_path: str | None) -> None:
    """Write text to a path or stdout."""
    if output_path:
        Path(output_path).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


def build_parser() -> argparse.ArgumentParser:
    """Build the command line parser."""
    parser = argparse.ArgumentParser(
        description="Detect quarter-over-quarter content decay from GSC exports."
    )
    parser.add_argument("current", help="Current-period GSC performance export")
    parser.add_argument("previous", help="Previous-period GSC performance export")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.20,
        help="Minimum decline ratio to flag, default 0.20",
    )
    parser.add_argument(
        "--metric",
        choices=["clicks", "impressions"],
        default="clicks",
        help="Metric to compare, default clicks",
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format, default json",
    )
    parser.add_argument("--output", help="Write report to this path")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the content decay CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        current_rows = load_export(args.current)
        previous_rows = load_export(args.previous)
        report = analyze_decay(
            current_rows,
            previous_rows,
            threshold=args.threshold,
            metric=args.metric,
        )
    except ContentDecayError as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
        return 1

    if args.format == "markdown":
        output = format_markdown(report)
    else:
        output = json.dumps(report, indent=2) + "\n"
    write_output(output, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
