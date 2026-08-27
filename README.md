# SOTA First Skill

A reusable Agent Skill for turning a vague “use the best method” request into an evidence-backed, architecture-reviewed, engineering-checked, locally validated implementation decision.

Instead of asking one generic agent to search a few links and immediately code, the skill organizes a staged expert council:

```text
Repository mapping and capability decomposition
                        │
                        ▼
       Broad public landscape investigation
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Industry practice  Academic frontier  Ecosystem/standards
      └─────────────────┼─────────────────┘
                        ▼
              Domain-specialist dossiers
                        │
                        ▼
         Multiple end-to-end architecture options
                        │
               ┌────────┴────────┐
               ▼                 ▼
      Architecture Review   Engineering Readiness
               └────────┬────────┘
                        ▼
               Evidence-audited decision
                        │
                        ▼
          Isolated representative feasibility spike
                        │
                        ▼
               Clean production integration
```

## What it answers

The workflow keeps six questions separate:

1. **Research SOTA** — what has the strongest credible current research result?
2. **Industry practice** — what methods are publicly disclosed by relevant leading companies, category leaders, maintainers, and recognized practitioners?
3. **Domain detail** — how does each serious method actually work, and what assumptions and failure modes does it have?
4. **Architecture compatibility** — which complete system shape best fits the repository?
5. **Engineering readiness** — can the exact implementation bundle coexist, build, deploy, operate, and fit the resource budget?
6. **Local feasibility** — does it measurably work under representative project conditions?

A method can win the paper benchmark and still lose the final engineering decision.

## Expert roles

Full mode can use separate subagents or role-separated passes:

- Research Director
- Repository Cartographer
- Industry Practice Investigator
- Academic Frontier Investigator
- Ecosystem and Standards Investigator
- Domain Specialists
- Solution Architect
- Architecture Reviewer
- Engineering Reviewer
- Evidence Auditor and Decision Chair
- Feasibility Experimenter
- Integration Engineer

When separate subagents are unavailable, reviews are labeled as same-agent structured reviews. The skill never pretends that a human expert or independent reviewer participated.

## Broad search, then deep analysis

The investigation phase searches more than libraries and papers.

It covers:

- Official engineering blogs and architecture documentation
- Conference talks and system papers
- Public implementations from major companies, category leaders, and high-signal startups
- Public postmortems and migration reports
- Current surveys, papers, benchmarks, leaderboards, and official code
- Independent reproductions and failure analyses
- Mature open-source ecosystems
- Standards, protocols, SDKs, registries, advisories, and vendor reference architectures
- Negative evidence, abandoned projects, and operational pain

It does not infer private company internals from marketing, hiring posts, or indirect stack signals.

The search first maps distinct solution families, then Domain Specialists deeply verify serious candidates.

## Multi-architecture synthesis

The Solution Architect combines compatible capabilities into two to four distinct end-to-end options.

Each option specifies:

- Components and responsibilities
- Interfaces, schemas, state, and data contracts
- Data and control flow
- Runtime and deployment topology
- CPU/GPU/storage/network placement
- Concurrency, queues, retries, cancellation, and backpressure
- Failure isolation and degraded behavior
- Security and privacy boundaries
- Observability and ownership
- Preliminary latency and resource budgets
- Migration and rollback

The workflow explicitly rejects “best component from every benchmark” Frankenstein architectures whose contracts, runtimes, resources, or assumptions conflict.

## Architecture Review Gate

The Architecture Reviewer compares all serious options across nine dimensions:

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

Gate statuses:

- `PASS`
- `CONDITIONAL PASS`
- `FAIL`
- `INCONCLUSIVE`

Hard blockers override weighted totals.

## Engineering Readiness Gate

The Engineering Reviewer evaluates concrete implementation bundles:

- Exact libraries, models, services, protocols, versions, runtimes, and drivers
- Pairwise API, schema, data-format, dependency, ABI, CUDA, platform, and license compatibility
- End-to-end latency and critical-path allocation
- CPU, GPU, VRAM, RAM, storage, network, startup, concurrency, and headroom
- Resource placement and contention
- Build, packaging, CI, deployment, observability, testing, migration, rollback, and ownership
- External service quotas, regions, cost, availability, and supply-chain risk

The Engineering Readiness score is also gated by hard blockers. It predicts buildability but does not replace local measurement.

## Staged endpoints

### Research-only

Search, analyze, synthesize, architecture-review, engineering-review, and recommend without running a spike or changing production state.

```text
Use $sota-first to investigate how leading companies, open-source
projects, and current academic work solve streaming egocentric
localization. Have domain specialists analyze the serious methods,
synthesize multiple architectures, and run architecture and engineering
reviews. Do not validate or implement.
```

### Feasibility validation

Continue to an isolated representative spike and stop before production integration.

```text
Use $sota-first to research candidate visual grounding pipelines,
compare complete architectures, review implementation compatibility and
GPU allocation, then validate the preferred bundle on representative
clips. Stop before integration.
```

### Integration

Continue through every passing gate and integrate the smallest reviewed and validated production boundary.

```text
Use $sota-first to research, architecture-review, engineering-review,
validate, and, if every required gate passes, integrate the most mature
PDF extraction architecture into the service.
```

## Research depth

- `Skip` — trivial or already-decided work
- `Quick mode` — focused search and compact review
- `Full mode` — complete expert-council workflow

Research depth and delivery endpoint are independent.

## Decisions and gates

Research strategy:

- `KEEP`
- `ADOPT`
- `EXTEND`
- `COMPOSE`
- `BUILD`

Architecture, Engineering, and Feasibility gates:

- `PASS`
- `CONDITIONAL PASS`
- `FAIL`
- `INCONCLUSIVE`

A high research score cannot override an Architecture, Engineering, or Feasibility failure.

## Repository layout

```text
skills/sota-first/
├── SKILL.md
└── references/
    ├── architecture-review.md
    ├── architecture-synthesis.md
    ├── domain-analysis.md
    ├── engineering-review.md
    ├── expert-orchestration.md
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

User scope:

```powershell
.\scripts\install.ps1
```

Repository scope:

```powershell
.\scripts\install.ps1 -Scope Repo -RepoPath C:\path\to\project
```

macOS/Linux:

```bash
./scripts/install.sh
```

Overwrite an existing installation with `-Force` or `--force`.

Manual locations:

```text
~/.agents/skills/sota-first/
<repo>/.agents/skills/sota-first/
```

## Validate

```bash
python scripts/validate_skill.py
```

GitHub Actions runs the same validation on pushes and pull requests. Superseded runs on the same branch are cancelled.

## Design principles

- Map the repository before searching externally
- Discover solution families before choosing implementations
- Public evidence before reputation
- Domain detail before composition
- Multiple coherent architectures before selection
- Independent adversarial review where available
- Architecture compatibility and engineering readiness as separate gates
- Hard blockers before weighted totals
- Explicit interface and resource budgets
- Representative local validation before production promotion
- Clean integration instead of prototype copying
- Honest uncertainty and truthful reviewer labels
- Stop at the requested endpoint

## Acknowledgments

The workflow is an original implementation inspired by research-before-coding practices, including ECC's `search-first` skill, and by Agent Skills authoring and evaluation patterns.

## License

MIT
