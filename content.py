# ALL visible copy lives here (incl. 中文 strings). Colours live in css/site.css :root only.
# Anything marked PLACEHOLDER must be replaced with real content before go-live.
SITE = {
  "name": "Lux Lashes",
  "domain": "https://lux-lashes.com",
  "title": "Lash extensions Freshwater | Northern Beaches | Lux Lashes",
  "desc": "Premium lash extensions at our Freshwater studio (1/71 Evans St) or mobile across the Northern Beaches and Mosman to Cremorne. 50% founding prices from $95.",
  "street": "1/71 Evans St", "suburb": "Freshwater", "state": "NSW", "postcode": "2096",
  "address": "1/71 Evans St, Freshwater NSW 2096",
  # PLACEHOLDER phone: no number in the Lux facts files. Replace both values with the real business number.
  "phone_tel": "+61000000000", "phone_display": "Phone TBC (placeholder)", "phone_short": "Call",
  "email": "hello@lux-lashes.com",
  "ig_handle": "@luxlashessydney", "ig_url": "https://www.instagram.com/luxlashessydney/",
  "areas": "Freshwater studio · mobile across the Northern Beaches and Mosman to Cremorne",
  "skip": "Skip to content", "book": "Book now", "see_prices": "See prices", "menu": "Menu",
  "dev_banner": "DEV PREVIEW, not the live site. Placeholders still to replace: phone number, mobile postcode list, reels, extra reviews. Photos are the illustrative images from the current site.",
  "founding_badge": "50% founding prices",
}
NAV = [("#prices", "Services & Prices"), ("#studio", "Studio"), ("#mobile", "Mobile"), ("#reviews", "Reviews"), ("#faq", "FAQ")]

HERO = {
  "eyebrow": "Freshwater studio · Northern Beaches mobile",
  "h1": "Premium lash extensions in Freshwater & across the Northern Beaches",
  "sub": "Visit our Freshwater studio or book mobile, Northern Beaches and Mosman to Cremorne.",
  "img": "lux-lashes-wispy-iconic-result-v1.jpg",
  "img_alt": "Macro close-up of a brown eye with a wispy lash extension set",
  "video_note": "PLACEHOLDER: slow image drift stands in for the hero video loop until real lash-application footage is filmed.",
}

CHOICE = {
  "eyebrow": "Two ways to book", "h2": "Studio or mobile, your choice.",
  "studio_h": "Freshwater studio",
  "studio_p": "Come to us at our private studio in Freshwater.",
  "studio_cta": "Book the studio", "map_label": "Open in Google Maps",
  "mobile_h": "Mobile visits", "mobile_p": "We come to you across the Northern Beaches and Mosman to Cremorne.",
  "mobile_cta": "Book a mobile visit",
  "pc_label": "Check your postcode", "pc_btn": "Check",
  "pc_ok": "Great news, we visit {pc}. Book a mobile appointment.",
  "pc_no": "Sorry, {pc} is outside our mobile area. Our Freshwater studio is open to everyone.",
  "pc_bad": "Please enter a 4-digit postcode.",
  "pc_studio": "Book the Freshwater studio instead",
}
# PLACEHOLDER postcode allow-list: NOT from the Lux facts files (none listed). Draft Northern Beaches + Mosman-to-Cremorne
# postcodes for Nick/Shenghua to confirm before go-live.
MOBILE_POSTCODES = ["2084","2085","2086","2087","2092","2093","2094","2095","2096","2097","2099","2100","2101","2102","2103","2104","2105","2106","2107","2108","2088","2089","2090"]

