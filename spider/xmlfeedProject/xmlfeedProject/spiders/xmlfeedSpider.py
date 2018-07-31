# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider

from xmlfeedProject.items import MyxmlItem


class XmlfeedspiderSpider(XMLFeedSpider):
    name = 'xmlfeedSpider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, selector):
        i = MyxmlItem()
        i['title'] = selector.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = selector.xpath("/rss/channel/item/link/text()").extract()
        i['author'] = selector.xpath("/rss/channel/item/author/text()")
        for j in range(len(i['title'])):
            print('第{}篇文章'.format(j+1))
            print('标题是：{}'.format(i['title'][j]))
            print('链接是: {}'.format(i['link'][j]))
            print('作者是: {}'.format(i['author'][j]))
        return i
