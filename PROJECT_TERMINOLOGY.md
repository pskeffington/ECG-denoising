# Project Terminology

This repository follows the portfolio-wide terminology hierarchy below.

- **Project** — the substantive research, engineering, civic, scholarly, or applied line of work. Project status describes the state of that work, not merely repository activity.
- **Repository** — an implementation and evidence container that supports a project. A repository may contain code, data structures, documentation, validation artifacts, generated outputs, and review records.
- **Proof packet** — the reviewable evidence bundle that supports a bounded claim about project progress, maturity, or readiness.
- **Artifact** — a specific file, output, report, dataset, model, figure, workflow result, or other inspectable object produced by the project or repository.
- **Product surface** — a demonstrable interface or packaged workflow such as a CLI, report generator, application, API, reproducible runner, or public-safe demo.
- **Portfolio** — the collection of projects and their supporting repositories, evidence, proof packets, and cross-project controls.

## Usage Rules

1. Use **project** for substantive mission, research question, applied objective, scholarly contribution, or overall project status.
2. Use **repository** for GitHub-specific implementation state, file organization, code maturity, repository evidence, or repository-local validation.
3. Do not treat repository existence, commit volume, or repository activity as proof of project completion, external validation, production readiness, or market value.
4. A repository valuation represents the evidenced contribution of that repository to a project or portfolio. It is not automatically the total value of the project.
5. When multiple repositories support one project, aggregate only after checking overlap, shared artifacts, duplicated evidence, and cross-repository dependencies.
6. Use **proof packet** only for a bounded bundle of evidence that can be reviewed against explicit claims and limitations.
7. Keep public-facing descriptions source-bounded and preserve the repository's stated safety, privacy, research, and evidence boundaries.

## Preferred Pattern

```text
project
  -> repository or repositories
  -> artifacts and validation
  -> proof packet
  -> bounded project claim or status
  -> portfolio aggregation, when applicable
```
