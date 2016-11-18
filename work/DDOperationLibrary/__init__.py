# -*- encoding:utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from keywords import Keywords
from utilities import Utilities

__author__ = 'bida'

_version_ = '1.0'


class DDOperationLibrary(Utilities,
                         Keywords):
    def __init__(self):
        pass

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION = _version_
