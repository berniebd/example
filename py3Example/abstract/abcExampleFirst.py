# -*- encoding:utf-8 -*-
__author__ = 'bida'

class Pizza(object):
    @staticmethod
    def get_radius():
        raise NotImplementedError

class FishPizza(Pizza):
    @staticmethod
    def get_radius():
        print('FishPizza')

if __name__ == '__main__':
    # Pizza()
    # Pizza().get_radius()
    fish_pizza = FishPizza()
    fish_pizza.get_radius()