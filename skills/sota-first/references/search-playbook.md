# Search Playbook

Load this reference for Phase A in Full mode. Adapt the search to the decision type instead of applying every item mechanically.

This playbook identifies and ranks candidates. It does not prove Architecture compatibility or local feasibility. End the search phase by preparing the evidence and proposed integration sketch required by the separate architecture and feasibility playbooks.

## 1. Repository reconnaissance

Inspect the project before searching externally.

### Instructions and architecture

- Applicable `AGENTS.md`, `CONTRIBUTING.md`, README files, design docs, ADRs, and issue templates
- Directory structure, layering rules, component boundaries, and ownership boundaries
- Existing interfaces, services, data models, schemas, events, state ownership, and extension points
- Request, event, data, and control flow
- Dependency graph, process boundaries, deployment topology, network paths, and hardware placement
- Reliability, security, privacy, observability, migration, and rollback conventions

### Runtime and dependencies

- Package manifests and lockfiles
- Framework, language, compiler, runtime, driver, and deployment versions
- Existing dependencies that already provide part of the requested capability
- Build, test, lint, benchmark, and deployment commands

### Constraints

- Latency, throughput, quality, memory, storage, compute, network, scaling, and availability
- Consistency, durability, ordering, concurrency, backpressure, and failure assumptions
- Supported platforms, browsers, devices, GPUs, operating systems, and offline requirements
- Security, privacy, compliance, tenancy, data residency, and licensing
- Team ownership, operational maturity, migration tolerance, and rollback needs

### Search patterns

Use targeted code search for the capability, likely interface names, protocol terms, schemas, dependencies, feature flags, tests, and related TODOs. Inspect relevant history when it can explain why an existing approach, boundary, or architecture was chosen or abandoned.

## 2. Classify the external research

### A. Software library or integration

Prioritize:

1. Official documentation and compatibility tables
2. Package registry metadata and release history
3. Security advisories and migration guides
4. Source repository activity, issue quality, and maintainer responsiveness
5. Independent production reports and ecosystem integrations

Check:

- Exact runtime, framework, platform, protocol, and deployment compatibility
- API stability, schema/versioning strategy, and upgrade path
- Transitive dependency size, conflicts, and risk
- License and commercial-use terms
- Maintenance bus factor and release cadence
- Observability, testing support, failure behavior, and rollback

### B. ML, CV, agent, retrieval, or research method

Prioritize:

1. Original paper or technical report
2. Official implementation, checkpoint, and project page
3. Benchmark or leaderboard owner
4. Credible independent reproduction
5. Deployment reports and issue trackers

Check:

- Task definition, dataset, split, metric, and evaluation protocol
- Publication and last-update dates
- Peer-reviewed status versus preprint or vendor report
- Training data, checkpoint availability, and usage terms
- Inference latency, throughput, memory, hardware, precision, and batch size
- Required calibration, mapping, sensors, prompts, services, or model-serving topology
- Reproduction quality and gap between paper and released code
- Streaming, online, offline, edge, batching, concurrency, cancellation, and failure behavior

Never compare numbers that use different datasets, metrics, resolutions, hardware, batch sizes, or test protocols without clearly normalizing or labeling the mismatch.

### C. System architecture or infrastructure

Prioritize:

1. Open standards and official reference architectures
2. Maintained reference implementations
3. Multiple independent production case studies
4. Failure analyses, operational guidance, migration reports, and postmortems

Check:

- Component and service boundaries
- API, event, schema, and state compatibility
- Consistency, availability, durability, and failure assumptions
- Scaling envelope, resource placement, and cost model
- Operational complexity, observability, incident recovery, and ownership
- Lock-in, portability, data migration, rollout, and rollback
- Security, privacy, tenancy, and trust boundaries

### D. Security- or privacy-sensitive capability

Prioritize official standards, vendor advisories, recognized security bodies, and primary documentation. Treat blog-only guidance as insufficient for the final recommendation. Identify threat model, supported algorithms, key management, trust boundaries, data flow, update policy, auditability, and known advisories.

## 3. Generate useful search queries

Build queries from:

- Exact capability and synonyms
- Current stack and version
- Hard constraints such as real-time, offline, edge, license, hardware, consistency, or topology
- Evidence type such as benchmark, official docs, release notes, reproduction, architecture case study, postmortem, security advisory, or migration
- Current year when freshness matters

Examples:

- `<capability> official documentation compatibility <framework version>`
- `<capability> benchmark official implementation real-time`
- `<method class> paper official code inference latency`
- `<library> release notes security advisory license migration`
- `<architecture> reference implementation production postmortem`
- `<candidate> API schema deployment topology failure modes`

Do not search only for “best.” Search for failure modes, limitations, migration pain, abandoned projects, negative evidence, incompatibilities, and operational incidents.

## 4. Source quality tiers

### Tier 1 — Primary and authoritative

- Official specifications and documentation
- Original papers and official technical reports
- Official repositories, releases, model cards, dataset cards, and benchmark maintainers
- Official security advisories and package registries

### Tier 2 — Strong corroboration

- Credible independent reproductions
- Reputable engineering and architecture reports with measurements and disclosed setup
- Maintainer issue discussions, migration reports, and production postmortems
- Peer-reviewed surveys that preserve comparison context

### Tier 3 — Discovery and caveats

- Community discussions, tutorials, aggregators, and informal comparisons

Use Tier 3 to discover candidates or operational problems. Do not base a high-confidence core claim on Tier 3 alone.

## 5. Minimum coverage for Full mode

Aim for:

- Two to four serious finalists
- At least one primary source for every finalist
- Independent corroboration for the recommended candidate when available
- A direct check of version, release date, license, repository compatibility, interfaces, and deployment requirements
- Negative evidence or known limitations for the leading candidate
- Enough repository evidence to sketch how the leading candidate would actually fit the system

When this coverage is impossible, state exactly what was unavailable and lower confidence.

## 6. Research log

Keep a compact log containing:

- Search date
- Repository revision
- Channels actually searched
- Queries or categories searched
- Sources used for each finalist
- Channels unavailable or skipped and why
- Facts that remain unresolved

The final user-facing verdict may summarize this log rather than exposing every query.

## 7. Architecture review handoff

Before leaving candidate selection, prepare:

- The recommended candidate and exact version, checkpoint, service tier, or commit
- Existing component, interface, data, deployment, security, and ownership boundaries affected
- The smallest proposed integration architecture
- New dependencies, runtime, platform, service, model-serving, or hardware requirements
- Expected data and control flow
- State, schema, protocol, migration, and rollback implications
- Inferred compatibility claims that an architecture reviewer must challenge
- A simpler design or alternative candidate worth comparing

Continue with `architecture-review.md` when architecture review is required.

## 8. Feasibility handoff

After the Architecture Review Gate, identify:

- Architecture gate status, score, hard blockers, and explicit conditions
- Which project-fit and architecture claims remain inferred rather than locally measured
- The highest-risk unknown most likely to reverse the recommendation
- Representative data, traffic, hardware, runtime, and deployment conditions
- Measurable acceptance thresholds, including architecture-derived conditions
- The smallest isolated experiment that can falsify the recommendation

For a Research-only request, this handoff is the stopping point. For a validation or integration request, continue with `feasibility-playbook.md`.
