# TrueCoach: REA findings (desk study)

Desk study, 12 October 2026, from public sources only. TrueCoach's terms ban competitive use, so no account was made. Android app 2.4.4 is installed on the study emulator but hasn't been opened.

Sources were TrueCoach's website, help centre, blog, App Store listing, Google Play Data safety section and 7 of its own YouTube tutorials (titles only). Nothing here was seen in the app, so there are no screen or tap counts and no JSON shapes. Where the docs disagree, both versions are given.

## Feature inventory

| Area | Coach can | Client can | Notes |
|---|---|---|---|
| Clients | Add remote, dual or in-person clients. Group, pause, archive, delete and export the client list | Accept an email invite and fill in their profile | In-person clients get no login. An email already used under another coach is refused |
| Programs | Build multi-week programs. Copy, paste, drag, multi-select, keyboard shortcuts, tags, duplicate, print to PDF. Sync edits to everyone on the program, or not | Move a workout date, if the coach allows it | No progression or deload feature in the docs |
| Workout builder | Warm-up, exercises, supersets (link 2 or more), circuits (EMOM, AMRAP), cool-down, demo videos, own videos | See the whole session first, swipe through demos | Library: Central Athlete's 1,200+ movements plus USA Weightlifting. Marketing pages say 3,000+ and 3,500+ |
| Logging | Enter results for dual and in-person clients. Mark complete or missed from the app | Enter results per exercise, attach photos or video, see past results for that exercise | Docs don't say if results are per-set fields or one text box. `competitors.md` says free text |
| Timers | Not covered | Stopwatch and countdown on iOS and Android. Interval timer on iOS only | Stopwatch time is copied, ready to paste into results |
| Habits | Daily, weekly or monthly habits. On Standard and up, goals for energy and hunger (1 to 10) and stress (1 to 5) | Log calories, protein, carbs, fat, weight, sleep, steps, energy, hunger and stress | Habit tracker is mobile only |
| Nutrition | Daily calorie, macro and fibre goals, instructions and files. History graph, compliance % and weekly average | Log daily totals in the app or a browser, or link MyFitnessPal | No food database, barcode or photo logging in the docs |
| Check-ins and forms | Questionnaires, assessments and check-ins built as workouts. Link metrics to them | Answer in the results box. Film movement tests | No form builder. Waivers are a shared file the client prints and returns |
| Progress | Custom metric sets. View photo sets | Front, side and back photos, 1 set per date. A then-and-now view | Coach's comparison view not described |
| Messaging | 1-to-1, broadcast to all clients (recipients hidden), groups, voice notes up to 7 minutes | Text, photos, videos and GIFs. Group chats | Client voice notes not documented. A client who isn't logged in gets the text by email |
| Triage | 7, 30 and 90-day compliance per client. A Needs Attention list for a sudden 20% drop | Can't see their own compliance | Compliance is exercises completed over exercises assigned |
| Automation | Zapier: 4 triggers, 1 action | Not covered | Help centre says Pro. Pricing page says Pro in one place and Standard in another |
| Payments | Stripe products, pricing plans, subscriptions, one-time payments, discounts, tax, proration, refunds | Update their card under Billing | Flat 5% a transaction, refunds included. US, UK, Australia and Canada only |
| Branding | Logo, 1 brand colour, a subdomain on truecoach.co | Sees the coach's logo and colour in the TrueCoach app | Standard and up. No own-name app in the docs |
| Wearables | View sleep, resting heart rate and step graphs | Connect Garmin, Fitbit, Oura, Google Fit, Polar, Apple Health or WHOOP | Through Terra. Standard and up |
| Coach profile | Public page with services, prices and testimonials | Browse and enquire | Standard and up |
| Export | Export workouts and the client list | Can't export their own workouts. Can turn on workout emails | |
| Coach mobile app | Same app as clients, switch roles in settings. Dashboard, messages, results, edit workouts. Add and edit clients from April 2026 | Same app | Launched as a beta in September 2024 |

