#!/usr/bin/env python3
"""Generate conservative manufacturer-oriented JSON-LD using only verified fields."""

from __future__ import annotations

import argparse
import json


def compact(value: str | None) -> str | None:
    return value.strip() if value and value.strip() else None


def drop_empty(obj):
    if isinstance(obj, dict):
        return {k: drop_empty(v) for k, v in obj.items() if drop_empty(v) not in (None, "", [], {})}
    if isinstance(obj, list):
        return [drop_empty(v) for v in obj if drop_empty(v) not in (None, "", [], {})]
    return obj


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate conservative JSON-LD.")
    parser.add_argument("--type", choices=["Organization", "Product", "WebSite"], required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--url")
    parser.add_argument("--description")
    parser.add_argument("--logo")
    parser.add_argument("--image", action="append")
    parser.add_argument("--category")
    parser.add_argument("--manufacturer")
    args = parser.parse_args()

    if args.type == "Organization":
        data = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": compact(args.name),
            "url": compact(args.url),
            "description": compact(args.description),
            "logo": compact(args.logo),
        }
    elif args.type == "WebSite":
        data = {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": compact(args.name),
            "url": compact(args.url),
            "description": compact(args.description),
        }
    else:
        data = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": compact(args.name),
            "url": compact(args.url),
            "description": compact(args.description),
            "image": args.image or [],
            "category": compact(args.category),
            "manufacturer": {"@type": "Organization", "name": compact(args.manufacturer)} if compact(args.manufacturer) else None,
        }

    print(json.dumps(drop_empty(data), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

