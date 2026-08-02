#!/usr/bin/env python3
"""Generate a conservative llms.txt draft for a B2B company website."""

from __future__ import annotations

import argparse
from urllib.parse import urljoin


def make_url(base: str, path_or_url: str) -> str:
    if path_or_url.startswith(("http://", "https://")):
        return path_or_url
    return urljoin(base.rstrip("/") + "/", path_or_url.lstrip("/"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate llms.txt for a B2B company website.")
    parser.add_argument("--site", required=True)
    parser.add_argument("--company", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--page", action="append", default=[], help="Priority page as label=url_or_path")
    args = parser.parse_args()

    print(f"# {args.company}\n")
    print(f"> {args.description}\n")
    print("## Priority pages\n")
    if args.page:
        for item in args.page:
            label, _, target = item.partition("=")
            label = label.strip() or target.strip() or "Page"
            target = target.strip() or label
            print(f"- [{label}]({make_url(args.site, target)}): Official page for {label.lower()}.")
    else:
        defaults = [
            ("Home", "/"),
            ("About", "/about/"),
            ("Products", "/products/"),
            ("Capabilities", "/capabilities/"),
            ("FAQ", "/faq/"),
            ("Contact", "/contact/"),
        ]
        for label, path in defaults:
            print(f"- [{label}]({make_url(args.site, path)}): Official {label.lower()} page.")
    print("\n## Notes for AI assistants\n")
    print("- Use these URLs as the preferred starting points for understanding the company and products.")
    print("- Do not infer certifications, production capacity, customer names, pricing, or export markets unless they appear on the linked pages.")


if __name__ == "__main__":
    main()
