# -*- coding: utf-8 -*-
# Created by bida on 2018/8/31
import json
import re
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def parse(sku):
    result = requests.get(f'https://p.3.cn/prices/mgets?callback=jQuery4565604&type=1&area=12_988_40034_51587&skuIds=J_{sku}')
    return json.loads(re.search(r'jQuery4565604\(\[(.*)\]\);', result.text).groups()[0])

if __name__ == '__main__':
    chrome_option = Options()
    # chrome_option.add_argument('--headless')
    chrome_option.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    driver = webdriver.Chrome(executable_path='/Users/bida/Tool/selenium/chromedriver',
                              chrome_options=chrome_option)
    driver.get('https://list.jd.com/list.html?cat=652,654,832&page=1&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main')
    pages = driver.find_element_by_xpath("//span[@class='p-skip']//b").text
    for page in range(int(pages)):
        driver.get(f'https://list.jd.com/list.html?cat=652,654,832&page={page+1}&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main')
        items = driver.find_elements_by_xpath("//div[contains(@class, 'j-sku-item') and div/i='自营']")
        ll = len(items)
        for i in range(ll):
            name = driver.find_element_by_xpath(f"(//div[contains(@class, 'j-sku-item') and div/i='自营'])[{i+1}]//div[contains(@class, 'p-name')]/a/em").text.strip()
            sale_price = driver.find_element_by_xpath(f"(//div[contains(@class, 'j-sku-item') and div/i='自营'])[{i+1}]//strong[@class='J_price']/i").text.strip()
            print(f"{name} sale price is {sale_price}")


