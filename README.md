# Lux Lashes refresh: DEV PREVIEW (Concept A "Warm Linen")
Not the live site. noindex + robots disallow. Go-live only after Nick approves.
- Copy: `content.py` (all text, incl. 中文 strings). Structure: `build.py`. Colours: `css/site.css` `:root` only.
- Rebuild: `python3 build.py`. Test: `python3 -m http.server 8111 & python3 testing/regress.py testing/config.json`
- Placeholders: phone, mobile postcode allow-list, reels, 2nd review, hero video (image drift stands in). Images are the illustrative images from the current lux-lashes.com.

## v2 redesign (30 Oct 2026)
`index.html` is now hand-written (css/v2.css, js/v2.js, assets/v2/). **Do not run build.py for the homepage** — it would overwrite v2. book/, ig/, founding-five/ are still the earlier build.
