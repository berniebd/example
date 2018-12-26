# -*- coding: utf-8 -*-
# Created by bida on 2018/9/17
import pytest
from arrow import Arrow


@pytest.mark.parametrize('input, expected', [('3*4', 12) for _ in range(10)])
def test_a(input, expected):
    print(f'a-{Arrow.now().format("HH:mm:ss.SSS")}')
    assert eval(input) == expected

@pytest.mark.parametrize('input, expected', [('3*4', 12) for _ in range(10)])
def test_b(input, expected):
    print(f'b-{Arrow.now().format("HH:mm:ss.SSS")}')
    assert eval(input) == expected

@pytest.mark.parametrize('input, expected', [('3*4', 12) for _ in range(10)])
def test_c(input, expected):
    print(f'c-{Arrow.now().format("HH:mm:ss.SSS")}')
    assert eval(input) == expected


# def test_a():
#     assert False


if __name__ == '__main__':
    pytest.main(['-n 2', 'testOne.py'])
