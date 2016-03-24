# -*- encoding:utf-8 -*-
import json

import chardet
import sys

__author__ = 'bida'


class HttpRequest():
    def __init__(self):
        pass

    @staticmethod
    def get_request(session, url, params=None):
        print '----------%s' % url
        params = params
        if params:
            for key, value in params.iteritems():
                print '----------%s : %s' % (key, value)
        try:
            resp = session.get(url, params=params).text
            return resp
        except Exception, e:
            print e

    @staticmethod
    def post_request(session, url, data=None, headers=None, files=None):
        print '----------%s' % url
        params = data
        if params:
            for key, value in params.iteritems():
                print '----------%s : %s' % (key, value)
        try:
            response = session.post(url, data=params, headers=headers, files=files)
            if response.status_code != 200:
                raise StandardError(u'********************无法访问url地址: ' + url)
            else:
                return response.text
        except Exception, e:
            print e

    @staticmethod
    def post_request_for_json_data(session, url, data=None):
        print '----------%s' % url
        params = data
        if params:
            for key, value in params.iteritems():
                print '----------%s : %s' % (key, value)

        headers = {'Content-Type': 'application/json'}

        try:
            resp = session.post(url, data=json.dumps(data), headers=headers).text
            return resp
        except Exception, e:
            print e
