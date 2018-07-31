# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class FirstdemoPipeline(object):
    def process_item(self, item, spider):
        return item

class BerniePipeline(object):
    def __init__(self):
        self.txt_file = codecs.open('bernie.txt', 'wb', encoding='utf-8')
        self.json_file = codecs.open('bernie.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        self.txt_file.write(str(item) + '\n')
        self.json_file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.txt_file.close()
        self.json_file.close()
