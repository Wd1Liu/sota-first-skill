#!/usr/bin/env python3
"""Validate the repository's Agent Skill without third-party dependencies."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "sota-first"
SKILL_FILE = SKILL_DIR / "SKILL.md"
EVAL_FILE = ROOT / "evals" / "activation.csv"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must begin with YAML front matter")

    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md front matter is not closed")

    result: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            fail(f"Unsupported front-matter line: {raw_line!r}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def validate_skill() -> None:
    if not SKILL_FILE.is_file():
        fail(f"Missing {SKILL_FILE.relative_to(ROOT)}")

    text = SKILL_FILE.read_text(encoding="utf-8")
    metadata = parse_front_matter(text)

    if metadata.get("name") != "sota-first":
        fail("front-matter name must be 'sota-first'")
    if not metadata.get("description"):
        fail("front-matter description is required")
    if len(metadata["description"]) < 80:
        fail("description is too vague to trigger reliably")

    required_phrases = [
        "Research SOTA",
        "Engineering recommendation",
        "Quick mode",
        "Full mode",
        "KEEP",
        "ADOPT",
        "EXTEND",
        "COMPOSE",
        "BUILD",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"SKILL.md is missing required concept: {phrase}")

    referenced_paths = set(re.findall(r"`(references/[^`]+\.md)`", text))
    expected_paths = {
        "references/search-playbook.md",
        "references/scoring-rubric.md",
        "references/verdict-template.md",
    }
    if referenced_paths != expected_paths:
        fail(
            "SKILL.md reference set differs from expected files: "
            f"found={sorted(referenced_paths)}, expected={sorted(expected_paths)}"
        )

    for relative in expected_paths:
        path = SKILL_DIR / relative
        if not path.is_file():
            fail(f"Missing referenced file: {path.relative_to(ROOT)}")
        if not path.read_text(encoding="utf-8").strip():
            fail(f"Referenced file is empty: {path.relative_to(ROOT)}")


def validate_evals() -> None:
    if not EVAL_FILE.is_file():
        fail(f"Missing {EVAL_FILE.relative_to(ROOT)}")

    with EVAL_FILE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    required_columns = {"id", "should_trigger", "prompt", "rationale"}
    if not rows:
        fail("activation eval file has no cases")
    if set(rows[0]) != required_columns:
        fail(f"activation eval columns must be {sorted(required_columns)}")

    ids: set[str] = set()
    positives = 0
    negatives = 0
    for row in rows:
        case_id = row["id"].strip()
        if not case_id or case_id in ids:
            fail(f"empty or duplicate eval id: {case_id!r}")
        ids.add(case_id)

        value = row["should_trigger"].strip().lower()
        if value == "true":
            positives += 1
        elif value == "false":
            negatives += 1
        else:
            fail(f"invalid should_trigger value for {case_id}: {value!r}")

        if not row["prompt"].strip() or not row["rationale"].strip():
            fail(f"eval case {case_id} has an empty prompt or rationale")

    if positives < 5 or negatives < 5:
        fail("activation evals need at least five positive and five negative cases")


def main() -> None:
    validate_skill()
    validate_evals()
    print("sota-first skill validation passed")


if __name__ == "__main__":
    main()
