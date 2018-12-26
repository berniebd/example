# -*- coding: utf-8 -*-
# Created by bida on 2018/12/14
import sys

if __name__ == '__main__':
    try:
        1 / 0
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback_details = {
            'filename': exc_traceback.tb_frame.f_code.co_filename,
            'lineno': exc_traceback.tb_lineno,
            'name': exc_traceback.tb_frame.f_code.co_name,
            'type': exc_type.__name__,
        }
        del( exc_type, exc_value, exc_traceback)
        print()