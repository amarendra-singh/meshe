globalThis.meshProductAudit=[];
await page.setViewportSize({width:1440,height:1000});
for(const handle of ['diy-screw-drill-puzzle-toy','3d-maze-cube','diy-instant-digital-camera','remote-watch-car']){
  await page.goto('https://2zs0x1-0z.myshopify.com/products/'+handle,{waitUntil:'domcontentloaded'});
  await page.locator('main h1').waitFor();
  const capture=()=>page.evaluate(()=>{
    const rect=e=>{const r=e.getBoundingClientRect();const s=getComputedStyle(e);return {text:e.innerText?.trim().slice(0,90),x:Math.round(r.x),y:Math.round(r.y+scrollY),w:Math.round(r.width),h:Math.round(r.height),font:s.fontFamily,size:s.fontSize,color:s.color,bg:s.backgroundColor,disabled:e.disabled||false};};
    const main=document.querySelector('main');
    return {url:location.href,width:innerWidth,pageWidth:document.documentElement.scrollWidth,title:main.querySelector('h1')?.innerText,headings:[...main.querySelectorAll('h1,h2,h3')].map(x=>x.innerText).slice(0,16),text:main.innerText.slice(0,2200),buttons:[...main.querySelectorAll('button')].filter(x=>x.getBoundingClientRect().height&&/cart|buy|sold|option/i.test(x.innerText)).map(rect).slice(0,6),galleryImages:[...main.querySelectorAll('.product__media img')].map(x=>({w:x.naturalWidth,h:x.naturalHeight,alt:x.alt})).slice(0,12),videos:main.querySelectorAll('video').length,variantSelectors:main.querySelectorAll('variant-selects,variant-radios,select[name="id"]').length,descriptionLength:main.querySelector('.product__description')?.innerText.length||0,accordions:[...main.querySelectorAll('summary')].map(x=>x.innerText).slice(0,12)};
  });
  const desktop=await capture();
  await page.setViewportSize({width:390,height:844});
  const mobile=await capture();
  meshProductAudit.push({handle,desktop,mobile:{width:mobile.width,pageWidth:mobile.pageWidth,buttons:mobile.buttons}});
  if(handle==='diy-screw-drill-puzzle-toy')await page.screenshot({path:'mesh-drill-mobile-top.png',fullPage:false});
  await page.setViewportSize({width:1440,height:1000});
}
return meshProductAudit;
