# -*- encoding:utf-8 -*-
from common.httpRequest import HttpRequest
from keywords.portal.portalLogin import PortalLogin
from parameter import portal

__author__ = 'bida'


class Promotion:
    def __init__(self):
        pass

    @classmethod
    def announce(cls):
        msg = u'展示促销信息'
        data = {u'requestBodyJson': {}, u'transCode': u'TY1019'}
        response = HttpRequest.post_data(PortalLogin.get_session(), portal.url, json_data=data, msg=msg)
        return response


if __name__ == '__main__':
    Promotion.announce()
