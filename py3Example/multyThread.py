# -*- encoding:utf-8 -*-
import random
import threading

__author__ = 'bida'


results = []
def compute():
    results.append(sum(random.randint(1, 100) for i in range(1000000)))

workers = [threading.Thread(target=compute) for i in range(8)]

for worker in workers:
    worker.start()

for worker in workers:
    worker.join()

print('results:{0}'.format(results))