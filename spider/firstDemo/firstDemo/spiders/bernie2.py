# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from firstDemo.items import CategoryItem


class Bernie2Spider(CrawlSpider):
    name = 'bernie2'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com',]

    def parse(self, response):
        main_item = CategoryItem()
        main_item['title'] = response.xpath('//title/text()').get()
        yield main_item
        for href in response.xpath("//div[@class='fs_col1']//a/@href"):
            yield Request(url='https://{0}'.format(href.get()),
                          callback=self.parse_channel)

    def parse_channel(self, response):
        category_item = CategoryItem()
        category_item['title'] = response.xpath('//title/text()').get()
        yield category_item
        for sub_category_url in response.xpath("//p[@class='item_header_sublinks']/a/@href"):
            print('category:', sub_category_url.get())
            yield Request(url=sub_category_url.get(),
                          callback=self.parse_sub_channel,
                          meta={'handle_httpstatus_list': [302]},
                          dont_filter=True)


    def parse_sub_channel(self, response):
        sub_category_item = CategoryItem()
        sub_category_item['title'] = response.xpath('//title/text()').get()
        print('sub_category:', sub_category_item['title'])
        yield sub_category_item