## Jobs

Steps are as the help docs describe them. Screen and tap counts not seen.

### Coach 1. Invite and onboard a client, with intake form and waiver

1. Click Add Client on the dashboard or client list, then pick remote, dual or in-person.
2. Enter first name, last name and email (no email for in-person). Optional: birthday, location, time zone, photo, units, gender, height and weight.
3. Save. Remote and dual clients get the invite email straight away and fill in anything left blank when they accept. If it's lost, the coach resends it or copies the link.
4. Intake: the docs suggest a ready-made onboarding program. Day 1 is a welcome workout with an intro video, day 2 a PAR-Q typed in as exercises, day 3 movement tests the client films, day 5 a first check-in.
5. Waiver: upload it to the shared document library. The client downloads, prints, fills in and sends it back. The coach attaches it to a client note.

- Good: in-person clients need no login. Only 3 required fields. The coach can copy the invite link and send it any way.
- Clumsy: no form builder or e-signature, so intake answers are free text and the waiver goes out and back on paper. One email can't belong to 2 coaches; the docs' fix is for the old coach to delete the client or the client to use another email.

### Coach 2. Build a 4-week program with a superset, progression and deload, save as a template and assign

1. Programs tab, create a program, then add weeks and workouts in a builder laid out like a calendar.
2. Type an exercise name and pick from the library. Add sets, reps, tempo and rest in the exercise details.
3. Click the link icon between 2 exercises for a superset. Use the circuit button for EMOM, AMRAP and circuits.
4. Save. The program is the template. It can be duplicated and tagged.
5. Assign from the Programs page to 1 or more clients, or from a client's calendar, starting on any program day.
6. Turn Sync on to push later edits to every assigned client, or off to leave them alone.

- Progression and deload: not documented. Each week would be written by hand.
- Video: Workout Builder, Programming made EASY and Selecting Multiple Workouts (video seen in title or description only).
- Good: Sync per program. Starting a client part-way through. Edits on one client's calendar don't touch the program.
- Clumsy: no progression rules. The docs don't say whether sets and reps are separate fields, so it's unclear what can be pre-filled for the client.

### Coach 3. Macro targets for training and rest days, and a meal plan

1. Client calendar sidebar, Nutrition, Add Plan.
2. Write instructions and upload files, such as a meal plan PDF or Word document.
3. Set daily calorie, macro and fibre goals.
4. Review under Nutrition, View history (graph, compliance %, weekly average) and the daily breakdown with the client's notes.
5. On Standard and up, set energy, hunger and stress goals from the sidebar.

- Training and rest-day targets: not documented. Goals are one daily set; the docs point to the planning tool for heavier days.
- Good: fibre is a goal. Nutrition has its own compliance %. Meal plans can sit in a program and be reused.
- Clumsy: meal plans are files or workouts. No food logging beyond daily totals.

### Coach 4. Weekly check-in form, then review a submitted check-in with photos side by side

1. Build the check-in as a workout, with each question as an exercise.
2. Link metrics, such as weight and measurements, so the client updates them in the same place.
3. Copy it into a program to repeat weekly or monthly.
4. The coach is notified when it's done and reads answers on the dashboard or calendar, or later with sidebar search.

- Photos side by side: the client app has a then-and-now view. A coach comparison view isn't described.
- Good: check-ins show up for the client like any workout.
- Clumsy: no question types, required fields or scoring. Answers are free text. Photos sit apart from the check-in.

### Coach 5. Message a client (text, voice note, video) and a group, and find a client who's gone quiet

1. Message icon at bottom left, New Message, pick a client. Also from the dashboard or the workout builder.
2. Voice note: tap the mic under the text box, record up to 7 minutes, play it back, then send or redo. Added 25 February 2026.
3. Broadcast: New Message, select all clients. Replies come back 1-to-1.
4. Groups: articles exist for creating groups, adding and removing members, and the client view. Titles seen, steps not read.
5. Quiet clients: the dashboard's Needs Attention list flags a sudden 20% drop in 7, 30 or 90-day compliance.

