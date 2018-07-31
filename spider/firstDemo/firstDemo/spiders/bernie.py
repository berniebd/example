# -*- encoding:utf-8 -*-
from scrapy import Spider

from firstDemo.items import CategoryItem

__auth__ = 'bida'

class FirstSpider(Spider):
    name = 'bernie'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com',]

    def parse(self, response):
        results = []
        for category in response.xpath("//div[@class='fs_col1']//a"):
            category_item = CategoryItem()
            category_item['category'] = category.xpath('text()').extract()[0]
            category_item['url'] = category.xpath('@href').extract()[0]
            results.append(category_item)
            print(category_item)
        print(results)
        return results