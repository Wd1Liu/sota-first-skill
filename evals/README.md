# Activation Evals

`activation.csv` contains positive and negative prompts for testing whether the skill triggers at the right boundary.

The most important behaviors are:

1. Trigger on explicit best/SOTA/mature requests and non-trivial architecture, dependency, ML, security, or performance decisions.
2. Avoid triggering on trivial edits, established local fixes, explanations, tests for existing behavior, and explicitly fixed implementations.
3. When triggered for implementation, produce a verdict and continue into implementation without an unnecessary approval pause.
4. Keep Research SOTA and Engineering recommendation separate.
5. Report missing search channels and uncertainty honestly.

A future automated eval can run each prompt through Codex, capture whether `sota-first` was selected, and score both activation and verdict quality.
