#!/usr/bin/env python3
"""Run lightweight post-remodel checks on an HTML file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from extract_page_signals import extract


def check(path: Path) -> dict:
    signals = extract(path)
    h1 = signals["headings"].get("h1", [])
    issues = []
    warnings = []

    if not signals["title"]:
        issues.append("Missing title tag.")
    elif len(signals["title"]) > 70:
        warnings.append("Title may be too long for search snippets.")

    if not signals["meta_description"]:
        warnings.append("Missing meta description.")
    elif len(signals["meta_description"]) > 170:
        warnings.append("Meta description may be too long for snippets.")

    if not h1:
        issues.append("Missing H1.")
    elif len(h1) > 1:
        warnings.append("Multiple H1 headings detected; verify hierarchy.")

    if signals["schema_count"]:
        for index, block in enumerate(signals["schema_blocks"], start=1):
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                issues.append(f"Invalid JSON-LD block {index}: {exc.msg}.")

    if signals["links_count"] == 0:
        warnings.append("No links detected; verify navigation and inquiry paths.")

    return {
        "file": str(path),
        "passed": not issues,
        "issues": issues,
        "warnings": warnings,
        "signals": {
            "title": signals["title"],
            "meta_description": signals["meta_description"],
            "h1": h1,
            "links_count": signals["links_count"],
            "schema_count": signals["schema_count"],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Check basic SEO/UI safety signals after remodel.")
    parser.add_argument("html_file")
    args = parser.parse_args()
    print(json.dumps(check(Path(args.html_file)), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

