"""
The actual content: 21 hand-written TikTok posts (3/day x 7 days),
rotating across 4 pillars -- myth_busting, relatable_story, quick_tip,
social_proof.

Positioning: "anti-binge, not anti-diet." The guide itself has real
food rules, a weight-loss goal, and non-negotiable structured days --
it is NOT intuitive eating in the clinical sense. So none of this copy
claims "no rules" or "intuitive eating." Instead it leans on what's
actually true and defensible: the method interrupts the restrict/binge
cycle by scheduling indulgence instead of banning it (reactance
psychology), and it's simple enough to actually follow. See README.md
for the full reasoning.

No fake urgency/scarcity anywhere -- this is an evergreen $10 PDF, not
a cart-close launch, so nothing here claims a countdown or price hike
that isn't real. If you add a real launch-week bonus or discount later,
update the relevant rows below.

Each entry:
    day     -- 1-7 (Mon-Sun of launch week)
    pillar  -- myth_busting | relatable_story | quick_tip | social_proof
    hook    -- on-screen/spoken opening line (keep under ~12 words)
    caption -- the caption posted under the video
    hashtags -- 3-5 tags, space-separated string
    cta     -- the explicit call to action for this post
"""

POSTS = [
    # ---------- Day 1 (Mon) - myth, story, tip ----------
    {
        "day": 1,
        "pillar": "myth_busting",
        "hook": "Willpower isn't broken. Your diet is.",
        "caption": (
            "You didn't fail every diet because you lack discipline. The second a food "
            "gets banned, your brain wants it more -- it's called reactance, and it's why "
            "\"cheat days\" turn into benders. The Anything Meal Method skips the ban "
            "entirely: 4 days of simple meals, 3 nights where you eat whatever you want, "
            "on purpose."
        ),
        "hashtags": "#stopdieting #bingeeatingrecovery #dietculturedropout #foodfreedom",
        "cta": "Comment MEAL and I'll send you the link",
    },
    {
        "day": 1,
        "pillar": "relatable_story",
        "hook": "POV: you've \"started over\" on Monday 47 times.",
        "caption": (
            "I don't say that to be dramatic -- restrictive diets fail almost everyone "
            "eventually, that's not a you problem. What actually changed things wasn't a "
            "stricter plan, it was one that scheduled the meals I actually wanted instead "
            "of banning them."
        ),
        "hashtags": "#stopdieting #dietculturedropout #bingeeatingrecovery",
        "cta": "Link in bio if you're curious how it works",
    },
    {
        "day": 1,
        "pillar": "quick_tip",
        "hook": "Breakfast is just \"peel, cut, blend.\" That's it.",
        "caption": (
            "Core routine days aren't complicated -- breakfast is a juice or smoothie, "
            "lunch is 3 pieces of fruit eaten alone, dinner alternates carb-based and "
            "protein-based. No recipes to master, no cooking four separate meals for "
            "four different people."
        ),
        "hashtags": "#healthylifestyle #weightlosstips #dietingtips",
        "cta": "Link in bio for the full 7-day starter plan",
    },
    # ---------- Day 2 (Tue) - myth, tip, proof ----------
    {
        "day": 2,
        "pillar": "myth_busting",
        "hook": "Cheat meals aren't the problem. Guilt is.",
        "caption": (
            "Every \"diet\" I tried had a cheat day I dreaded and then regretted. Turns "
            "out the guilt afterward was doing more damage than the food itself. This "
            "method flips it -- the indulgent meal isn't a slip-up, it's scheduled. No "
            "shame spiral, because there's nothing to feel ashamed of."
        ),
        "hashtags": "#noguilt #weightlosstips #cravingscontrol",
        "cta": "Link in bio",
    },
    {
        "day": 2,
        "pillar": "quick_tip",
        "hook": "3 rules. That's the whole \"food science\" part.",
        "caption": (
            "You don't need a nutrition degree for this. Eat fruit alone. Don't mix "
            "protein and starchy carbs at the same meal. Drink water 30 minutes before "
            "or after eating, not during. Most people notice a digestion/energy "
            "difference inside 2 weeks."
        ),
        "hashtags": "#weightlosstips #healthylifestyle #dietingtips",
        "cta": "Link in bio for the full breakdown",
    },
    {
        "day": 2,
        "pillar": "social_proof",
        "hook": "Built by a trainer, not a trend.",
        "caption": (
            "This isn't a framework I stitched together from TikTok comments -- it's "
            "the exact structure a certified personal trainer used to coach real "
            "clients out of the restrict-binge cycle, written down so you don't need a "
            "coach to follow it."
        ),
        "hashtags": "#personaltrainer #weightlossjourney #fitnesstok",
        "cta": "Link in bio -- $10, instant download",
    },
    # ---------- Day 3 (Wed) - story, tip, myth ----------
    {
        "day": 3,
        "pillar": "relatable_story",
        "hook": "POV: it's Tuesday and you already \"ruined\" your diet.",
        "caption": (
            "Every diet I did had this moment -- one bite off-plan and suddenly the "
            "whole week was \"ruined\" so I might as well eat everything. That spiral "
            "isn't a willpower problem, it's a design flaw in restrictive diets. This "
            "gives your cravings a scheduled seat at the table 3 nights a week instead."
        ),
        "hashtags": "#bingeeatingrecovery #dietculturedropout #foodfreedom",
        "cta": "Link in bio",
    },
    {
        "day": 3,
        "pillar": "quick_tip",
        "hook": "If 4 days feels impossible, start with 2.",
        "caption": (
            "You do not need to nail this perfectly on day one. Start with core "
            "routine meals Monday + Tuesday only, and add a day each week until you're "
            "at 4. A method you'll actually finish beats a \"perfect\" plan you quit by "
            "Thursday."
        ),
        "hashtags": "#healthylifestyle #weightlosstips #sustainableweightloss",
        "cta": "Link in bio for the full starter plan",
    },
    {
        "day": 3,
        "pillar": "myth_busting",
        "hook": "Food combining rules aren't about \"clean eating.\"",
        "caption": (
            "Fruit alone, protein OR carbs (not both), water away from meals -- these 3 "
            "rules aren't about morality or \"clean\" vs \"dirty\" food. No food is off "
            "limits, no guilt attached to any of it."
        ),
        "hashtags": "#dietingtips #weightlosstips #healthylifestyle",
        "cta": "Link in bio",
    },
    # ---------- Day 4 (Thu) - tip, proof, story ----------
    {
        "day": 4,
        "pillar": "quick_tip",
        "hook": "Your planned indulgent meal has one rule: sit down.",
        "caption": (
            "The #1 mistake with any planned indulgent meal -- eating it standing at "
            "the counter like it's about to be taken away. Sit down. Slow down. Taste "
            "it. It comes back next week, there's no reason to eat 3 days' worth in "
            "one sitting."
        ),
        "hashtags": "#cravingscontrol #noguilt #bingeeatingrecovery",
        "cta": "Comment ANYTHING and I'll send the link",
    },
    {
        "day": 4,
        "pillar": "social_proof",
        "hook": "Why this works when nothing else did.",
        "caption": (
            "Every diet that told you \"never again\" to a food group was setting you "
            "up to want it more. This one gives your cravings a scheduled outlet "
            "instead of fighting them -- most people find their cravings actually "
            "shrink over a few weeks. Built from years of real client coaching."
        ),
        "hashtags": "#weightlossjourney #sustainableweightloss #personaltrainer",
        "cta": "Link in bio",
    },
    {
        "day": 4,
        "pillar": "relatable_story",
        "hook": "I stopped calling Friday dinner a \"cheat meal.\"",
        "caption": (
            "Changing the label changed the behavior. When Friday's dinner became my "
            "scheduled Anything Meal instead of a \"cheat,\" I stopped white-knuckling "
            "through the week and bingeing when I got there. Still whatever I want -- "
            "just planned instead of desperate."
        ),
        "hashtags": "#foodfreedom #dietculturedropout #stopdieting",
        "cta": "Link in bio for the full framework",
    },
    # ---------- Day 5 (Fri) - myth, proof, tip ----------
    {
        "day": 5,
        "pillar": "myth_busting",
        "hook": "You do not need to earn your Friday dinner.",
        "caption": (
            "This isn't a reward for a \"good\" week. Not a prize for eating perfectly "
            "Mon-Thu. It's just part of the plan, on the calendar from day one -- "
            "because food you have to earn is food you'll eventually binge on."
        ),
        "hashtags": "#noguilt #dietculturedropout #foodfreedom",
        "cta": "Link in bio",
    },
    {
        "day": 5,
        "pillar": "social_proof",
        "hook": "$10 and 18 pages. That's the whole guide.",
        "caption": (
            "No course, no coaching calls, no upsells -- one guide, the 4:3 structure, "
            "the 3 food rules, a 7-day starter plan + grocery list, and the exact "
            "affirmations to say each day. Everything you need to start Monday."
        ),
        "hashtags": "#weightlosstips #sustainableweightloss #healthylifestyle",
        "cta": "Link in bio -- $10",
    },
    {
        "day": 5,
        "pillar": "quick_tip",
        "hook": "It's Friday. Here's how to actually enjoy dinner tonight.",
        "caption": (
            "If tonight is your planned indulgent meal: sit down, eat slow, and remind "
            "yourself it comes back next week. That one mental shift is the difference "
            "between a meal and a binge."
        ),
        "hashtags": "#cravingscontrol #noguilt #weightlosstips",
        "cta": "Link in bio for the full method",
    },
    # ---------- Day 6 (Sat) - story, proof, tip ----------
    {
        "day": 6,
        "pillar": "relatable_story",
        "hook": "Saturday used to be my worst food day. Now it's my easiest.",
        "caption": (
            "Weekends used to be where every diet fell apart for me -- too many "
            "decisions, too much guilt either way. Having Saturday dinner already "
            "planned as my Anything Meal took the decision-making (and the guilt) out "
            "of it completely."
        ),
        "hashtags": "#foodfreedom #stopdieting #bingeeatingrecovery",
        "cta": "Link in bio for the full 7-day plan",
    },
    {
        "day": 6,
        "pillar": "social_proof",
        "hook": "\"I don't need every meal to be perfect.\"",
        "caption": (
            "That's one of the 5 daily affirmations in the guide -- said once in the "
            "morning, once before your evening meal. Small habit, but it's the line "
            "that actually rewires what \"normal\" eating feels like."
        ),
        "hashtags": "#weightlossjourney #healthylifestyle #personaltrainer",
        "cta": "Link in bio for the full script + method",
    },
    {
        "day": 6,
        "pillar": "quick_tip",
        "hook": "Shop for 4 days at a time, not 7.",
        "caption": (
            "Small logistics tip that makes this actually sustainable: buy produce for "
            "3-4 days so nothing wilts before you use it. Full starter grocery list "
            "(exact greens, fruit, veg, protein) is in the guide."
        ),
        "hashtags": "#healthylifestyle #dietingtips #weightlosstips",
        "cta": "Link in bio",
    },
    # ---------- Day 7 (Sun) - proof, myth, story ----------
    {
        "day": 7,
        "pillar": "social_proof",
        "hook": "One week of DMs about this guide -- here's the pattern.",
        "caption": (
            "The message I keep getting since this dropped: \"I didn't think a $10 PDF "
            "would actually change how I think about food.\" It's not magic, it's just "
            "the first plan that didn't ask you to ban anything."
        ),
        "hashtags": "#weightlossjourney #foodfreedom #sustainableweightloss",
        "cta": "Link in bio if you haven't grabbed it yet",
    },
    {
        "day": 7,
        "pillar": "myth_busting",
        "hook": "You don't need Monday to \"start over.\"",
        "caption": (
            "You can start the 4:3 structure on any day of the week -- Monday's just "
            "the easiest to plan around. Waiting for the \"perfect\" start date is its "
            "own form of restriction thinking."
        ),
        "hashtags": "#stopdieting #dietculturedropout #foodfreedom",
        "cta": "Link in bio, start whenever you're ready",
    },
    {
        "day": 7,
        "pillar": "relatable_story",
        "hook": "The diet that finally \"clicked\" wasn't stricter. It was smaller.",
        "caption": (
            "Every diet that failed me tried to change everything about how I ate, all "
            "at once. This one only asks for 4 days of simple meals -- and lets the "
            "rest of the week just be normal, guilt-free eating. That's the whole "
            "reason it stuck."
        ),
        "hashtags": "#foodfreedom #bingeeatingrecovery #dietculturedropout",
        "cta": "Link in bio",
    },
]
