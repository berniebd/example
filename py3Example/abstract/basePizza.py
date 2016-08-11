# -*- encoding:utf-8 -*-
import abc

__author__ = 'bida'


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
        """method that should do nothing"""

if __name__ == '__main__':
    BasePizza().get_radius()