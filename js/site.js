(()=>{const L=window.LUX||{},C=L.choice||{},PCS=new Set(L.postcodes||[]);
const ev=(n,d)=>{(window.dataLayer=window.dataLayer||[]).push(Object.assign({event:n},d||{}))};
document.addEventListener('click',e=>{const a=e.target.closest('[data-ev]');if(a)ev(a.dataset.ev,{href:a.getAttribute('href')})});
// reveal on scroll
const rv=document.querySelectorAll('.rv');if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{rootMargin:'0px 0px -8% 0px'});rv.forEach(r=>io.observe(r))}else rv.forEach(r=>r.classList.add('in'));
// postcode check
const checkPc=v=>{v=(v||'').trim();if(!/^\d{4}$/.test(v))return{s:'bad',m:C.pc_bad};return PCS.has(v)?{s:'ok',m:C.pc_ok.replace('{pc}',v)}:{s:'no',m:C.pc_no.replace('{pc}',v)}};
document.querySelectorAll('form[data-pc]').forEach(f=>f.addEventListener('submit',e=>{const r=checkPc(f.pc.value),m=f.querySelector('.pc__msg');m.className='pc__msg '+r.s;
 if(r.s==='ok'){m.textContent=r.m;return}e.preventDefault();m.textContent=r.m;
 if(r.s==='no'){const a=document.createElement('a');a.className='btn';a.href=f.getAttribute('action')+'?mode=studio';a.textContent=C.pc_studio;m.append(document.createElement('br'),a)}}));
// ticket flip (kit ticket-pricing)
document.querySelectorAll('.tix__w').forEach(w=>{const f=w.querySelector('.tix__f .tix__flip'),b=w.querySelector('.tix__back');const set=o=>{w.classList.toggle('on',o);f.setAttribute('aria-pressed',String(o));w.querySelector('.tix__f').inert=o;w.querySelector('.tix__b').inert=!o;(o?b:f).focus({preventScroll:true})};w.querySelector('.tix__b').inert=true;f.addEventListener('click',()=>set(true));b.addEventListener('click',()=>set(false))});
// faq single-open + FAQPage schema (kit faq-accordion)
document.querySelectorAll('.faq__list').forEach(list=>{const it=[...list.querySelectorAll('details')];it.forEach(d=>d.addEventListener('toggle',()=>{if(d.open)it.forEach(o=>o!==d&&(o.open=false))}));
 const s=document.createElement('script');s.type='application/ld+json';s.textContent=JSON.stringify({"@context":"https://schema.org","@type":"FAQPage",mainEntity:it.map(d=>({"@type":"Question",name:d.querySelector('summary').textContent.trim(),acceptedAnswer:{"@type":"Answer",text:d.querySelector('.faq__a').textContent.trim()}}))});document.head.append(s)});
// look finder
const tabs=[...document.querySelectorAll('.look__tab')],imgs=[...document.querySelectorAll('.look__img')];
tabs.forEach(t=>t.addEventListener('click',()=>{tabs.forEach(x=>x.setAttribute('aria-selected',String(x===t)));imgs.forEach((im,i)=>im.classList.toggle('on',i==t.dataset.i))}));
// 中文 toggle: swaps only elements that carry real zh strings (look finder); hook for more.
let zh=false;document.querySelectorAll('[data-lang-toggle]').forEach(b=>b.addEventListener('click',()=>{zh=!zh;document.documentElement.lang=zh?'zh-Hans':'en-AU';
 document.querySelectorAll('[data-lang-toggle]').forEach(x=>{x.textContent=zh?x.dataset.zh:x.dataset.en;x.setAttribute('aria-pressed',String(zh))});
 document.querySelectorAll('[data-zh]:not([data-lang-toggle])').forEach(el=>el.textContent=zh?el.dataset.zh:el.dataset.en);
 document.querySelectorAll('[data-alt-zh]').forEach(el=>el.alt=zh?el.dataset.altZh:el.dataset.altEn)}));
