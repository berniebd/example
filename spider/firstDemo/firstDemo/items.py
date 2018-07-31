# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstdemoItem(scrapy.Item):
    # define the fields for your item here like:
    urlname = scrapy.Field()
    pass

class CategoryItem(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    pass
