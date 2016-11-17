# -*- encoding:utf-8 -*-
from abc import ABCMeta, abstractmethod

__author__ = 'bida'


class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def get_radius(self):
        pass


class FishPizza(Pizza):
    def get_radius(self):
        print('get radius')


    def print_radius(self):
        print('print radius')

if __name__ == '__main__':
    fish_pizza = FishPizza()
    fish_pizza.get_radius()
    fish_pizza.print_radius()