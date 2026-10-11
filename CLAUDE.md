# Infinilift: notes for Claude

- The plan is `docs/plan.md`. The research behind it is in `docs/research/`.
- Work on your own branch and open PRs into `staging`. Only `staging` (release PRs) and `hotfix/*` branches go into `main`. See `CONTRIBUTING.md`.
- Write PR descriptions, issues, the README and everything in `docs/` with the `alio-humaniser` skill, in Caelan's voice (`.claude/skills/alio-humaniser/references/alio-voice.md`, "Caelan's own voice"). Australian English. Code and code comments don't need it.
- Keep docs to the words someone needs to build or test the thing.
- In-app copy speaks for the coach's business, not Alio!. Use the client's voice once they have one, otherwise plain, friendly Australian English.
- This repo is public. Never commit keys, real client data or anything from Alio!'s private repos.
- Database changes are new files in `supabase/migrations/`. Never edit an applied migration.
- For any screen change, check web, iOS and Android, and say in the PR which ones you checked.
