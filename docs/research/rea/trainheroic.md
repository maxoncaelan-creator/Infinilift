# TrainHeroic: REA findings

Desk study, 12 October 2026, from public sources only. TrainHeroic's terms ban competitive use, so no account was made. Android app 8.38.0 is installed on the study emulator but hasn't been opened. Only P1, P2, P3 and P5 were studied.

## Feature inventory

| Area | Coach can | Athlete can | Notes |
|---|---|---|---|
| Offline logging | Not documented | View and log sessions with no signal. Logs sync when signal returns | Demo videos don't play offline. A black bar shows while offline |
| Editing after logging | Edit and log for an athlete on mobile (article title only, not read) | Change logged sets, readiness answers, duration and intensity at any time | Edits save as they're made |
| Getting in | Invite by email, which makes a one-time access code. Make reusable team codes for big in-person groups. Delete codes | Create an account, then join a coach by code, buy a Marketplace program or log their own training. Add more codes later from Settings | Athletes who join by code count towards the coach's plan |
| Swaps | Set suggested swaps per exercise, on the web only | Swap any single exercise. Coach suggestions sit at the top of the list | Not for circuits. Coaches can't turn swaps off |
| Adding work | See added sets and exercises against the prescription | Add sets. Add exercises to the end of a session | Athletes can't delete prescribed sets, only leave them blank |
| Rescheduling | Reschedule from the session menu on mobile (search snippet only) | Move one session to another day, or accept a prompt to move it to today | No moving several sessions at once |
| Status page | n/a | n/a | Public, 4 components, 7-day history |

## Jobs

Every job below is as the help docs and videos describe it, apart from the status page, which was viewed directly. Screen and tap counts not seen.

### Log a session (P5)
1. Open the session from the calendar and tap Start Session. A session timer starts.
2. Usually, answer a readiness survey on sleep, mood, energy, stress and soreness.
3. Dismiss the coach's intro note, if there is one.
4. In each block, tick each prescribed set, or tap the table and change reps or weight on the keypad, then Done. Plus and minus buttons add or remove extra sets.
5. Swipe, or use the arrows, to move to the next block.
6. On the last block, set intensity on a slider, adjust the duration, add comments, then Finish Session.

- Good: a prescribed set can be ticked off without typing.
- Clumsy: one block per screen, so a session is a swipe per block. The survey sits in front of the first set. Prescribed sets can't be removed, only left blank.

### Log sets offline (P1, P3)
1. Lose signal. The help article tells athletes to switch on flight mode to use offline mode.
2. A black bar at the top says logs are kept on the phone until there's a connection.
3. View and log sessions as normal. Demo videos don't play.
4. When wifi or mobile data returns, the logs are added to the athlete's history automatically.

- Good: logging doesn't depend on signal, and the bar tells the athlete their sets are kept.
- Clumsy: the article is 4 short paragraphs from 2023. It doesn't say how many days of program are kept on the phone, whether a session must be opened online first, what happens to unsynced sets if the app is closed or crashes, how weak signal (as opposed to flight mode) is handled, or what happens if the coach edits the session in the meantime. No synced or waiting mark per set is documented.

### Edit a session after logging (P1)
1. Find the session on the training calendar.
2. Tap the block to fix in the session overview. The logging view opens.
3. Scroll to the exercise and tap the table to change the numbers. Changes save as they're made.
4. For readiness answers, open the first block and swipe left. For duration and intensity, open the last block, swipe right, tap Done Training, change them on the summary, then Finish Session.

- Good: everything logged can be fixed later, with no separate save step.
- Clumsy: readiness and duration edits are hidden behind swipes past the first and last blocks. The docs don't say whether the coach is told about an edit.

### Get in after install (P2)
1. Install the app. The first screen is a login screen with a create-account option.
2. Enter full name, email and password.
3. Enter the access code from the coach's invite email.
4. Set up a profile and take a short tour. The coach's programming is on the calendar.

Without a code, the athlete picks 1 of 3 paths after sign-up: connect with a coach by code, buy programming on the Marketplace (no code needed, and Apple subscriptions also work), or log their own training. They can switch paths later. To join another coach on an existing account: profile picture, Settings, My Training, Enter Access Code, type the code, Next, Connect. History stays on the one account.

- Good: no dead end. Anyone can make an account and self-coach, and a code can be added any time without a second account.
- Clumsy: the docs only describe email and password, with no Apple, Google or one-time code sign-in. The code is typed by hand, and no invite link that skips it is documented. The docs tell athletes to check spam for the invite. Joining a second coach is buried in Settings.

