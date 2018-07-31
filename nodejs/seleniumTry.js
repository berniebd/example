const {Builder, By, Key, until} = require('selenium-webdriver');
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// rl.question('Please input captcha characters:', (captcha) => {
//     // console.log('The captcha is: ${captcha}');
//     rl.close();
// });
let driver = new Builder()
    .forBrowser('firefox')
    .build();

console.log('1');
driver.get('http://www.baidu.com');
console.log('2');
driver.findElement(By.name('wd')).sendKeys('webdriver', Key.RETURN);
console.log('3');
driver.wait(until.titleIs('webdriver_百度搜索'), 1000);
console.log('4');
//driver.quit();