- Video messages: the features page lists video in chat. No coach steps found.
- Good: the 20% drop rule is simple to copy. Voice notes can be checked before sending. Clients not in the app still get the text by email.
- Clumsy: compliance only counts assigned exercises, so a client with nothing assigned is never flagged. No last-seen date or read ticks documented. The plan tier for voice notes isn't stated.

### Coach 6. Automation, such as a message on day 3 and a check-in every Sunday

No built-in scheduler for messages or check-ins is documented. The docs offer 2 routes:
1. Program as sequence: put a day-3 welcome workout and a Sunday check-in workout in a program and assign it.
2. Zapier (Pro): copy the API key from Settings, Integration, into Zapier. Triggers: added to a client group, new client, workout created, workout completed. Action: add a client.

- Zapier can't send a TrueCoach message or assign a check-in, so a day-3 message has to be a workout.
- Good: automatic emails for invites, daily workouts and missed workouts.
- Clumsy: real automation means Zapier on the top plan, with 1 action.

### Coach 7. Make a package and take a payment, stopping before a real charge

1. Connect Stripe.
2. Create a product, such as 1-to-1 coaching, and 1 or more pricing plans billed weekly, monthly or yearly.
3. Create a subscription: pick the client and plan, add tax, start and end dates and billing cycle, then start it.
4. The client gets an email asking for billing details, and can later update their card under Billing.

- Fees: a flat 5% on each successful card payment, on the total including tax, and again on refunds (article dated 3 December 2025). The pricing page FAQ says there are no extra fees.
- Video: TrueCoach Payments Tutorial, Connecting TrueCoach to Stripe and Payments Onboarding (video seen in title or description only).
- Good: product, plan, subscription is easy to follow. Discounts and proration have their own articles (titles seen).
- Clumsy: the coach starts every subscription. No checkout link, storefront or self-serve cancel in the pages read. 5% against Stripe's 1.65% + A$0.30 for Australian cards.

### Coach 8. Branding: what can change and what it costs

1. Account Settings, Theming.
2. Pick a brand colour, upload a logo (PNG, JPG or SVG, about 10 to 20 KB, at least 116 by 116 px square) and set a subdomain.

- Cost: included from Standard (US$57.99 a month on the pricing page, 12 October 2026). An older Android post says 8 colours on the 20-client tier; the help article says any colour.
- Good: no branding add-on fee. The colour carries to web and mobile.
- Clumsy: app name, icon, store listing and emails don't change. Clients install TrueCoach from the stores.

### Client 1. Accept the invite and sign up

1. Open the invite email and accept.
2. Fill in the profile form, set a password and accept again.
3. Log in on the web or in the app (iOS, or Android `co.truecoach.client`).

- Sign in with Apple or Google, one-time codes or a way to find a coach: not documented.
- Video: TrueCoach Client Tutorial (video seen in title or description only).

### Client 2. Log a workout, with flight mode halfway

1. Open today's workout. The whole session shows first.
2. Tap the update-results button on an exercise, enter results, attach photos or video.
3. Tap it again to save.
4. Past results for each exercise are under exercise history.

- Offline: the help centre says nothing about offline logging or results entered without signal. The features page offers printing a workout to PDF for gyms with poor signal. What happens to sets logged in flight mode is not covered.

### Client 3. Log food: Australian product, barcode, photo

Not covered. The docs only describe typing daily totals or linking MyFitnessPal, so any search or barcode would happen in MyFitnessPal.

### Client 4. Submit a check-in with progress photos

1. Open the check-in workout, type answers into each results box and save.
2. Account tab, Progress Pictures, add front, side and back photos from the camera or camera roll.
3. Pick a date for older photos. Only 1 set per date.

