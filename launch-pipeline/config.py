"""
Shared settings for the Anything Meal Method launch pipeline.

Edit the values below before running any of the generator scripts.
Everything else in this pipeline reads from here so you only have to
update links/dates/commission in one place.
"""

from datetime import date

# --- Product ---
PRODUCT_NAME = "The Anything Meal Method Guide"
PRICE_USD = 10

# --- Links ---
# Payhip "preview" link: lets people see sample pages before buying.
# Good for cold/awareness traffic that doesn't know you yet.
PREVIEW_LINK = "https://payhip.com/preview/NdVT8"

# Payhip direct checkout / buy link -- skips the product page and goes
# straight to cart/checkout for this item.
CHECKOUT_LINK = "https://payhip.com/buy?s=1&cart_links%5B%5D=NdVT8&qty%5BNdVT8%5D=1"

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
AFFILIATE_INFO_LINK = "REPLACE_WITH_YOUR_PAYHIP_AFFILIATE_SIGNUP_LINK"

# --- Launch window ---
# TikTok only content, 7 days starting this date (Mon by default).
LAUNCH_START_DATE = date(2026, 8, 10)

# On/after this day number (1-7), the "bio_link" column switches from
# the preview link to the checkout link -- awareness first, then close.
# See README for the reasoning.
CHECKOUT_SWITCH_DAY = 6

# --- Tracking / attribution ---
UTM_SOURCE = "tiktok"
UTM_MEDIUM = "organic_social"
UTM_CAMPAIGN = "anything_meal_7day_launch"

# --- Affiliate program ---
AFFILIATE_COMMISSION_PCT = 40
