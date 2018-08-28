# -*- coding: utf-8 -*-
# Created by bida on 2018/8/20
import asyncio
import time
from asyncio import coroutine
from random import randint


@coroutine
def start_state():
    print("Start State called")
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from start_state_2(input_value)
    else:
        result = yield from start_state_1(input_value)
    print(f'Resume of the Transition : \nStart State calling {result}')

@coroutine
def start_state_1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    time.sleep(1)
    print('....Evaluating...')
    if input_value == 0:
        result = yield from start_state_3(input_value)
    else:
        result = yield from start_state_2(input_value)
    result = f'state 1 calling {result}'
    return f'{output_value} {result}'

@coroutine
def start_state_2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    time.sleep(1)
    print('....Evaluating...')
    if input_value == 0:
        result = yield from start_state_1(input_value)
    else:
        result = yield from start_state_3(input_value)
    result = f'state 2 calling {result}'
    return f'{output_value} {result}'

@coroutine
def start_state_3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    time.sleep(1)
    print('....Evaluating...')
    if input_value == 0:
        result = yield from start_state_1(input_value)
    else:
        result = yield from end_state(input_value)
    result = f'state 3 calling {result}'
    return f'{output_value} {result}'

@coroutine
def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}'
    print('....Stop Evaluating...')
    return output_value

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
