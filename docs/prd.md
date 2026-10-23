# Infinilift MVP PRD

Status: draft, 23 October 2026. Built from `docs/research/`. Comes before `docs/plan.md`.

## The problem

Coaching apps lose logged workouts, fail without signal, take too many taps to log a set, leave new people stuck at sign-up, and charge coaches extra for basics. The fifteen pain points are in `pain-points.md`. Each one maps to a feature below. Phase 1 is the MVP. Phase 2 starts after the beta.

## Users

- **Coach:** writes programs, sees client logs, messages clients.
- **Client:** follows the program, logs sets, messages the coach.

## Pain points to features

| Pain point | Feature | Phase |
|---|---|---|
| P1 Logged workouts get lost | 4 Log a workout | 1 |
| P2 New people can't get in | 1 Join, 2 Invite a client | 1 |
| P3 Slow, crashes, no signal | 4 Log a workout, 8 Report a problem | 1 |
| P4 Updates break things | 9 Safe updates | 1 |
| P5 Too many taps | 4 Log a workout | 1 |
| P6 Health data wrong or missing | 12 Health sync | 2 |
| P7 Food database wrong outside the US | 13 Food diary | 2 |
| P8 Features missing on some screens | 10 Full parity | 1 |
| P9 Video fails both ways | 14 Form-check video | 2 |
| P10 Messages go missing | 7 Messages | 1 |
| P11 Clients can't see last time | 5 Last time | 1 |
| P12 Coaches pay extra for basics | 15 Flat plan and payments | 2 (free invites in phase 1) |
| P13 Rest timers unreliable | 6 Rest timer | 1 |
| P14 Support can't be reached | 8 Report a problem | 1 |
| P15 Clients locked out of their data | 11 Client keeps history, 16 Data export | 1, 2 |

## Features

**Phase 1 (MVP)**

1. **Join.** Sign up with Apple, Google or an email code, or enter an invite code. No passwords.
2. **Invite a client.** Coach sends an invite by email or link. Client accepts and lands on their coach's thread.
3. **Build and assign a program.** Coach adds weeks, days, exercises, sets, reps, rest and notes. Assigns it with a start date. Copies a week.
4. **Log a workout.** Today's workout on one screen. Each set is pre-filled from the plan. A tick saves to the phone at once and syncs later. Survives app switch, lock, crash and restart.
5. **Last time.** Each exercise shows the last weight and reps logged for it, from any workout.
6. **Rest timer.** Starts on tick, uses the coach's default, and goes off with the phone locked.
7. **Messages.** One thread per client. Text only. Shows sending, sent and failed. Retries by itself.
8. **Report a problem.** A button on every screen. Works offline. Attaches app version and device.
9. **Safe updates.** Most fixes ship over the air. Forced updates are for security fixes only. Releases roll out in stages and roll back when crashes or failed saves rise. No feature is removed without notice.
10. **Full parity.** Every feature works on web, iPhone and Android.
11. **Client keeps history.** When coaching ends, the coach loses access. The client keeps their logged workouts.

**Phase 2**

12. **Health sync.** Apple Health and Health Connect. Steps are one de-duplicated daily total. Clients can correct a value. Finished workouts write back.
13. **Food diary.** Australian food data first, with barcodes. A missed barcode is saved for everyone. Coach can hide numbers from a client.
14. **Form-check video.** Clips shrink on the phone and upload in the background. Coach replies with a video or a note pinned to a moment.
15. **Flat plan and payments.** One plan with the basics included. No client-slot fees. Payments go to the coach's own Stripe account. Checkout shows the exact charge and renewal date.
16. **Data export.** Clients download their history.

Also later: check-ins, progress photos, automations, own-name apps, supersets and progression rules, importing old programs.

## Tech stack

| Need | Tool | Phase |
|---|---|---|
| App, web, iOS, Android | Expo (React Native) and TypeScript | 1 |
| Web hosting | Vercel, static export of the Expo web build | 1 |
| Database, auth, realtime | Supabase, Sydney. Postgres, Auth, Realtime, Row Level Security | 1 |
| On-device store | SQLite. Every set is written locally, then synced from a queue | 1 |
| Build and over-the-air updates | EAS Build and EAS Update | 1 |
| Push notifications | Expo Push | 1 |
| Email (invites, codes) | Resend, as Supabase's mail provider | 1 |
| Crashes and failed saves | Sentry | 1 |
| Analytics and staged rollouts | PostHog feature flags and funnels | 1 |
| Public status page | Better Stack | 1 |
| Tests | GitHub Actions for lint, types and unit tests. Maestro for airplane-mode and force-quit flows | 1 |
| Staging access | Cloudflare Access, per `CONTRIBUTING.md` | 1 |
| Video and progress photos | Cloudflare R2. No egress fees, and video downloads drive cost | 2 |
| Payments | Stripe Connect, coaches' own accounts | 2 |
| Health data | HealthKit and Health Connect, through native modules | 2 |
| Food data | FSANZ food data and Open Food Facts | 2 |

Schema changes are new files in `supabase/migrations/`. Keys live in EAS, Supabase and GitHub secrets, never in the repo.

**Data rule:** analytics, crash reports and logs never carry health values, food entries, message text or photos. Check PostHog's hosting regions before setup; the app's own data stays in Sydney.

## Method

Build in slices. Each slice is one PR into `staging` and ships once it works there.

1. **Skeleton.** App runs on all three platforms. Sign-in works. CI passes. A test build reaches TestFlight and Play internal testing.
2. **Coach side.** Features 2 and 3.
3. **Client logging.** Features 4 and 5. Test in airplane mode and after a force-quit before merging.
4. **Rest timer and problem report.** Features 6 and 8.
5. **Messages and safe updates.** Features 7 and 9.
6. **Beta.** Three coaches, 30 clients, four weeks, on a production release.
7. **Phase 2.** One slice per feature, 12 to 16, in the order the beta asks for them.

**Done means:** works on web, iPhone and Android; the PR says which were checked; no logged set is lost in the airplane-mode and force-quit tests.

## Measures (proposed)

- No logged set lost in testing.
- A set that matches the plan takes one tap.
- A new client logs a set within five minutes of the invite.
- Three coaches run a full four-week program.

## Decisions to confirm

1. **Coach app:** web only, or web and phone? This PRD assumes both.
2. **Payments:** free invites in phase 1, Stripe in phase 2.
3. **Tool choices:** the stack above is my proposal. Confirm PostHog, Sentry, Better Stack and Resend, or name replacements.
