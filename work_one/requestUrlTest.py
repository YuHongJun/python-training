#1.单进程：
# import requests,time
# start_time=time.time()
# [requests.get('http://www.liaoxuefeng.com/') for x in range(100)]
# print("用时：{}秒".format(time.time()-start_time))

#2.多线程

# import threadpool,requests
# def run(url):
#     r=requests.get(url=url)
# pool=threadpool.ThreadPool(10)
# reqs=threadpool.makeRequests(run,['http://www.liaoxuefeng.com' for x in range(100)])
# [pool.putRequest(x) for x in reqs]
# pool.wait()
# print("用时：{}秒".format(time.time()-start_time))

#3.多进程

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import multiprocessing,time,requests
# start_time=time.time()
# def run(url):
#     r=requests.get(url=url)
#     #print(1)
# if __name__=='__main__':
#     pool=multiprocessing.Pool(10)
#     [pool.apply_async(run,args=('http://www.liaoxuefeng.com',)) for x in range(100)]
#     pool.close()
#     pool.join()
#     print("用时：{}秒".format(time.time()-start_time))

#4.协程（异步IO）

import asyncio, aiohttp, time
start_time=time.time()
async def run(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            pass
loop=asyncio.get_event_loop()
tasks=[asyncio.ensure_future(run('http://www.liaoxuefeng.com')) for x in range(100)]
loop.run_until_complete(asyncio.wait(tasks))
print("用时：{}秒".format(time.time()-start_time))