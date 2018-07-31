# -*- encoding:utf-8 -*-
from collections import namedtuple

__auth__ = 'bida'

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    print(results)
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':
        [45.5, 56.4, 33.4, 56.2, 56.6, 45.3],
    'girls;m':
        [1.5, 1.56, 1.67, 1.67, 1.68, 1.89],
    'boys;kg':
        [67.7, 87.7, 76.6, 65.4, 67.7, 78.7],
    'boys;m':
        [1.87, 1.87, 1.76, 1.67, 1.90, 1.67, 1.90]
}

if __name__ == '__main__':
    main(data)