### Swap an exercise (P5)
Coach, web only: in the exercise library, open an exercise and add alternatives in its suggested swaps section. They can also be added when making a custom exercise in the session builder. Either way they show wherever that exercise is programmed. They can't be set from the mobile app.

Athlete:
1. Tap the swap icon beside the exercise name, or the block's 3-dot menu and Swap Exercise.
2. The coach's suggestions are pinned at the top. Below them, search the coach's library and TrainHeroic's library.
3. Pick an exercise and confirm. The session updates straight away.

- Good: suggestions live on the exercise, so the coach sets them once. The swap list is one tap from the exercise. The coach sees the swap in place of the original, with changed prescriptions crossed out, and blocks coloured green (as prescribed), yellow (changed) or red (missed).
- Clumsy: circuits can't be swapped. Coaches can't limit athletes to the suggested list or turn swaps off, and the docs say that's deliberate. An older coach FAQ says the list ranks the most-used exercises first, which doesn't match the 2026 article. A search snippet says athletes on a program access code don't get the coach's custom library for swaps. That article wasn't opened.

### Move a session to another day (P5)
1. While training: open a session from another day and tap Start Session. The app asks whether to move it to today, and yes moves it.
2. Ahead of time: open the session's 3-dot menu, choose reschedule, then pick a date.

- Good: the prompt covers the common case, training a day late, with one answer.
- Clumsy: one session at a time. Athletes on a team or a coach-assigned program can't shift a block of sessions, and the docs tell them to message the coach. Marketplace buyers shift a program by removing and re-adding it.

### Check the status page (P3)
1. Open status.trainheroic.com. A help centre search found no article that links to it.
2. A banner gives the overall state. 4 components are listed: coach website, Marketplace, mobile and payments.
3. A 7-day grid shows uptime per component, with 6 states from operational to major outage.

- Good: it's public, and mobile is listed apart from the coach website.
- Clumsy: no incident write-ups or subscribe option on the page. The back arrow on the grid didn't load earlier weeks in this session. Mobile is one component, so a sync fault can't be told apart from a login fault.

## Services

| Purpose | Service | Source type |
|---|---|---|
| Status page | Site24x7 StatusIQ | Asset hosts on the public status page |
| App sign-in | Not named. Docs describe email and password only | Help articles |
| Offline storage and sync | Not named | Help articles, Play Data safety |
| Crash and performance data | Not named. Crash logs, diagnostics and other performance data are collected for analytics | Play Data safety |
| Marketplace purchases | Apple subscriptions, as one way to buy | Help article |

Play declares no data shared with third parties. The App Store says identifiers may be used to track people across other companies' apps. SDK names weren't checked, because that needs the manifest and the terms rule it out.

## Pain points checked

| Id | Happened? | What we saw |
|---|---|---|
| P1 | Documented fix, partial | Logging works offline and syncs on reconnect. Every logged value can be edited later and saves as it's changed. Nothing on resuming a session after a crash or app kill, unsynced data or sync conflicts |
| P2 | Documented fix, partial | No dead end: create an account, then use a code, the Marketplace or self-coaching. A new code joins on the same account. But passwords only, codes typed by hand and invites by email that can land in spam |
| P3 | Documented fix, partial | Offline mode and a public status page. No demo videos offline, no speed figures and a coarse 4-part status page. The calendar video shows a refresh option on empty days, so coach changes may not arrive by themselves |
| P5 | Documented fix | Coach-suggested swaps pinned first, a swap icon on each exercise, and single-session rescheduling with a move-to-today prompt. Not for circuits or several sessions. Tap counts not seen |

## For Infinilift

Keep:
- 3 ways in after sign-up, with new coach codes joining the same account and history kept.
- Editing any logged value later, saved as it's changed.
- Swap suggestions stored on the exercise and pinned at the top of the swap list.
- Prescribed against done for the coach, with swaps shown in place and each block coloured.
- The move-to-today prompt when a client starts a session from another day.
- An offline banner that says sets are kept on the phone, and a public status page split by component.

Fix:
- Offline that covers weak signal, app kills and restarts, with a synced or waiting mark per set and the next 14 days kept on the phone.
- Demo videos for upcoming sessions kept on the phone, or a still and text cue when they can't play.
- Sign in with Apple, Google or a one-time code. Invite links that carry the code. "I have an invite or code" on the first screen, not in Settings.
- Coach-approved swaps set from the phone too, and for supersets and circuits.
- Moving several sessions at once, for example shifting the rest of the week by a day.
- Program changes pushed to the phone, with no manual refresh.
- Status page with incident notes and subscriptions, linked from "Report a problem", with sync as its own component.

Skip:
- A readiness survey in front of the first set by default.
- One block per screen as the only layout.

## Limits

