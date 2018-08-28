# -*- coding: utf-8 -*-
# Created by bida on 2018/8/3

import asyncio
import aiohttp
import time


async def download(url): # 通过async def定义的函数是原生的协程对象
    print("get: %s" % url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            # response = await resp.read()

# 此处的封装不再需要
# async def wait_download(url):
#    await download(url) # 这里download(url)就是一个原生的协程对象
#    print("get {} data complete.".format(url))


async def main():
    start = time.time()
    await asyncio.wait([
        download("http://www.163.com"),
        download("http://www.mi.com"),
        download("http://www.baidu.com")])
    end = time.time()
    print("Complete in {} seconds".format(end - start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

