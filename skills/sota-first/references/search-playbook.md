# Search Playbook

Load this reference in Full mode. Adapt the search to the decision type instead of applying every item mechanically.

## 1. Repository reconnaissance

Inspect the project before searching externally.

### Instructions and architecture

- Applicable `AGENTS.md`, `CONTRIBUTING.md`, README files, design docs, ADRs, and issue templates
- Directory structure and ownership boundaries
- Existing interfaces, services, data models, and extension points

### Runtime and dependencies

- Package manifests and lockfiles
- Framework, language, compiler, runtime, and deployment versions
- Existing dependencies that already provide part of the requested capability
- Build, test, lint, benchmark, and deployment commands

### Constraints

- Latency, throughput, quality, memory, storage, compute, network, and availability
- Supported platforms, browsers, devices, GPUs, operating systems, and offline requirements
- Security, privacy, compliance, data residency, and licensing
- Team conventions, operational maturity, migration tolerance, and rollback needs

### Search patterns

Use targeted code search for the capability, likely interface names, protocol terms, dependencies, feature flags, tests, and related TODOs. Inspect relevant history when it can explain why an existing approach was chosen or abandoned.

## 2. Classify the external research

### A. Software library or integration

Prioritize:

1. Official documentation and compatibility tables
2. Package registry metadata and release history
3. Security advisories and migration guides
4. Source repository activity, issue quality, and maintainer responsiveness
5. Independent production reports and ecosystem integrations

Check:

- Exact runtime/framework compatibility
- API stability and upgrade path
- Transitive dependency size and risk
- License and commercial-use terms
- Maintenance bus factor and release cadence
- Observability, testing support, and failure behavior

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
- Required calibration, mapping, sensors, prompts, or external services
- Reproduction quality and gap between paper and released code
- Real-time, streaming, online, or edge constraints when applicable

Never compare numbers that use different datasets, metrics, resolutions, hardware, batch sizes, or test protocols without clearly normalizing or labeling the mismatch.

### C. System architecture or infrastructure

Prioritize:

1. Open standards and official reference architectures
2. Maintained reference implementations
3. Multiple independent production case studies
4. Failure analyses, operational guidance, and migration reports

Check:

- Consistency, availability, durability, and failure assumptions
- Scaling envelope and cost model
- Operational complexity, observability, and incident recovery
- Lock-in, portability, data migration, and rollback
- Security boundaries and threat model

### D. Security- or privacy-sensitive capability

Prioritize official standards, vendor advisories, recognized security bodies, and primary documentation. Treat blog-only guidance as insufficient for the final recommendation. Identify threat model, supported algorithms, key management, update policy, data flow, and known advisories.

## 3. Generate useful search queries

Build queries from:

- Exact capability and synonyms
- Current stack and version
- Hard constraints such as real-time, offline, edge, license, or hardware
- Evidence type such as benchmark, official docs, release notes, reproduction, security advisory, or migration
- Current year when freshness matters

Examples:

- `<capability> official documentation compatibility <framework version>`
- `<capability> benchmark official implementation real-time`
- `<method class> paper official code inference latency`
- `<library> release notes security advisory license`
- `<architecture> reference implementation production postmortem`

Do not search only for “best.” Search for failure modes, limitations, migration pain, abandoned projects, and negative evidence.

## 4. Source quality tiers

### Tier 1 — Primary and authoritative

- Official specifications and documentation
- Original papers and official technical reports
- Official repositories, releases, model cards, dataset cards, and benchmark maintainers
- Official security advisories and package registries

### Tier 2 — Strong corroboration

- Credible independent reproductions
- Reputable engineering reports with measurements and disclosed setup
- Maintainer issue discussions and migration reports
- Peer-reviewed surveys that preserve comparison context

### Tier 3 — Discovery and caveats

- Community discussions, tutorials, aggregators, and informal comparisons

Use Tier 3 to discover candidates or operational problems. Do not base a high-confidence core claim on Tier 3 alone.

## 5. Minimum coverage for Full mode

Aim for:

- Two to four serious finalists
- At least one primary source for every finalist
- Independent corroboration for the recommended candidate when available
- A direct check of version, release date, license, and repository compatibility
- Negative evidence or known limitations for the leading candidate

When this coverage is impossible, state exactly what was unavailable and lower confidence.

## 6. Research log

Keep a compact log containing:

- Search date
- Channels actually searched
- Queries or categories searched
- Sources used for each finalist
- Channels unavailable or skipped and why
- Facts that remain unresolved

The final user-facing verdict may summarize this log rather than exposing every query.