PRICES_H = {"eyebrow": "Services & prices", "h2": "Founding prices, half off.", "note": "50% founding price", "intro": "Our founding offer: every full set at half our standard price, for a limited time.", "cta": "Book this set", "details": "Details", "back": "Back"}
SETS = [
  {"id": "classic", "name": "Classic", "price": 95, "line": "One extension per natural lash for clean, natural definition.", "img": "lux-lashes-en-detail-classic-v1.jpg", "alt": "Macro view of a natural-looking classic lash set on a green eye", "inc": ["Eye-shape consultation", "Personal lash mapping", "Aftercare guidance"]},
  {"id": "hybrid", "name": "Hybrid", "price": 110, "line": "Classic and volume lashes mixed for texture and dimension.", "img": "lux-lashes-en-detail-hybrid-v1.jpg", "alt": "Macro view of a textured hybrid lash set", "inc": ["Eye-shape consultation", "Personal lash mapping", "Aftercare guidance"]},
  {"id": "wispy", "name": "Wispy", "price": 125, "line": "Soft feathered fans with defined spikes for an airy finish.", "img": "lux-lashes-wispy-iconic-detail-v1.jpg", "alt": "Macro view of a wispy lash set with defined spikes", "inc": ["Choice of wispy looks", "Personal lash mapping", "Aftercare guidance"]},
  {"id": "russian", "name": "Russian volume", "price": 135, "line": "Handmade lightweight fans for soft, full volume.", "img": "lux-lashes-en-detail-russian-volume-v1.jpg", "alt": "Macro view of a full Russian volume lash set", "inc": ["Eye-shape consultation", "Handmade volume fans", "Aftercare guidance"]},
]

# Look finder. zh strings are the real 简体中文 strings from the current lux-lashes.com site.
LOOKS_H = {"eyebrow": "Lash look finder", "h2": "Find your look.", "hint": "Tap a look to preview it.", "hint_zh": "轻点图片，切换自然睫毛与设计效果", "label_zh": "款式示意", "label": "Style preview"}
LOOKS = [
  {"en": "Iconic", "zh": "标志束感", "img": "lux-lashes-wispy-iconic-result-v1.jpg", "alt": "Iconic wispy look: bold separated spikes", "alt_zh": "标志束感嫁接效果特写，呈现鲜明分离的轻盈睫毛束"},
  {"en": "Doll eye", "zh": "灵动圆眼", "img": "lux-lashes-wispy-doll-result-v1.jpg", "alt": "Doll eye look: longest lashes at the centre of the eye", "alt_zh": "灵动圆眼束感嫁接效果特写，中央睫毛纤长立体"},
  {"en": "Cat eye", "zh": "提拉猫眼", "img": "lux-lashes-wispy-cat-result-v1.jpg", "alt": "Cat eye look: lashes lengthening and lifting to the outer corner", "alt_zh": "提拉猫眼束感嫁接效果特写，眼尾纤长上扬"},
  {"en": "Feather", "zh": "轻盈羽翼", "img": "lux-lashes-wispy-feather-result-v1.jpg", "alt": "Feather look: fine, soft and natural lash spacing", "alt_zh": "轻盈羽翼束感嫁接效果特写，纤细留白自然"},
  {"en": "Volume", "zh": "层次浓密", "img": "lux-lashes-wispy-volume-result-v2.jpg", "alt": "Volume look: full, layered lashes", "alt_zh": "干净清晰的层次浓密束感嫁接完成效果"},
]
LANG = {"toggle_en": "中文", "toggle_zh": "EN", "toggle_label": "切换为简体中文 / Switch language"}

REELS_H = {"eyebrow": "On Instagram", "h2": "Fresh sets, straight from the studio.", "follow": "Follow @luxlashessydney"}
# PLACEHOLDER reels: no reel files or URLs in /workspace/lux-shared. Tiles link to the profile until real reel URLs + posters are added.
REELS = [{"label": f"Reel placeholder {i}", "img": img, "alt": f"Reel placeholder {i}: lash close-up"} for i, img in enumerate(["lux-lashes-wispy-cat-detail-v3.jpg", "lux-lashes-wispy-doll-detail-v1.jpg", "lux-lashes-wispy-feather-detail-v1.jpg", "lux-lashes-en-classic-v1.jpg", "lux-lashes-wispy-volume-detail-v3.jpg", "lux-lashes-en-detail-hybrid-v1.jpg"], 1)]

