# Builds index.html, book/index.html, ig/index.html. STRUCTURE here, COPY in content.py, COLOURS in css/site.css :root.
import json, os, html, re
WM=re.sub(r'<\?xml[^>]*>\s*','',open('assets/wordmark.svg').read()).replace(' role="img" aria-labelledby="title"','').replace('<title id="title">Lux Lashes</title>','').replace('<svg ','<svg class="wm" aria-hidden="true" focusable="false" ',1)
from content import *
S = SITE
e = html.escape
def img(src, alt, p, cls="", lazy=True, w=None, h=None):
    return f'<img src="{p}assets/img/{src}" alt="{e(alt)}"{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}{" loading=\"lazy\"" if lazy else ""} decoding="async">'
def tel(cls="", label=None): return f'<a class="{cls}" href="tel:{S["phone_tel"]}" data-ev="phone_tap">{e(label or S["phone_display"])}</a>'
SCHEMA = {"@context": "https://schema.org", "@type": "BeautySalon", "name": S["name"], "url": S["domain"], "email": S["email"],
  "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["suburb"], "addressRegion": S["state"], "postalCode": S["postcode"], "addressCountry": "AU"},
  "areaServed": ["Freshwater NSW", "Northern Beaches NSW", "Mosman NSW", "Cremorne NSW"], "sameAs": [S["ig_url"]],
  "makesOffer": [{"@type": "Offer", "name": f'{s["name"]} lash extensions full set (50% founding price)', "price": s["price"], "priceCurrency": "AUD"} for s in SETS]}
