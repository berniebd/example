# -*- encoding:utf-8 -*-
import arrow

__author__ = 'bida'

if __name__ == '__main__':
    utc = arrow.utcnow()
    print utc

    print utc.replace(hours=-5)
    print utc.replace(days=3)

    local = utc.to('Asia/Shanghai')
    print local

    print local.timestamp

    print local.format()
    print local.format('YYYY-MM-DD HH:mm:ss SSSSSS ZZ')
    print local.format('YYYY-MM-DD HH:mm:ss SSS ZZ')

    print local.replace(days=-1).humanize(locale='zh_cn')
    print local.humanize(locale='zh_cn')