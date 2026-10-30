addEventListener('load',()=>document.documentElement.classList.add('loaded'));
setTimeout(()=>document.documentElement.classList.add('loaded'),1200);
const nav=document.querySelector('.nav');addEventListener('scroll',()=>nav.classList.toggle('solid',scrollY>80),{passive:true});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.15});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
document.querySelectorAll('[data-ba]').forEach(b=>{const r=b.querySelector('input');const f=()=>b.style.setProperty('--p',r.value+'%');r.addEventListener('input',f);f()});
const hi=document.querySelector('.hero__img');if(document.documentElement.classList.contains('motion'))addEventListener('scroll',()=>{if(scrollY<innerHeight)hi.style.translate=`0 ${scrollY*.25}px`},{passive:true});