REVIEWS_H = {"eyebrow": "Reviews", "h2": "Early client feedback."}
# Real review from the current site. Second card is a PLACEHOLDER.
REVIEWS = [
  {"quote": "Melissa rated her complete Wispy Set treatment experience 9.5 out of 10.", "name": "Melissa F.", "service": "Wispy Set · 29 August 2026", "score": "9.5/10"},
  {"quote": "PLACEHOLDER: add the next real client review here (first name + service).", "name": "Client name", "service": "Service", "score": ""},
]

STEPS_H = {"eyebrow": "How it works", "h2": "Three easy steps."}
STEPS = [("Choose your set", "Classic, Hybrid, Wispy or Russian volume, all at founding prices."), ("Studio or mobile", "Come to Freshwater, or we visit you on the Northern Beaches and Mosman to Cremorne."), ("Relax", "Lie back while your lashes are mapped and applied with care.")]

FAQ_H = {"eyebrow": "FAQ", "h2": "Good to know."}
FAQ = [
  ("Where are you?", "Our studio is at 1/71 Evans St, Freshwater NSW 2096. We also offer mobile visits across the Northern Beaches and Mosman to Cremorne."),
  ("Do you come to me?", "Yes, if you are on the Northern Beaches or between Mosman and Cremorne. Pop your postcode into the checker. If you are outside the mobile area, you are welcome at our Freshwater studio."),
  ("What is the founding offer?", "During our founding period every full set is 50% off: Classic $95, Hybrid $110, Wispy $125 and Russian volume $135."),
  ("How do I choose a style?", "Use the look finder for ideas, or simply tell us the look you love. We map every set to your eye shape at your appointment."),
  ("How do I look after my lashes?", "You will get personal aftercare guidance at the end of your appointment, so your set stays fresh for longer."),
]

CTA = {"h2": "Ready for your lashes?", "p": "Book your founding-price set at our Freshwater studio or at home.", "btn": "Book now"}

FOOT = {"areas_h": "Service areas", "areas": "Freshwater studio. Mobile across the Northern Beaches and from Mosman to Cremorne.", "contact_h": "Contact", "follow_h": "Follow", "legal": "© 2026 Lux Lashes. Dev preview."}

BOOK = {
  "title": "Book lash extensions | Freshwater studio or mobile | Lux Lashes",
  "desc": "Book a classic, hybrid, wispy or Russian volume set at our Freshwater studio or mobile on the Northern Beaches and Mosman to Cremorne.",
  "eyebrow": "Book", "h1": "Book your lashes", "intro": "Five quick steps. We confirm your time by email.",
  "s1": "1. Studio or mobile", "studio": "Freshwater studio", "studio_sub": "1/71 Evans St, Freshwater NSW 2096", "mobile": "Mobile visit", "mobile_sub": "Northern Beaches and Mosman to Cremorne",
  "s2": "2. Your postcode", "s2_studio": "2. Studio location",
  "s3": "3. Choose your set", "s4": "4. Preferred date and time", "date": "Preferred date", "time": "Preferred time",
  "times": ["Morning", "Afternoon", "Evening"],
  "s5": "5. Your details", "name": "Full name", "mobile_no": "Mobile number", "email": "Email",
  "next": "Next", "back": "Back", "submit": "Send booking request",
  "summary": "Your booking", "sum_where": "Where", "sum_set": "Set", "sum_price": "Price", "sum_when": "When", "sum_note": "50% founding price",
  "err": "Please complete this step.",
  "done_h": "Thank you, your request is in.", "done_p": "We will email you to confirm your time.",
  "done_dev": "DEV PREVIEW: nothing was sent. The form handler is connected at go-live.",
  "review_q": "“Melissa rated her complete Wispy Set treatment experience 9.5 out of 10.” Melissa F., Wispy Set",
}

IG = {
  "title": "Lux Lashes | Book from Instagram | Freshwater & Northern Beaches",
  "desc": "Founding prices from $95. Book lash extensions at our Freshwater studio or mobile on the Northern Beaches and Mosman to Cremorne.",
  "h1": "Lux Lashes", "sub": "Lash extensions · Freshwater studio + Northern Beaches mobile",
  "book": "Book now", "prices_h": "50% founding prices", "where_h": "Studio or mobile",
  "reels_h": "Latest reels", "reviews_h": "Reviews", "site": "Visit the full site",
}
