# The pipeline

Four stages, in order. Each reads the previous stage's output, so running
them out of order fails loudly (or produces nonsense).

```
content_bank.py + config.py
  |
  v
[ 1: generate_calendar.py ]        attaches real dates to the 21 hand-written posts
  |                                 -> output/content_calendar.csv
  v
[ 2: generate_utm_links.py ]       tags Payhip preview/checkout links per post,
  |                                 picks the daily bio link (preview -> checkout)
  |                                 -> output/content_calendar_with_links.csv
  v
[ 3: generate_tracking_sheet.py ]  one blank row per post, ready to log by hand
  |                                 -> output/tracking_sheet.csv
  v
[ 4: generate_affiliate_dms.py ]   personalized outreach DMs from an accounts list
                                    -> output/affiliate_dms.csv
```

Stage 4 only depends on `config.py`, not on the calendar — it can run any
time after `config.py` is filled in.

## Why this order

Stage 1 is the only stage that touches the actual copy (`content_bank.py`).
Everything after it is mechanical: attaching links, attaching tracking rows,
formatting DMs. Doing the copywriting first means stages 2-3 never need to
know anything about pillars or hooks — they just carry the `day` and
`pillar` columns through.

Stage 2 must run after stage 1 because UTM `utm_content` slugs are built
from each post's day, pillar, and hook. Stage 3 must run after stage 1 (it
reads the calendar CSV, not the UTM one — it doesn't need the links) for the
same reason: no calendar, no rows to track.

## What each stage owns

| Stage | Owns | Does not own |
|---|---|---|
| `generate_calendar.py` | Turning hand-written posts + a start date into dated rows | The copy itself — that's `content_bank.py`, written by hand |
| `generate_utm_links.py` | UTM tagging, and the daily preview-vs-checkout bio link decision | Which links exist — those come from `config.py` |
| `generate_tracking_sheet.py` | A blank row per post to log real numbers into | Merging with numbers already logged — re-running it overwrites |
| `generate_affiliate_dms.py` | Turning an account list into personalized pitches | Whether the affiliate program is actually enabled in Payhip — check the dashboard yourself |

## Re-running stages

Stages 1 and 2 are idempotent — re-run them any time `content_bank.py` or
`config.py` changes. Stage 3 (`generate_tracking_sheet.py`) is **not**: it
overwrites `output/tracking_sheet.csv` without merging, so once real numbers
are being logged, stop re-running it (or copy the data out first). Stage 4
is idempotent per accounts file — re-run it whenever the accounts list
changes.

## See also

`skills/launch-pipeline/SKILL.md` is the entry point for running this
pipeline inside Claude Code — it covers gathering inputs, writing the
content bank, and the Payhip link mechanics that stages 2 and 4 depend on.
