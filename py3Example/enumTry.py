# -*- encoding:utf-8 -*-
from enum import Enum

__auth__ = 'bida'

class Color(Enum):
    RED = 1
    BLUE = 2
    Black = 3

print(Color.RED)
print(type(Color.RED))
print(repr(Color.RED))
print(Color.RED.name)
print(Color.RED.value)
print(Color.__members__)
print(Color.__members__.items())