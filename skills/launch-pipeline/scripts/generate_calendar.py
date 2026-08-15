#!/usr/bin/env python3
"""
Generate the 7-day / 21-post content calendar as a CSV.

Usage:
    python3 generate_calendar.py [--start-date YYYY-MM-DD] [--out PATH]

Reads the hand-written posts in content_bank.py, attaches a real
calendar date to each day using --start-date (defaults to
config.LAUNCH_START_DATE), and writes:

    day, date, pillar, hook, caption, hashtags, cta

to output/content_calendar.csv (or --out).
"""
import argparse
import csv
import os
from datetime import timedelta, date as date_cls

import config
from content_bank import POSTS

COLUMNS = ["day", "date", "pillar", "hook", "caption", "hashtags", "cta"]


def build_rows(start_date: date_cls):
    rows = []
    for post in POSTS:
        post_date = start_date + timedelta(days=post["day"] - 1)
        rows.append(
            {
                "day": post["day"],
                "date": post_date.isoformat(),
                "pillar": post["pillar"],
                "hook": post["hook"],
                "caption": post["caption"],
                "hashtags": post["hashtags"],
                "cta": post["cta"],
            }
        )
    rows.sort(key=lambda r: r["day"])
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", default=None, help="YYYY-MM-DD, defaults to config.LAUNCH_START_DATE")
    parser.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "output", "content_calendar.csv"))
    args = parser.parse_args()

    start_date = (
        date_cls.fromisoformat(args.start_date) if args.start_date else config.LAUNCH_START_DATE
    )

    rows = build_rows(start_date)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} posts to {args.out}")


if __name__ == "__main__":
    main()
