# -*- encoding:utf-8 -*-
from parameters.tms import tmsBase
from utilities.Singleton import Singleton
from utilities.httpRequest import HttpRequest
from parameters.tms.tmsBase import user
import requests

__author__ = 'bida'


class TmsLogin(Singleton):
    _sessions = dict()

    def __init__(self):
        pass

    @classmethod
    def get_session(cls, account):
        if account not in cls._sessions.keys():
            print u'*' * 20 + unicode(account) + u'用户: ' + user[account]['username'] + u' 登陆系统'
            session = requests.session()

            data = dict()
            data['username_'] = user[account]['username']
            data['password_'] = user[account]['password']
            data['randCode'] = '1234'

            resp = HttpRequest.post_request(session, tmsBase.base_url + '/security_check_', data=data)
            if u'用户名或密码错误' in resp:
                raise StandardError(u'用户名或密码错误')

            print resp
            cls._sessions[account] = session

        return cls._sessions[account]
