# -*- coding: utf-8 -*-
import json
import re
from time import sleep

import requests
import scrapy
from scrapy import Request

from jd.items import JdItem


class JdcameraSpider(scrapy.Spider):
    name = 'jdCamera'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['https://list.jd.com/list.html?cat=652,654,832&page=1&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main']

    def parse(self, response):
        pages = response.xpath("//span[@class='p-skip']//b/text()").get()
        print('*'*100)
        print(pages)
        print('*'*100)
        # for i in range(1, int(pages) + 1):
        for i in range(int(pages)):
            yield Request(url=f'https://list.jd.com/list.html?cat=652,654,832&page={i+1}&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main',
                          callback=self.parse_camera)

    def parse_camera(self, response):
        ll = len(response.xpath("//div[contains(@class, 'j-sku-item')]").extract())
        # rr = response.xpath("//div[contains(@class, 'j-sku-item') and /div/i='自营']")
        # print(rr)
        # print(f"lenth is {ll}")
        for i in range(ll):
            name = response.xpath(f"(//div[contains(@class, 'j-sku-item')]/div[contains(@class, 'p-name')]/a/em)[{i+1}]/text()").get().strip()
            sku = response.xpath(f"(//div[contains(@class, 'j-sku-item')]//@data-sku)[{i+1}]").get()
            prices = requests.get(f'https://p.3.cn/prices/mgets?callback=jQuery4565604&type=1&area=12_988_40034_51587&skuIds=J_{sku}').text
            sale_price = json.loads(re.search(r'jQuery4565604\(\[(.*)\]\);', prices).groups()[0])['p']
            print(f'{name} - {sku} sale price is {sale_price}')
            # attributes = response.xpath(f"(//div[contains(@class, 'j-sku-item') and div/i='自营'])[{i}]//a[@class='attr']/@title")
            # print(attributes)


