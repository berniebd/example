# -*- coding: utf-8 -*-
# Created by bida on 2018/8/6
from celeryTry.mytasks import adds

def deal_err():
    print('deal error!')

if __name__ == '__main__':
    r = adds.delay('aa', 'bb')
    print(r)


    r2 = adds.apply_async(('a', 'b'))
    print(r2)

    r3 = adds.apply_async(('a', 'b'), link=[adds.s('cc'), adds.s('dd')])
    print(r3)
    print(r3)

    r4 = adds.apply_async(('a', 'b'))
    print(r4)