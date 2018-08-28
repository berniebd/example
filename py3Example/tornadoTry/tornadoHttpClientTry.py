# -*- coding: utf-8 -*-
# Created by bida on 2018/8/14
from tornado.concurrent import Future
from tornado.httpclient import HTTPClient, AsyncHTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body

async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body

# def asynchronous_fetch(url):
#     http_client = AsyncHTTPClient()
#     my_future = Future()
#     fetch_future = http_client.fetch(url)
#     fetch_future.add_done_callback(
#         lambda f: my_future.set_result(f.result)
#     )
#     return my_future



if __name__ == '__main__':
    result = synchronous_fetch('http://www.baidu.com')
    print(result)
    print(type(result))
    print(result.decode())
    print(type(result.decode()))
    print('*'*100)

    r = asynchronous_fetch('https://www.baidu.com')
    print(r)


