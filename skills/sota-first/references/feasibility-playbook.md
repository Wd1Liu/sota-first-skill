# Feasibility Validation Playbook

Use this reference when the delivery phase includes feasibility validation. Research identifies a promising candidate; validation determines whether that candidate actually works under this repository's constraints.

A paper result, successful installation, working import, or toy demo is not sufficient proof of feasibility.

## 1. Define a validation contract

Before running a spike, state:

- The candidate and exact version, checkpoint, service tier, or commit being tested
- The project assumption or risk being tested
- Representative inputs, traffic, data, hardware, runtime, and operating conditions
- Measurable acceptance thresholds
- Hard failure conditions
- The smallest experiment that can falsify the recommendation
- Which changes are disposable and how they will be cleaned up

Use concrete thresholds whenever possible. Examples include latency percentiles, throughput, memory, task quality, failure recovery, compatibility, startup time, dependency size, or integration effort.

## 2. Test the highest-risk unknown first

Order experiments by decision value, not implementation convenience.

Typical high-risk unknowns include:

- A required API or runtime is incompatible with the repository
- Real latency or memory exceeds the deployment budget
- Quality drops materially on representative project data
- Streaming, online, offline, or edge behavior differs from the published setup
- A checkpoint, license, model term, dataset, or service capability is unavailable
- Integration requires an architectural rewrite rather than a thin adapter
- Error handling, observability, rollback, or failure recovery is inadequate

Stop early when a hard disqualifier is confirmed. Do not build a polished prototype for a candidate that has already failed a non-negotiable constraint.

## 3. Isolate the experiment

Prefer, in order:

1. Read-only compatibility checks and documented capability probes
2. A temporary directory or disposable script outside production paths
3. A temporary worktree, throwaway branch, or clearly isolated experiment directory
4. A shadow path that does not affect production traffic or persistent data

During validation:

- Do not treat experimental code as production integration
- Avoid persistent manifest, lockfile, migration, infrastructure, or configuration changes unless they are isolated and necessary for the test
- Record every temporary dependency and environment change
- Do not commit secrets, credentials, model weights, datasets, or generated artifacts
- Clean up disposable artifacts, or list exactly what remains and why

## 4. Use representative conditions

A validation result is useful only when its setup covers the constraint being tested.

### Software library or integration

Check:

- Exact runtime and framework compatibility
- Installation and transitive dependency impact
- API shape, error behavior, retries, cancellation, and concurrency
- Required configuration, credentials, and external services
- Testability, observability, migration, and rollback
- Whether the integration remains a thin boundary or spreads through the codebase

### ML, CV, agent, retrieval, or research method

Check the relevant subset of:

- Quality on representative project samples, not only published datasets
- End-to-end latency, including preprocessing and postprocessing
- Throughput, p50/p95 latency, warm-up, startup, and streaming behavior
- Peak and steady-state CPU, GPU memory, RAM, storage, and network use
- Hardware, precision, resolution, batch size, sequence length, and context settings
- Checkpoint access, model/data terms, calibration, prompts, sensors, maps, or external services
- Robustness to the project's expected edge cases and failure modes

### System architecture or infrastructure

Check:

- Expected load and scaling envelope
- Availability, consistency, durability, and recovery behavior
- Operational complexity, observability, backup, migration, and rollback
- Cost drivers and external service limits
- Failure injection or degraded-mode behavior when practical

### Security- or privacy-sensitive capability

Check:

- Threat model and trust boundaries
- Safe defaults and configuration requirements
- Data flow, retention, encryption, key or credential management
- Current advisories and supported versions
- Failure behavior and auditability

A disposable security test does not replace a proper security review when one is required.

## 5. Record the environment and results

Capture enough detail to reproduce the decision:

- Date and repository revision
- Candidate version or commit
- Hardware, operating system, runtime, framework, and relevant drivers
- Dataset, sample, traffic shape, or workload
- Configuration, precision, batch size, resolution, and other material settings
- Commands or test procedure
- Raw measurements and observed failure modes
- Differences from published or vendor-reported conditions

Separate external claims from locally measured results.

## 6. Assign a feasibility status

Use exactly one status:

- **PASS** — All hard thresholds were met, the critical integration assumptions were verified, and no new disqualifier appeared.
- **CONDITIONAL PASS** — The candidate is viable only under explicit conditions or with bounded follow-up work that still fits the project constraints.
- **FAIL** — A hard threshold or non-negotiable constraint was violated.
- **INCONCLUSIVE** — The test could not resolve a material uncertainty because data, access, tooling, environment, or evidence was insufficient.

Do not convert an inconclusive result into a pass because the candidate appears promising.

## 7. Decide the transition

- For a research-only request, do not enter validation unless the user requested it.
- For a validation-only request, stop after the feasibility verdict and do not integrate production code.
- For a research-validate-integrate request, continue directly after **PASS**.
- After **CONDITIONAL PASS**, continue only when the conditions can be satisfied within the stated constraints and requested scope; otherwise stop and report the condition.
- After **FAIL**, test the next justified finalist or revise the research verdict. Do not force the failed candidate into production.
- After **INCONCLUSIVE**, identify the smallest missing test or evidence needed. Do not integrate unless the unresolved uncertainty is explicitly non-material.

## 8. Promote cleanly, not by accident

When integration is authorized after a pass:

- Recreate the minimal production implementation cleanly
- Do not blindly copy temporary scripts, hard-coded paths, debug logging, test credentials, or experimental configuration
- Preserve the acceptance test or benchmark that established feasibility
- Document any difference between the validated spike and the final integration
- Keep a rollback path for high-impact changes
