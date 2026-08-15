# Payhip link mechanics

Three different Payhip links get used in this pipeline, and mixing them up
either breaks tracking or sends people to a signup flow that doesn't work.
Check this before filling in `config.py`.

## The three links

**Preview link** (`PREVIEW_LINK`). Lets a visitor see sample pages before
buying. Use this for cold/awareness traffic — days 1-5 of the launch,
before the audience has any context for the product.

**Checkout link** (`CHECKOUT_LINK`). Skips the product page and goes
straight to cart/checkout. Use this for warm traffic — days 6-7, once
several days of content have built context and the ask shifts from
"here's what this is" to "here's how to get it."

**Affiliate signup link** (`AFFILIATE_INFO_LINK`). This is the one that
trips people up.

## The affiliate link is not what you think it is

On Payhip, affiliate links work in two steps, and only the seller can do
step one:

1. **You** (the seller) go to your Payhip dashboard → Marketing →
   Affiliates, enable the affiliate program for this specific product, and
   set the commission percentage there. Payhip then gives you a **signup
   link/code** for that program.
2. You share that signup link with people you want as affiliates. Only
   *after* someone signs up under it does Payhip generate **their own**
   personal tracked commission link, in the form
   `payhip.com/b/yourproduct/{their-affiliate-key}`.

There is no way to hand-craft a working per-affiliate link yourself ahead
of time — it does not exist until they sign up. So:

- `config.AFFILIATE_INFO_LINK` must be the **signup** link from step 1, not
  the product page and not a guessed per-affiliate URL.
- The commission % in `config.AFFILIATE_COMMISSION_PCT` must match what you
  actually set in the dashboard. If they're out of sync, the DMs promise a
  number Payhip won't honor.
- The affiliate program must actually be **enabled** for this product. A
  valid-looking signup link with the program still off will 404 or dead-end
  for anyone who clicks it.

`generate_affiliate_dms.py` checks for the literal placeholder string and
refuses to look correct until it's replaced, but it cannot verify the
program is actually enabled or that the commission % matches — confirm
both in the dashboard before sending anything.

## Why the bio link switches mid-week

Most short-form platforms allow exactly one live, clickable link in a
profile (no in-caption links). That forces a choice: send the whole week's
traffic to the same link, or vary it.

This pipeline varies it. `config.CHECKOUT_SWITCH_DAY` (default: day 6)
controls when `bio_link_utm` flips from the preview link to the checkout
link:

- **Days before the switch**: bio link is `PREVIEW_LINK`. Let cold viewers
  see what they're buying before asking for money — lower friction, more
  clicks, builds the case.
- **Switch day onward**: bio link is `CHECKOUT_LINK`. The audience has now
  seen several days of content; skip the product page and go straight to
  checkout for people who are already convinced.

If the platform supports multiple bio links (a link-in-bio tool, or a
platform without the single-link constraint), ignore `bio_link_utm`
entirely and use `preview_link_utm` / `checkout_link_utm` as two separate
buttons instead.
