# Payroll Onboarding Portal — Plan (Layout & Content)

**Status:** Draft v0.1 for discussion with Brendan (Payroll) and Kevin
**Scope of this draft:** structure, layout, interactions and card-by-card content. Branding, visual style and the final tech platform come later.
**Sources:** *First Call Step by Step* (Brendan's call outline), *Call alternative – Staffology* (the written guide for clients who can't take the call), and the Chris & Brendan setup/onboarding meeting of 21 Sept 2026.

---

## 1. What we're building, in one paragraph

A friendly, click-through **card deck** that teaches a new employer what Brendan covers on the payroll setup call: who's who, the monthly routine, the documents they get, HMRC, and their responsibilities as an employer. It is **not a test**. It's split into short sections the employer can come back to at any time (for example, opening the Payslip section with their first payslip in front of them). At the end they choose one of two paths: **"I'm confident, start my payroll"** or **"I'd like a call with the payroll team"**. The phone call stays as the safety net. The portal is an alternative for confident clients, not a replacement for everyone.

### Goals (from the meeting)

| Goal | What it means for the design |
|---|---|
| Fewer setup calls: even ~30–35% of clients skipping the call is a win | Clear fork at the end. Confident clients can finish without waiting for an appointment. |
| Keep the "human" feel, CILNI's biggest selling point | Warm, plain-English tone. Brendan's voice narrates each card. "You're not alone" message. A call is always one tap away. |
| People actually take in the key points and don't just race to the tick box | Short cards, one idea each. Key facts and figures pulled out large and in colour. Light interactions that aren't a quiz. Recap cards at the end. |
| No quizzes (they feel like a test and put people off) | Use "try it" calculators, tap-to-reveal, and "got it" recaps. Never right/wrong questions. |
| Persistent, so they can come back and pick up where they left off | Saved progress, a section hub, and every section can be revisited after they finish. |
| Covers CILNI on liability | Record which cards were viewed, plus a timestamped acknowledgement at the end. |
| Works on a phone or tablet | Cards designed mobile-first. Big tap targets, swipe to go forward or back. |

### Who it's for

The person who will be the **registered employer**. That's often a parent or family member managing a direct payment for the service user, and technical ability varies hugely: some are very confident, others are proud just to get a password in. Assume a stressed reader who has just jumped through a lot of hoops with the Trust.

---

## 2. Overall structure

```
                ┌──────────────────────────┐
  Link / login ─▶│  WELCOME                 │  short welcome video + "how this works"
                └────────────┬─────────────┘
                             ▼
                ┌──────────────────────────┐
                │  HUB (landing page)      │◀─────────────── come back any time
                │  section tiles + progress│
                └────────────┬─────────────┘
          ┌──────────┬───────┼────────┬──────────┬──────────┐
          ▼          ▼       ▼        ▼          ▼          ▼
       1 Who's    2 Your   3 Your   4 Your    5 HMRC    6 Your     7 When things
         who      staff &  monthly  documents           responsi-    change (FAQs)
                  pay      routine                      bilities
          └──────────┴───────┴────────┴──────────┴──────────┘
                             ▼
                ┌──────────────────────────┐
                │  WRAP-UP                 │  3 recap cards → acknowledgement
                └────────────┬─────────────┘
                   ┌─────────┴──────────┐
                   ▼                    ▼
          "I'm confident —       "I'd like a call"
           start my payroll"      (availability + questions)
                   ▼                    ▼
                ┌──────────────────────────┐
                │  DONE: what happens next │  portal stays available as a reference
                └──────────────────────────┘
```

- **Suggested order, but not locked.** The hub numbers the sections and highlights "Up next", but any tile can be opened. The **Finish** step unlocks once every section has been viewed. This gives us the liability record without trapping anyone.
- **Estimated time:** about 20–25 minutes in total, 2–4 minutes per section. Show the time on each tile. It reassures people.
- **"Talk to us" is always visible.** There's a persistent button in the header on every screen. Nobody should feel stuck with no way out.

---

## 3. Screen layouts

### 3.1 Welcome screen (first visit only)

```
┌──────────────────────────────────────────────┐
│  Welcome to CILNI Payroll, [First name]      │
│  ┌────────────────────────────────────────┐  │
│  │          ▶  Welcome video (2–3 min)     │  │
│  └────────────────────────────────────────┘  │
│  How this works                              │
│   • 7 short sections, about 20 minutes       │
│   • Not a test: there are no wrong answers   │
│   • Stop any time. We'll save your place     │
│   • Prefer to talk? You can ask for a call   │
│     at any point                             │
│                                              │
│   [ Let's start ]      [ I'd rather talk ]   │
└──────────────────────────────────────────────┘
```

