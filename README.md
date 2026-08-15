# launch-pipeline

A 7-day short-form-video launch pipeline for a paid digital product on
Payhip, packaged as a [Claude Code Skill](https://code.claude.com/docs/en/skills).

Stdlib-only Python does the mechanical part — dates, UTM params, CSV
plumbing. The skill handles the part scripts can't: gathering the real
product details, writing 21 posts that make only defensible claims, and
knowing the Payhip link mechanics well enough not to send an affiliate DM
that points at a link nobody can sign up under.

## What is in here

```
skills/
  launch-pipeline/
    SKILL.md                       entry point: gather inputs, write copy, run the scripts
    references/
      content-bank-guide.md        pillars, hook/caption/hashtag/CTA conventions, the one rule that matters
      payhip-affiliate-mechanics.md preview vs checkout vs affiliate-signup links, the bio-link switch
    scripts/
      config.example.py            settings template -- copy to config.py per launch
      content_bank.example.py      content template -- copy to content_bank.py per launch
      generate_calendar.py         stage 1: hand-written posts + start date -> dated CSV
      generate_utm_links.py        stage 2: UTM tags + daily bio-link choice
      generate_tracking_sheet.py   stage 3: blank results sheet, one row per post
      generate_affiliate_dms.py    stage 4: accounts list -> personalized outreach DMs
      accounts_example.txt         sample input for stage 4
docs/
  PIPELINE.md                      how the four stages chain, and what each one owns
launch-pipeline/                   a completed real-world instance of this skill's output
                                    (a live product launch, real links) -- see its own README.md
```

## Why a skill, not just scripts

The scripts alone can't decide what to write. The hard part of a launch
like this is writing 21 posts that are honest about what the product
actually does — no invented urgency, no vaguer promise than the product
delivers — and getting the Payhip affiliate link mechanics right on the
first try (the signup link and a per-affiliate link are not the same
thing, and mixing them up sends outreach to a dead end). `SKILL.md`
carries that judgment; the scripts carry the plumbing.

## Install

```bash
./install.sh
```

This symlinks `skills/launch-pipeline` into `~/.claude/skills/`, so updates
land with a `git pull`. Pass `--copy` for an independent copy, `--project`
to install at the project level instead of user level.

To install manually, copy `skills/launch-pipeline` into `~/.claude/skills/`
(user-level) or `.claude/skills/` (project-level).

## Use

In Claude Code, the skill triggers on intent:

```
plan a 7-day TikTok launch for this product
build the content calendar and UTM links for my Payhip launch
write affiliate outreach DMs for this product
```

The skill will ask for the product details, Payhip links, and launch date
it needs, help write the content bank, then run the four generator scripts
in order. See `docs/PIPELINE.md` for what each stage does and why the
order matters.

### Scripts are templates, not a shared instance

`config.py` and `content_bank.py` hold one specific launch's real data
(checkout links, affiliate links, the actual 21 posts). Don't edit the
`.example.py` files in place for a real launch — copy them into a working
directory per launch instead, the way `launch-pipeline/` in this repo does
for its own product.

## Honest limits

- **This assumes Payhip and a single-bio-link platform.** Adapt
  `config.py` and skip the platform-specific parts of
  `references/payhip-affiliate-mechanics.md` if either doesn't apply.
- **The scripts don't validate copy quality or claims.** They validate
  that a placeholder link wasn't left in `config.py` — nothing checks
  whether the content bank's claims are actually defensible. That's the
  skill's job, not the scripts'.
- **`generate_tracking_sheet.py` overwrites its output.** It does not
  merge with numbers already logged by hand.
