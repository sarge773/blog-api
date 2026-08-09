# Anything Meal Method — 7-day launch pipeline

Stdlib-only Python scripts (no dependencies to install). Run from this
directory.

## Before you run anything

Edit `config.py`:

- `CHECKOUT_LINK` — done, set to your real Payhip checkout link.
- `AFFILIATE_INFO_LINK` — done, set to your Payhip affiliate signup link.
  Just confirm you've actually enabled the affiliate program for this
  product in Payhip (Marketing → Affiliates) and that the commission % set
  there matches `AFFILIATE_COMMISSION_PCT` (40%) — the signup link alone
  doesn't turn the program on if you haven't flipped that switch.
- `LAUNCH_START_DATE` defaults to Mon 2026-08-10 — change it or pass
  `--start-date` to `generate_calendar.py`.

## Positioning decision baked into the content

The guide itself has real food rules, a weight-loss goal, and
non-negotiable structured days — it is not clinical "intuitive eating,"
and marketing it that way risks pushback from that exact audience. The
content bank instead leads with what's actually true and defensible:
**this ends the restrict-binge cycle by scheduling indulgence instead of
banning it** (reactance psychology — Fri/Sat/Sun dinners are planned, not
"earned" or forbidden). No copy here claims "no rules," "intuitive
eating," or invents launch-week urgency/discounts that don't exist. If
you add a real limited-time bonus later, edit the relevant rows in
`content_bank.py`.

Platform: TikTok only (hook length, hashtag count 3–5, and CTA style are
tuned for that — rework `content_bank.py` if you also want IG/YouTube
Shorts variants).

## Run order

```bash
python3 generate_calendar.py          # -> output/content_calendar.csv
python3 generate_utm_links.py         # -> output/content_calendar_with_links.csv
python3 generate_tracking_sheet.py    # -> output/tracking_sheet.csv
python3 generate_affiliate_dms.py --accounts accounts_example.txt   # -> output/affiliate_dms.csv
```

### 1. `generate_calendar.py`
21 hand-written posts (3/day × 7 days) across 4 pillars (myth_busting,
relatable_story, quick_tip, social_proof), pulled from
`content_bank.py`. Columns: `day, date, pillar, hook, caption, hashtags,
cta`. The content itself lives in `content_bank.py` — edit it directly to
change copy; re-run this script to regenerate the CSV with new dates.

### 2. `generate_utm_links.py`
Reads the calendar CSV and adds three columns: `preview_link_utm`,
`checkout_link_utm`, `bio_link_utm`. Every post gets a unique
`utm_content` (e.g. `d1_myth_busting_willpower-isnt-broken`) so you can
see in Payhip/analytics exactly which video drove which click.

**`bio_link_utm` logic:** TikTok only allows one live link in your bio.
Days 1–5 use the preview link (let cold viewers see the guide before
asking for money); from `config.CHECKOUT_SWITCH_DAY` (default: day 6)
it switches to the checkout link for the audience that's already seen
several days of content. Change the switch day, or ignore
`bio_link_utm` entirely and use the two separate columns if you're on a
link-in-bio tool that supports multiple buttons.

### 3. `generate_tracking_sheet.py`
One row per scheduled post: `date, day, pillar, post, views,
link_clicks, sales, notes`. Open in Excel/Numbers/Sheets and fill in
`views`/`link_clicks` from TikTok analytics and your UTM click data,
and `sales` from your Payhip dashboard filtered by date, once a day.

**Re-running this script overwrites the file** — it doesn't merge with
data you've already logged. Once you start logging real numbers, stop
re-running it (or copy your data out first).

### 4. `generate_affiliate_dms.py`
Paste your list of niche accounts into a text file (see
`accounts_example.txt` for the format: `@handle | short niche note`,
note is optional), then:

```bash
python3 generate_affiliate_dms.py --accounts your_accounts.txt
```

Outputs `handle, niche_note, dm_pitch, affiliate_info_link` — 3
rotating DM templates so the outreach doesn't read as obviously
copy-pasted, personalized with each account's niche note where given,
offering `config.AFFILIATE_COMMISSION_PCT`% (default 40%).

**Read this before sending:** on Payhip, *you* generate a unique
affiliate signup code from your dashboard (Marketing → Affiliates) and
share that with people you want as affiliates. Only after someone signs
up under your code does Payhip generate their own personal tracked
commission link (format: `payhip.com/b/yourproduct/{their-affiliate-key}`)
— you can't hand-craft a working per-affiliate link yourself ahead of
time. So `affiliate_info_link` in the output must be your signup
code/link, not the product page. The script prints a warning and refuses
to look correct until you've set `config.AFFILIATE_INFO_LINK` to that
real signup link — don't send these DMs while it's still the
placeholder.

## Files

```
config.py                        shared settings — edit this first
content_bank.py                  the actual 21 posts (edit content here)
generate_calendar.py
generate_utm_links.py
generate_tracking_sheet.py
generate_affiliate_dms.py
accounts_example.txt             sample input for the DM generator
sales_page_copy.md               Payhip sales page description (short blurb + full page + FAQ)
output/                          generated CSVs, committed so you have them immediately — re-run the
                                  scripts and re-commit after you edit config.py/content_bank.py
```
