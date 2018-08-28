# -*- coding: utf-8 -*-
# Created by bida on 2018/8/24
import fire


class Calculator(object):
    def double(self, number, count):
        return number * count

if __name__ == '__main__':
    fire.Fire(Calculator)