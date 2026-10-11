# REA study: context pack

Claude Code on Caelan's computer reads this first. It says what we're doing, what to look at and where the results go.

## The job

Infinilift is a coaching app Alio! Brand Studios is building. It's one codebase for web, iOS and Android. Coaches run programs, nutrition, check-ins, messages and payments; clients train, log and check in from the app.

The plan merges the most-used features of the two most popular coaching apps, ABC Trainerize and TrueCoach, plus Everfit. Then it fixes what their users complain about, borrowing from smaller apps that already do it better.

What's done:

- `docs/research/pain-points.md`: the ranked pain points from about 2,700 store reviews of the three apps, and the smaller apps that solve each one.
- `docs/research/competitors.md`: what each of the 9 platforms we looked at does and costs.

This study uses REA (https://github.com/morluto/rea) to see how the apps actually work: screens, steps, data and the services they're built on. The results go in this folder and feed `docs/plan.md`.

## Rules

- Study how the apps behave, not their code. Use them the way a coach and a client would, and write down what they do in your own words.
- Read each app's terms before you start. If they ban reverse engineering, stick to normal use, screenshots and the route list, and skip step 5 below.
- Never copy their code, text, images, icons or exercise videos into this repo.
- Use test accounts and made-up client details. Never open anyone else's data.
- Screenshots and captures stay on this computer, out of git.
- This repo is public. Never commit logins, tokens, keys, email addresses or raw network captures.
- Stop before any real payment. Use Stripe test mode or stop at the checkout screen.

## What you need

| Thing | Why |
|---|---|
| Node.js 22.19+ or 24.11+, and npm | Runs REA |
| Google Chrome | REA watches the web apps through Chrome's debugging port |
| Android Studio with a Google Play emulator (Pixel, Android 15 or newer) | Runs the client apps. REA reads the emulator through adb |
| JDK 17+ and jadx-headless-mcp 0.7.1 | Optional. Only for step 5 |
| A coach account on each app, plus a test client | See below |

REA doesn't cover iPhone apps. The Android apps stand in for both.

Caelan makes the accounts by hand, on the day of the study, because trials run out:

| App | Account | Notes |
|---|---|---|
| ABC Trainerize | 30-day free trial, unlimited clients, no card | Add-ons aren't in the trial. Drops to the free plan (1 client) afterwards |
| TrueCoach | Free trial | Check the length and whether it wants a card at sign-up |
| Everfit | Free Starter plan, plus the 30-day trial of paid features, no card | |
| Smaller apps | Listed in `pain-points.md` with each app's free plan or trial | Only the features named there |

For each app, invite a test client using a plus address on your own email, for example `you+trainerize@yourdomain`.

## How to study one app

1. **Open Chrome for REA.** Close other Chrome windows, then start one with its own profile and a debugging port, and log in to the coach web app there.
   - macOS: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222 --user-data-dir="$HOME/rea-chrome"`
   - Windows: `"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir=%USERPROFILE%\rea-chrome`
2. **Map the app.** `list_browser_targets` on `http://127.0.0.1:9222`, then `analyze_web_bundle` on the coach app's tab. Turn the route list into the feature inventory, so nothing is missed.
3. **Walk the jobs below.** Caelan clicks; Claude runs `observe_web_session` for each job and `inspect_web_page` with JSON body shapes on (names and types only, never values), and saves a screenshot at each step. Count the screens and taps.
4. **Do the client side.** Install the client app from Google Play in the emulator, sign in as the test client and repeat the client jobs, using `capture_adb_screen` at each step and `read_adb_logcat` when something breaks.
5. **Optional, only if the terms allow it.** `pull_adb_package`, then `inspect_android_package`, to list the third-party services in the app's manifest (payments, chat, video, analytics, health). Note the service names only.
6. **Write it up** in `docs/research/rea/<app>.md` using the template below.

### Coach jobs

1. Invite and onboard a client, including intake form and waiver.
2. Build a 4-week program with a superset, progression and a deload week, save it as a template and assign it.
3. Set macro targets (training and rest days) and a meal plan.
4. Make a weekly check-in form, then review a submitted check-in with photos side by side.
5. Message a client (text, voice note, video) and a group. Find a client who's gone quiet.
6. Set up an automation, for example a message on day 3 and a check-in every Sunday.
7. Make a package and take a payment, stopping before any real charge.
8. Branding: what can change (logo, colours, app name) and what it costs.

### Client jobs

1. Accept the invite and sign up.
2. Log a workout. Halfway through, switch on flight mode, log two more sets, then switch it off. Note what happens to those sets.
3. Log food: search an Australian product, scan a barcode, try a photo if offered.
4. Submit a check-in with progress photos.
5. Connect Health Connect (and a wearable if you have one), then check whether steps and workouts show up for the coach.
6. Message the coach.

### Pain points

For every pain point in `pain-points.md` that applies to this app, try to make it happen and record the result. For the smaller apps, study only the features listed against them there.

## Template

```markdown
# <App>: REA findings

Studied <date> on <plan>. Web version <x>, Android version <y>.

## Feature inventory
| Area | Coach can | Client can | Notes |

## Jobs
### <Job>
Steps: <numbered, with screen and tap counts>
Good: <what to copy>
Clumsy: <what to fix>

## Data
Entities and fields seen in JSON shapes. Names and types only.

## Services
Third-party services seen (manifest, network hosts), by purpose.

## Pain points checked
| Id | Happened? | What we saw |

## For Infinilift
Keep:
Fix:
Skip:

## Limits
What couldn't be seen, and why.
```

## Hand back

1. When every app is done, write `docs/research/rea/merge.md`: one table with feature, the app that does it best, how it does it, and what Infinilift should do.
2. Commit to a branch called `research/rea`, push it and open a PR into `staging`.
3. Write the PR description with the `alio-humaniser` skill: what was studied, the 5 biggest findings and what couldn't be checked.
