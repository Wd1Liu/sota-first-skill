# SOTA First Skill

A reusable Agent Skill that makes coding agents research a repository, compare current state-of-the-art and production-mature approaches, have the proposed integration reviewed for architecture and system compatibility, validate the selected candidate under representative project constraints, and optionally integrate it into the feature.

It is designed to answer four distinct questions:

1. What is the strongest current research approach for the task?
2. What should this project actually adopt given its product, hardware, latency, licensing, maintenance, and integration constraints?
3. Does the proposed design fit the existing architecture, interfaces, data contracts, runtime, deployment topology, failure model, security boundaries, ownership, and evolution path?
4. Does the reviewed candidate measurably work in this repository before it becomes production code?

The skill keeps **Research SOTA**, **Engineering recommendation**, **Architecture compatibility**, and **local feasibility** separate.

## Workflow

```text
Repository and external research
             │
             ▼
Engineering recommendation
             │
             ▼
Architecture Expert Review Gate
             │
             ▼
Isolated feasibility validation
             │
             ▼
Production integration
```

A request may stop after research and architecture review, stop after feasibility validation, or continue through all passing gates into Integration.

## Two independent controls

### Research depth

- `Skip` — no external selection work is needed
- `Quick mode` — compact repository check and targeted evidence review
- `Full mode` — complete repository, evidence, comparison, architecture, and risk analysis

### Delivery phase

- `Research-only` — search, compare, architecture-review when relevant, and recommend without implementing
- `Feasibility validation` — run an isolated, disposable spike without integrating production code
- `Integration` — promote an architecture-reviewed and validated candidate into the real feature

When the user requests the full pipeline, the skill continues through each passing gate without pausing for redundant approval. When the user requests only research, architecture review, or validation, it stops at that boundary.

## Architecture expert review

For architecture-sensitive work, the skill requires a concrete integration sketch covering component boundaries, responsibilities, interfaces, schemas, state, dependencies, runtime, data and control flow, deployment topology, failure isolation, security boundaries, observability, ownership, migration, and rollback.

The review should use a dedicated architect agent or subagent when the active harness provides one. Otherwise it performs a separate second-pass review and labels it `same-agent structured review`; it must not falsely claim independent expert review.

The architecture reviewer scores nine dimensions:

| Dimension | Weight |
|---|---:|
| Boundary and responsibility fit | 15% |
| Interface and data-contract fit | 15% |
| Dependency, runtime, and platform fit | 15% |
| Deployment, topology, and resource fit | 10% |
| Reliability and failure isolation | 10% |
| Security, privacy, and compliance fit | 10% |
| Observability and operability | 10% |
| Migration, compatibility, and rollback | 5% |
| Maintainability, ownership, and evolution | 10% |

Each dimension receives a 1–5 score. The weighted result is reported on a 0–100 scale, but hard blockers override the number.

Architecture gate outcomes:

- `PASS` — score at least 80, no hard blocker, and no dimension below 3
- `CONDITIONAL PASS` — score 65–79, or a bounded non-blocking weakness with explicit remediation
- `FAIL` — score below 65, a hard blocker, or a critical dimension scored 1
- `INCONCLUSIVE` — material architecture evidence or the integration design is missing

The reviewer must present both the strongest compatibility argument and the strongest objection. Architecture conditions are transferred into feasibility thresholds and production acceptance criteria.

## What it does

- Inspects the current repository before searching externally
- Identifies existing architecture, interfaces, data contracts, dependencies, deployment, hardware, and ownership constraints
- Selects Quick or Full research depth based on decision risk
- Supports research-only, architecture-review-only, validation-only, and full research-review-validate-integrate workflows
- Prioritizes official documentation, original papers, official code, registries, benchmarks, standards, advisories, architecture reports, and postmortems
- Compares research strength and predicted project fit without collapsing them into one score
- Requires a separate Architecture Review Gate for material system changes
- Defines a falsifiable feasibility contract with measurable thresholds
- Runs representative spikes in an isolated disposable environment
- Prevents a paper benchmark, architecture score, successful import, or toy demo from being treated as local proof
- Integrates only the reviewed and validated production boundary
- Preserves architecture conditions, acceptance tests, operational ownership, and rollback information
- Reports unavailable tools, missing evidence, and uncertainty honestly

## Decisions and gates

The research phase ends with one implementation strategy:

- `KEEP` — retain the repository's existing suitable solution
- `ADOPT` — use a mature solution substantially as-is
- `EXTEND` — use a mature foundation with a thin project-specific layer
- `COMPOSE` — combine a small number of complementary mature components
- `BUILD` — implement a focused custom boundary because no candidate satisfies the constraints

Architecture review and feasibility validation each end with one status:

- `PASS`
- `CONDITIONAL PASS`
- `FAIL`
- `INCONCLUSIVE`

A high research score cannot override an architecture or feasibility failure.

## Repository layout

```text
skills/sota-first/
├── SKILL.md
└── references/
    ├── architecture-review.md
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

The installers refuse to overwrite an existing copy unless `-Force` or `--force` is supplied.

## Usage

### Research and architecture review only

```text
Use $sota-first to research the strongest approaches for real-time
indoor localization, propose how the leading candidate would fit this
repository, and have an architecture reviewer score system compatibility.
Do not run a spike or implement anything.
```

Expected result: research verdict, proposed integration architecture, architecture scorecard and gate, rejected alternatives, and feasibility handoff. No production changes.

### Research plus feasibility validation

```text
Use $sota-first to choose the best visual grounding method for our GPU
and latency constraints, architecture-review the proposed pipeline, then
run an isolated representative feasibility spike. Stop before integration.
```

Expected result: research verdict, Architecture Review Gate, and measured feasibility verdict. No production integration.

### Research, review, validate, and integrate

```text
Use $sota-first to research the most mature PDF extraction pipeline,
architecture-review its fit with our service and data contracts, validate
it on representative documents, and if every required gate passes,
integrate it into the service.
```

Expected result: staged verdicts, clean integration, preserved contract checks and acceptance tests, operational ownership, and rollback information.

### Resume a later phase

```text
The prior research verdict is still current. Run the Architecture Review
Gate for the proposed design and stop before feasibility validation.
```

```text
The candidate passed architecture review. Validate its conditions on
representative traffic, but do not integrate it yet.
```

```text
The reviewed candidate passed feasibility. Integrate the validated
boundary and preserve its architecture and acceptance checks.
```

The skill should not activate for trivial edits such as fixing a typo, formatting a file, or renaming a local variable.

## Validate

```bash
python scripts/validate_skill.py
```

The repository includes activation cases with expected research depth, delivery phase, and architecture-review requirement so trigger and phase-selection behavior can be evaluated over time.

## Design principles

- Primary evidence before popularity
- Repository and architecture fit before novelty
- Concrete integration design before architecture scoring
- Adversarial review before endorsement
- Hard blockers before weighted totals
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