- No account was made and the app wasn't opened, because the terms ban competitive use, bots and reverse engineering. So there are no screens, tap counts, offline test, sync timing or data shapes.
- Most help articles date from 2023 and may not match app 8.38.0 on Android or 9.1.0 on iOS. The download article still says iOS 15.1, while the App Store needs iOS 16.4.
- The reschedule article linked from the logging article asks for a help centre sign-in. The public version was used instead.
- The status page showed only the current week. No past incidents were found.
- Play Data safety and App Store privacy don't name SDKs, and the manifest wasn't inspected.
- No TrainHeroic video was found on offline mode, joining with a code, suggested swaps or rescheduling. Transcripts were read for 3 videos. 2 were seen in title or description only.

Videos worth watching by hand:
- Taps to log sets and move between blocks: https://www.youtube.com/watch?v=c_OwGgkIkSc from 0:45 to 1:37.
- How a coach invites and organises clients: https://www.youtube.com/watch?v=qbsZo-jKZkM from 0:17.
- Where swap sits on the session overview before starting: https://www.youtube.com/watch?v=vsbd-A15AZw at 0:24.
- Whether the calendar needs a manual refresh after coach changes: https://www.youtube.com/watch?v=ljMeNAJVfLA at 0:38.

## Sources

Help centre:
- Offline mode for athletes: https://support.trainheroic.com/hc/en-us/articles/18156682333581-Offline-Mode-for-the-TrainHeroic-Mobile-App
- Athlete app quick guide: https://support.trainheroic.com/hc/en-us/articles/18156771156109-Using-the-TrainHeroic-Mobile-App
- Create account and join coach: https://support.trainheroic.com/hc/en-us/articles/18839678608269-For-Athletes-How-to-Create-Your-Account-and-Join-Your-Coach
- Three ways to train: https://support.trainheroic.com/hc/en-us/articles/18156797401485-I-didn-t-receive-an-Access-Code-How-do-I-get-started
- Access code on existing account: https://support.trainheroic.com/hc/en-us/articles/18156766715021-How-to-use-an-Access-Code-In-App
- Coach access codes and invites: https://support.trainheroic.com/hc/en-us/articles/18171015052813-For-Coaches-Creating-Access-Codes
- Downloading the app: https://support.trainheroic.com/hc/en-us/articles/18170940515853-Downloading-the-TrainHeroic-Mobile-App
- Logging a training session: https://support.trainheroic.com/hc/en-us/articles/18156631592589-Logging-your-Training-Session
- Editing a logged session: https://support.trainheroic.com/hc/en-us/articles/18156588540429-As-an-athlete-how-can-I-edit-my-logged-session
- Athlete swaps and added exercises: https://support.trainheroic.com/hc/en-us/articles/18157017943693-As-an-athlete-how-can-I-swap-or-add-exercises-during-a-session
- Coach suggested swaps setup: https://support.trainheroic.com/hc/en-us/articles/43887451682061-For-Coaches-Suggested-Swaps
- What athletes can modify: https://support.trainheroic.com/hc/en-us/articles/18156760246029-For-Coaches-How-can-athletes-adjust-or-modify-their-training-sessions
- Athlete rescheduling: https://support.trainheroic.com/hc/en-us/articles/18156964554765-As-an-athlete-can-I-reschedule-my-training-sessions
- Navigating the training calendar: https://support.trainheroic.com/hc/en-us/articles/18156648701965-Navigating-your-Training-Calendar

Other pages:
- Public status page: https://status.trainheroic.com
- Google Play listing: https://play.google.com/store/apps/details?id=com.TrainHeroic.TrainHeroic
- Play Data safety: https://play.google.com/store/apps/datasafety?id=com.TrainHeroic.TrainHeroic
- App Store listing, Australia: https://apps.apple.com/au/app/trainheroic-strength-training/id955074569
- Coach features and pricing: https://www.trainheroic.com/coach/

Videos, all from TrainHeroic's own channels:
- Logging a session, support channel: https://www.youtube.com/watch?v=EnFto0YARnk (transcript, 0:08 survey, 0:32 to 0:58 sets and swaps)
- Getting started, first session: https://www.youtube.com/watch?v=vsbd-A15AZw (transcript, 0:07 rescheduling, 0:24 to 0:32 swaps)
- Navigating the training calendar: https://www.youtube.com/watch?v=ljMeNAJVfLA (transcript, 0:38 to 0:47 refresh)
- How to log a session: https://www.youtube.com/watch?v=c_OwGgkIkSc (video seen in title or description only, chapters used)
- Coach Playbook, connecting clients: https://www.youtube.com/watch?v=qbsZo-jKZkM (video seen in title or description only, chapters used)
