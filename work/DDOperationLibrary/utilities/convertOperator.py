# -*- encoding:utf-8 -*-
from lxml import etree
import demjson

__author__ = 'bida'


class ConvertOperator:
    def __init__(self):
        pass

    @staticmethod
    def convert_json_string_to_object(content):
        """
        将字符串格式相应结果转换为python dict对象
        :param content:
        :return:
        """
        try:
            result = demjson.decode(content)
            return result
        except Exception, e:
            print e
            print '待转换内容不是json格式字符串'

    @staticmethod
    def convert_html_to_list(content):
        """
        将html格式相应结果转换为python list对象，list的每一个元素为dict
        :param content:
        :return:
        """
        try:
            doc = etree.fromstring(content.replace('\t', '').replace('<br>', '<br/>').replace('</br>', '<br/>'))
            heads_etree = doc.xpath('//table/thead/tr/th')
            heads_list = list()
            for head in heads_etree:
                heads_list.append(head.text.strip())
            length = len(heads_list)
            rows_etree = doc.xpath('//table/tr')

            result = list()

            for row in rows_etree:
                row_dict = dict()
                for index in range(length):
                    if row[index].text == '' or row[index].text is None:
                        row_dict[heads_list[index]] = ''
                    else:
                        row_dict[heads_list[index]] = row[index].text.strip()
                result.append(row_dict)

            return result
        except Exception, e:
            print e
            print '待转换内容不是html格式字符串'
