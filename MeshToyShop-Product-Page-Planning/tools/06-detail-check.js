const out={};
const k=researchPages.kobbo;
await k.locator('h1').filter({hasText:'Little Explorer'}).first().waitFor({state:'visible'});
out.kobbo=await k.evaluate(()=>({text:document.body.innerText.slice(0,6500),buttons:[...document.querySelectorAll('button')].filter(e=>e.getBoundingClientRect().height&&/cart|buy/i.test(e.innerText)).map(e=>({text:e.innerText,y:Math.round(e.getBoundingClientRect().y),position:getComputedStyle(e).position}))}));
for(const key of ['rabitat','smartivity']){
 const p=researchPages[key];await p.evaluate(()=>scrollTo(0,0));
 out[key]=await p.evaluate(()=>({topText:document.body.innerText.slice(0,2100),viewport:{w:innerWidth,h:innerHeight},controls:[...document.querySelectorAll('input,button')].filter(e=>e.getBoundingClientRect().height&&(/pin|check|color|cart/i.test((e.placeholder||'')+' '+e.innerText))).map(e=>({tag:e.tagName,text:e.innerText?.slice(0,70),placeholder:e.placeholder,aria:e.getAttribute('aria-label')})).slice(0,10)}));
 await p.screenshot({path:key+'-mobile-top.png',fullPage:false});
}
return out;
