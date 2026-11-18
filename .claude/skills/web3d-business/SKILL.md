---
name: web3d-business
description: The business layer that turns 3D web craft into $15k–$150k+ projects — positioning/niche, portfolio strategy, case studies, value-based pricing, proposals, the client process, and where to find high-budget clients. Use when working on selling, pricing, pitching, or packaging 3D web work. Part of the web3d pipeline.
---

# web3d-business — Positioning & Sales

Craft is ~30% of a high-ticket sale; positioning, portfolio, and process are the rest. A great site with no credibility sells for $3k; the same craft inside a sharp studio brand sells for $40k+.

## The honest ladder

- **$3–8k** — polished animated site, no brand behind you.
- **$15–40k** — custom WebGL, solo expert *with a real portfolio*. ← realistic near-term target.
- **$50–150k** — small studio, strong brand, case studies, repeat/referral pipeline.
- **$200k+** — named studio, enterprise/agency clients, awards.

You climb it with **proof**, not promises. $500k from a cold prospect on day one is not real; engineer the climb.

## Positioning

- **Niche down.** "3D websites for [luxury watchmakers / Web3 / architecture firms / premium DTC]" beats "we make cool sites." A niche lets you charge more and get referred.
- **Have a studio identity** (name, site, POV) — its own site must itself be a flagship 3D piece (the cobbler's-shoes rule: your site IS the pitch).
- **Be able to take money before chasing volume.** A domain, a business email, a payment processor and a one-page contract are prerequisites, not polish: without them a "yes" cannot be converted to cash, and every extra lead is wasted.

## Portfolio

- **3 exceptional pieces > 10 mediocre.** Each must clear the web3d anti-slop bar.
- If you lack client work, **build concept pieces** for dream brands (clearly marked as concepts). They land real clients.
- Each piece needs a **case study**: the problem, the concept, the signature moment, before/after or metrics, your role. Story sells.
- **Submit to Awwwards / FWA / CSSDA.** A single SOTD badge changes your pricing power and inbound.

## Pricing

- **Value-based, fixed project price** — never hourly (hourly punishes speed/skill). Price on the client's outcome and budget, not your hours.
- **Pricing below the ladder's $3–8k rung is defensible only while proving the motion** — it buys proof at the cost of committing you to volume. Raise on *demand* (leads outpacing capacity), not on an arbitrary client count.
- **Tier every proposal** (Good / Better / Best) — anchors high, lets them choose up.
- **Deposit 50% upfront**, milestone the rest. Scope in writing; change orders for scope creep.

## Finding $50k+ clients

- **Subcontract to agencies** — they have the budgets and the clients; you supply the WebGL they can't. Fastest path to big-budget work.
- **Niche industries with money + weak digital** (luxury, real estate, watches, spirits, automotive, finance).
- **Inbound from awards + a flagship studio site.** Outbound: targeted, showing a concept piece for *their* brand.
- **Referrals** — every happy client is asked for one. This becomes the main channel at the top of the ladder.

## The build-before-pitch motion

Pick a business with money and a weak site → **generate a full spec site under their own brand** → deploy
it live → DM them the link. The prospect sees their own business, already done, before being asked for
anything. Almost nobody does this, because it only works if building is nearly free.

**It requires a re-skin engine.** `web-template-v1` is the model: one master build plus a per-brand JSON
(name, handle, copy, buttons, currency, terminology swaps), generated sites sharing the master's assets.
~5 minutes per site. **Build the engine early** — it is the weapon, not the sites.

### Rules paid for in real failures (2026-11-18)

- **A spec site sent to a prospect is a live sales asset with an indefinite lifetime.** Never host prospect
  sites in the repo that holds the portfolio, and **never delete one to free disk**. This has already
  happened once: a storage cleanup deleted 35 deployed spec sites and every DM already sent went to a 404.
  One Vercel project per prospect, or a dedicated prospect-sites repo. Check storage headroom *before* a
  bulk run.
- **Log the objection verbatim after every prospect conversation.** Sites built with no recorded objections
  means the funnel cannot be diagnosed, and the next hundred DMs repeat the same unknown mistake. At zero
  closes, one recorded objection beats ten more sites.
- **Check the goal's arithmetic before accepting it.** When a revenue target and a volume target are both
  stated, divide one by the other — they frequently describe businesses several times apart. State the
  contradiction rather than planning against both.
- **Interrogate the "cheap market" instinct.** Price is relative to local budgets — a fixed USD price can be
  expensive for SMBs in one market and unremarkable in another. The market that feels cheapest to operate
  in is often the hardest to sell into. Check before committing.
- **Check repo visibility before committing business data.** `api.github.com/repos/{owner}/{repo}` reports
  it. A public repo publishes revenue, pricing and prospect contact details. Business memory and CRM data
  belong in a private repo; skill files keep the rules, never the numbers.
- **Instrument before scaling.** Fixing conversion at low volume is cheap; scaling a 0% funnel costs
  everything and returns nothing.

## Client process (signals professionalism, justifies price)

Discovery → written proposal (tiers, scope, timeline) → 50% deposit → concept/art direction sign-off → build → perf/QA gate → launch + handover → ask for referral + testimonial → add to portfolio/case study.

Feed wins, prices, and objections into `web3d-evolve` so pricing and pitch improve every deal.
