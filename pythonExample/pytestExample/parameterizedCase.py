# -*- encoding:utf-8 -*-
import logging

__author__ = 'bida'
import pytest

@pytest.mark.parametrize("test_input, expected", [
    ("3+5", 8),
    ("1+4", 6),
    ("2+4", 6),
    ("3+4", 6),
    ("4+4", 6),
    ("5+4", 6),
    ("6+4", 6),
    ("7+4", 6),
    ("8+4", 6),
    ("6*9", 42)
])
def test_eval(test_input, expected):
    logging.info(test_input)
    logging.info(expected)

    assert eval(test_input) == expected
