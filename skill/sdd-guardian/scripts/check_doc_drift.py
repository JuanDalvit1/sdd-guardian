#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


CORE_DOCS = [
    "PROJECT.md",
    "STATE.md",
    "docs/architecture/overview.md",
    "docs/architecture/components.md",
    "docs/architecture/flows.md",
    "docs/ops/deploy.md",
    "docs/ops/environments.md",
    "docs/ops/runbook.md",
    "docs/domain/invariants.md",
]

RULES = {
    "architecture": {
        "patterns": [
            "src/",
            "app/",
            "frontend/",
            "backend/",
            "services/",
            "packages/",
            "api/",
            "routes/",
            "schema",
            "migration",
        ],
        "docs": [
            "PROJECT.md",
            "docs/architecture/overview.md",
            "docs/architecture/components.md",
            "docs/architecture/flows.md",
        ],
    },
    "ops": {
        "patterns": [
            ".gitlab-ci.yml",
            ".github/workflows/",
            "Dockerfile",
            "docker-compose",
            "compose",
            "deploy",
            "systemd",
            "infra/",
            "nginx",
            ".env",
        ],
        "docs": [
            "STATE.md",
            "docs/ops/deploy.md",
            "docs/ops/environments.md",
            "docs/ops/runbook.md",
        ],
    },
    "domain": {
        "patterns": [
            "domain/",
            "entities/",
            "models/",
            "permissions",
            "policy",
            "rules",
            "invariant",
        ],
        "docs": ["docs/domain/invariants.md"],
    },
    "readme": {
        "patterns": [
            "README.md",
            "package.json",
            "pyproject.toml",
            "go.mod",
            "Cargo.toml",
            "bootstrap/",
        ],
        "docs": ["README.md", "PROJECT.md"],
    },
}


def infer_categories(changed_paths: list[str]) -> dict[str, list[str]]:
    matches: dict[str, list[str]] = {key: [] for key in RULES}
    for changed in changed_paths:
        lower = changed.lower()
        for category, rule in RULES.items():
            for pattern in rule["patterns"]:
                if pattern.lower() in lower:
                    matches[category].append(changed)
                    break
    return {key: value for key, value in matches.items() if value}


def main() -> int:
    parser = argparse.ArgumentParser(description="Map project changes to documentation updates.")
    parser.add_argument("--root", default=".", help="Project root to analyze.")
    parser.add_argument("--changed", nargs="*", default=[], help="Changed paths to evaluate.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when core docs are missing.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    missing = [doc for doc in CORE_DOCS if not (root / doc).exists()]
    has_adr_dir = (root / "docs" / "adr").exists()

    category_matches = infer_categories(args.changed)
    recommended = set()
    for category in category_matches:
        recommended.update(RULES[category]["docs"])

    if category_matches.get("architecture") or category_matches.get("domain"):
        recommended.add("docs/adr/")

    report = {
        "root": str(root),
        "mode": "bootstrap" if missing else "update",
        "missing_core_docs": missing,
        "has_adr_dir": has_adr_dir,
        "changed_paths": args.changed,
        "matched_categories": category_matches,
        "recommended_updates": sorted(recommended),
    }

    if args.pretty:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(report, separators=(",", ":"), ensure_ascii=False))

    if args.strict and (missing or not has_adr_dir):
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

