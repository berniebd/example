# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

from arrow import Arrow


class JdPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('camera.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('create table if not exists camera (name text, brand text, price real, crawl_time datetime)')

    def process_item(self, item, spider):
        name = item['name']
        brand = item['brand']
        price = item['price']
        crawl_time = Arrow.now().format('YYYY-MM-DD HH:mi:ss')
        self.cursor.execute(f"insert into camera values('{name}', '{brand}', '{price}', '{crawl_time}')")
        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
