# -*- encoding:utf-8 -*-
import sys
import os
from keywords.cs.baseAction.csLogon import CsLogon
from parameters.cs import csBase
from utilities.httpRequest import HttpRequest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))

__author__ = 'bida'


class ProductQuery:
    def __init__(self):
        pass

    @staticmethod
    def query_product_info(product_id, city_id='9000', warehouse_id=''):
        """
        查询商品信息
        :param product_id:商品id
        :param city_id: 城市id
        :param warehouse_id: 仓库id
        :return:
        """
        print u'*' * 20 + u'查询商品信息'
        url = csBase.base_url + u'ProductInfoSearchBiz/QueryProductInfo'

        data = dict()
        data['product_id'] = product_id
        data['city_id'] = city_id
        data['warehouse_id'] = warehouse_id

        resp = HttpRequest.post_request(CsLogon.get_session(), url, data=data)

        print resp
        return resp


# print ProductQuery.query_product_info('1')
