# -*- encoding:utf-8 -*-
import abc

__author__ = 'bida'


class Sheep(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_size(self):
        return

    # @abc.abstractmethod
    # def load(self, input):
    #     return
    #
    # @abc.abstractmethod
    # def save(self, output, data):
    #     return