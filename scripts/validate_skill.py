#!/usr/bin/env python3
"""Validate the repository's Agent Skill without third-party dependencies."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "sota-first"
SKILL_FILE = SKILL_DIR / "SKILL.md"
ARCHITECTURE_FILE = SKILL_DIR / "references" / "architecture-review.md"
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


def require_phrases(text: str, phrases: list[str], source: str) -> None:
    for phrase in phrases:
        if phrase not in text:
            fail(f"{source} is missing required concept: {phrase}")


def validate_skill() -> None:
    if not SKILL_FILE.is_file():
        fail(f"Missing {SKILL_FILE.relative_to(ROOT)}")

    text = SKILL_FILE.read_text(encoding="utf-8")
    metadata = parse_front_matter(text)

    if metadata.get("name") != "sota-first":
        fail("front-matter name must be 'sota-first'")
    if not metadata.get("description"):
        fail("front-matter description is required")
    if len(metadata["description"]) < 160:
        fail("description is too vague to trigger reliably")

    require_phrases(
        text,
        [
            "Research SOTA",
            "Engineering recommendation",
            "Architecture compatibility",
            "Architecture Review Gate",
            "dedicated architect",
            "same-agent structured review",
            "Quick mode",
            "Full mode",
            "Research-only",
            "Feasibility validation",
            "Integration",
            "KEEP",
            "ADOPT",
            "EXTEND",
            "COMPOSE",
            "BUILD",
            "PASS",
            "CONDITIONAL PASS",
            "FAIL",
            "INCONCLUSIVE",
        ],
        "SKILL.md",
    )

    referenced_paths = set(re.findall(r"`(references/[^`]+\.md)`", text))
    expected_paths = {
        "references/architecture-review.md",
        "references/feasibility-playbook.md",
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


def validate_architecture_review() -> None:
    if not ARCHITECTURE_FILE.is_file():
        fail(f"Missing {ARCHITECTURE_FILE.relative_to(ROOT)}")

    text = ARCHITECTURE_FILE.read_text(encoding="utf-8")
    require_phrases(
        text,
        [
            "Reviewer role and independence",
            "integration architecture sketch",
            "hard blockers",
            "Boundary and responsibility fit",
            "Interface and data-contract fit",
            "Dependency, runtime, and platform fit",
            "Deployment, topology, and resource fit",
            "Reliability and failure isolation",
            "Security, privacy, and compliance fit",
            "Observability and operability",
            "Migration, compatibility, and rollback",
            "Maintainability, ownership, and evolution",
            "Architecture compatibility =",
            "Architecture Review Gate",
            "PASS",
            "CONDITIONAL PASS",
            "FAIL",
            "INCONCLUSIVE",
        ],
        "architecture-review.md",
    )

    weights = [15, 15, 15, 10, 10, 10, 10, 5, 10]
    if sum(weights) != 100:
        fail("internal architecture weights must sum to 100")


def validate_evals() -> None:
    if not EVAL_FILE.is_file():
        fail(f"Missing {EVAL_FILE.relative_to(ROOT)}")

    with EVAL_FILE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    required_columns = {
        "id",
        "should_trigger",
        "expected_depth",
        "expected_phase",
        "expected_architecture_review",
        "prompt",
        "rationale",
    }
    if not rows:
        fail("activation eval file has no cases")
    if set(rows[0]) != required_columns:
        fail(f"activation eval columns must be {sorted(required_columns)}")

    ids: set[str] = set()
    trigger_counts: Counter[str] = Counter()
    depth_counts: Counter[str] = Counter()
    phase_counts: Counter[str] = Counter()
    architecture_counts: Counter[str] = Counter()

    valid_depths = {"skip", "quick", "full"}
    valid_phases = {"none", "search", "validate", "integrate"}
    valid_architecture = {"none", "optional", "required"}

    for row in rows:
        case_id = row["id"].strip()
        if not case_id or case_id in ids:
            fail(f"empty or duplicate eval id: {case_id!r}")
        ids.add(case_id)

        trigger = row["should_trigger"].strip().lower()
        depth = row["expected_depth"].strip().lower()
        phase = row["expected_phase"].strip().lower()
        architecture = row["expected_architecture_review"].strip().lower()

        if trigger not in {"true", "false"}:
            fail(f"invalid should_trigger value for {case_id}: {trigger!r}")
        if depth not in valid_depths:
            fail(f"invalid expected_depth value for {case_id}: {depth!r}")
        if phase not in valid_phases:
            fail(f"invalid expected_phase value for {case_id}: {phase!r}")
        if architecture not in valid_architecture:
            fail(
                f"invalid expected_architecture_review value for {case_id}: "
                f"{architecture!r}"
            )

        if trigger == "false" and (
            depth != "skip" or phase != "none" or architecture != "none"
        ):
            fail(
                f"non-trigger case {case_id} must use expected_depth=skip, "
                "expected_phase=none, and expected_architecture_review=none"
            )
        if trigger == "true" and (depth == "skip" or phase == "none"):
            fail(
                f"trigger case {case_id} must use quick/full depth and a "
                "search/validate/integrate phase"
            )

        if not row["prompt"].strip() or not row["rationale"].strip():
            fail(f"eval case {case_id} has an empty prompt or rationale")

        trigger_counts[trigger] += 1
        depth_counts[depth] += 1
        phase_counts[phase] += 1
        architecture_counts[architecture] += 1

    if trigger_counts["true"] < 10 or trigger_counts["false"] < 5:
        fail("activation evals need at least ten positive and five negative cases")
    if depth_counts["quick"] < 1 or depth_counts["full"] < 1:
        fail("activation evals must cover both Quick and Full research depth")
    for phase in ("search", "validate", "integrate"):
        if phase_counts[phase] < 1:
            fail(f"activation evals must cover the {phase!r} delivery phase")
    if architecture_counts["required"] < 3:
        fail("activation evals need at least three required architecture reviews")
    if architecture_counts["optional"] < 1:
        fail("activation evals need at least one optional architecture review")


def validate_english_documentation() -> None:
    cjk_ideograph = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF]")
    documentation = sorted(ROOT.rglob("*.md")) + sorted(ROOT.rglob("*.csv"))

    for path in documentation:
        text = path.read_text(encoding="utf-8")
        match = cjk_ideograph.search(text)
        if match:
            line_number = text.count("\n", 0, match.start()) + 1
            fail(
                "documentation must remain English-only; found a CJK ideograph in "
                f"{path.relative_to(ROOT)}:{line_number}"
            )


def main() -> None:
    validate_skill()
    validate_architecture_review()
    validate_evals()
    validate_english_documentation()
    print("sota-first skill validation passed")


if __name__ == "__main__":
    main()
