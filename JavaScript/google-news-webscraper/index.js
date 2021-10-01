const puppeteer = require('puppeteer');
const chalk = require('chalk');

(async () => {
    const browser = await puppeteer.launch();

    const page = await browser.newPage();
    await page.goto('https://news.google.com/topstories');
    
    const headlines = await page.evaluate(() => Array.from(document.querySelectorAll('h3'), element => element.textContent));

    headlines.map(headline => console.log(chalk.bgHex('#FFFF').hex('#000F').bold(headline)+'\n'))

    await browser.close();
})();
