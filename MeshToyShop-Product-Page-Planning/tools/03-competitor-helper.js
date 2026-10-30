globalThis.researchPages={};
globalThis.inspectCompetitor=async function(key,url){
 const p=await context.newPage();researchPages[key]=p;
 await p.setViewportSize({width:1440,height:1000});
 await p.goto(url,{waitUntil:'domcontentloaded',timeout:25000});
 const capture=()=>p.evaluate(()=>{
  const visible=e=>e.getBoundingClientRect().height>0&&getComputedStyle(e).visibility!=='hidden';
  const geo=e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return {text:(e.innerText||e.getAttribute('aria-label')||'').trim().slice(0,85),x:Math.round(r.x),y:Math.round(r.y+scrollY),w:Math.round(r.width),h:Math.round(r.height),font:s.fontFamily,size:s.fontSize,color:s.color,bg:s.backgroundColor,disabled:e.disabled||false};};
  const h=document.querySelector('h1');
  return {url:location.href,title:document.title,width:innerWidth,pageWidth:document.documentElement.scrollWidth,h1:h?geo(h):null,buttons:[...document.querySelectorAll('button,input[type="submit"],a')].filter(e=>visible(e)&&/^(add to (cart|bag)|buy (it )?now|sold out|personalise|check$)/i.test((e.innerText||e.value||'').trim())).slice(0,7).map(geo),headings:[...document.querySelectorAll('h1,h2,h3,summary')].filter(visible).map(e=>e.innerText.trim()).filter(Boolean).slice(0,25),excerpt:document.body.innerText.slice(document.body.innerText.indexOf(h?.innerText||''),document.body.innerText.indexOf(h?.innerText||'')+3200),visibleVideos:[...document.querySelectorAll('video')].filter(visible).length};
 });
 const desktop=await capture();
 await p.setViewportSize({width:390,height:844});
 const mobile=await capture();
 return {key,desktop,mobile:{width:mobile.width,pageWidth:mobile.pageWidth,h1:mobile.h1,buttons:mobile.buttons}};
};
return await Promise.allSettled([inspectCompetitor('rabitat','https://www.rabitat.com/products/hyde'),inspectCompetitor('smartivity','https://www.smartivity.in/products/rocket-launcher')]);
