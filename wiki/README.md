# {{REPO_NAME}}: the knowledge base

Everything this project claims, with its sources, in one place. Research accumulates here as it happens: a fetched paper, a licence, a design decision and its evidence. It does not stay in chat scrollback that ends with the session.

This wiki is published as a GitHub Pages site by `.github/workflows/pages.yml`. Enable it once with: `gh api repos/{owner}/{repo}/pages -X POST -f build_type=workflow`.

## Rules of the house

- **Every claim carries a source.** A statement without one is a TODO, not knowledge.
- **Tier honestly** where the project deals in contested material: *Established* (peer-reviewed, survey, published data), *Debated* (real scholarship, contested), *Speculative* (one author's construction, or our own reading). Adapt the tier names to the domain. Keep the discipline.
- **Machine data provenance lives in `SECURITY.md`.** The wiki's provenance page summarizes and defers to it.
- **One page per subject**, indexed here. Deep working notes go to `research/` with an audit trail. The wiki page cites them.

## Pages

| Page | Holds |
|---|---|
| [History of the dark factory method](history/index.html) | How the method developed, January to October 2026, in six eras, with a source for each claim |
| [Timeline](history/timeline.html) | Dated external events, template milestones, and every blog order |
| [The autonomy levels](method/five-levels.html) | Shapiro's five levels and River's driving-style levels |
| [The factory pattern](method/factory-pattern.html) | What the repository holds so an agent can work from a cold clone |
| [Principles and evidence](method/principles.html) | Each principle, the template file that carries it, and the blog orders that support it |
| [The blog, mirrored](blog/index.html) | All 44 orders of the River.io blog The Dark Factory |
| [Glossary](glossary.html) | Terms used in the method |