### 3.2 Hub / landing page

```
┌──────────────────────────────────────────────┐
│ CILNI Payroll            [ ☎ Talk to us ]    │
│ Hi [First name] · You're 3 of 7 through  ███░ │
├──────────────────────────────────────────────┤
│ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│ │1 Who's   │ │2 Your    │ │3 Your    │       │
│ │  who     │ │  staff & │ │  monthly │       │
│ │ ✓ Done   │ │  pay     │ │  routine │       │
│ │          │ │ ✓ Done   │ │ ▶ Up next│       │
│ │ 3 min    │ │ 4 min    │ │ 4 min    │       │
│ └──────────┘ └──────────┘ └──────────┘       │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│ │4 Docu-   │ │5 HMRC    │ │6 Your    │  ...  │
│ │  ments   │ │          │ │  respons.│       │
│ └──────────┘ └──────────┘ └──────────┘       │
├──────────────────────────────────────────────┤
│ Quick links: 📄 Reading your payslip ·        │
│ 💷 Paying HMRC · 📅 The monthly routine ·     │
│ 📖 Jargon buster                              │
├──────────────────────────────────────────────┤
│        [ Finish & choose next step ]         │
│        (unlocks when all sections viewed)    │
└──────────────────────────────────────────────┘
```

After they finish, the hub turns into their **reference page**. The quick links matter most then ("I've just got my first payslip, what does it mean?").

### 3.3 Card view (the core screen)

```
┌──────────────────────────────────────────────┐
│ ← Hub   4 · Your documents     ● ● ◉ ○ ○ ○   │  ← section progress dots
├──────────────────────────────────────────────┤
│                                              │
│          [ simple illustration ]             │
│                                              │
│   Pay HMRC on the                            │
│   SAME DAY                                   │  ← key fact, large and in colour
│   you pay your employee.                     │
│                                              │
│   Your P30 shows one total. That covers      │
│   tax, National Insurance and student loan   │
│   for all your staff.                        │
│                                              │
│   ▸ Tell me more                             │  ← optional expander
│                                              │
│   🔊 Listen (0:25)   📝 Show transcript       │  ← Brendan's narration
│                                              │
├──────────────────────────────────────────────┤
│  [ ‹ Back ]    [ ? I'd like help with this ] │
│                            [   Next ›   ]    │
└──────────────────────────────────────────────┘
```

**Card anatomy rules**

