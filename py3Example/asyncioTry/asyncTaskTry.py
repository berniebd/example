# -*- coding: utf-8 -*-
# Created by bida on 2018/8/20
import asyncio
from asyncio import coroutine


@coroutine
def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print(f'Asyncio.Task:Computing factorial {i}')
        yield from asyncio.sleep(1)
        f *= i
    print(f'Asyncio.Task - factorial({number}) = {f}')


@coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print(f"Asyncio.Task:Computing fibonacci {i}")
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print(f'Asyncio.Task - fibonacci({number}) = {a}')

@coroutine
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n-i+1) / i
        print(f'Asyncio.Task: Computing binomialCoeff {i}')
        yield from asyncio.sleep(1)
    print(f'Asyncio.Task:Computing binomialCoeff({n}, {k}) = {result}')

if __name__ == '__main__':
    tasks = [
        asyncio.Task(factorial(10)),
        asyncio.Task(fibonacci(10)),
        asyncio.Task(binomialCoeff(20, 10))
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()