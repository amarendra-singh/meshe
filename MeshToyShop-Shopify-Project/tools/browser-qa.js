const currentHandoffUrl = new URL(page.url());
const handoffBase = globalThis.meshHandoffBaseUrl || new URL(currentHandoffUrl.pathname.endsWith('/wireframes/index.html') ? '../' : './', currentHandoffUrl).href;
if (!handoffBase.startsWith('file:')) throw new Error('Open a local handoff HTML page first, or supply globalThis.meshHandoffBaseUrl.');
const handoffUrl = relative => new URL(relative, handoffBase).href;
await page.setViewportSize({width:1440,height:1000});
await page.goto(handoffUrl('START-HERE.html'),{waitUntil:'load'});
for (const img of await page.locator('.board img').all()) {
  await img.scrollIntoViewIfNeeded();
  await img.evaluate(el => el.decode());
}
const gallery = await page.evaluate(() => ({title:document.title,boards:document.querySelectorAll('.board img').length,loaded:[...document.querySelectorAll('.board img')].every(x=>x.complete&&x.naturalWidth>0),width:innerWidth,documentWidth:document.documentElement.scrollWidth}));
await page.evaluate(()=>scrollTo(0,0));
await page.screenshot({path:'gallery-desktop.png',fullPage:false});
await page.goto(handoffUrl('wireframes/index.html'),{waitUntil:'load'});
const checks=[];
for(const width of [1280,768,390,320]) {
  await page.locator('[data-width="'+width+'"]').click();
  checks.push(await page.evaluate(()=>{
    const c=document.querySelector('#canvas');
    const cols=s=>getComputedStyle(document.querySelector(s)).gridTemplateColumns;
    const w=s=>Math.round(document.querySelector(s).getBoundingClientRect().width);
    return {canvasWidth:w('#canvas'),canvasClient:c.clientWidth,canvasScroll:c.scrollWidth,sections:c.querySelectorAll('.wf').length,categories:cols('.categories'),discovery:cols('.products'),faq:cols('.faq-groups'),growth:cols('.growth-grid'),videoCard:w('.rail-card'),faqQuestions:document.querySelectorAll('.faq-question').length};
  }));
  if(width===1280 || width===390){
    await page.locator('#canvas').scrollIntoViewIfNeeded();
    await page.evaluate(()=>scrollTo(0,document.querySelector('#canvas').getBoundingClientRect().top+scrollY-80));
    await page.screenshot({path:'wireframe-'+width+'.png',fullPage:false});
  }
}
await page.goto(handoffUrl('TECHNICAL-HANDBOOK.html'),{waitUntil:'load'});
await page.setViewportSize({width:390,height:844});
const handbook=await page.evaluate(()=>({chapters:document.querySelectorAll('article').length,width:innerWidth,documentWidth:document.documentElement.scrollWidth,brokenImages:[...document.images].filter(x=>x.complete&&!x.naturalWidth).length}));
await page.screenshot({path:'handbook-mobile.png',fullPage:false});
await page.setViewportSize({width:1440,height:1000});
await page.goto(handoffUrl('START-HERE.html'),{waitUntil:'load'});
return {gallery,wireframes:checks,handbook};
