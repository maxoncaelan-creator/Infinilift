# ABC Trainerize: REA findings

Desk study, 12 October 2026, from public sources only. Trainerize's terms ban competitive use, so no account was made. Android app 8.18.4 is installed on the study emulator but hasn't been opened.

Read: 33 public pages (help centre, trainerize.com, Google Play, App Store) and 9 YouTube videos (8 from Trainerize's channel, 1 third-party), one page at a time. iOS app 8.18.7 (App Store, 6 September 2026). Google Play listing updated 14 August 2026. Known-issues page last updated 9 October 2026. Everything below is what Trainerize documents, not what we saw the app do.

## Feature inventory

| Area | Coach can | Client can | Notes |
|---|---|---|---|
| Clients | Add on web or app, import phone contacts, bulk CSV, pick 1 of 4 client types | Join from an emailed invite | Basic clients don't use a seat. Offline clients have no login |
| Onboarding | Build onboarding forms, set a default, schedule forms later | Fill in the form during account setup | Paid plans only, not in the trial. Owner or admin builds forms. No built-in waiver |
| Programs | Phased master programs on a day-numbered calendar, subscribe or copy to clients, AI builder from a prompt or a text, PDF, CSV or Excel file | See today's items in a to-do list | Subscribed clients get master changes; copies don't |
| Workouts | Regular, superset, circuit and interval workouts; progression grid per scheduled day | Track sets, auto-fill past weights, swap exercises by filter, keep notes per exercise | Moving a scheduled workout drops its progressions |
| Nutrition | Daily goal (calories, calories and protein, or full macros) with a variance band, BMR and TDEE calculator, smart or flexible meal plans, PDF plans | Log meals in the app or through MyFitnessPal or Fitbit, scan barcodes, add custom foods | Meal plans need the nutrition add-on. One goal for every day |
| Check-ins and progress | Build forms (single, multiple, text, 1 to 10 rating), schedule and repeat, compare submissions, edit answers; insights widgets; photo compare with slider and markers (web) | Get a push, answer from the to-do list; see the coach's widget layout | No photo question. Forms can't be deleted |
| Messaging | 1:1 and group chat, voice up to 5 minutes, video up to 3 minutes or 50 MB (app only), files up to 10 MB (web), product offers, booking slots | Chat and voice notes; save photos and videos the coach sends | Typing indicator. No read or delivery state documented |
| Triage | Auto tags: not signed in, not messaged, not responded, low compliance, failing payment, program ending | n/a | Thresholds adjustable |
| Automation | Program auto-messages by day and time, account-wide welcome flow, product automation on purchase, start and end | Gets messages shown as from their coach | Repeating messages can't be edited as a set |
| Payments | Stripe products (main, add-on, session pack; recurring, one-time or free), checkout links, trials, invoices | Buy, and cancel recurring products when allowed | Paid add-on, not in the trial. Cards only |
| Branding | Pro: icon, launch screen, top bar, favicon, own Google Play listing. Studio: own store listings and themed app | Branded Android app; on iPhone, branding after sign-in | US$169 one-time on Pro. 8 to 12 weeks |
| Health | See synced steps, sleep, heart rate, weight and body fat in the dashboard and graphs | Connect Apple Health, Health Connect, Garmin, Fitbit, Withings, Apple Watch app | Health Connect only syncs while the app is open |
| Data out | Export the client list as CSV (name, email, phone, trainer), print workouts to PDF, export payment transactions | Nothing documented | Client history can't be exported |

## Jobs

Steps are as the help docs describe them. Screen and tap counts not seen.

### Coach 1. Invite and onboard a client, with intake form and waiver
1. Web: Add New > Client, fill in the fields, pick a client type, send the invite. App: Clients > plus > new client or import a contact.
2. The email asks the client to set a password, get the app and fill in the onboarding form, if it's on.
3. Intake: Master Libraries > Forms > New > Onboarding (owner or admin only), then turn it on under Settings > Automated Messages and Events.
4. Waiver: no built-in signing. The docs point to Zapier and an e-signing tool, or a tick box at checkout and a PDF in the welcome email.
- Good: one email covers account, app and intake. Answers land on the client's profile and the coach is notified. A red tag flags clients not set up after 3 days.
- Clumsy: onboarding forms aren't on Free or the trial. Waivers need Zapier and a separate e-signing tool.

### Coach 2. Build a 4-week program with a superset, progression and deload, save as a template and assign it
1. Master Libraries > Programs > New > Build New > phased program. Set the number of phases and weeks each, pick a folder, save. Photos and weigh-ins land at each phase's start and end unless unticked.
2. Add workouts to each phase, new or imported. Superset: select exercises in the builder > Superset, then set the inline rest and sets.
3. Schedule workouts on the program calendar, which counts days, not dates.
4. Progression: Edit next to a workout > Progression Spreadsheet. Change targets per scheduled day, drag to copy a day, save.
5. Assign: Summary & Subscribers > Add Subscribers, or copy the program to the client.
- Deload: no deload feature is documented. A lighter phase or lower targets in the spreadsheet would do it (our inference).
- Good: the master program is the template, with a clear rule: subscribers get later edits, copies don't. Since 29 April 2026 the spreadsheet shows the client's latest stats, colour-codes supersets and takes keyboard entry and paste.
- Clumsy: workouts must be scheduled before the spreadsheet works, and moving or rescheduling one removes its progressions. Items can't be dragged across phases. Auto-fill breaks when an exercise appears twice in a workout (open issue).

### Coach 3. Set macro targets for training and rest days, and a meal plan
1. Client profile > Goals and Habits > New > Daily Nutrition Goal. Pick the type, set the variance, optionally use the BMR and TDEE calculator.
2. Pick how the client tracks (app, MyFitnessPal, Fitbit or not at all) and save. The client is notified.
3. Meal plan: client profile > Meal Plan. Flexible plan: set the goal, drag recipes onto days, duplicate days, adjust servings, publish or save a draft. Or generate a smart plan of up to 7 days, or attach a PDF.
- Training and rest days: not documented. The goal is one daily target.
- Good: the variance band makes compliance fair. Each logged meal keeps a copy of the goal at the time. Plans copy to other clients. Since 26 August 2026 a coach can let a client edit their own plan with targets locked.
- Clumsy: each macro must be about 15% of calories or more, so very low-carb or low-fat splits may not save. A day counts only if every target is inside the band. Meal plans need the nutrition add-on, and the flexible planner is still marked beta.

### Coach 4. Make a weekly check-in form, then review a submitted one with photos side by side
1. Master Libraries > Forms > New (owner or admin only). Drag in questions (up to 7 options each), mark required ones, save.
2. Schedule it on a program or client calendar with a weekly repeat. The client gets a push and sees it in the day's to-do list.
3. The coach gets an in-app notification (no email option), opens the client card > Check-in and turns on Compare.
4. Photos: Insights Dashboard > Progress Photos > Compare. Pick dates and front, side or back, then side by side or slider.
- Good: compare across dates or across different forms. Coaches can fix an answer, and the form shows who edited it and when. Photo compare got a full-screen view, slider, zoom and markers on 16 September 2026.
- Clumsy: no photo question type, so the check-in and the photos are two items in two places. Editing a form doesn't change copies already scheduled. Forms can't be deleted. Check-in forms only arrived around October 2025 (launch video seen in title or description only).

### Coach 5. Message a client (text, voice, video) and a group; find a client who's gone quiet
1. Messages (web or app) > pick a conversation. Voice: microphone, up to 5 minutes. Video: app only, up to 3 minutes or 50 MB.
2. Group: Messages > New > add people > send as a group. A mass message goes as one group only up to 10 clients.
3. Quiet clients: auto tags on the Overview page and as a client-list filter (no sign-in for 7 days, no message sent or answered for a week, low compliance). Thresholds can be changed.
- Good: auto tags cover triage well, including failing payments and programs about to end. Product offers and booking slots can be sent in chat.
- Clumsy: no read or delivery state in the docs. Video can't be sent from the web. Voice notes are deleted after 6 months. Shortened links don't open in the app.

### Coach 6. Set up automation: a message on day 3 and a check-in every Sunday
1. Master program > Calendar > day 3 > Auto Messages. Write it, set a time (client's time zone), add a repeat if needed, schedule.
2. Check-in: program calendar > Schedule > Check-in Form, repeat weekly.
3. Account-wide messages: Settings > Automated Messages and Events. Product automation runs on purchase, start and end.
- Good: workouts, messages, forms and photo reminders share one program calendar. Product end automation offboards a client (unsubscribe, remove from groups, change client type).
- Clumsy: automated messages look like they came from the coach. A repeating message can't be edited as a set; delete and reschedule. Automation isn't undone when a product is cancelled. Calendars count days, so the weekday depends on the start date; products can start on the next Monday to line this up.

### Coach 7. Make a package and take a payment, stopping before a real charge
1. Buy the Stripe add-on (US$10 a month; not on Free or the trial).
2. Payments > Setup: pick country and currency (fixed once confirmed), connect Stripe, verify.
3. Payments > Products > Add Product: type, payment type (fixed once saved), start rule (purchase day, next Monday or a fixed date), and options for Trainerize.me, client self-cancel (on by default for recurring) and new clients only.
4. Set automation, then share the checkout link or sell to a client by hand.
- Good: buy-and-start with no manual steps. Self-cancel is the default. Session packs, invoices and a transactions CSV.
- Clumsy: the add-on isn't in the trial, so a coach can't try payments before paying. Cards only: no Apple Pay, Google Pay, buy now pay later or bank transfer. Nothing was tested here.

### Coach 8. Branding: what can change and what it costs
1. Pro branded app: US$169 once, on Pro. Upload a logo and colour in a web publisher; staff check it by hand; 8 to 12 weeks; no preview.
2. Pro changes the icon, launch screen (logo centred, an image, an overlay colour), top bar and favicon. In-app theme colours stay default. Android gets its own Google Play listing under Trainerize's developer account.
3. iPhone clients get the main app, named Fitness App on the home screen, with branding after sign-in.
4. Studio (from US$275 a month) adds its own App Store and Google Play listings and more control over the in-app look. Apple's US$99 a year developer fee is extra.
- Good: a one-time fee for an own-name Android app.
- Clumsy: on Pro, iPhone clients never see the coach's name in the store or on the home screen. Cancelling the plan turns the branded app off.

### Client 1. Accept the invite and sign up
1. Open the invite email, set a password, download the app, fill in the onboarding form if it's on.
- Store listings say the app only works after an invite from a coach or gym. Sign-in options other than email and password are not covered in the pages read.
- Good: intake sits inside setup, after the password and profile.
- Clumsy: no way in without the email. A broken App Store link in iPhone invites was fixed in 8.7.0 (24 February 2026).

### Client 2. Log a workout, with flight mode switched on halfway
1. Calendar > today > tap the workout > Track. Enter stats set by set; auto-fill brings in past weights.
2. Tap End. An older article says stats also save if the client taps Close, and sync to the website.
- Offline: Trainerize documents nothing about logging without signal or what happens to sets entered offline. The release notes use offline only for the client type with no login. Not covered.
- Good: exercise swaps by muscle, equipment or level (3 February 2026). One note per exercise carries forward (19 April 2026).
- Clumsy: the main logging article is years old and still names a check-in step the release notes say was removed. The app shows 12 months of exercise history; the web shows all.

### Client 3. Log food: search an Australian product, scan a barcode, try a photo
1. Plus > Meal. Take or pick a photo, or skip.
2. Search foods (a tick marks USDA-checked entries), scan a barcode (US, Canada, Australia and the UK), or pick from Recent or Custom.
3. Adjust servings and log. The meal is labelled breakfast, lunch, dinner or snack by the phone's clock.
- The photo is attached to the meal; no photo recognition is documented. The FitMetrics add-on lists AI meal analysis, with no detail. The food database's source isn't named, so Australian coverage is unknown.
- Good: missing or wrong foods can be reported from search. A meal can go on several days at once.
- Clumsy: one breakfast, lunch and dinner a day. Coaches can't log for a client. On iPhone, meal photos can end up blank if the app closes during upload (open issue).

### Client 4. Submit a check-in with progress photos
1. Tap the push or open the form from the day's to-do list, answer, submit.
- Photos are a separate scheduled reminder. The client steps for adding photos are not covered in the pages read.
- Clumsy: two items for one check-in.

### Client 5. Connect Health Connect and check what reaches the coach
1. Link the wearable's app to Health Connect first.
2. In Trainerize: More (...) > Health Connect > Connect, allow every data type. The first sync brings 2 weeks of data.
3. The coach sees it on the client dashboard tiles, activity feed, progress graphs and insights widgets.
- Good: one link covers Samsung Health, Oura, Whoop, Polar, Suunto, Zepp, InBody and Renpho.
- Clumsy: data doesn't sync while the app is closed. Two articles disagree on what syncs (one lists workouts, one doesn't) and where the button is. Double-counted Samsung steps are fixed by the client changing Samsung settings. Writing workouts back isn't documented.

### Client 6. Message the coach
1. Messages > the coach's chat. Text and voice notes; photos and videos from the coach can be saved.
- Whether clients can send video isn't stated in the pages read.
- Clumsy: one client type has 1-way messaging only (we didn't read how that works).

## Data

No public API reference is published. The help article on the API names data areas only (goals, habits, body stats, nutrition, workouts, appointments). API and webhooks come with Studio, Enterprise or the FitMetrics add-on, with a 180-day lookback and 250,000 calls a month. No entity or field names recorded. Third-party reconstructions of the API exist and weren't used.

## Services

| Purpose | Service | Source |
|---|---|---|
| Payments | Stripe (cards, 45+ countries); PayPal and Square only through Zapier | Help centre, pricing, integrations page |
| Health data | Apple Health, Google Health Connect (since 2 February 2025) | Integrations page, help centre, release notes |
| Wearables | Apple Watch app, Garmin, Fitbit, Withings; via Health Connect: Samsung Health, Oura, Whoop, Polar, Suunto, Zepp, InBody, Renpho | Integrations page, help centre |
| Food | MyFitnessPal, Fitbit food logs; USDA checks on in-app foods | Integrations page, help centre |
| Video | YouTube import for exercise videos; Google Cast to TVs; built-in video calls and streaming (provider not named) | Integrations page, release notes, pricing |
| Calendar | Google Calendar | Integrations page |
| Automation | Zapier to Google Forms, Typeform, Dropbox Sign, SignNow, Mailchimp, AWeber, HubSpot | Integrations page, help centre |
| Gym software | ABC Glofox, ABC Ignite, Mindbody (Studio and Enterprise) | Integrations page |
| AI | AI Workout Builder; FitMetrics add-on (provider not named) | Release notes, pricing |
| Status | Statuspage widget on help pages | Help centre page embed |

Google Play Data safety: no data shared with third parties; collects device IDs, name, email, phone, photos and videos, crash logs, health and fitness data and contacts; encrypted in transit; data can't be deleted on request. App Store privacy: health, contact info, user content, identifiers, usage, sensitive info and diagnostics, all linked to the user.

## Pain points checked

| Id | Happened? | What we saw |
|---|---|---|
| P1 | Not covered | Nothing on failed saves or logging without signal. An old article says stats save even on Close. No lost-workout entry on the known-issues page (9 October 2026) |
| P2 | Documented limit | Clients can only get in through a coach's email invite. Red tag after 3 days without setup. iPhone invite link fixed February 2026 |
| P3 | Documented limit | No offline mode documented. Mobile exercise history was cut to 90 days for speed, now 365. A status widget sits on help pages and the site footer links a status page |
| P4 | Partly covered | Client app redesigned 17 November 2025. A third-party coach video describes a switch back to the old layout (description only). No dark mode in the release notes, apart from an old note turning it off on iOS 13 |
| P5 | Partly covered | Exercise swaps by filter (February 2026), auto-fill and notes. Tap counts not documented |
| P6 | Documented limit | Health Connect only syncs with the app open. Double-counted Samsung steps left to the client to fix. Fitbit food sync is manual for now (open) |
| P7 | Documented limit | USDA checks only; database source not named. Barcode scanning is offered in Australia. Goals cover calories, protein, carbs and fat only |
| P8 | Documented limit | Video messages app only. Form building documented on web only. Mobile insights can't set date ranges or layout |
| P9 | Documented limit | Video up to 3 minutes or 50 MB, app only. iPhone meal photos go blank if the app closes mid-upload (open) |
| P10 | Documented limit | Typing indicator only; no read state documented. Automated messages look like the coach's. Voice notes deleted after 6 months. No email alert for check-ins |
| P11 | Documented limit | Auto-fill uses only an exercise's first appearance (open). App history capped at 12 months (2 September 2026) |
| P12 | Documented limit | Add-ons: nutrition US$20 to 45, business US$25, video US$10, payments US$10 a month; branded app US$169 once; FitMetrics from US$6 a client |
| P13 | Partly covered | Interval timer runs in the background since 2020; an iPhone countdown bug fixed in 8.18.x. Rest timer chime is silent on silent or vibrate. Lock-screen timer not covered |
| P14 | Partly covered | Support by email and in the app; Free gets the help centre and webinars only. Support won't help with API work |
| P15 | Documented limit | Self-cancel is on by default for recurring products. Deactivated clients lose login. Client history can't be exported. Play says data can't be deleted on request |

## For Infinilift

Keep:
- Master program as the template, with a visible rule for live updates versus copies, and photos and weigh-ins at each phase's start and end.
- A progression grid across weeks that shows the client's latest stats and takes keyboard entry and paste.
- Auto tags for quiet, slipping and failing-payment clients, with thresholds the coach sets.
- Check-in and photo compare across dates (slider, zoom, markers), and coach edits that show who changed what.
- Product automation on purchase, start and end, with self-cancel on by default.
- A variance band on nutrition goals, saved with each logged meal.
- Per-exercise notes that carry forward, swaps filtered by muscle and equipment, and AI import from text, PDF, CSV and Excel.
- A public known-issues page with dates and workarounds, and release notes by platform.

Fix:
- Offline-first logging, documented, since Trainerize documents none.
- Training and rest-day targets, with no minimum share per macro.
- Photo questions inside check-in forms, reviewed on one screen.
- Rescheduling a workout keeps its progressions.
- Built-in waiver signing, and intake forms on the free plan and trial.
- Sent and read state, automated messages labelled, voice notes kept with the thread, and video from web and app uploaded in the background.
- Health data synced in the background, steps de-duplicated by us, workouts written back.
- Full history on every device, last time from any appearance of the exercise, client export and a deletion request path.
- Wallet payments at checkout, and payments a coach can try in test mode during the trial.

Skip:
- Paid add-ons for payments, nutrition, video and branding, and waivers only through Zapier.
- Country, currency and payment type that can't change after setup.
- An 8 to 12 week branded app queue with no preview.

## Limits

- No account, so no screens, tap counts, JSON shapes, network hosts or manifest. The installed Android app wasn't opened.
- Not checked: offline logging, rest timer on a locked screen, Australian food search results, what reaches the coach from Health Connect, the checkout page.
- Help articles vary in age. The core logging article predates the release notes, and two Health Connect articles disagree.
- The pricing page's plan cards and its FAQ show different numbers (the cards look like annual billing). Prices above are the monthly figures in the FAQ and compare table, in USD before tax.
- YouTube transcripts didn't load in the study browser, so every video below was used by title, description and chapters only. The 2 Vimeo videos on help pages had no readable transcript.

Videos worth watching by hand:
- Coach 3, training and rest-day macros: https://www.youtube.com/watch?v=5n0e8zDu7Kg at 11:30
- Client 2, the logging flow and tap count: https://www.youtube.com/watch?v=5n0e8zDu7Kg at 13:35
- Client 3, barcode scan (third-party): https://www.youtube.com/watch?v=nHxdil0VlRc at 08:25
- Client 4, check-in from the client side: https://www.youtube.com/watch?v=SVeKktdMgd8 at 0:00
- Coach 2, phase setup for a deload: https://www.youtube.com/watch?v=gFgQDbhvDAE at 0:26

## Sources

Help centre:
- [Adding clients](https://help.trainerize.com/hc/en-us/articles/208689066-How-To-Add-Clients-To-ABC-Trainerize)
- [Old consultation form](https://help.trainerize.com/hc/en-us/articles/208689146-About-The-Client-Consultation-Form)
- [Waivers and PAR-Q forms](https://help.trainerize.com/hc/en-us/articles/360043514452-Managing-Waivers-PAR-Q-forms-and-Agreements-with-Clients)
- [Onboarding forms](https://help.trainerize.com/hc/en-us/articles/48660477450388-How-to-Create-and-Manage-Onboarding-Forms)
- [Phased programs](https://help.trainerize.com/hc/en-us/articles/115004404763-What-is-a-Program-How-do-I-build-one-)
- [Progression spreadsheet](https://help.trainerize.com/hc/en-us/articles/212130826-Progressing-Regressing-Workouts-with-the-Progressions-Spreadsheet)
- [Supersets and circuits](https://help.trainerize.com/hc/en-us/articles/208688926-How-to-Create-Superset-and-Circuit-Workouts)
- [Nutrition goals](https://help.trainerize.com/hc/en-us/articles/360001127403-How-to-Create-a-Nutrition-Goal-for-a-Client)
- [Flexible meal planner](https://help.trainerize.com/hc/en-us/articles/47042957643156-Flexible-Meal-Planner)
- [In-app meal tracking](https://help.trainerize.com/hc/en-us/articles/4405482601364-Calories-or-Full-Macro-Tracking-In-App)
- [Check-in forms](https://help.trainerize.com/hc/en-us/articles/31369316335124-Sharing-Check-In-Forms-with-Clients)
- [Client insights dashboard](https://help.trainerize.com/hc/en-us/articles/46648417703956-Using-the-Client-Insights-Dashboard)
- [Sending messages](https://help.trainerize.com/hc/en-us/articles/208688846-How-to-Send-and-View-Individual-Messages)
- [Voice messages](https://help.trainerize.com/hc/en-us/articles/23582579681044-Voice-Messages)
- [Auto client tags](https://help.trainerize.com/hc/en-us/articles/208689156-Auto-Client-Tags-Attending-To-Clients-Needing-Attention)
- [Program auto-messages](https://help.trainerize.com/hc/en-us/articles/360000397966-How-To-Use-and-Setup-Program-Auto-Messages)
- [Stripe payments add-on](https://help.trainerize.com/hc/en-us/articles/6147809498004-Stripe-Integrated-Payments)
- [Building a product](https://help.trainerize.com/hc/en-us/articles/115004618063-Step-2-Build-a-Product)
- [Pro branded app](https://help.trainerize.com/hc/en-us/articles/360000152823-Pro-Custom-Branded-App-What-s-included-)
- [Health Connect wearables](https://help.trainerize.com/hc/en-us/articles/34692533005204-Syncing-Wearable-Data-to-ABC-Trainerize-Using-Google-Health-Connect)
- [Connecting Health Connect](https://help.trainerize.com/hc/en-us/articles/32997239774612-How-Can-Clients-Connect-Google-Health-to-ABC-Trainerize)
- [Health Connect troubleshooting](https://help.trainerize.com/hc/en-us/articles/46257852947860-Troubleshooting-the-Google-Health-Connect-Integration)
- [Logging a workout](https://help.trainerize.com/hc/en-us/articles/208689026-How-do-I-use-the-mobile-app-when-I-m-working-out)
- [Known issues list](https://help.trainerize.com/hc/en-us/articles/360034499751-Known-Issues-We-Are-Currently-Working-On)
- [API and webhooks](https://help.trainerize.com/hc/en-us/articles/37082084919060-Using-API-and-Webhooks-With-ABC-Trainerize)
- [What can be exported](https://help.trainerize.com/hc/en-us/articles/31089834946324-What-Information-Can-Be-Exported-from-ABC-Trainerize)
- [Deactivating clients](https://help.trainerize.com/hc/en-us/articles/208689116-How-to-Deactivate-and-Reactivate-Clients)

Trainerize website and stores:
- [Pricing and add-ons](https://www.trainerize.com/pricing/)
- [Integrations list](https://www.trainerize.com/integrations/)
- [Release notes](https://www.trainerize.com/updates/)
- [Google Play listing](https://play.google.com/store/apps/details?id=com.trainerize.Trainerize)
- [Google Play data safety](https://play.google.com/store/apps/datasafety?id=com.trainerize.Trainerize)
- [App Store listing](https://apps.apple.com/au/app/fitness-app-abc-trainerize/id516851502)

Videos (title, description and chapters only):
- [Workflow demo, 9 July 2026](https://www.youtube.com/watch?v=5n0e8zDu7Kg): chapters 2:17, 7:00, 11:30, 13:35, 14:25
- [Building a master program](https://www.youtube.com/watch?v=gFgQDbhvDAE): chapters 0:26, 2:01, 4:27
- [Creating and selling programs](https://www.youtube.com/watch?v=c43hHtf9f5M): chapters 0:18, 6:55
- [Adding new clients](https://www.youtube.com/watch?v=oUYzcqMpTs0): no chapters
- [Coach nutrition tracking](https://www.youtube.com/watch?v=KvoqVu80FMc): chapters 0:16, 0:46, 2:18
- [Smart meal planner](https://www.youtube.com/watch?v=3MWXZqCuoUY): no chapters
- [Turning off auto-messages](https://www.youtube.com/watch?v=L-xWVoenhrc): chapters 0:47, 1:54, 3:35
- [Check-in forms launch](https://www.youtube.com/watch?v=SVeKktdMgd8): 1 October 2025, 32 seconds
- [Third-party: 2026 layout, food logging](https://www.youtube.com/watch?v=nHxdil0VlRc): No Bad Days, 29 November 2025, chapters 0:57, 04:44, 08:25
- Embedded videos on the progression spreadsheet and building a product pages above: not readable
