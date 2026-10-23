# Prompts for Claude Code on Caelan's computer

Paste these one at a time. Each one waits for the last to finish. Plan on 30 to 60 minutes for setup and about an hour per big app.

## 1. Set up

```text
Clone https://github.com/maxoncaelan-creator/Infinilift, or pull it if it's already on this computer. Make a branch called research/rea from origin/staging if staging has docs/research/rea/README.md, otherwise from origin/ccr-0b55b61a-jzsa99. Read CLAUDE.md, docs/research/rea/README.md and docs/research/pain-points.md.

Get this computer ready for the study, but don't analyse anything yet:
1. Check for Node.js, npm, Google Chrome, Android Studio, adb, an Android emulator with Google Play, and (optional) a JDK 17+ and jadx-headless-mcp 0.7.1. Tell me what's missing and how to install it here. Please ask before installing anything.
2. Run `npx rea-agents setup`, pick Claude Code only, and show me the changes before you apply them.
3. Tell me when to restart Claude Code.
```

## Before prompt 2 (by hand)

1. Make the coach account and test client for the app (table in `docs/research/rea/README.md`).
2. Start Chrome for REA with the command in step 1 of "How to study one app", and log in as the coach.
3. Start the emulator, sign in to Google Play, install the app's client app and sign in as the test client.

## 2. Study an app

Run this for ABC Trainerize, then TrueCoach, then Everfit. Change the name each time.

```text
We're doing the REA study in docs/research/rea/README.md. This one is ABC Trainerize. Chrome for REA is open on port 9222 with the coach logged in, and the emulator is running with the client app signed in.

Follow "How to study one app" in order. Map the app first. Then take me through each coach job and client job one at a time: tell me exactly what to click, wait for me to say "done", then observe and record. Try every pain point in docs/research/pain-points.md that applies to this app. Keep to the rules section. Write docs/research/rea/trainerize.md as you go and commit after each section.
```

## 3. Study the smaller apps

```text
Now the smaller apps listed under "Study with REA" in docs/research/pain-points.md. Same method and rules, but only the features named against each app. One file each in docs/research/rea/. Tell me which accounts to make before we start each one.
```

## 4. Wrap up

```text
Write docs/research/rea/merge.md as described in the hand-back section. Then check every file in docs/research/rea/ against the rules: no logins, emails, tokens, copied text or images, and no raw captures. Run python3 .claude/skills/alio-humaniser/scripts/tell_scan.py on each file and fix what it flags. Commit, push research/rea and open a PR into staging with a description written using the alio-humaniser skill. If the GitHub CLI isn't set up, push and give me the compare link instead.
```

When the PR is up, tell Claude in the Infinilift cloud session. It'll read the findings and write them into `docs/plan.md`.
