# SOTA First Skill

A reusable Agent Skill that makes coding agents research the repository, compare current state-of-the-art and production-mature approaches, validate the selected candidate under real project constraints, and optionally integrate it into the feature.

It is designed to answer three distinct questions:

1. What is the strongest current research approach for the task?
2. What should this project actually adopt given its hardware, latency, licensing, maintenance, and integration constraints?
3. Does the recommended candidate measurably work in this repository before it becomes production code?

The skill deliberately separates **Research SOTA** from the **Engineering recommendation**, and separates both from **local feasibility**.

## Two independent controls

The workflow uses two independent dimensions.

### Research depth

- `Skip` — no external selection work is needed
- `Quick mode` — compact repository check and targeted evidence review
- `Full mode` — complete repository, evidence, comparison, and risk analysis

### Delivery phase

- `Research-only` — search, compare, and recommend without implementing
- `Feasibility validation` — run an isolated, disposable spike without integrating production code
- `Integration` — promote a validated candidate into the real feature

A request can stop after any phase or continue through all three:

```text
Research and selection
        │
        ▼
Feasibility validation
        │
        ▼
Production integration
```

When the user requests the full pipeline, the skill continues through each passing gate without pausing for redundant approval. When the user requests only research or validation, it stops at that boundary.

## What it does

- Inspects the current repository before searching externally
- Selects Quick or Full research depth based on decision risk
- Supports research-only, validation-only, and research-validate-integrate workflows
- Prioritizes official documentation, original papers, official code, registries, benchmarks, and security advisories
- Compares research strength and project fit on separate axes
- Defines a falsifiable feasibility contract with measurable thresholds
- Runs representative spikes in an isolated disposable environment
- Uses `PASS`, `CONDITIONAL PASS`, `FAIL`, or `INCONCLUSIVE` as the integration gate
- Prevents a toy demo, successful import, or paper benchmark from being treated as local proof
- Integrates only the validated production boundary and preserves the acceptance test
- Reports unavailable search channels and uncertainty instead of pretending the search was exhaustive

## Decisions and gates

The research phase ends with one of five implementation strategies:

- `KEEP` — retain the repository's existing suitable solution
- `ADOPT` — use a mature solution substantially as-is
- `EXTEND` — use a mature foundation with a thin project-specific layer
- `COMPOSE` — combine a small number of complementary mature components
- `BUILD` — implement a focused custom boundary because no candidate satisfies the constraints

The feasibility phase ends with one status:

- `PASS` — all hard thresholds and critical assumptions were verified
- `CONDITIONAL PASS` — viable only under explicit bounded conditions
- `FAIL` — a hard threshold or non-negotiable constraint was violated
- `INCONCLUSIVE` — a material uncertainty could not be resolved

A research verdict is not a feasibility pass.

## Repository layout

```text
skills/sota-first/
├── SKILL.md
└── references/
    ├── feasibility-playbook.md
    ├── scoring-rubric.md
    ├── search-playbook.md
    └── verdict-template.md
scripts/
├── install.ps1
├── install.sh
└── validate_skill.py
evals/
├── README.md
└── activation.csv
```

## Install for Codex

Codex discovers user-scoped skills from `~/.agents/skills` and repository-scoped skills from `.agents/skills`.

### Windows PowerShell — user scope

```powershell
.\scripts\install.ps1
```

### Windows PowerShell — current repository only

```powershell
.\scripts\install.ps1 -Scope Repo -RepoPath C:\path\to\project
```

### macOS/Linux — user scope

```bash
./scripts/install.sh
```

### macOS/Linux — current repository only

```bash
./scripts/install.sh --scope repo --repo /path/to/project
```

The installers refuse to overwrite an existing copy unless `-Force` (PowerShell) or `--force` (shell) is supplied.

## Manual installation

User scope:

```text
~/.agents/skills/sota-first/
```

Repository scope:

```text
<repo>/.agents/skills/sota-first/
```

Copy the entire `skills/sota-first` directory into the chosen location.

## Usage

### Research-only

```text
Use $sota-first to research and compare the most mature approaches for
real-time indoor localization from an egocentric video stream. Do not
implement or change project files.
```

Expected result: a research verdict, candidate comparison, recommendation, and feasibility handoff. No production changes.

### Research plus feasibility validation

```text
Use $sota-first to choose the best visual grounding method for our GPU
and latency constraints, then run an isolated representative feasibility
spike. Stop before production integration.
```

Expected result: a research verdict followed by a measured feasibility verdict. No production integration.

### Research, validate, and integrate

```text
Use $sota-first to research the most mature PDF extraction pipeline,
validate it on representative project documents, and if it passes the
acceptance thresholds, integrate it into the service.
```

Expected result: research verdict, feasibility gate, clean integration, preserved acceptance tests, and rollback information.

### Resume a later phase

```text
The prior SOTA-first research verdict is still current. Validate the
recommended model on representative clips, but do not integrate it yet.
```

```text
The candidate has passed the SOTA-first feasibility gate. Integrate the
validated boundary and preserve its acceptance benchmark.
```

The skill should not activate for trivial edits such as fixing a typo, formatting a file, or renaming a local variable.

## Validate

```bash
python scripts/validate_skill.py
```

The repository includes activation cases with expected research depth and delivery phase so trigger and phase-selection behavior can be evaluated over time.

## Design principles

- Primary evidence before popularity
- Repository fit before novelty
- Research selection before feasibility claims
- Representative validation before production promotion
- Comparable benchmarks only
- Current versions and exact dates for time-sensitive claims
- Minimal custom code after selection
- Clean promotion instead of accidental prototype-to-production copying
- Honest uncertainty and explicit search coverage

## Compatibility

The package follows the open Agent Skills structure used by current OpenAI Codex: a skill directory anchored by `SKILL.md` with `name` and `description` front matter, plus optional references and scripts.

## Acknowledgments

The workflow is an original implementation inspired by the broader “research before coding” pattern, including ECC's `search-first` skill, and by OpenAI's Agent Skills authoring and evaluation guidance.

## License

MIT
