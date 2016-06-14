# -*- encoding:utf-8 -*-
from abstractClassTry.balckSheep import BlackSheep
from abstractClassTry.sheep import Sheep

__author__ = 'bida'

if __name__ == '__main__':
    Sheep.register(BlackSheep)

    assert issubclass(BlackSheep, Sheep)
    assert isinstance(BlackSheep(), Sheep)