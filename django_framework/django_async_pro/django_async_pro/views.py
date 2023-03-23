import asyncio
from time import sleep

import httpx
from django.http import HttpResponse


# 异步视图 - 无异步或同步任务
async def index(request):
    return HttpResponse("this is django3.* async Django views")


# 异步任务
async def http_call_async():
    for num in range(6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


# 同步任务
def http_call_sync():
    for num in range(6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


# 异步视图 - 调用异步任务
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('async view call async request')


# 同步视图 - 调用普通同步任务
def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking HTTP request')


# 导入 同步转异步包
from asgiref.sync import async_to_sync, sync_to_async
# async_to_sync 将异步转同步
# sync_to_async 将同步转异步

# 同步转异步(sync to async)
async def async_with_sync_view(request):
    loop = asyncio.get_event_loop()
    async_function = sync_to_async(http_call_sync)
    loop.create_task(async_function())
    return HttpResponse("Non-blocking HTTP request sync to async")


















