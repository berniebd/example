# -*- encoding:utf-8 -*-
import requests
from common.httpRequest import HttpRequest
from common.singleton import Singleton
from parameter.portal import envConfig


class PortalLogin(Singleton):
    _session = None

    def __init__(self):
        pass

    @classmethod
    def get_session(cls):
        """
        登陆经销商门户网站
        :return:
        """
        if cls._session is None:
            msg = u'*' * 20 + u'用户: 【' + envConfig.username + u'】 登陆系统，登录密码为【' + envConfig.password + u'】'
            session = requests.session()
            request_body_json = {'password': envConfig.password, 'userCode': envConfig.username, 'redirect': ''}
            data = {'requestBodyJson': request_body_json, 'transCode': 'TY1015'}
            response = HttpRequest.post_data(session, envConfig.url, json_data=data, msg=msg)
            if u'用户名或密码不正确' in response.text:
                raise StandardError(u'用户名或密码不正确')

            cls._session = session
        return cls._session