1. **One idea per card.** A heading plus 1–3 short sentences, about 40 words at most on the face of the card.
2. **Facts and figures are highlighted.** Any number, date or "do/don't" is larger and in an accent colour (for example "7 days", "13 characters", "5.6 weeks", "DO NOT pay cash").
3. **"Tell me more" expander** for the detail Brendan would add on the call if asked. The card stays short, and the detail is there for people who want it.
4. **Narration (Brendan's voice)** is optional, with a transcript for accessibility. Tone of voice carries the emphasis and reassurance that text can't, especially employer vs employee.
5. **"I'd like help with this" button** on every card. It quietly flags the card, and the flagged topics are sent with a call request, so Brendan knows what someone struggled with before he phones. It gives us a signal without a quiz.
6. **Jargon terms are underlined.** Tapping one opens a plain-English definition (for example *nominated representative*, *P30*, *tax code*).
7. **Mobile:** the card fills the screen, you swipe left or right, and the buttons sit at thumb height. Landscape works too.

### 3.4 Card types

| Type | Used for | Example |
|---|---|---|
| **Info** | A single point | "We're your payroll provider, not your funder" |
| **Key figure** | A number to remember | "Pay date = **1 calendar month** after your first employee starts" |
| **Do / Don't** | Rules | "✗ Don't pay cash · ✓ Bank transfer or cheque" |
| **Annotated document** | Payslip, Trust summary, P30 | A sample payslip with numbered hotspots; tap each to see what it means |
| **Timeline / cycle** | The monthly routine | A circular diagram, with each step revealed in turn |
| **Try it** (calculator) | Makes a rule personal, and nothing is submitted | "Enter your employee's start date" → "Your first pay date is **17 June**, then the **17th** of every month" |
| **Tap to reveal / "What would you do?"** | Scenarios, **not scored** | "You get a letter from HMRC asking for money you've already paid. What now?" → tap → answer |
| **Section recap** | End of each section | "3 things to remember" + **[Got it]** |
| **Video** | Welcome and, later, short 60–90s clips | Welcome video, "Opening your payslip" clip |

---

## 4. Content: card by card

Draft copy is written in the portal's voice: plain English, second person, warm. Items marked **⚑** need Brendan to confirm the current process or figure.

### 0 · Welcome (3 cards)

| # | Card | Draft copy / notes |
|---|---|---|
| 0.1 | Welcome video | 2–3 min: who we are, what the portal covers, and the promise that we're here to help. |
| 0.2 | You're not alone | "Setting up as an employer can feel like a lot, especially after everything with the Trust. Many of our team have been through direct payments themselves, or with family. Every situation is a bit different, but we'll always do our best to help." |
| 0.3 | How this works | ~20 minutes, no test, save and come back, ask for a call any time. |

### 1 · Who's who (6 cards, ~3 min)
*The submission form's most common errors come from getting these roles wrong, so this section comes first.*

| # | Card | Draft copy / notes |
|---|---|---|
| 1.1 | **You are the employer** | "The **employer** is the person who agreed with CILNI's Advice Team to take on this role. HMRC will register **you** and write to **you**." Tell me more: this is not always the person who receives care. If you manage the account for a family member, it's usually you. |
| 1.2 | **The employee** | "Your **employee** is the person you pay to provide support, such as a personal assistant." **The employer and the employee can never be the same person.** |
| 1.3 | **The Trust funds you. We run the payroll.** | "Your Health & Social Care Trust provides the funding. CILNI is your **payroll provider**. We **don't** hold your money, can't see your bank account, and can't change your funding." |
| 1.4 | **What you tell us, we report** | "As a payroll bureau, we're **legally required** to report any hours and pay you tell us about to HMRC. So only tell us about work paid for from your direct payment. A gift to a friend or family member isn't payroll. If you're unsure whether something counts, ask us *before* you send it in." ⚑ *Wording to agree with Brendan and Kevin. This replaces the tactful "have a think before you tell us" line from the call.* |
| 1.5 | **Nominated representative** | "Someone you choose to deal with CILNI on your behalf, using your authority. You can remove them at any time. Only **you or your nominated representative** can make changes. Social workers can't." |
| 1.6 | Recap | 3 things: you're the employer · the Trust funds and we run payroll · we must report what you tell us. **[Got it]** |

### 2 · Your staff and their pay (7 cards, ~4 min)

| # | Card | Draft copy / notes |
|---|---|---|
| 2.1 | Check your details | "Before we start, we'll confirm each employee's **start date, hours and rate of pay**. These often change after the Advice Team first sees them, so tell us if anything is different." |
| 2.2 | Set hours or variable hours? | Side-by-side: **Monthly (set hours):** same hours every month, predictable. **Variable (zero hours):** hours change month to month. Tell me more: the pros and cons of each. ⚑ *Brendan to supply the key points he gives on the call.* |
| 2.3 | Your pay rate | "Your rate is either **set by a budget from our team**, or **chosen by you**, as long as it's at or above the **National Minimum Wage**." Caution: if you choose your own rate, our support is limited if it leads to a surplus or shortfall in funding. ⚑ *Show the current NMW figure.* |
| 2.4 | **Your pay date** (try it) | "Your pay date is **one calendar month** after your first employee starts." Calculator: enter the start date → "Your first pay date is **17 June 2026**, then the **17th** of every month." |
| 2.5 | Payments for earlier work | "If you ask us to pay for work done before payroll started, we can, but it goes through payroll and **it will be taxed**." |
| 2.6 | CILNI's fees | ⚑ *"Give details about CILNI payments" is on the call checklist. Brendan to supply content.* |
| 2.7 | Recap | **[Got it]** |

### 3 · Your monthly routine (7 cards, ~4 min)
*This is the heart of the portal. Brendan's end-of-call summary: "We email you, you check it, we send documents, you pay the employee and HMRC, and you move on with your month."*

| # | Card | Draft copy / notes |
|---|---|---|
| 3.1 | The month in 4 steps | Cycle diagram: **① We email you → ② You check the hours → ③ We send your documents → ④ You pay your employee and HMRC.** |
| 3.2 | ① Our email: **7 days** before pay day | "Each month, **7 days before your pay date**, we'll email asking you to confirm your employees' hours." ⚑ *Guide says always reply to confirm. Brendan's call summary says "no changes? you can ignore it". Which is correct?* |
| 3.3 | ② The three types of hours | **Standard hours:** based on your weekly funding from the Trust, and can be shared across employees. **Annual leave:** paid time off, and we keep a running total. **Extra hours:** for example covering someone's holiday, shown separately on the payslip. |
| 3.4 | Reply to **payroll@cilni.org** | "Send your hours back as soon as you can. We need **at least 1 full working day** to prepare your documents. In busy periods, please allow up to your pay date." |
| 3.5 | ③ What arrives | Payslips · Summary for the Trust · P30 (HMRC payment). Each one is covered in Section 4. |
| 3.6 | ④ Pay day | "Pay your employee the **net pay** shown at the bottom of their payslip, and pay HMRC the amount on your P30, **ideally on the same day**." |
| 3.7 | Recap | **[Got it]** |

### 4 · Your documents (10 cards, ~5 min)

| # | Card | Draft copy / notes |
|---|---|---|
| 4.1 | Opening your payslips 🔒 | "Payslips are **password-protected**. Pick a password you're happy to share with your employee." |
| 4.2 | Password trouble? | Tips: passwords are case-sensitive · watch for extra spaces · try copying and pasting it · still stuck? tap *I'd like help* and we'll check it with you. *This is the biggest source of frustration on calls, so it gets its own card and a future 60s video.* |
| 4.3 | **Reading a payslip** (annotated) | Sample payslip with hotspots: ① gross pay ② **tax code** ③ income tax ④ **National Insurance** ⑤ **pension** ⑥ student loan if any ⑦ **net pay**: the amount you pay. |
| 4.4 | Why are there deductions? | Tell me more cards on tax code, NI and pension, in plain English. ⚑ *Brendan's call explanations.* |
| 4.5 | Check it, then send it | "If the payslip looks right, send it to your employee **with their pay**. If something's wrong, tell us and we'll fix it before you pay." Option: employees can receive payslips directly. ⚑ *Is this still offered?* |
| 4.6 | The summary for the Trust (annotated) | "A **gross-to-net summary** of each month's payroll. Keep it for your records. The Trust may ask for it **quarterly**, along with your **bank statements**." |
| 4.7 | Why the Trust wants bank statements | They check your spending matches your payroll. Tell me more: not every Trust asks regularly (Belfast Trust is the one most likely to). ⚑ |
| 4.8 | Your buffer | "The Trust pays an **advance of 5–8 weeks** of funding, so there should always be money in the account on pay day." |
| 4.9 | The P30 (annotated) | "Shows **one total** owed to HMRC for all your employees: income tax, NI and student loan combined. You don't need to work anything out." |
| 4.10 | Recap | **[Got it]** |

### 5 · HMRC (7 cards, ~4 min)
*A real case: a client didn't read the written guide, paid nothing, and was then angry about HMRC letters. This section has to stand out.*

| # | Card | Draft copy / notes |
|---|---|---|
| 5.1 | We register you with HMRC | "Once you've confirmed your details are right, **we** register you as an employer with HMRC. It's the tax for your *employees*, not your own tax bill." |
| 5.2 | **⚠ Don't pay HMRC yet** | "Until your HMRC references arrive, **don't pay HMRC**. You **can** still pay your employees, and the payslip figures are correct." Big warning styling. |
| 5.3 | Your **13-character** reference | "In about **2 weeks** we'll email your HMRC bank details and your **13-character reference**. It **never changes**." ⚑ *Confirm timescale.* |
| 5.4 | Set up HMRC as a payee | "Add HMRC as a payee in your online banking with your 13-character reference. Then each month, just pay that payee." Other options: cheque, phone. Tell me more: step-by-step for common banks. |
| 5.5 | Why the dates don't match | "HMRC's months run from the **6th to the 5th**, so the tax period on your P30 won't always match your pay date. That's normal." ⚑ *Check the wording matches how Brendan explains it.* |
| 5.6 | "What would you do?" (tap to reveal) | "You get an HMRC letter asking for money." → **Already paid?** Contact us and we'll help challenge it. **Not paid?** Pay the amount due (a little interest may be added). |
| 5.7 | Recap | **[Got it]** |

### 6 · Your responsibilities as an employer (10 cards, ~5 min)

| # | Card | Draft copy / notes |
|---|---|---|
| 6.1 | **Don't pay cash** | "Always pay by **bank transfer or cheque**. Cash leaves no record, and if an employee disputes their pay you'd have no proof." |
| 6.2 | Sickness | "If your employee is off sick, tell us when you send in the hours. They may be entitled to **Statutory Sick Pay**." ⚑ |
| 6.3 | Maternity, paternity and other statutory pay | "Tell us as early as possible. We'll work out what's due." ⚑ |
| 6.4 | **Holidays: 5.6 weeks** (try it) | "Employees are entitled to **5.6 weeks'** paid holiday a year, including bank holidays." Calculator: days worked per week → annual entitlement. ⚑ *Confirm how CILNI handles part-time and variable hours.* |
| 6.5 | Holiday year and carry-over | "Your holiday year runs from ___. Up to **1.6 weeks** can be carried over." Cover: record it as **extra hours** for whoever covers. ⚑ |
| 6.6 | Employer's liability insurance | Short card: what it is and that it's required. ⚑ *Brendan only covers this "if questioned". Should it be optional (a Tell me more)?* |
| 6.7 | **Workplace pension** | "Employees who meet the age and earnings thresholds must be **automatically enrolled**. We'll tell you when someone goes in and what to do." ⚑ *Current thresholds and CILNI's process.* |
| 6.8 | Letters from The Pensions Regulator | "Every **3 years** you'll get a letter about a (re-)declaration. We get a copy and deal with it, so **just file it away**." |
| 6.9 | Your account, your say | "Our contract is with **you**. Changes must come from you or your nominated representative." |
| 6.10 | Recap | **[Got it]** |

### 7 · When things change (FAQ cards, ~3 min)
*These also work as a searchable reference after onboarding.*

| # | Card |
|---|---|
| 7.1 | Taking on a new employee: what to send us and when. ⚑ |
| 7.2 | An employee leaves: tell us their last day and any holiday owed. ⚑ |
| 7.3 | Bank holidays: how they're paid. ⚑ |
| 7.4 | Changes to your funding or information from the Trust: forward it to us. ⚑ |
| 7.5 | Change of hours, rate, address or bank details. ⚑ |
| 7.6 | Not sure? Ask us. "Even if it's not a payroll question, we'll point you in the right direction." |

### Wrap-up (5–6 cards)

| # | Card | Notes |
|---|---|---|
| W.1–W.3 | **Recap cards** | "Your month in 4 steps" · "Your 5 golden rules" (don't pay cash · don't pay HMRC until you get your reference · use the 13-character reference · pay HMRC on pay day · tell us about sickness, leave and changes) · "Where to find help". |
| W.4 | **Acknowledgement** | Checkboxes: ☐ I'm the registered employer ☐ I understand the monthly routine ☐ I won't pay HMRC until I get my reference ☐ I know I can come back to this portal and contact CILNI any time. *Suggested wording: "By ticking these, you confirm you're happy for us to set up your payroll. You can come back to this portal at any time."* ⚑ *Final wording to agree with Kevin.* |
| W.5 | **Choose your next step** | **A. "I'm confident, start my payroll"** → confirmation. **B. "I'd like a call first"** → preferred days (Mon–Fri) and time of day (morning/afternoon), best phone number, optional "What would you like to go over?" box, pre-filled with any cards they flagged. Expectation line: *"Calls are booked first come, first served. We can't promise a time, but a member of the team will contact you as soon as possible."* |
| W.6 | **What happens next** | A: "We'll set up your payroll and send your documents before your first pay date." B: "We'll be in touch to arrange your call." Both: "This portal stays available. Bookmark it." |

### Jargon buster (always available)
Employer · Employee · Nominated representative · Direct payment · The Trust · Payroll bureau · Gross pay · Net pay · Tax code · National Insurance · P30 · HMRC reference · Auto-enrolment · Statutory Sick Pay · Holiday year.

**Total:** about **55–60 cards**. Most people will get through it in about 20 minutes, less if they skip the "Tell me more" parts.

---

## 5. Keeping people engaged without a quiz

1. **Short cards with one idea each**, and the key number jumps out.
2. **Brendan's voice** on every card for tone, emphasis and reassurance.
3. **"Try it" calculators** (pay date, holiday) make the rule personal and nothing is submitted, so nothing can go wrong.
4. **Annotated real documents.** Tapping around a sample payslip is interactive and useful.
5. **"What would you do?" tap-to-reveal scenarios**, never scored.
6. **A section recap with "Got it"** gives a small sense of progress, and the hub fills up.
7. **Progress saved** so they can stop without penalty.
8. **Welcome video now, 60–90s clips later** (for example "Opening your payslip", "Setting up HMRC as a payee"), embedded on the matching cards.

*Chris is also researching learning and retention principles. Anything useful slots in here.*

---

## 6. Two versions to prototype

The meeting left one decision open: **should the portal also replace the submission form?**

| | **Version A: Learn only** (recommended first) | **Version B: Learn + submit** |
|---|---|---|
| What it is | The card deck above. The submission form stays separate, as now. | "A little explanation, a little information-gathering", with data-entry cards placed right after the card that explains them. For example, the employer details form sits directly after card 1.1 *You are the employer*. |
| Pros | Simple. No new data errors. Quick to build and test. | One journey instead of two forms, and data is collected at the moment it's understood. Could make the client "live" at the end. |
| Cons | Clients still do two things (form + portal). | Every field is a chance for panic mistakes. Needs a staff review step and validation. Needs a proper web app, not Canva. |
| Needs | Nothing extra. | Guardrails and a draft → approve workflow (below). |

**Recommendation:** build and pilot **Version A** first. Design the card structure so Version B's data cards can be added later without re-writing content.

**Guardrails Version B would need** (from the common submission-form errors Brendan described):
- Employer and employee **can't be the same person**. Flag it if the same name appears twice.
- The service user's name shouldn't go in the employer fields unless they're genuinely the employer. Ask "Are you filling this in for someone else?" first.
- Bank details: ask for the **direct payment account**, and warn if it looks like the employee's details are being entered.
- "Are the funds available in your direct payment account?" gets a follow-up if **No**, and a gentle check if the answer looks inconsistent.
- Address and postcode lookup to cut down typos.
- Every submission lands as a **Draft**. Payroll can **edit and correct** it, then **Approve**. There's no "reject and start again", because re-doing a 30-minute journey would lose people.

---

## 7. Behind the scenes (staff side)

| Need | Prototype (Canva / simple page) | Later (web app on CILNI server) |
|---|---|---|
| Know who has finished | Email to payroll when someone completes: name, path chosen, date | Dashboard |
| Call requests | A spreadsheet row with availability, phone number, questions and flagged cards | Queue with status |
| Liability record | Timestamped acknowledgement plus the sections viewed | Stored against the client record |
| Access | An unlisted link sent by email (as with registration) | Simple login or magic link, eventually alongside the budgeting system in one CILNI login |
| Saved progress | Stored in the browser | Stored on the server, so it works on any device |
| Data check | Brendan cross-checks against Salesforce, as now | Draft → approve workflow and Salesforce cross-check |

---

## 8. Suggested phases

1. **Content sign-off.** Brendan reviews section 4 and answers the ⚑ items. Agree the wording for the tricky cards (1.4 "we must report", W.4 acknowledgement).
2. **Clickable prototype (Version A),** with placeholder illustrations and no narration. Test it with Brendan, Kevin and a couple of friendly clients.
3. **Pilot:** send the link *before* the normal setup call to a handful of new employers. Measure how much shorter the call gets and what people flag.
4. **Add narration and the welcome video.** Then offer the "confident, no call" path for real.
5. **Branding and visual design.**
6. **Web app** (saved progress across devices, staff dashboard). Optionally Version B.

**How we'll know it's working:** % choosing "no call" · time to complete · the most-flagged cards (and whether they need rewriting) · HMRC and payslip-password queries in the first 3 months, compared with clients who had a call.

---

## 9. Open questions for Brendan and Kevin

1. Monthly email: must clients always reply, or only if there are changes? (The guide and the call summary say different things.)
2. What should the "CILNI payments" card say (fees, how and when they're paid)?
3. Can employees still receive payslips directly?
4. Current process and figures for pension auto-enrolment, SSP, maternity/paternity, holiday year and carry-over, bank holidays.
5. Wording for "what you tell us, we must report". How direct can we be?
6. Should employer's liability insurance be a full card, or tucked into "Tell me more"?
7. Final acknowledgement wording, and does it need a named signature and date?
8. Should the Finish step require every section to be viewed, or only the "essentials" (Sections 1, 3, 5)?
9. The step-by-step mentions Connect-era features (HMRC tab, "mark as paid", calendar/documents tab). Is any of that still relevant with Staffology, or is everything by email now?
10. Access for now: an unlisted link or a simple login?
