#!/usr/bin/env python3
"""
Append UTM tracking params to the Payhip preview + checkout links for
every post in the content calendar.

Usage:
    python3 generate_utm_links.py [--calendar PATH] [--out PATH]

Reads output/content_calendar.csv (run generate_calendar.py first) and
writes output/content_calendar_with_links.csv with three extra columns:

    preview_link_utm  -- PREVIEW_LINK tagged for this exact post
    checkout_link_utm -- CHECKOUT_LINK tagged for this exact post
    bio_link_utm       -- whichever of the two you should actually put
                          in your TikTok bio that day (see below)

Why bio_link_utm exists: TikTok only gives you ONE live clickable link
in your bio at a time (no in-caption links). So for most of the week
you want the lower-friction PREVIEW_LINK in bio -- let cold viewers see
what they're buying before you ask for money. From
config.CHECKOUT_SWITCH_DAY onward (default: day 6, the weekend close),
it switches to CHECKOUT_LINK for the audience that's already watched
several days of content and is ready to buy.

If you use a link-in-bio tool (Linktree etc.) instead of a raw URL, you
can ignore bio_link_utm and just use preview_link_utm /
checkout_link_utm directly as the two buttons.

Every post gets a unique utm_content value so you can tell in Payhip/
your analytics exactly which video drove which click, e.g.:

    d1_myth_busting_willpower-isnt-broken

utm_source/medium/campaign come from config.py.
"""
import argparse
import csv
import os
import re
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

import config

IN_COLUMNS = ["day", "date", "pillar", "hook", "caption", "hashtags", "cta"]
OUT_COLUMNS = IN_COLUMNS + ["preview_link_utm", "checkout_link_utm", "bio_link_utm"]


def slugify(text: str, max_words: int = 6) -> str:
    words = re.sub(r"[^a-z0-9\s-]", "", text.lower()).split()
    return "-".join(words[:max_words])


def add_utm(url: str, *, source: str, medium: str, campaign: str, content: str) -> str:
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query))
    query.update(
        {
            "utm_source": source,
            "utm_medium": medium,
            "utm_campaign": campaign,
            "utm_content": content,
        }
    )
    return urlunsplit(parts._replace(query=urlencode(query)))


def build_rows(calendar_rows):
    out_rows = []
    for row in calendar_rows:
        day = int(row["day"])
        content_id = f"d{day}_{row['pillar']}_{slugify(row['hook'])}"

        preview_utm = add_utm(
            config.PREVIEW_LINK,
            source=config.UTM_SOURCE,
            medium=config.UTM_MEDIUM,
            campaign=config.UTM_CAMPAIGN,
            content=content_id,
        )
        checkout_utm = add_utm(
            config.CHECKOUT_LINK,
            source=config.UTM_SOURCE,
            medium=config.UTM_MEDIUM,
            campaign=config.UTM_CAMPAIGN,
            content=content_id,
        )
        bio_utm = checkout_utm if day >= config.CHECKOUT_SWITCH_DAY else preview_utm

        out_rows.append(
            {
                **row,
                "preview_link_utm": preview_utm,
                "checkout_link_utm": checkout_utm,
                "bio_link_utm": bio_utm,
            }
        )
    return out_rows


def main():
    here = os.path.dirname(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument("--calendar", default=os.path.join(here, "output", "content_calendar.csv"))
    parser.add_argument("--out", default=os.path.join(here, "output", "content_calendar_with_links.csv"))
    args = parser.parse_args()

    if not os.path.exists(args.calendar):
        raise SystemExit(f"{args.calendar} not found -- run generate_calendar.py first")

    with open(args.calendar, newline="", encoding="utf-8") as f:
        calendar_rows = list(csv.DictReader(f))

    out_rows = build_rows(calendar_rows)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_COLUMNS)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} rows with UTM links to {args.out}")
    if "REPLACE_WITH_YOUR_CHECKOUT_LINK" in config.CHECKOUT_LINK:
        print(
            "NOTE: config.CHECKOUT_LINK is still a placeholder -- edit config.py with your "
            "real Payhip checkout/product link, then re-run this script."
        )


if __name__ == "__main__":
    main()
