"""
Shared settings for the 7-day launch pipeline. Copy this file to
config.py and edit the values below before running any of the generator
scripts. Everything else in this pipeline reads from config.py so you
only have to update links/dates/commission in one place.
"""

from datetime import date

# --- Product ---
PRODUCT_NAME = "Example Product"
PRICE_USD = 10

# --- Links ---
# Payhip "preview" link: lets people see sample pages before buying.
# Good for cold/awareness traffic that doesn't know you yet.
PREVIEW_LINK = "https://payhip.com/preview/REPLACE_WITH_YOUR_PREVIEW_LINK"

# Payhip direct checkout / buy link -- skips the product page and goes
# straight to cart/checkout for this item.
CHECKOUT_LINK = "https://payhip.com/buy?s=1&cart_links%5B%5D=REPLACE_WITH_YOUR_CHECKOUT_LINK"

# Your Payhip affiliate signup link/code, from your own dashboard:
# Marketing > Affiliates > enable the affiliate program for this
# product, set the commission % there too (match
# AFFILIATE_COMMISSION_PCT below), then copy the unique signup
# code/link shown there. You share THIS with people you want as
# affiliates -- once they sign up under it, Payhip generates their own
# personal tracked link automatically (format:
# payhip.com/b/yourproduct/{their-affiliate-key}). There is no way to
# pre-generate that per-affiliate link yourself before they've signed
# up, so this must be the signup code/link, not the product page.
# See references/payhip-affiliate-mechanics.md for the full mechanics.
AFFILIATE_INFO_LINK = "https://payhip.com/auth/register/REPLACE_WITH_YOUR_PAYHIP_AFFILIATE_SIGNUP_LINK"

# --- Launch window ---
# Single-bio-link platform (TikTok by default), 7 days starting this
# date (Mon by default). Change it or pass --start-date to
# generate_calendar.py.
LAUNCH_START_DATE = date(2026, 1, 5)

# On/after this day number (1-7), the "bio_link" column switches from
# the preview link to the checkout link -- awareness first, then close.
# See references/payhip-affiliate-mechanics.md for the reasoning.
CHECKOUT_SWITCH_DAY = 6

# --- Tracking / attribution ---
UTM_SOURCE = "tiktok"
UTM_MEDIUM = "organic_social"
UTM_CAMPAIGN = "REPLACE_WITH_YOUR_CAMPAIGN_SLUG"

# --- Affiliate program ---
AFFILIATE_COMMISSION_PCT = 40
