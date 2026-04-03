#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".turbo",
    ".cache",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "__pycache__",
    ".venv",
    "venv",
}

MANIFEST_CANDIDATES = [
    "package.json",
    "pnpm-workspace.yaml",
    "tsconfig.json",
    "pyproject.toml",
    "requirements.txt",
    "go.mod",
    "Cargo.toml",
    "pom.xml",
    "composer.json",
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    ".gitlab-ci.yml",
]

DOC_CANDIDATES = [
    "README.md",
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

ENTRYPOINT_CANDIDATES = [
    "src/main.ts",
    "src/index.ts",
    "src/main.py",
    "src/index.js",
    "main.py",
    "app.py",
    "manage.py",
]


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def relative_paths(root: Path, paths: list[Path]) -> list[str]:
    return sorted(str(path.relative_to(root)).replace("\\", "/") for path in paths)


def detect_languages(root: Path, files: list[Path]) -> list[str]:
    languages = set()
    suffixes = {path.suffix for path in files}
    if ".py" in suffixes or (root / "pyproject.toml").exists():
        languages.add("python")
    if {".ts", ".tsx", ".js", ".jsx"} & suffixes or (root / "package.json").exists():
        languages.add("javascript-or-typescript")
    if ".go" in suffixes or (root / "go.mod").exists():
        languages.add("go")
    if ".rs" in suffixes or (root / "Cargo.toml").exists():
        languages.add("rust")
    if ".java" in suffixes or (root / "pom.xml").exists():
        languages.add("java")
    return sorted(languages)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a project and summarize documentation-relevant signals.")
    parser.add_argument("--root", default=".", help="Project root to scan.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    files = list(iter_files(root))
    manifests = [root / candidate for candidate in MANIFEST_CANDIDATES if (root / candidate).exists()]
    docs = [root / candidate for candidate in DOC_CANDIDATES if (root / candidate).exists()]
    ci_files = [path for path in files if ".github/workflows" in path.as_posix() or path.name == ".gitlab-ci.yml"]
    env_files = [path for path in files if path.name.startswith(".env") or path.name.endswith(".env.example")]
    tests = [
        path for path in files
        if any(part in {"test", "tests", "__tests__"} for part in path.parts)
        or path.name.endswith(("_test.py", ".spec.ts", ".test.ts", ".spec.js", ".test.js"))
    ]
    entrypoints = [root / candidate for candidate in ENTRYPOINT_CANDIDATES if (root / candidate).exists()]
    adr_dir = root / "docs" / "adr"
    adr_files = sorted(adr_dir.glob("*.md")) if adr_dir.exists() else []

    report = {
        "root": str(root),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "detected": {
            "languages": detect_languages(root, files),
            "manifests": relative_paths(root, manifests),
            "ci_files": relative_paths(root, ci_files),
            "env_files": relative_paths(root, env_files),
            "tests": relative_paths(root, tests[:50]),
            "entrypoints": relative_paths(root, entrypoints),
            "docs_present": relative_paths(root, docs),
            "adr_files": relative_paths(root, adr_files),
        },
        "pack_status": {
            "has_project_md": (root / "PROJECT.md").exists(),
            "has_state_md": (root / "STATE.md").exists(),
            "has_docs_dir": (root / "docs").exists(),
            "has_adr_dir": adr_dir.exists(),
            "missing_core_docs": [
                candidate for candidate in DOC_CANDIDATES if not (root / candidate).exists()
            ],
        },
    }

    if args.pretty:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(report, separators=(",", ":"), ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

