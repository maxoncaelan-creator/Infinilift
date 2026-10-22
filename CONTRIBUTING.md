# Working on Infinilift

Every change goes to staging first. Main is what clients use.

## Branches and environments

| | Your branch | `staging` | `main` |
|---|---|---|---|
| What it is | One change | What's being tested | Production |
| Web | localhost | Staging web address, behind Cloudflare Access | Live web address |
| iPhone | Development build | "Infinilift Staging" on TestFlight | App Store |
| Android | Development build | Google Play internal testing | Google Play |
| Over-the-air updates | None | EAS Update channel `staging` | EAS Update channel `production` |
| Database | Supabase in Docker (`supabase start`) | Supabase project `infinilift-staging`, Sydney | Supabase project `infinilift-production`, Sydney |
| Payments | Stripe test mode | Stripe test mode | Stripe live |
| Data | Seed data | Made-up data only | Real clients |

Staging and production apps have different bundle IDs, so both install on the same phone. The deploy workflows arrive with the app scaffold (step 1 of `docs/plan.md`).

## Making a change

1. Branch from `staging`: `feature/…` or `fix/…`. AI sessions name their own branches; treat them the same.
2. Keep it to one change. Open a PR into `staging` and fill in the template.
3. Write the PR description with the `alio-humaniser` skill. The "Plain-English check" flags stock phrasing but never blocks a merge.
4. Wait for "Lint, types and tests" to pass, then squash and merge.
5. Staging updates by itself. Test it on web, iPhone and Android.

## Releasing to production

1. Open a PR from `staging` into `main` titled "Release [DATE]", listing what's in it.
2. "Lint, types and tests" must pass.
3. Merge with a merge commit, never squash. Squashing a long-running branch makes the next release carry the same commits again.
4. Production deploys from `main`. If a release changes native code (new permissions, new native modules), it needs new store builds. Otherwise it goes out over the air.

## Hotfixes

1. Branch `hotfix/…` from `main`, fix it and open a PR into `main`.
2. Once it's merged, open a PR from `main` into `staging` (merge commit) so staging has the fix too.

## Database changes

- Every change is a new file in `supabase/migrations/`. Never edit one that's been applied.
- Merging to `staging` applies it to the staging database. Merging to `main` applies it to production.
- Never change the production database by hand in the Supabase dashboard.

## Secrets and data

- Never commit keys or passwords. `.env.example` lists the names. Real values live in GitHub environment secrets, EAS and Supabase.
- Staging and local use made-up data only. Never copy client data out of production.

## Writing

PR descriptions, issues, the README and everything in `docs/` are written in plain Australian English with the `alio-humaniser` skill, in Caelan's voice. Code and code comments don't need it.

## Repo settings (once)

1. **Rules.** Settings → Rules → Rulesets → New ruleset → Import a ruleset. Import `.github/rulesets/main.json`, then `.github/rulesets/staging.json`.
2. **Default branch.** Settings → General → Default branch: `staging`, so new PRs and AI sessions start from it.
3. **Merging.** Settings → General → Pull Requests: allow squash and merge commits, untick rebase, tick "Automatically delete head branches".
4. **Environments.** Settings → Environments: add `staging` (deploys from `staging` only) and `production` (deploys from `main` only), each with its own secrets.
5. **Visibility.** This repo is public, so rulesets and environments are free. If it goes private, they need a paid GitHub plan: Pro for a personal account, Team for an organisation.
6. **Second developer.** When one joins, set required approvals to 1 in both rulesets.