### Client 5. Connect Health Connect and a wearable, and check the coach sees it

1. Log in at app.truecoach.co in a browser, profile icon, Wearables, add new connection.
2. Finish the Terra connection flow and come back to the graphs.
3. Apple Health connects through the iOS app instead.

- Health Connect isn't mentioned; Google Fit is. Data is sleep hours, resting heart rate and steps, with a graph per device. Workouts aren't mentioned. Data arrives after each provider syncs. Standard and Pro only.
- The coach's view has its own article (title seen, not read).

### Client 6. Message the coach

Real-time chat with text, photos, videos and GIFs, plus group chats. Client voice notes and steps aren't documented.

## Data

None published. No public API reference was found. The Zapier link uses a per-account API key. Its trigger and action names point to client, client group and workout records, with no fields or types given.

## Services

| Purpose | Service | Source |
|---|---|---|
| Payments | Stripe | Help centre, Payments collection |
| Wearables link | Terra | Help centre, client wearables article |
| Health and wearables | Apple Health, Google Fit, Garmin, Fitbit, Oura, Polar, WHOOP | Help centre, Wearables FAQ |
| Food | MyFitnessPal | Help centre and pricing page |
| Automation | Zapier | Help centre and pricing page |
| Exercise videos | Central Athlete library, USA Weightlifting movements | Help centre, workout builder article |
| Help centre | Intercom (articles and images on Intercom hosts) | Help centre pages |
| Data declared on Android | Device IDs, photos, videos, files, name, email, phone, crash logs, performance data. Nothing shared with third parties. No way to request deletion. No health or fitness data declared | Google Play Data safety |
| Data declared on iOS | Email, user ID and crash data linked to you; performance data not linked | App Store privacy section |

## Pain points checked

| Id | Happened? | What we saw |
|---|---|---|
| P1 | Not covered | Results save when the client taps update results on each exercise. No autosave, draft or recovery documented |
| P2 | Documented limit | Email invite only. An email already under another coach is refused; the fix is to delete it from the old coach or use another email |
| P3 | Documented limit | No offline mode in the docs. Printing a PDF is the suggested answer to poor signal |
| P4 | Not covered | App Store history is mostly bug fixes. 13.0.2 fixed habit entry for users outside the US |
| P5 | Not covered | Per-exercise results with a save tap each time. Tap counts not seen |
| P6 | Documented limit | Through Terra. Google Fit listed, Health Connect not mentioned. One graph per device, no merged total. Sync delays acknowledged. Standard and Pro only |
| P7 | Documented limit | No food database. Daily totals typed in or pulled from MyFitnessPal |
| P8 | Documented limit | Habit tracker mobile only. Interval timer iOS only. Wearables connect in a browser. Coach app started as a beta in 2024; adding clients came to iOS in April 2026 |
| P9 | Documented limit | 200 MB per video, about 60 seconds. The client must stay in the app until the upload finishes; leaving makes it fail |
| P10 | Not covered | Clients not logged in get messages by email. Read ticks, retries and failed sends not documented |
| P11 | Partly documented | Exercise history shows past results per exercise. Pre-filling from last time not documented |
| P12 | Documented limit | Wearables, branding, coach profile and advanced habits from Standard. Zapier on Pro. 5% on every payment and refund |
| P13 | Documented limit | Stopwatch and countdown, interval on iOS only. Keeps running outside the app; alerts need notifications on. No auto-start after a set |
| P14 | Not covered | Not in the pages read. Help articles point to a support email |
| P15 | Documented limit | Clients can't export their own workouts, only get them by email. Play listing says deletion can't be requested. Self-serve cancel not found |

## For Infinilift

