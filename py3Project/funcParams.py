# -*- encoding:utf-8 -*-
__author__ = 'bida'
from lxml import etree


doc = etree.parse('complicate.xml')
items = doc.xpath('//COMCODE')
for item in items:
    print(item.text)