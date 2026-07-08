from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run_script(script: str, args: list[str]) -> int:
    return subprocess.call([PY, str(REPO / "scripts" / script), *args], cwd=REPO)


def run_script_checked(script: str, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([PY, str(REPO / "scripts" / script), *args], cwd=REPO, text=True, capture_output=True, check=False)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="claude-blog-brain", description="Operate Claude Blog Brain.")
    sub = parser.add_subparsers(dest="command", required=True)
    p_new = sub.add_parser("new")
    p_new.add_argument("client")
    p_new.add_argument("--client-name", default="")
    p_new.add_argument("--owner", default="Daniel Agrici")
    p_new.add_argument("--out-dir", default="~/claude-blog-brain-vaults")
    p_ingest = sub.add_parser("ingest")
    p_ingest.add_argument("--vault", required=True)
    p_ingest.add_argument("--file", required=True)
    p_synth = sub.add_parser("synthesize")
    p_synth.add_argument("--vault", required=True)
    p_report = sub.add_parser("report")
    p_report.add_argument("--vault", required=True)
    p_report.add_argument("--out", default="")
    p_report.add_argument("--html-only", action="store_true")
    p_visuals = sub.add_parser("visuals")
    p_visuals.add_argument("--vault", required=True)
    p_lint = sub.add_parser("lint")
    p_lint.add_argument("--vault", required=True)
    p_lint.add_argument("--template", action="store_true")
    p_next = sub.add_parser("next")
    p_next.add_argument("--vault", required=True)
    p_blog_ingest = sub.add_parser("blog-ingest")
    p_blog_ingest.add_argument("input")
    p_blog_ingest.add_argument("-o", "--output", default="")
    p_blog_synth = sub.add_parser("blog-synthesize")
    p_blog_synth.add_argument("input")
    p_blog_synth.add_argument("-o", "--output", default="")
    p_blog_synth.add_argument("-l", "--ledger", default="")
    p_blog_report = sub.add_parser("blog-report")
    p_blog_report.add_argument("input")
    p_blog_report.add_argument("-o", "--output", default="")
    p_blog_report.add_argument("--json-errors", action="store_true")
    p_blog_pipeline = sub.add_parser("blog-pipeline")
    p_blog_pipeline.add_argument("--input", required=True)
    p_blog_pipeline.add_argument("--out-dir", required=True)
    p_demo = sub.add_parser("demo")
    p_demo.add_argument("--out", default="")
    p_demo.add_argument("--force", action="store_true")
    p_demo.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "new":
        call = ["--client", args.client, "--client-name", args.client_name or args.client, "--owner", args.owner, "--out-dir", args.out_dir]
        return run_script("scaffold_vault.py", call)
    if args.command == "ingest":
        return run_script("ingest_source.py", ["--vault", args.vault, "--file", args.file])
    if args.command == "synthesize":
        return run_script("synthesize_brain.py", ["--vault", args.vault])
    if args.command == "report":
        call = ["--vault", args.vault]
        if args.out:
            call += ["--out", args.out]
        if args.html_only:
            call.append("--html-only")
        return run_script("render_brain_report.py", call)
    if args.command == "visuals":
        return run_script("generate_vault_visuals.py", ["--vault", args.vault])
    if args.command == "lint":
        call = ["--vault", args.vault]
        if args.template:
            call.append("--template")
        return run_script("lint_vault.py", call)
    if args.command == "next":
        return run_script("guide_next_action.py", ["--vault", args.vault])
    if args.command == "blog-ingest":
        call = [args.input]
        if args.output:
            call += ["-o", args.output]
        return run_script("ingest_blog_input.py", call)
    if args.command == "blog-synthesize":
        call = [args.input]
        if args.ledger:
            call += ["-l", args.ledger]
        if args.output:
            call += ["-o", args.output]
        return run_script("synthesize_blog_plan.py", call)
    if args.command == "blog-report":
        call = [args.input]
        if args.output:
            call += ["-o", args.output]
        if args.json_errors:
            call.append("--json-errors")
        return run_script("render_blog_report.py", call)
    if args.command == "blog-pipeline":
        return run_blog_pipeline(args.input, args.out_dir)
    if args.command == "demo":
        call = []
        if args.out:
            call += ["--out", args.out]
        if args.force:
            call.append("--force")
        if args.json:
            call.append("--json")
        return run_script("build_demo_vault.py", call)
    return 2


def run_blog_pipeline(input_path: str, out_dir: str) -> int:
    out = Path(out_dir).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    ingested = out / "ingested-blog-post.json"
    plan = out / "blog-optimization-plan.json"
    report = out / "blog-optimization-report.md"
    steps = [
        ("ingest_blog_input.py", [input_path, "-o", str(ingested)]),
        ("synthesize_blog_plan.py", [str(ingested), "-o", str(plan)]),
        ("render_blog_report.py", [str(plan), "-o", str(report), "--json-errors"]),
    ]
    for script, call in steps:
        proc = run_script_checked(script, call)
        if proc.returncode:
            if proc.stdout:
                print(proc.stdout, end="")
            if proc.stderr:
                print(proc.stderr, end="", file=sys.stderr)
            return proc.returncode
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
