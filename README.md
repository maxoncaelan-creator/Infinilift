# Infinilift

Infinilift is a coaching app for personal trainers, online coaches and small gyms. Coaches write programs, set nutrition targets, run check-ins, message clients and take payments. Clients train, log food and check in. It runs on the web, iPhone and Android from one codebase.

Alio! Brand Studios builds it and gives it to client businesses under their own brand.

Status: research done. The plan comes after the REA study. No app code yet.

## Where things are

| Path | What it is |
|---|---|
| `docs/plan.md` | The build plan, written after the REA study |
| `docs/research/competitors.md` | The 9 platforms we studied: what they do, what they cost, where they fall short |
| `docs/research/pain-points.md` | What about 2,700 store reviews of Trainerize, TrueCoach and Everfit complain about, and which smaller apps already fix it |
| `docs/research/rea/` | The hands-on study with REA: the context pack, the prompts and the findings |
| `CONTRIBUTING.md` | Branches, staging, releases and the one-time repo settings |
| `.claude/skills/alio-humaniser/` | Writes PR descriptions and docs in plain English. Copied from the private ALIO-Brand-Studio repo, without the private messages in the voice file; change it there first |

## How a change reaches clients

Your branch → PR into `staging` → test on staging (web, TestFlight, Google Play internal testing) → release PR into `main` → production.