Keep:
- Remote, dual and in-person client types, with no login for in-person.
- Sync on or off per program, and starting a client on any program day.
- A Needs Attention list for a sudden compliance drop, counting sessions and messages too.
- Copy, paste, drag, multi-select and keyboard shortcuts in the calendar.
- Voice notes up to 7 minutes with playback before sending, for clients as well.
- A copyable invite link.
- Stopwatch time dropped into the result.

Fix:
- Real check-in and intake forms with question types, schedules and e-signed waivers.
- Set rows that save on the phone as each set is entered, with or without signal.
- Australian food search and barcodes inside the app.
- Health Connect directly, with one daily step total and workouts written back.
- Background video upload past 60 seconds that survives leaving the app.
- Built-in automations for messages and check-ins, on every plan.
- Client checkout link, self-serve cancel, client data export and deletion requests.
- Interval timer on iOS and Android, on the lock screen.
- One clear fee, not charged again on refunds.

Skip:
- Check-ins and intake disguised as workouts.
- Zapier as the only automation path.
- Printing a PDF as the answer to poor signal.

## Limits

- No account, trial or app launch, because TrueCoach's terms ban competitive use. Nothing was seen first hand: no screens, tap counts, JSON shapes, network hosts or manifest.
- The Google Play listing page didn't load in the page reader, so the Android version, installs and Android release notes weren't read. Only the Data safety section loaded.
- YouTube pages didn't load either, so no transcript, description or chapter list was read. Titles and channel names were confirmed through YouTube's public embed lookup, 1 request per video. No timestamps are known.
- Dated help articles run from 2022 to December 2025 and may lag the app. Many don't say which platform they describe.
- Docs disagree on Zapier's plan (Standard or Pro), colour count (8 or any) and fees (none or 5%). The pricing page showed US$26.34 for Starter; `competitors.md` has US$29.98 from 11 October. The page doesn't say whether its prices are monthly or annual billing.
- Titles seen but not read: group messages, archived clients, cancelling subscriptions, one-time payments, connecting Stripe, the coach's wearables view, the MyFitnessPal collection.
- About 38 pages read plus 9 video lookups, a little over the planned 30.

Videos worth watching by hand, for jobs the docs don't cover (timestamps unknown, so from 0:00):
- Client 2, logging and saving results: TrueCoach Client Tutorial, https://www.youtube.com/watch?v=nLNytN0fH7E
- Coach 2, exercise fields and supersets: Workout Builder, https://www.youtube.com/watch?v=A5Lx2gSYqHA
- Coach 7, what the client sees when paying: Payments Onboarding, https://www.youtube.com/watch?v=UPAvch9LNgM
- Coach 5, client comments on workouts: Programming made EASY, https://www.youtube.com/watch?v=taNYj66Mojs

## Sources

Vendor site:
- https://truecoach.co/pricing/ (plans, prices, trial terms)
- https://truecoach.co/features/ (feature areas and integrations)
- https://truecoach.co/blog/truecoach-product-updates-every-fitness-trainer-needs-to-know/ (2025 web and app updates)
- https://truecoach.co/blog/introducing-voice-notes-for-personal-trainers-in-truecoach/ (voice notes launch post)

