"""
Template for the content bank: 21 hand-written posts (3/day x 7 days),
rotating across 4 pillars -- myth_busting, relatable_story, quick_tip,
social_proof.

Copy this file to content_bank.py and replace POSTS with the real
posts for this launch. See ../references/content-bank-guide.md before
writing copy -- it covers hook length, hashtag count, pillar
definitions, and the rule that matters most: only claim what the
product can actually back up.

Each entry:
    day      -- 1-7 (Mon-Sun of launch week)
    pillar   -- myth_busting | relatable_story | quick_tip | social_proof
    hook     -- on-screen/spoken opening line (keep under ~12 words)
    caption  -- the caption posted under the video
    hashtags -- 3-5 tags, space-separated string
    cta      -- the explicit call to action for this post

Only day 1 is filled in below, one post per pillar, as a worked
example -- fill in the remaining 18 posts (days 2-7) the same way.
"""

POSTS = [
    {
        "day": 1,
        "pillar": "myth_busting",
        "hook": "REPLACE: name a common wrong belief about the problem.",
        "caption": (
            "REPLACE: correct the belief in 1-3 sentences, using the real "
            "mechanism the product relies on -- not a bigger, vaguer promise."
        ),
        "hashtags": "#replace #with #real #tags",
        "cta": "Comment WORD and I'll send you the link",
    },
    {
        "day": 1,
        "pillar": "relatable_story",
        "hook": "REPLACE: POV framing of the exact frustration the buyer feels.",
        "caption": (
            "REPLACE: first-person, specific -- not generic. What changed, "
            "and why it wasn't what they expected."
        ),
        "hashtags": "#replace #with #real #tags",
        "cta": "Link in bio if you're curious how it works",
    },
    {
        "day": 1,
        "pillar": "quick_tip",
        "hook": "REPLACE: one small, concrete, usable piece of advice.",
        "caption": (
            "REPLACE: make it useful even to someone who never buys -- "
            "that's what earns trust."
        ),
        "hashtags": "#replace #with #real #tags",
        "cta": "Link in bio for the full breakdown",
    },
    # ---------- Day 2 (Tue) ----------
    # {"day": 2, "pillar": "myth_busting", ...},
    # {"day": 2, "pillar": "quick_tip", ...},
    # {"day": 2, "pillar": "social_proof", ...},
    # ---------- Day 3 (Wed) ----------
    # ...
    # ---------- Day 4 (Thu) ----------
    # ...
    # ---------- Day 5 (Fri) ----------
    # ...
    # ---------- Day 6 (Sat) ----------
    # ...
    # ---------- Day 7 (Sun) ----------
    # ...
]
