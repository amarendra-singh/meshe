await page.goto('https://2zs0x1-0z.myshopify.com/',{waitUntil:'domcontentloaded'});
return {observation:await tabbit.observe({frames:'none',maxChars:6500}),links:await page.locator('a[href*="/products/"]').evaluateAll(xs=>xs.map(x=>({text:x.innerText,url:x.href})).slice(0,35))};
