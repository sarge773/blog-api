---
name: launch-pipeline
version: 1.0.0
description: |
  Build a 7-day short-form-video launch pipeline for a paid digital product:
  a hand-written content calendar (3 posts/day across 4 pillars), UTM-tagged
  tracking links for a Payhip preview/checkout pair, a daily results tracking
  sheet, and personalized affiliate outreach DMs. Use when a user wants to
  plan or launch a TikTok (or similar) product launch, needs a content
  calendar with hooks/captions/hashtags/CTAs, wants UTM tracking on Payhip
  links, or wants to recruit affiliates for a paid product via DM.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - AskUserQuestion
---

# Launch pipeline: 7-day product launch on Payhip

You are running a short, evergreen product launch: one paid digital product,
one platform, seven days, three posts a day. Stdlib-only Python scripts do
the mechanical generation (dates, UTM params, CSV plumbing); you do the
positioning and copywriting work they depend on.

## Scope note

This pipeline assumes a **Payhip** product (preview link + checkout link +
affiliate program) and **one platform with a single bio link** (TikTok is
the default; the mechanics apply to any platform with the same
one-link-in-bio constraint). If the user's product lives elsewhere or the
platform allows multiple links, adapt `config.py` and skip the parts of
`references/payhip-affiliate-mechanics.md` that don't apply.

## Your task

### 1. Gather the inputs

Ask the user (or read from context) for:

- Product name and price
- What the product actually claims/delivers — you need this to write
  defensible copy, not just marketable copy (see step 2)
- Payhip preview link and checkout link
- Whether an affiliate program is enabled for this product, its commission
  %, and the affiliate **signup** link (not a per-affiliate link — see
  `references/payhip-affiliate-mechanics.md`, this trips people up)
- Launch start date (defaults to next Monday if not given)
- Which day (1-7) the bio link should switch from preview to checkout
  (default: day 6 — five days of awareness content before asking for the
  sale)

### 2. Write the content bank

Write 21 posts (3/day × 7 days) rotating across four pillars:
`myth_busting`, `relatable_story`, `quick_tip`, `social_proof`.

Read `references/content-bank-guide.md` before writing copy — it covers
hook length, hashtag count, pillar definitions, and the single rule that
matters most: **only make claims the product can actually back up.** Do not
invent urgency, discounts, or scarcity that isn't real. If the guide has
real rules or a real structure, lead with those; don't market it as looser
or vaguer than it is.

Put the finished posts in `content_bank.py` (copy the shape from
`scripts/content_bank.example.py`).

### 3. Set up the working directory

Copy `scripts/*.py` and `scripts/accounts_example.txt` into wherever the
user wants to run this launch from (a new `launch-pipeline/` directory is
the convention this pipeline was built around). Then:

- Copy `config.example.py` → `config.py` and fill in the real values from
  step 1.
- Copy `content_bank.example.py` → `content_bank.py` and replace the
  example posts with the real ones from step 2.

### 4. Run the pipeline in order

```bash
python3 generate_calendar.py          # -> output/content_calendar.csv
python3 generate_utm_links.py         # -> output/content_calendar_with_links.csv
python3 generate_tracking_sheet.py    # -> output/tracking_sheet.csv
python3 generate_affiliate_dms.py --accounts accounts.txt   # -> output/affiliate_dms.csv
```

Each script reads the previous stage's CSV — run them in this order. See
`docs/PIPELINE.md` (repo root) for what each stage owns and why the order
matters.

### 5. Before handing off affiliate DMs

`generate_affiliate_dms.py` prints a warning and refuses to look correct
if `config.AFFILIATE_INFO_LINK` is still a placeholder. Do not tell the
user to send the generated DMs until they've confirmed in their Payhip
dashboard that the affiliate program is actually enabled for this product
— see `references/payhip-affiliate-mechanics.md` for exactly what to check.

## Re-running scripts

`generate_calendar.py` and `generate_utm_links.py` are safe to re-run after
editing `content_bank.py` or `config.py`. `generate_tracking_sheet.py`
**overwrites** its output and does not merge with data already logged —
warn the user before re-running it once they've started filling in real
numbers.

## Output format

Tell the user what was generated and where (the four CSVs under `output/`),
and flag any placeholder values in `config.py` that still need real links
before anything goes out.
