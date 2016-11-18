# -*- encoding:utf-8 -*-
from parameters.cs import csBase
from utilities.httpRequest import HttpRequest
import requests

__author__ = 'bida'


class CsLogon:
    def __init__(self):
        pass

    __session = None

    @classmethod
    def get_session(cls):
        if cls.__session is None:
            print u'*' * 20 + u'登陆客服系统'
            cls.__session = requests.session()

            data = dict()
            data['username'] = csBase.username
            data['password'] = csBase.password

            url = csBase.base_url + u'Common/LoginAction'

            resp = HttpRequest.post_request(cls.__session, url, data=data)
            if u'用户名或密码错误' in resp:
                raise StandardError(u'用户名或密码错误')

            # print resp
        return cls.__session


# CsLogon().get_session()
