# -*- coding: utf-8 -*-
# Created by bida on 2018/8/20
import asyncio
from asyncio import coroutine


@coroutine
def first_coroutine(future, N):
    count = 0
    for i in range(1, N + 1):
        count = count + 1
    yield from asyncio.sleep(4)
    future.set_result(f'first coroutine (sum of N integers) result = {count}')

@coroutine
def second_coroutine(future, N):
    count = 1
    for i in range(2, N + 1):
        count *= i
    yield from asyncio.sleep(4)
    future.set_result(f'second coroutine (factorial) result = {count}')

def get_result(future):
    print(future.result())

if __name__ == '__main__':
    N1 = 5
    N2 = 6

    loop = asyncio.get_event_loop()
    future_1 = asyncio.Future()
    future_2 = asyncio.Future()

    tasks = [
        first_coroutine(future_1, N1),
        second_coroutine(future_2, N2)
    ]

    future_1.add_done_callback(get_result)
    future_2.add_done_callback(get_result)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
