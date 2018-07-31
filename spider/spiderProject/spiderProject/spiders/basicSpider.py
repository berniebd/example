# -*- coding: utf-8 -*-
import scrapy


class BasicspiderSpider(scrapy.Spider):
    name = 'basicSpider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
