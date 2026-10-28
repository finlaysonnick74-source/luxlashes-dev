#!/usr/bin/env python3
"""Fold check: the hero CTAs must be fully visible with >=24px clearance at common window sizes
(and, on mobile, sit above the sticky Book+Call bar). Usage: python3 testing/fold_check.py [base_url] [shots_dir]"""
import sys,os
from playwright.sync_api import sync_playwright
BASE=sys.argv[1] if len(sys.argv)>1 else "http://127.0.0.1:8111"; OUT=sys.argv[2] if len(sys.argv)>2 else "testing/runs/fold"
SIZES=[(1440,700),(1366,768),(1280,720),(1280,800),(1536,864),(1920,1080),(390,844),(375,667)]
SEL=".hero__a .btn"; CLEAR=24; os.makedirs(OUT,exist_ok=True); fails=0
with sync_playwright() as p:
  b=p.chromium.launch()
  for motion in ("reduce","no-preference"):
    for w,h in SIZES:
      pg=b.new_page(viewport={"width":w,"height":h},reduced_motion=motion);pg.goto(BASE+"/");pg.wait_for_timeout(1800)
      r=pg.evaluate(f"""()=>{{const bs=[...document.querySelectorAll('{SEL}')];const bot=Math.max(...bs.map(b=>b.getBoundingClientRect().bottom));
        const bar=document.querySelector('.mbar');const bt=bar&&getComputedStyle(bar).display!=='none'?bar.getBoundingClientRect().top:innerHeight;
        const hero=document.querySelector('.hero').getBoundingClientRect();return {{n:bs.length,bot,bt,heroBot:hero.bottom,ih:innerHeight}}}}""")
      limit=min(h-CLEAR,r["bt"]-CLEAR if r["bt"]<h else h)
      ok=r["n"]>=2 and r["bot"]<=limit
      fails+=not ok
      print(f"{'PASS' if ok else 'FAIL'} {motion:13s} {w}x{h}: CTA bottom {r['bot']:.0f} <= {limit:.0f} (sticky bar top {r['bt']:.0f}, hero bottom {r['heroBot']:.0f})")
      if motion=="no-preference": pg.screenshot(path=f"{OUT}/fold-{w}x{h}.png")
      pg.close()
print("fold_check:", "0 failures" if not fails else f"{fails} failures"); sys.exit(1 if fails else 0)
