await page.goto('https://2zs0x1-0z.myshopify.com/products/diy-screw-drill-puzzle-toy',{waitUntil:'domcontentloaded'});
await page.setViewportSize({width:390,height:844});
const images=await page.locator('.product__media img').evaluateAll(async xs=>Promise.all(xs.map(async x=>{try{await x.decode();return {alt:x.alt,decoded:true,w:x.naturalWidth,h:x.naturalHeight};}catch{return {alt:x.alt,decoded:false};}})));
await page.getByRole('button',{name:'Cart',exact:true}).click();
return {images,observation:await tabbit.observe({frames:'none',maxChars:3500})};
