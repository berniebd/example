# -*- coding: utf-8 -*-
# Created by bida on 2018/8/3
from concurrent import futures
from time import sleep

def say(m, n):
    for _ in range(5):
        print(m * n)
        sleep(1)
    return f'finished {m}, {n}'

data = [(1, 2), (2, 3), (3, 4), (4, 5)]
datam = [1, 2, 3, 4]
datan = [2, 3, 4, 5]

if __name__ == '__main__':
    workers = 3
    with futures.ProcessPoolExecutor(max_workers=workers) as executor:
        futures = executor.map(say, datam, datan)
        future = executor.submit(say, 3, 5)
        futures = [executor.submit(say, item[0], item[1]) for item in data]
        for future in futures:
            print(future)
