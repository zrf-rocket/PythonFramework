from tornado import (
    gen,  # 基于生成器的协同程序
    locks,  # 同步原语
    queues,  # 协程的异步队列
    process  # 多个进程的实用程序，包括将服务器复刻为多个进程和管理子进程。
)
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient


# 基于 python generator 实现的异步编程接口。通过该模块提供的 coroutine （注：这里 coroutine 指的是 ”协程” 概念而不是后面具体实现的
# decorator：@gen.decorator），大大简化了在 Tornado 中编写异步代码的工作 —— 支持 “同步方式编写异步代码” ，避免编写烦人的回调函数。

# 协同程序提供了一种在异步环境中工作比链接回调更简单的方法。使用协程的代码在技术上是异步的，但它是作为单个生成器而不是单独的函数集合编写的。

# 基于协程的处理程序
class IndexHandlerGen(RequestHandler):
    @gen.coroutine
    def get(self):
        # 与 django 和 flask 不一样，tornado 既可以是 wsgi 应用，也可以是 wsgi 服务。
        http_client = AsyncHTTPClient()  # 是Tornado的tornado.httpclient提供了一个基于框架本身的异步HTTP客户端。
        response = yield http_client.fetch("http://example.com")
        print(response)
        self.render("response.html", **{"response": response})

# Tornado中的异步函数返回 Awaitable 或 Future ；生成此对象将返回其结果。
# 还可以生成其他可扩展对象的列表或dict，这些对象将同时启动并并行运行；结果列表或dict将在完成后返回
class HandlerGenOthers(RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response1, response2 = yield [http_client.fetch(""),
                                      http_client.fetch("")]
        response_dict = yield dict(response3=http_client.fetch(""), response4=http_client.fetch(""))
        response3 = response_dict["response3"]
        response4 = response_dict["response4"]


# 本模块中的“decorator and generator”方法是本机协程（使用 async def 和 await ）在python 3.5中引入。不需要与旧版本的Python兼容的应用程序应该使用本机协程。这个模块的某些部分对于本机协程仍然有用，特别是 multi ， sleep ， WaitIterator 和 with_timeout . 其中一些功能在 asyncio 也可以使用模块，尽管这两个模块未必100%兼容。
# gen.sleep(1)
# gen.multi()
# gen.WaitIterator
# gen.with_timeout()
#




# gen.is_coroutine_function

# gen.chain_future
# gen.singledispatch()
