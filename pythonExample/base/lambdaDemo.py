# -*- encoding:utf-8 -*-
__author__ = 'bida'

s = 'amc,'
nums = range(3)
g = lambda x, y: s.replace('m', str(x)) + s.replace('m', str(y))
print reduce(g, nums)


# nums = range(2, 49)
# for i in range(2, 8):
#     nums = filter(lambda x: x == i or x % i, nums)
# print nums


# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# print filter(lambda x: x % 3 == 0, foo)

# print [x for x in foo if x % 3 == 0]

# def make_increment (n):return lambda x:x + n
#
# f = make_increment(3)
# g = make_increment(6)
#
# print f(42)
# print g(42)
# print make_increment(12)(22)