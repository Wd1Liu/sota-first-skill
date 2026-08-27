# SOTA First Skill

A reusable Agent Skill that makes coding agents research the repository, current state of the art, production maturity, and project fit **before** implementing a non-trivial feature.

It is designed to answer two distinct questions:

1. What is the strongest current research approach for the task?
2. What should this project actually adopt given its hardware, latency, licensing, maintenance, and integration constraints?

The skill deliberately separates **Research SOTA** from the **Engineering recommendation** and ends with one of five decisions: `KEEP`, `ADOPT`, `EXTEND`, `COMPOSE`, or `BUILD`.

## What it does

- Inspects the current repository before searching externally
- Selects Quick or Full research mode based on decision risk
- Prioritizes official documentation, original papers, official code, registries, benchmarks, and security advisories
- Compares research strength and production fit on separate axes
- Blocks substantial implementation in Full mode until a compact research verdict exists
- Continues directly into implementation when the user already requested it
- Reports unavailable search channels and uncertainty instead of pretending the search was exhaustive

## Repository layout

```text
skills/sota-first/
├── SKILL.md
└── references/
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

Codex currently discovers user-scoped skills from `~/.agents/skills` and repository-scoped skills from `.agents/skills`.

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

Explicit invocation in Codex:

```text
Use $sota-first to choose the most mature approach for real-time indoor localization from an egocentric video stream, then implement the selected approach.
```

The description also allows implicit activation for requests such as:

```text
Add a production-ready PDF extraction pipeline to this project.
```

```text
Choose the best visual grounding model for our latency and GPU constraints, then integrate it.
```

```text
Design a new caching layer for this service.
```

It should not activate for trivial edits such as fixing a typo, formatting a file, or renaming a local variable.

## Validate

```bash
python scripts/validate_skill.py
```

The repository also includes activation examples under `evals/` so trigger behavior can be evaluated and refined over time.

## Design principles

- Primary evidence before popularity
- Repository fit before novelty
- Comparable benchmarks only
- Current versions and exact dates for time-sensitive claims
- Minimal custom code after selection
- Honest uncertainty and explicit search coverage

## Compatibility

The package follows the open Agent Skills structure used by current OpenAI Codex: a skill directory anchored by `SKILL.md` with `name` and `description` front matter, plus optional references and scripts.

## Acknowledgments

The workflow is an original implementation inspired by the broader “research before coding” pattern, including ECC’s `search-first` skill, and by OpenAI’s Agent Skills authoring and evaluation guidance.

## License

MIT
