# Infinilift MVP PRD

Status: draft, 22 October 2026. Built from `docs/research/`. Comes before `docs/plan.md`.

## The problem

Coaching apps lose logged workouts, fail without signal, take too many taps to log a set, and leave new people stuck at sign-up. The MVP fixes the eight pain points that block use: P1, P2, P3, P5, P10, P11, P13 and P14 in `pain-points.md`.

## Users

- **Coach:** writes programs, sees client logs, messages clients.
- **Client:** follows the program, logs sets, messages the coach.

## MVP scope

| # | Feature | Done when | Pain point |
|---|---|---|---|
| 1 | Join | Sign up with Apple, Google or an email code, or enter an invite code. No passwords. | P2 |
| 2 | Invite a client | Coach sends an invite by email or link. Client accepts and lands on their coach's thread. | P2 |
| 3 | Build and assign a program | Coach adds weeks, days, exercises, sets, reps, rest and notes. Assigns it with a start date. Copies a week. | |
| 4 | Log a workout | Today's workout on one screen. Each set is pre-filled from the plan. A tick saves to the phone at once and syncs later. Survives app switch, lock, crash and restart. | P1, P3, P5 |
| 5 | Last time | Each exercise shows the last weight and reps logged for it, from any workout. | P11 |
| 6 | Rest timer | Starts on tick, uses the coach's default, and goes off with the phone locked. | P13 |
| 7 | Messages | One thread per client. Text only. Shows sending, sent and failed. Retries by itself. | P10 |
| 8 | Report a problem | A button on every screen. Works offline. Attaches app version and device. | P14 |

Every feature works on web, iPhone and Android.

## Not in the MVP

Payments (coaches invite clients for free until phase 2), check-ins and progress photos, food diary, wearables, form-check video, automations, own-name apps, supersets and progression rules, client data export, importing old programs.

## Tech stack

- **App:** Expo (React Native) and TypeScript. One codebase for web, iOS and Android.
- **On-device data:** SQLite. Every set is written locally first, then synced from a queue.
- **Backend:** Supabase in Sydney. Postgres, Auth (Apple, Google, email code), Realtime for messages. Row Level Security: clients see their own data, coaches see their clients'.
- **Push:** Expo Notifications.
- **Build and release:** EAS Build and EAS Update, following `CONTRIBUTING.md`.

Schema changes are new files in `supabase/migrations/`.

## Method

Build in slices. Each slice is one PR into `staging` and ships once it works there.

1. **Skeleton.** App runs on all three platforms. Sign-in works. CI passes. A test build reaches TestFlight and Play internal testing.
2. **Coach side.** Features 2 and 3.
3. **Client logging.** Features 4 and 5. Test in airplane mode and after a force-quit before merging.
4. **Rest timer and problem report.** Features 6 and 8.
5. **Messages.** Feature 7.
6. **Beta.** Three coaches, 30 clients, four weeks, on a production release.

**Done means:** works on web, iPhone and Android; the PR says which were checked; no logged set is lost in the airplane-mode and force-quit tests.

## Measures (proposed)

- No logged set lost in testing.
- A set that matches the plan takes one tap.
- A new client logs a set within five minutes of the invite.
- Three coaches run a full four-week program.

## Decisions to confirm

1. **Coach app:** web only, or web and phone? This PRD assumes both.
2. **Payments:** free invites in the MVP, Stripe in phase 2.
