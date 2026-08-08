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

# Payhip direct checkout / buy link. Payhip product pages also serve as
# the checkout, so if you don't have a separate short "buy now" link,
# it's fine to point this at your product page URL instead (Payhip adds
# the buy button there automatically). Replace the placeholder below.
CHECKOUT_LINK = "https://payhip.com/b/REPLACE_WITH_YOUR_CHECKOUT_LINK"

# Where you send affiliates to sign up / grab their own tracked link.
# Payhip generates each affiliate's unique referral link automatically
# once they join your affiliate program (Store > Affiliates) -- you
# cannot hand-craft that per-affiliate link yourself. Point this at the
# page where they can apply / where you'll explain how it works.
AFFILIATE_INFO_LINK = "https://payhip.com/preview/NdVT8"

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
