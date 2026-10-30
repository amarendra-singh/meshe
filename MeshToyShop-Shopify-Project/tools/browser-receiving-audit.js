const base = globalThis.meshHandoffBaseUrl || new URL('./', page.url()).href;
if (!base.startsWith('file:')) throw new Error('Open START-HERE.html first.');
await page.setViewportSize({width:1440,height:1000});
const output={pages:[],wireframes:[]};
for(const name of ['FINAL-MOCKUPS.html','ASSET-LIBRARY.html','TECHNICAL-HANDBOOK.html']) {
  await page.goto(new URL(name,base).href,{waitUntil:'load'});
  await page.evaluate(async()=>{ await Promise.all([...document.images].map(img=>{img.loading='eager';return img.decode();})); });
  output.pages.push(await page.evaluate(name=>({name,images:document.images.length,loaded:[...document.images].every(x=>x.complete&&x.naturalWidth>0),chapters:document.querySelectorAll('article').length,overflow:document.documentElement.scrollWidth>innerWidth}),name));
}
await page.goto(new URL('wireframes/index.html',base).href,{waitUntil:'load'});
for(const width of [320,390,749,750,768,989,990,1280]) {
  await page.evaluate(w=>document.querySelector('#canvas').style.width=w+'px',width);
  output.wireframes.push(await page.evaluate(()=>{
    const c=document.querySelector('#canvas'),h=document.querySelector('.hero-area');
    const p=getComputedStyle(document.querySelector('.hero-copy'),'::after');
    const cols=s=>getComputedStyle(document.querySelector(s)).gridTemplateColumns.split(' ').length;
    const hw=h.getBoundingClientRect().width;
    return {width:c.clientWidth,scroll:c.scrollWidth,sections:c.querySelectorAll('.wf').length,heroWidth:hw,curveDipPx:-parseFloat(p.bottom),curveRatio:-parseFloat(p.bottom)/hw,categories:cols('.categories'),discovery:cols('.products'),growth:cols('.growth-grid'),faq:cols('.faq-groups'),faqQuestions:document.querySelectorAll('.faq-question').length};
  }));
}
await page.getByRole('button',{name:'Mobile 390',exact:true}).click();
await page.evaluate(()=>scrollTo(0,document.querySelector('#wf-S02').getBoundingClientRect().top+scrollY-80));
await page.screenshot({path:'receiving-audit-mobile.png',fullPage:false});
await page.goto(new URL('TECHNICAL-HANDBOOK.html',base).href,{waitUntil:'load'});
await page.setViewportSize({width:390,height:844});
output.mobileHandbook=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,chapters:document.querySelectorAll('article').length}));
await page.screenshot({path:'receiving-audit-handbook.png',fullPage:false});
await page.setViewportSize({width:1440,height:1000});
await page.goto(new URL('START-HERE.html',base).href,{waitUntil:'load'});
return output;
