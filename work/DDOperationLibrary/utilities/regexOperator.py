import re

__author__ = 'bida'

class RegexOperator:
    def __init__(self):
        pass

    @staticmethod
    def get_regex_content(regex, string):
        try:
            p = re.compile(regex)
            return p.findall(string)[0]
        except Exception, e:
            print e

    @staticmethod
    def get_regex_content_all(regrex,string):
        try:
            p = re.compile(regrex)
            return p.findall(string)
        except Exception, e:
            print e