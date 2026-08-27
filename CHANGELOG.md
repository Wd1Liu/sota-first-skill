# Changelog

## 0.3.0 — 2026-08-27

- Added a dedicated Architecture Expert Review Gate
- Added a concrete integration-architecture sketch before scoring
- Added nine weighted system-compatibility dimensions and a 0–100 score
- Added hard architecture blockers that override weighted totals
- Added `PASS`, `CONDITIONAL PASS`, `FAIL`, and `INCONCLUSIVE` architecture outcomes
- Added adversarial review questions covering invariants, coupling, ownership, contracts, failure domains, and simpler alternatives
- Added truthful reviewer modes for dedicated architect/subagent and same-agent structured review
- Added architecture conditions to feasibility contracts and production acceptance criteria
- Added re-review rules when validation or implementation changes boundaries, contracts, topology, dependencies, or ownership
- Expanded activation evals with architecture-review expectations

## 0.2.0 — 2026-08-27

- Split research depth from delivery phase
- Added explicit Research-only, Feasibility validation, and Integration phases
- Added isolated feasibility spikes with falsifiable acceptance thresholds
- Added `PASS`, `CONDITIONAL PASS`, `FAIL`, and `INCONCLUSIVE` integration gates
- Added phase handoffs so later requests can resume without repeating valid prior work
- Added a dedicated feasibility validation playbook
- Added research, feasibility, and integration result templates
- Expanded activation evals with expected depth and phase labels
- Added validation that documentation remains English-only

## 0.1.0 — 2026-08-27

- Initial `sota-first` Agent Skill
- Quick and Full research modes
- Separate Research SOTA and Engineering recommendation evaluation
- Search playbook, scoring rubric, and verdict templates
- Safe user- and repository-scoped installers
- Activation eval dataset and validation workflow
