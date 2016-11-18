# -*- encoding:utf-8 -*-
import json

import demjson
import simplejson

__author__ = 'bida'


class HttpRequest():
    def __init__(self):
        pass

    @staticmethod
    def get_request(session, url, params=None, msg=''):
        print '*' * 20 + msg
        print '----------%s' % url
        params = params
        if params:
            for key, value in params.iteritems():
                print '----------%s : %s' % (key, value)
        try:
            resp = session.get(url, params=params)
            return resp
        except Exception, e:
            print e

    @staticmethod
    def post_data(session, url, data=None, json_data=None, headers=None, files=None, msg=u''):
        print u'*' * 20 + msg
        print u'----------%s' % url

        if data is not None:
            print u'----------post data:\n%s' % data
        if json_data is not None:
            print u'----------post json format data:\n%s' % simplejson.dumps(json_data, 'utf-8').decode()
        try:
            response = session.post(url, data=data, json=json_data, headers=headers, files=files)
            if response.status_code != 200:
                raise StandardError(u'********************无法访问url地址: ' + url)
            else:
                print '--------response text:\n%s' % response.text
                return response
        except Exception, e:
            print e.message
