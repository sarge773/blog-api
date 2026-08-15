#!/usr/bin/env python3
"""
Generate a blank daily results tracking sheet, pre-filled with one row
per scheduled post so you just fill in numbers as you go.

Usage:
    python3 generate_tracking_sheet.py [--calendar PATH] [--out PATH]

Reads output/content_calendar.csv (run generate_calendar.py first) and
writes output/tracking_sheet.csv with:

    date, day, pillar, post, views, link_clicks, sales, notes

"post" is a short human-readable label (day + pillar + hook) so you can
tell rows apart at a glance without re-opening the calendar CSV.
views/link_clicks/sales/notes are left blank -- log them by hand once a
day (TikTok analytics for views/clicks on that video, Payhip dashboard
or your UTM-tagged link's click count for link_clicks, Payhip sales
dashboard filtered by date for sales).

Re-running this script overwrites the sheet, so once you start logging
real numbers, either stop re-running it or move your data elsewhere
first -- it does not merge with existing data.
"""
import argparse
import csv
import os

COLUMNS = ["date", "day", "pillar", "post", "views", "link_clicks", "sales", "notes"]


def build_rows(calendar_rows):
    rows = []
    for row in calendar_rows:
        hook_short = row["hook"] if len(row["hook"]) <= 60 else row["hook"][:57] + "..."
        rows.append(
            {
                "date": row["date"],
                "day": row["day"],
                "pillar": row["pillar"],
                "post": f'D{row["day"]} {row["pillar"]}: {hook_short}',
                "views": "",
                "link_clicks": "",
                "sales": "",
                "notes": "",
            }
        )
    return rows


def main():
    here = os.path.dirname(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument("--calendar", default=os.path.join(here, "output", "content_calendar.csv"))
    parser.add_argument("--out", default=os.path.join(here, "output", "tracking_sheet.csv"))
    args = parser.parse_args()

    if not os.path.exists(args.calendar):
        raise SystemExit(f"{args.calendar} not found -- run generate_calendar.py first")

    with open(args.calendar, newline="", encoding="utf-8") as f:
        calendar_rows = list(csv.DictReader(f))

    rows = build_rows(calendar_rows)

    if os.path.exists(args.out):
        print(f"WARNING: {args.out} already exists and will be overwritten. "
              f"If it has logged data in it, back it up first (Ctrl+C now to cancel).")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {args.out}")


if __name__ == "__main__":
    main()