def head(p, title, desc, path, cls=""):
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{S["domain"]}/{path}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:locale" content="en_AU"><meta property="og:image" content="{p}assets/img/{HERO["img"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{p}css/site.css?v=1">
<script type="application/ld+json">{json.dumps(SCHEMA, ensure_ascii=False)}</script>
<script>document.documentElement.classList.add('js');if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('motion')</script>
</head><body class="{cls}">
<a class="skip" href="#main">{S["skip"]}</a>
<p class="devbar" role="note">{e(S["dev_banner"])}</p>
<div class="drift" aria-hidden="true"></div>
'''
def header(p, home=True):
    pre = "" if home else f"{p}index.html"
    links = "".join(f'<li><a href="{pre}{h}">{e(t)}</a></li>' for h, t in NAV)
    return f'''<header class="hd"><div class="w hd__in">
<a class="brand" href="{p}index.html" aria-label="Lux Lashes home">{WM}</a>
<nav aria-label="Primary"><ul class="hd__nav" id="navlist">{links}</ul></nav>
<div class="hd__act"><button class="lang" type="button" aria-label="{e(LANG["toggle_label"])}" data-lang-toggle data-en="{LANG["toggle_en"]}" data-zh="{LANG["toggle_zh"]}">{LANG["toggle_en"]}</button>
{tel("hd__tel")}<a class="btn" href="{p}book/" data-cta data-ev="book_click">{S["book"]}</a></div></div></header>
<main id="main">'''
def footer(p):
    return f'''</main>
<footer class="ft"><div class="w ft__g">
<div><p class="ft__brand" aria-label="Lux Lashes">{WM}</p><p>{e(S["address"])}</p></div>
<div><h2 class="ft__h">{FOOT["areas_h"]}</h2><p>{e(FOOT["areas"])}</p></div>
<div><h2 class="ft__h">{FOOT["contact_h"]}</h2><p>{tel()}</p><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div><h2 class="ft__h">{FOOT["follow_h"]}</h2><p><a href="{S["ig_url"]}" rel="noopener">{S["ig_handle"]}</a></p><p><button class="lang" type="button" aria-label="{e(LANG["toggle_label"])}" data-lang-toggle data-en="{LANG["toggle_en"]}" data-zh="{LANG["toggle_zh"]}">{LANG["toggle_en"]}</button></p></div>
</div><p class="w ft__legal">{FOOT["legal"]}</p></footer>
<nav class="mbar" aria-label="Quick actions"><a class="btn mbar__book" href="{p}book/" data-ev="book_click">{S["book"]}</a><a class="mbar__call" href="tel:{S["phone_tel"]}" data-ev="phone_tap">{S["phone_short"]}</a></nav>
<script>window.LUX={json.dumps({"postcodes": MOBILE_POSTCODES, "choice": CHOICE, "sets": [{"id": s["id"], "name": s["name"], "price": s["price"]} for s in SETS], "book": BOOK, "address": S["address"]}, ensure_ascii=False)};</script>
<script src="{p}js/site.js?v=1" defer></script></body></html>'''
def eyb(t): return f'<p class="eyb">{e(t)}</p>'
def pc_checker(p, idp):
    return f'''<form class="pc" data-pc action="{p}book/" method="get"><input type="hidden" name="mode" value="mobile"><label for="{idp}">{CHOICE["pc_label"]}</label>
<div class="pc__row"><input id="{idp}" name="pc" inputmode="numeric" pattern="[0-9]{{4}}" maxlength="4" autocomplete="postal-code" placeholder="e.g. 2096"><button class="btn btn--ghost" type="submit">{CHOICE["pc_btn"]}</button></div>
<p class="pc__msg" role="status" aria-live="polite"></p></form>'''
def choice(p):
    return f'''<section class="s" id="studio"><div class="w">{eyb(CHOICE["eyebrow"])}<h2 class="rv">{CHOICE["h2"]}</h2>
<div class="two">
<article class="card rv"><h3>{CHOICE["studio_h"]}</h3><p>{CHOICE["studio_p"]}</p><p class="addr">{e(S["address"])}</p>
<a class="maplink" href="https://www.google.com/maps/search/?api=1&amp;query=1%2F71+Evans+St+Freshwater+NSW+2096" rel="noopener">{CHOICE["map_label"]} ↗</a>
<a class="btn" href="{p}book/?mode=studio" data-cta data-ev="book_click">{CHOICE["studio_cta"]}</a></article>
<article class="card rv" id="mobile"><h3>{CHOICE["mobile_h"]}</h3><p>{CHOICE["mobile_p"]}</p>{pc_checker(p, "pc-home")}
<a class="btn" href="{p}book/?mode=mobile" data-cta data-ev="book_click">{CHOICE["mobile_cta"]}</a></article>
</div></div></section>'''
def prices(p, compact=False):
    cards = ""
    for i, s in enumerate(SETS, 1):
        inc = "".join(f"<li>{e(x)}</li>" for x in s["inc"])
        cards += f'''<div class="tix__w rv"><div class="tix__t"><div class="tix__f">{img(s["img"], s["alt"], p, "tix__img")}
<div class="tix__body"><p class="tix__row"><span>{PRICES_H["note"]}</span><span>No. 0{i}</span></p><h3 class="tix__nm">{e(s["name"])}</h3><p class="tix__line">{e(s["line"])}</p>
<p class="tix__pr">${s["price"]}</p><div class="tix__ba"><a class="btn" href="{p}book/?set={s["id"]}" data-ev="book_click">{PRICES_H["cta"]}<span class="sr"> {e(s["name"])}</span></a><button type="button" class="tix__flip" aria-pressed="false">{PRICES_H["details"]}<span class="sr"> for {e(s["name"])}</span></button></div></div></div>
<div class="tix__b"><p class="tix__row"><span>{e(s["name"])}</span><span>${s["price"]}</span></p><ul>{inc}</ul><div class="tix__ba"><a class="btn" href="{p}book/?set={s["id"]}">{PRICES_H["cta"]}<span class="sr"> {e(s["name"])}</span></a><button type="button" class="tix__flip tix__back">{PRICES_H["back"]}</button></div></div></div></div>'''
    return f'''<section class="s s--surface" id="prices"><div class="w">{eyb(PRICES_H["eyebrow"])}<h2 class="rv">{PRICES_H["h2"]}</h2><p class="lead">{PRICES_H["intro"]}</p><div class="tix__g">{cards}</div></div></section>'''
def looks(p):
    tabs = "".join(f'<button type="button" class="look__tab" role="tab" aria-selected="{"true" if i==0 else "false"}" data-i="{i}" data-en="{e(l["en"])}" data-zh="{e(l["zh"])}">{e(l["en"])}</button>' for i, l in enumerate(LOOKS))
    imgs = "".join(f'<img src="{p}assets/img/{l["img"]}" alt="{e(l["alt"])}" data-alt-en="{e(l["alt"])}" data-alt-zh="{e(l["alt_zh"])}" class="look__img{" on" if i==0 else ""}" loading="lazy" decoding="async">' for i, l in enumerate(LOOKS))
    return f'''<section class="s" id="looks"><div class="w look">{eyb(LOOKS_H["eyebrow"])}<h2 class="rv">{LOOKS_H["h2"]}</h2>
<p class="muted" data-en="{e(LOOKS_H["hint"])}" data-zh="{e(LOOKS_H["hint_zh"])}">{LOOKS_H["hint"]}</p>
<div class="look__tabs" role="tablist" aria-label="{LOOKS_H["label"]}">{tabs}</div><div class="look__stage">{imgs}</div></div></section>'''
def reels(p, n=6):
    t = "".join(f'<a class="reel" href="{S["ig_url"]}" rel="noopener">{img(r["img"], r["alt"], p)}<span class="reel__lbl">{e(r["label"])}</span></a>' for r in REELS[:n])
    return f'''<section class="s s--surface" id="reels"><div class="w">{eyb(REELS_H["eyebrow"])}<h2 class="rv">{REELS_H["h2"]}</h2><div class="reels">{t}</div>
<p class="center"><a class="btn btn--ghost" href="{S["ig_url"]}" rel="noopener">{REELS_H["follow"]}</a></p></div></section>'''
def reviews(n=2):
    t = "".join(f'<figure class="rev card rv">{f"<p class=rev__score>{r["score"]}</p>" if r["score"] else ""}<blockquote>“{e(r["quote"])}”</blockquote><figcaption><strong>{e(r["name"])}</strong> · {e(r["service"])}</figcaption></figure>' for r in REVIEWS[:n])
    return f'<section class="s" id="reviews"><div class="w">{eyb(REVIEWS_H["eyebrow"])}<h2 class="rv">{REVIEWS_H["h2"]}</h2><div class="two">{t}</div></div></section>'
def steps():
    t = "".join(f'<li class="card rv"><span class="step__n">0{i}</span><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(STEPS, 1))
    return f'<section class="s s--surface"><div class="w">{eyb(STEPS_H["eyebrow"])}<h2 class="rv">{STEPS_H["h2"]}</h2><ol class="steps">{t}</ol></div></section>'
def faq():
    t = "".join(f'<details{" open" if i==0 else ""}><summary>{e(q)}</summary><div class="faq__a"><p>{e(a)}</p></div></details>' for i, (q, a) in enumerate(FAQ))
    return f'<section class="s" id="faq"><div class="w faq">{eyb(FAQ_H["eyebrow"])}<h2 class="rv">{FAQ_H["h2"]}</h2><div class="faq__list" data-single>{t}</div></div></section>'
def cta(p):
    return f'<section class="cta"><div class="w cta__in"><h2>{CTA["h2"]}</h2><p>{CTA["p"]}</p><div class="cta__a"><a class="btn" href="{p}book/" data-cta data-ev="book_click">{CTA["btn"]}</a>{tel("cta__tel")}</div></div></section>'
def hero(p):
    return f'''<section class="hero"><div class="hero__media">{img(HERO["img"], HERO["img_alt"], p, "hero__img", lazy=False)}</div>
<div class="w hero__in"><p class="badge">{S["founding_badge"]}</p>{eyb(HERO["eyebrow"])}<h1 class="hero__h">{HERO["h1"]}</h1><p class="hero__sub">{HERO["sub"]}</p>
<div class="hero__a"><a class="btn" href="{p}book/" data-cta data-ev="book_click">{S["book"]}</a><a class="btn btn--ghost" href="#prices">{S["see_prices"]}</a></div></div>
<!-- {HERO["video_note"]} --></section>'''
def page_home():
    p = ""
    return head(p, S["title"], S["desc"], "") + header(p) + hero(p) + choice(p) + prices(p) + looks(p) + reels(p) + reviews() + steps() + faq() + cta(p) + footer(p)
def page_book():
    p = "../"; B = BOOK
    sets = "".join(f'<label class="opt"><input type="radio" name="set" value="{s["id"]}" required><span><strong>{e(s["name"])}</strong><em>${s["price"]} · {B["sum_note"]}</em></span></label>' for s in SETS)
    times = "".join(f'<option>{t}</option>' for t in B["times"])
    return head(p, B["title"], B["desc"], "book/", "pg-book") + header(p, False) + f'''<section class="s"><div class="w bk">
<div class="bk__main">{eyb(B["eyebrow"])}<h1>{B["h1"]}</h1><p class="lead">{B["intro"]}</p>
<form class="bkf" id="bkf" name="booking" method="post" action="#" novalidate>
<input type="hidden" name="utm_source"><input type="hidden" name="utm_medium"><input type="hidden" name="utm_campaign">
<p class="hp"><label>Leave blank <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<fieldset class="step" data-step="1"><legend>{B["s1"]}</legend>
<label class="opt"><input type="radio" name="mode" value="studio" required><span><strong>{B["studio"]}</strong><em>{B["studio_sub"]}</em></span></label>
<label class="opt"><input type="radio" name="mode" value="mobile"><span><strong>{B["mobile"]}</strong><em>{B["mobile_sub"]}</em></span></label></fieldset>
<fieldset class="step" data-step="2"><legend data-l-studio="{B["s2_studio"]}" data-l-mobile="{B["s2"]}">{B["s2"]}</legend>
<div class="only-mobile"><label for="pc">{CHOICE["pc_label"]}</label><div class="pc__row"><input id="pc" name="postcode" inputmode="numeric" maxlength="4" pattern="[0-9]{{4}}" autocomplete="postal-code" placeholder="e.g. 2096"><button class="btn btn--ghost" type="button" data-pc-check>{CHOICE["pc_btn"]}</button></div>
<p class="pc__msg" role="status" aria-live="polite"></p><button class="btn" type="button" data-to-studio hidden>{CHOICE["pc_studio"]}</button></div>
<div class="only-studio"><p class="addr">{e(S["address"])}</p></div></fieldset>
<fieldset class="step" data-step="3"><legend>{B["s3"]}</legend><div class="opts">{sets}</div></fieldset>
<fieldset class="step" data-step="4"><legend>{B["s4"]}</legend><div class="row2"><label>{B["date"]}<input type="date" name="date" required></label><label>{B["time"]}<select name="time" required><option value="">Choose…</option>{times}</select></label></div></fieldset>
<fieldset class="step" data-step="5"><legend>{B["s5"]}</legend><label>{B["name"]}<input name="name" required autocomplete="name"></label>
<div class="row2"><label>{B["mobile_no"]}<input type="tel" name="phone" required autocomplete="tel" pattern="(\\+61|0)4[0-9 ]{{8,10}}"></label><label>{B["email"]}<input type="email" name="email" required autocomplete="email"></label></div></fieldset>
<p class="bkf__err" role="alert"></p>
<div class="bkf__nav"><button class="btn btn--ghost" type="button" data-back>{B["back"]}</button><button class="btn" type="button" data-next>{B["next"]}</button><button class="btn" type="submit" data-submit data-cta>{B["submit"]}</button></div>
</form>
<div class="done" hidden tabindex="-1"><h2>{B["done_h"]}</h2><p>{B["done_p"]}</p><p class="devnote">{B["done_dev"]}</p></div>
</div>
<aside class="sum card" aria-live="polite"><h2 class="sum__h">{B["summary"]}</h2><dl>
<dt>{B["sum_where"]}</dt><dd data-sum="where">–</dd><dt>{B["sum_set"]}</dt><dd data-sum="set">–</dd><dt>{B["sum_when"]}</dt><dd data-sum="when">–</dd><dt>{B["sum_price"]}</dt><dd data-sum="price">–</dd></dl>
<p class="muted small">{B["sum_note"]}</p><p class="small sum__q">{e(B["review_q"])}</p><p class="small">{tel()}</p></aside>
</div></section>''' + footer(p)
def page_ig():
    p = "../"; G = IG
    pr = "".join(f'<li><span>{e(s["name"])}</span><strong>${s["price"]}</strong></li>' for s in SETS)
    rl = "".join(f'<a class="reel" href="{S["ig_url"]}" rel="noopener">{img(r["img"], r["alt"], p)}<span class="reel__lbl">{e(r["label"])}</span></a>' for r in REELS[:3])
    rv = "".join(f'<figure class="rev card"><blockquote>“{e(r["quote"])}”</blockquote><figcaption><strong>{e(r["name"])}</strong> · {e(r["service"])}</figcaption></figure>' for r in REVIEWS[:2])
    return head(p, G["title"], G["desc"], "ig/", "pg-ig") + f'''<main id="main" class="ig">
<header class="ig__hd"><a class="brand" href="../index.html" aria-label="Lux Lashes home">{WM}</a>
<h1 class="sr">{G["h1"]}</h1><p class="muted">{G["sub"]}</p><a class="btn btn--block" href="../book/" data-cta data-ev="book_click">{G["book"]}</a></header>
<section class="card"><h2 class="ig__h">{G["prices_h"]}</h2><ul class="ig__pr">{pr}</ul></section>
<section class="card"><h2 class="ig__h">{G["where_h"]}</h2><div class="ig__two"><a class="opt opt--link" href="../book/?mode=studio"><span><strong>{BOOK["studio"]}</strong><em>{BOOK["studio_sub"]}</em></span></a><a class="opt opt--link" href="../book/?mode=mobile"><span><strong>{BOOK["mobile"]}</strong><em>{BOOK["mobile_sub"]}</em></span></a></div></section>
<section><h2 class="ig__h">{G["reels_h"]}</h2><div class="reels reels--3">{rl}</div></section>
<section><h2 class="ig__h">{G["reviews_h"]}</h2>{rv}</section>
<p class="center"><a class="btn btn--block" href="../book/" data-cta>{G["book"]}</a></p>
<p class="center small">{tel()} · <a href="mailto:{S["email"]}">{S["email"]}</a> · <a href="{S["ig_url"]}" rel="noopener">{S["ig_handle"]}</a> · <a href="../index.html">{G["site"]}</a></p>
</main>
<nav class="mbar" aria-label="Quick actions"><a class="btn mbar__book" href="../book/" data-ev="book_click">{S["book"]}</a><a class="mbar__call" href="tel:{S["phone_tel"]}" data-ev="phone_tap">{S["phone_short"]}</a></nav>
<script>window.LUX={json.dumps({"postcodes": MOBILE_POSTCODES, "choice": CHOICE, "sets": [], "book": BOOK}, ensure_ascii=False)};</script><script src="../js/site.js?v=1" defer></script></body></html>'''
os.makedirs("book", exist_ok=True); os.makedirs("ig", exist_ok=True)
open("index.html", "w").write(page_home()); open("book/index.html", "w").write(page_book()); open("ig/index.html", "w").write(page_ig())
open("robots.txt", "w").write("User-agent: *\nDisallow: /\n"); open(".nojekyll", "w").write("")
print("built")
