# Writing the content bank

`content_bank.py` holds the 21 posts the whole pipeline is built from.
Everything downstream — the calendar, the UTM slugs, the tracking sheet
labels — is derived from these entries, so get the copy right before
running any script.

## The four pillars

Rotate across all four every day where possible (each day gets 3 posts,
so a day typically skips one pillar):

- **myth_busting** — names a common belief about the problem the product
  solves and corrects it. This is usually the strongest hook of the four.
- **relatable_story** — first-person or "POV" framing of the exact
  frustration the target buyer has felt. Specific, not generic.
- **quick_tip** — one small, concrete, usable piece of advice. Should be
  useful even to someone who never buys — that's what earns trust.
- **social_proof** — credibility (who built it, why it works, what people
  are saying), or a concrete fact about the product itself (price, page
  count, what's included).

## Per-post fields

```python
{
    "day": 1,                 # 1-7
    "pillar": "myth_busting",
    "hook": "...",             # on-screen/spoken opening line, under ~12 words
    "caption": "...",          # the caption posted under the video
    "hashtags": "#a #b #c",    # 3-5 tags, space-separated
    "cta": "...",              # explicit call to action
}
```

**Hook.** The first line has to work with no context — assume the viewer
has seen nothing else you've posted. Keep it under ~12 words. Lead with the
tension or the correction, not a setup.

**Caption.** One to three sentences that pay off the hook. State the real
mechanism or claim, don't just re-hype the hook.

**Hashtags.** 3-5, space-separated. Mix broad (audience-sized) and specific
(problem-sized) tags. More than 5 reads as spammy; fewer under-targets.

**CTA.** Vary these across the week — "link in bio," "comment X and I'll
send it," "link in bio for the full breakdown." Repeating the exact same
CTA every post reads as a bot.

## The one rule that matters most

**Only claim what the product can actually back up.**

Before writing a single post, get straight on what the product actually
is: does it have real rules and structure, or is it genuinely flexible?
Does it target weight loss, habit change, something else? Marketing it as
looser, vaguer, or more universal than it actually is will draw exactly the
audience most likely to feel misled and churn or refund.

Do not invent:
- Urgency or a countdown that doesn't exist (an evergreen product isn't a
  "cart closes Friday" launch)
- Discounts or price changes that aren't real
- Claims of endorsement, press coverage, or specific results you can't
  source

Lead with what's actually true and defensible. A specific, honest mechanism
("this schedules the thing you'd otherwise binge on, instead of banning
it") beats a vague, bigger promise every time — and it's the version that
doesn't generate refund requests.

## Platform tuning

The defaults (hook length, 3-5 hashtags, CTA style) are tuned for TikTok.
For Instagram Reels or YouTube Shorts, the same structure works, but:
- Hashtag conventions differ (IG tolerates more tags; YouTube Shorts
  barely uses them)
- "Comment X and I'll DM you" CTAs work on IG/TikTok, not YouTube
- Caption length limits and link-in-bio constraints vary — check
  `references/payhip-affiliate-mechanics.md` for how the bio-link switch
  logic assumes a single-link platform
