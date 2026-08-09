#!/usr/bin/env python3
"""
Turn a pasted list of niche accounts into personalized affiliate
outreach DMs.

Usage:
    python3 generate_affiliate_dms.py --accounts accounts.txt [--out PATH]

Input file format (see accounts_example.txt): one account per line,

    @handle | short note on their niche/content (optional)

Blank lines and lines starting with # are ignored. The note is
optional -- without it, the DM just says "your page" instead of
referencing a specific niche.

Output: output/affiliate_dms.csv with columns
    handle, niche_note, dm_pitch, affiliate_info_link

IMPORTANT -- about the "affiliate link": on Payhip, YOU (the seller)
generate a unique affiliate signup code from your dashboard (Marketing
> Affiliates), and share THAT with people you want as affiliates. Only
after someone signs up under your code does Payhip generate their own
personal tracked commission link -- you cannot pre-generate that
per-affiliate link yourself. So affiliate_info_link here must be your
signup code/link, not the product page. Set it in
config.AFFILIATE_INFO_LINK once you've enabled the affiliate program
for this product in your Payhip dashboard.

Commission rate comes from config.AFFILIATE_COMMISSION_PCT.
"""
import argparse
import csv
import os

import config

TEMPLATES = [
    (
        "Hey! Been seeing {niche_clause} and thought you'd vibe with something I just "
        "launched -- {product_name} (${price}), a simple framework for people done with "
        "restrict-binge dieting. I'm offering {commission}% commission on every sale "
        "through your own affiliate link (that's ${commission_amount:.0f}/sale on a "
        "${price} product), no cost to you to promote. Takes 2 min to set up an "
        "affiliate account here: {affiliate_link}. Want me to send a couple of "
        "ready-to-post clips too?"
    ),
    (
        "Hi -- quick one. I run {product_name}, a ${price} guide for people stuck in "
        "the diet-binge cycle. Looking for a few accounts like yours to partner with as "
        "affiliates -- {commission}% commission per sale, your own tracked link via "
        "Payhip: {affiliate_link}. Takes 2 minutes to join, no upfront cost. Let me "
        "know if you want the details or a sample post to work from."
    ),
    (
        "Hey! Loved {niche_clause} -- mind if I send over a quick collab idea? I've got "
        "a ${price} guide, {product_name}, that fits your audience, and I'm running "
        "{commission}% affiliate commission on it through Payhip. Free to join here: "
        "{affiliate_link}. No pressure either way!"
    ),
]


def parse_accounts(path):
    accounts = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "|" in line:
                handle, note = line.split("|", 1)
                handle, note = handle.strip(), note.strip()
            else:
                handle, note = line.strip(), ""
            accounts.append((handle, note))
    return accounts


def niche_clause(note: str) -> str:
    return f"your {note} content" if note else "your page"


def build_rows(accounts):
    rows = []
    commission = config.AFFILIATE_COMMISSION_PCT
    commission_amount = config.PRICE_USD * commission / 100
    for i, (handle, note) in enumerate(accounts):
        template = TEMPLATES[i % len(TEMPLATES)]
        pitch = template.format(
            niche_clause=niche_clause(note),
            product_name=config.PRODUCT_NAME,
            price=config.PRICE_USD,
            commission=commission,
            commission_amount=commission_amount,
            affiliate_link=config.AFFILIATE_INFO_LINK,
        )
        rows.append(
            {
                "handle": handle,
                "niche_note": note,
                "dm_pitch": pitch,
                "affiliate_info_link": config.AFFILIATE_INFO_LINK,
            }
        )
    return rows


def main():
    here = os.path.dirname(__file__)
    parser = argparse.ArgumentParser()
    parser.add_argument("--accounts", default=os.path.join(here, "accounts_example.txt"))
    parser.add_argument("--out", default=os.path.join(here, "output", "affiliate_dms.csv"))
    args = parser.parse_args()

    if not os.path.exists(args.accounts):
        raise SystemExit(f"{args.accounts} not found")

    accounts = parse_accounts(args.accounts)
    if not accounts:
        raise SystemExit(f"No accounts found in {args.accounts}")

    rows = build_rows(accounts)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["handle", "niche_note", "dm_pitch", "affiliate_info_link"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} personalized DMs to {args.out}")
    if "REPLACE_WITH_YOUR_PAYHIP_AFFILIATE_SIGNUP_LINK" in config.AFFILIATE_INFO_LINK:
        print(
            "NOTE: config.AFFILIATE_INFO_LINK is still a placeholder -- go to your Payhip "
            "dashboard > Marketing > Affiliates, enable the affiliate program for this "
            "product, set the commission % to match AFFILIATE_COMMISSION_PCT, and paste the "
            "signup code/link shown there into config.py. Then re-run this script -- do not "
            "send these DMs until that's fixed, the current link does not let anyone sign up "
            "as an affiliate."
        )


if __name__ == "__main__":
    main()