Help centre:
- Index and article lists: [help centre collection index](https://help.truecoach.co/en/), [client tutorials article list](https://help.truecoach.co/en/collections/1412062-truecoach-client-tutorials), [managing clients article list](https://help.truecoach.co/en/collections/1396584-managing-clients), [programs article list](https://help.truecoach.co/en/collections/1396570-programs), [calendar and sidebar article list](https://help.truecoach.co/en/collections/1396559-the-workout-calendar-sidebar), [messaging article list](https://help.truecoach.co/en/collections/5484575-messaging), [payments article list](https://help.truecoach.co/en/collections/2015316-payments), [wearables article list](https://help.truecoach.co/en/collections/8538883-wearables)
- Clients and onboarding: [adding a new client](https://help.truecoach.co/en/articles/2403903-adding-a-new-client), [client first sign-in steps](https://help.truecoach.co/en/articles/2950800-client-accessing-my-truecoach-account-for-the-first-time), [client app download links](https://help.truecoach.co/en/articles/2632440-client-truecoach-tutorial), [onboarding program example](https://help.truecoach.co/en/articles/3889427-creating-an-onboarding-sequence), [what clients see](https://help.truecoach.co/en/articles/2403707-the-truecoach-client-experience), [waivers, intake and check-ins](https://help.truecoach.co/en/articles/3363240-waivers-questionnaires-assessments-and-check-in-s), [client progress photo steps](https://help.truecoach.co/en/articles/6812443-client-uploading-progress-pictures)
- Programs: [building and assigning programs](https://help.truecoach.co/en/articles/3047401-programs), [workout builder and supersets](https://help.truecoach.co/en/articles/3047972-the-workout-builder-basics)
- Nutrition and habits: [nutrition coaching approach](https://help.truecoach.co/en/articles/3047504-using-truecoach-for-nutrition-clients), [nutrition goals and history](https://help.truecoach.co/en/articles/3047252-nutrition-tracking), [Standard plan habit tracker](https://help.truecoach.co/en/articles/9675861-advanced-habit-nutrition-tracking)
- Messaging and triage: [coach messaging steps](https://help.truecoach.co/en/articles/2403915-messaging-your-clients), [voice note steps and limits](https://help.truecoach.co/en/articles/13861965-voice-notes-messaging), [compliance and Needs Attention](https://help.truecoach.co/en/articles/2403738-compliance-rates)
- Automation and payments: [Zapier triggers and action](https://help.truecoach.co/en/articles/8688374-zapier-integration), [products, plans and subscriptions](https://help.truecoach.co/en/articles/3491622-products-pricing-plans-and-subscriptions), [client billing view](https://help.truecoach.co/en/articles/3491674-payments-from-client-view), [5% processing fee article](https://help.truecoach.co/en/articles/3491685-understanding-processing-fees)
- Branding and wearables: [branding and theming settings](https://help.truecoach.co/en/articles/2393617-enhanced-custom-theming), [supported wearables and plans](https://help.truecoach.co/en/articles/8417196-wearables-faq), [client wearable connection steps](https://help.truecoach.co/en/articles/8800819-client-connecting-and-viewing-wearables)
- Client app: [client timers by platform](https://help.truecoach.co/en/articles/4409323-client-in-app-timers), [client export limits](https://help.truecoach.co/en/articles/2653729-client-exporting-workouts), [client video upload steps](https://help.truecoach.co/en/articles/2580531-client-uploading-a-video-to-a-workout), [video size and staying in app](https://help.truecoach.co/en/articles/3363353-best-practices-for-client-video-uploading), [combined coach and client app](https://help.truecoach.co/en/articles/8421397-truecoach-app-for-coaches-clients)

Stores:
- https://apps.apple.com/au/app/truecoach/id1439127794 (App Store listing and history)
- https://play.google.com/store/apps/datasafety?id=co.truecoach.client&hl=en (Play Data safety section)
- https://play.google.com/store/apps/details?id=co.truecoach.client (Play listing, didn't load)

Videos (all on the TrueCoach by Xplor channel, titles only, no timestamps):
- https://www.youtube.com/watch?v=A5Lx2gSYqHA (Workout Builder walkthrough)
- https://www.youtube.com/watch?v=CpKol4zL7Rc (multi-select copy and drag)
- https://www.youtube.com/watch?v=taNYj66Mojs (programming overview)
- https://www.youtube.com/watch?v=nLNytN0fH7E (client app tutorial)
- https://www.youtube.com/watch?v=vKaDD9VlU2c (payments setup tutorial)
- https://www.youtube.com/watch?v=e-xna5ZbWXc (connecting Stripe)
- https://www.youtube.com/watch?v=UPAvch9LNgM (payments onboarding)
