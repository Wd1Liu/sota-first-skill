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
REF_DIR = SKILL_DIR / "references"
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
    description = metadata.get("description", "")
    if len(description) < 300:
        fail("front-matter description is too vague to trigger the expert workflow reliably")

    require_phrases(
        text,
        [
            "Research SOTA",
            "Industry practice",
            "Domain analysis",
            "Architecture compatibility",
            "Engineering readiness",
            "Local feasibility",
            "Research Director",
            "Repository Cartographer",
            "Industry Practice Investigator",
            "Academic Frontier Investigator",
            "Ecosystem and Standards Investigator",
            "Domain Specialists",
            "Solution Architect",
            "Architecture Reviewer",
            "Engineering Reviewer",
            "Evidence Auditor and Decision Chair",
            "Quick mode",
            "Full mode",
            "Research-only",
            "Feasibility validation",
            "Integration",
            "Architecture Review Gate",
            "Engineering Readiness Gate",
            "same-agent structured review",
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
        "references/architecture-synthesis.md",
        "references/domain-analysis.md",
        "references/engineering-review.md",
        "references/expert-orchestration.md",
        "references/feasibility-playbook.md",
        "references/scoring-rubric.md",
        "references/search-playbook.md",
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


def validate_reference_content() -> None:
    checks: dict[str, list[str]] = {
        "expert-orchestration.md": [
            "Research Director",
            "Repository Cartographer",
            "Industry Practice Investigator",
            "Academic Frontier Investigator",
            "Ecosystem and Standards Investigator",
            "Domain Specialists",
            "Solution Architect",
            "Architecture Reviewer",
            "Engineering Reviewer",
            "Evidence Auditor and Decision Chair",
            "same-agent structured review",
            "Conflict resolution",
            "Cost and scope control",
        ],
        "search-playbook.md": [
            "Industry Practice lane",
            "Academic Frontier lane",
            "Ecosystem and Standards lane",
            "Architecture search",
            "Negative-evidence search",
            "Landscape map",
            "Never claim a company uses an undisclosed method",
        ],
        "domain-analysis.md": [
            "Candidate dossier",
            "Mechanism",
            "Contract",
            "Operating envelope",
            "Failure modes",
            "Implementation variants",
            "Composition requirements",
            "Cross-specialist reconciliation",
        ],
        "architecture-synthesis.md": [
            "capability graph",
            "Normalize component contracts",
            "distinct architecture options",
            "Frankenstein architectures",
            "Architecture option",
            "Preliminary budgets",
            "Architecture revision loop",
        ],
        "architecture-review.md": [
            "Reviewer role and independence",
            "Hard blockers",
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
            "Comparative review",
            "Architecture Review Gate",
        ],
        "engineering-review.md": [
            "Engineering Readiness",
            "Pin the implementation bundle",
            "Pairwise compatibility matrix",
            "Resource and performance budget",
            "Resource placement",
            "Hard blockers",
            "Dependency, version, runtime, and platform compatibility",
            "Engineering readiness =",
            "Engineering Readiness Gate",
            "Relationship to feasibility",
        ],
        "feasibility-playbook.md": [
            "Architecture gate status",
            "Engineering gate status",
            "Validation contract",
            "highest-risk unknown first",
            "Representative conditions",
            "locally measured",
            "PASS",
            "CONDITIONAL PASS",
            "FAIL",
            "INCONCLUSIVE",
        ],
        "scoring-rubric.md": [
            "Research strength",
            "Public practice and ecosystem evidence",
            "Predicted project fit",
            "Research SOTA",
            "Strongest public industry precedent",
        ],
        "verdict-template.md": [
            "Investigation coverage",
            "Solution landscape",
            "Candidate dossier summary",
            "Candidate architectures",
            "Architecture Review Gate",
            "Engineering Readiness Gate",
            "Pairwise compatibility matrix",
            "Resource and latency budget",
            "Final decision",
            "Feasibility Gate",
            "Integration result",
        ],
    }

    for filename, phrases in checks.items():
        path = REF_DIR / filename
        if not path.is_file():
            fail(f"Missing {path.relative_to(ROOT)}")
        require_phrases(path.read_text(encoding="utf-8"), phrases, filename)

    architecture_weights = [15, 15, 15, 10, 10, 10, 10, 5, 10]
    engineering_weights = [10, 20, 15, 20, 10, 10, 5, 10]
    if sum(architecture_weights) != 100:
        fail("architecture review weights must sum to 100")
    if sum(engineering_weights) != 100:
        fail("engineering review weights must sum to 100")


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
        "expected_panel",
        "expected_architecture_review",
        "expected_engineering_review",
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
    panel_counts: Counter[str] = Counter()
    architecture_counts: Counter[str] = Counter()
    engineering_counts: Counter[str] = Counter()

    valid_depths = {"skip", "quick", "full"}
    valid_phases = {"none", "search", "validate", "integrate"}
    valid_panels = {"none", "compact", "full"}
    valid_review = {"none", "optional", "required"}

    for row in rows:
        case_id = row["id"].strip()
        if not case_id or case_id in ids:
            fail(f"empty or duplicate eval id: {case_id!r}")
        ids.add(case_id)

        trigger = row["should_trigger"].strip().lower()
        depth = row["expected_depth"].strip().lower()
        phase = row["expected_phase"].strip().lower()
        panel = row["expected_panel"].strip().lower()
        architecture = row["expected_architecture_review"].strip().lower()
        engineering = row["expected_engineering_review"].strip().lower()

        if trigger not in {"true", "false"}:
            fail(f"invalid should_trigger value for {case_id}: {trigger!r}")
        if depth not in valid_depths:
            fail(f"invalid expected_depth value for {case_id}: {depth!r}")
        if phase not in valid_phases:
            fail(f"invalid expected_phase value for {case_id}: {phase!r}")
        if panel not in valid_panels:
            fail(f"invalid expected_panel value for {case_id}: {panel!r}")
        if architecture not in valid_review:
            fail(f"invalid architecture review value for {case_id}: {architecture!r}")
        if engineering not in valid_review:
            fail(f"invalid engineering review value for {case_id}: {engineering!r}")

        if trigger == "false":
            if (
                depth != "skip"
                or phase != "none"
                or panel != "none"
                or architecture != "none"
                or engineering != "none"
            ):
                fail(
                    f"non-trigger case {case_id} must use skip/none/none/none/none"
                )
        else:
            if depth == "skip" or phase == "none" or panel == "none":
                fail(
                    f"trigger case {case_id} must use quick/full depth, "
                    "a delivery phase, and compact/full panel"
                )

        if depth == "quick" and panel == "full":
            fail(f"Quick case {case_id} should not require a full panel")
        if not row["prompt"].strip() or not row["rationale"].strip():
            fail(f"eval case {case_id} has an empty prompt or rationale")

        trigger_counts[trigger] += 1
        depth_counts[depth] += 1
        phase_counts[phase] += 1
        panel_counts[panel] += 1
        architecture_counts[architecture] += 1
        engineering_counts[engineering] += 1

    if trigger_counts["true"] < 15 or trigger_counts["false"] < 8:
        fail("evals need at least fifteen trigger and eight non-trigger cases")
    if depth_counts["quick"] < 2 or depth_counts["full"] < 8:
        fail("evals must cover Quick and Full research depth")
    for phase in ("search", "validate", "integrate"):
        if phase_counts[phase] < 2:
            fail(f"evals must cover the {phase!r} endpoint at least twice")
    if panel_counts["compact"] < 3 or panel_counts["full"] < 8:
        fail("evals must cover compact and full expert panels")
    if architecture_counts["required"] < 6:
        fail("evals need at least six required architecture reviews")
    if engineering_counts["required"] < 6:
        fail("evals need at least six required engineering reviews")
    if architecture_counts["optional"] < 2 or engineering_counts["optional"] < 2:
        fail("evals need optional review cases")


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
    validate_reference_content()
    validate_evals()
    validate_english_documentation()
    print("sota-first expert-council skill validation passed")


if __name__ == "__main__":
    main()