// booking form
const f=document.getElementById('bkf');if(!f)return;const B=L.book,q=new URLSearchParams(location.search);
['utm_source','utm_medium','utm_campaign'].forEach(k=>{if(q.get(k))f[k].value=q.get(k)});
const steps=[...f.querySelectorAll('.step')],err=f.querySelector('.bkf__err'),nx=f.querySelector('[data-next]'),bk=f.querySelector('[data-back]'),sb=f.querySelector('[data-submit]');let cur=0;
const s2=steps[1],pcIn=f.postcode,pcMsg=s2.querySelector('.pc__msg'),toStudio=s2.querySelector('[data-to-studio]');let pcOk=false;
const mode=()=>(f.querySelector('[name=mode]:checked')||{}).value;
const show=i=>{cur=i;steps.forEach((s,j)=>s.classList.toggle('cur',j===i));bk.hidden=i===0;nx.hidden=i===steps.length-1;sb.hidden=i!==steps.length-1;err.textContent='';
 s2.classList.toggle('m-studio',mode()==='studio');s2.querySelector('legend').textContent=mode()==='studio'?s2.querySelector('legend').dataset.lStudio:s2.querySelector('legend').dataset.lMobile;ev('form_step',{step:i+1});summ()};
const runPc=()=>{const r=checkPc(pcIn.value);pcMsg.className='pc__msg '+r.s;pcMsg.textContent=r.m;pcOk=r.s==='ok';toStudio.hidden=r.s!=='no';return pcOk};
s2.querySelector('[data-pc-check]').addEventListener('click',runPc);pcIn.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();runPc()}});
toStudio.addEventListener('click',()=>{f.querySelector('[name=mode][value=studio]').checked=true;pcMsg.textContent='';toStudio.hidden=true;show(1)});
const valid=i=>{const s=steps[i];if(i===1&&mode()==='mobile')return runPc();const els=[...s.querySelectorAll('input,select')].filter(x=>x.required);
 for(const el of els){if(el.type==='radio'){if(!s.querySelector(`[name=${el.name}]:checked`))return false}else if(!el.checkValidity()){el.focus();return false}}return true};
nx.addEventListener('click',()=>{if(!valid(cur)){err.textContent=err.textContent||B.err;if(cur!==1||mode()!=='mobile')err.textContent=B.err;else err.textContent='';return}show(cur+1)});
bk.addEventListener('click',()=>show(Math.max(0,cur-1)));
f.addEventListener('change',summ);
function summ(){const m=mode(),st=(L.sets||[]).find(x=>x.id===(f.querySelector('[name=set]:checked')||{}).value);const d=document.querySelector.bind(document);
 d('[data-sum=where]').textContent=m==='studio'?B.studio+', '+L.address:m==='mobile'?B.mobile+(pcOk?' ('+pcIn.value+')':''):'–';
 d('[data-sum=set]').textContent=st?st.name:'–';d('[data-sum=price]').textContent=st?'$'+st.price:'–';
 d('[data-sum=when]').textContent=[f.date.value,f.time.value].filter(Boolean).join(', ')||'–'}
f.addEventListener('submit',e=>{e.preventDefault();if(!valid(cur)){err.textContent=B.err;return}ev('form_submit',{mode:mode()});f.hidden=true;const dn=document.querySelector('.done');dn.hidden=false;dn.focus()});
// preselect from URL
const pm=q.get('mode');if(pm){const r=f.querySelector(`[name=mode][value=${pm}]`);if(r)r.checked=true}
const ps=q.get('set');if(ps){const r=f.querySelector(`[name=set][value=${ps}]`);if(r)r.checked=true}
if(q.get('pc'))pcIn.value=q.get('pc');
show(pm?1:0);if(pm==='mobile'&&q.get('pc'))runPc();
})();
