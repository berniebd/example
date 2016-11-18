# -*- encoding:utf-8 -*-
from convertOperator import ConvertOperator
from sshOperator import SshOperator
from regexOperator import RegexOperator
from dbOperator import DbOperator

__author__ = 'bida'


class Utilities(ConvertOperator,
                SshOperator,
                RegexOperator,
                DbOperator):
    def __init__(self):
        pass
