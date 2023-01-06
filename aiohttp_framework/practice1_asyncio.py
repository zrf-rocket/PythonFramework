import asyncio
import aiohttp
import aiofiles
import aiosignal
import time


# 创建获取网页的函数，传递参数为session和一个url
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    # 创建session并把session和需要获取网页的url作为参数传递给协程函数fetch，协程函数把网页文本下载下来
    async with aiohttp.ClientSession() as session:
        html = await fetch(session=session, url="http://httpbin.org/headers")
        print(html)



if __name__ == '__main__':
    asyncio.run(main())
