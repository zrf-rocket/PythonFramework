# Python_Framework

## 介绍
1. Python框架：Flask、Django、Tornado、web.py、Falcon、Bottle、Asgineer、apidaora 、Sanic、Starlette、Fastapi、Aiohttp、Quart、cyclone、Twisted、Buildbot。
2. 模板引擎：jinja2、mako、Chameleon、cheetah。
3. 定时任务：celery 、airflow、apscheduler。

## 什么是Web Framework？
1. Python3 Web框架（Web framework）开发框架，用来支持动态网站、网络应用和网络服务的开发。这大多数的web框架提供了一套开发和部署网站的方式，也为web行为提供了一套通用的方法。web框架已经实现了很多功能，开发人员使用框架提供的方法并且完成自己的业务逻辑，就能快速开发web应用。浏览器和服务器的通信是基于HTTP协议进行通信的。
2. Web Application Framework（Web应用程序框架）或简单的Web Framework（Web框架）表示一个库和模块的集合，使Web应用程序开发人员能够编写应用程序，而不必担心协议，线程管理等细节。

## WSGI
Web Server Gateway Interface（Web服务器网关接口，WSGI）已被用作Python Web应用程序开发的标准。 WSGI是Web服务器和Web应用程序之间通用接口的规范。

## 安装教程
> 虚拟环境可以使用virtualenv、pipenv：virtualenv c:\env
> 
> 进入虚拟环境：c:\env\Scripts\activate
>
> 安装依赖包：pip install -r requirements_base.txt


## 语言框架优缺点
1. Aiohttp
* 优点：用于 asyncio 和 Python 的异步 HTTP 客户端 / 服务器。支持客户端和 HTTP 服务器，支持开箱即用的服务器 WebSockets 和客户端 WebSockets，没有回调地狱。Web 服务器具有中间件、信号和可插入路由。
* 缺点：根据 RFC 7231 aiohttp 2.0 版本后做了接受 HEAD 请求的调整，使用之前版本并且用 add_ get () 添加的请求，如果使用 HEAD 方法访问会返回 405。如果处理器会写入很多响应体内容，你可以在执行 HEAD 方法时跳过处理响应体内容以提高执行效率。

2. Bottle
*  优点：Bottle 是一个用于 Python 的快速、简单和轻量级的 WSGI 微型网络框架。它作为单个文件模块分发，除了 Python 标准库之外没有任何依赖项。支持干净和动态的 URL。快速和 Pythonic 内置模板引擎，支持 mako、jinja2 和 cheetah 模板。方便地访问表单数据、文件上传、cookie、标题和其他与 HTTP 相关的元数据。
*  缺点：Bottle 极简主义的一个后果是有些功能根本就不存在。不支持表单验证，包括 CSRF 保护等功能。如果要构建支持高度用户交互的 Web 应用程序，则需要自己添加它们。

3. cyclone
* 优点：Cyclone是Python的Web服务器框架，它将 Tornado API 实现为 Twisted 协议。Twisted 是一个事件驱动的 Python 网络编程框架。它是最成熟的非阻塞 I/O 库之一，可供公众使用。Tornado 是 FriendFeed 网络服务器的开源版本，它是最流行和最快速的 Python 网络服务器之一，具有用于构建网络应用程序的非常不错的API。除了丰富的功能集之外，Cyclone还解决了C10K问题。
* 缺点：Cyclone不再支持 python 2.x。

4. Django
* 优点：是一个高层次 Python Web 开发框架，特点是开发快速、代码较少、可扩展性强。Django 采用 MTV（Model、Template、View）模型组织资源，框架功能丰富，模板扩展选择最多。对于专业人员来说，Django 是当之无愧的 Python 排名第一的 Web 开发框架。
* 缺点：包括一些轻量级应用不需要的功能模块，不如 Flask 轻便。过度封装很多类和方法，直接使用比较简单，但改动起来比较困难。相比于 C,C++ 性能，Djang 性能偏低。模板实现了代码和样式完全分离，不允许模板里出现 Python 代码，灵活度不够。另外学习曲线也相对陡峭。

5. Falcon
* 优点：Falcon 是一个支持大规模微服务 API 或移动 App 后端响应的 Web 开发框架，它完全基于 Python 并提供了非常高的性能、可靠性和可扩展性。Falcon 定位独特且特色鲜明，对于 App 开发者，后端系统构建不妨考虑 Falcon。
* 缺点：Falcon 缺点是其打包模块有点太少，有路由，中间件，钩子，除此之外就不提供其他功能了（裸壳）。额外其他功能，比如验证等都需要开发人员来开发扩展。因为其设计中就假设用于构建 REST API。

6. Fastapi
* 优点：FastAPI 是一个现代、快速（高性能）的 Web 框架，用于基于标准 Python 类型提示使用 Python 3.6+ 构建 API。非常高的性能，与 NodeJS 和 Go 相当（感谢 Starlette 和 Pydantic）。可用的最快的 Python 框架之一。减少大约 40% 的人为（开发人员）引发的错误。简短，简单，直观，健壮。
* 缺点：本身不带模板语法，需要安装模板语法

7. Flask
* 优点：Flask 是一个 Python Web 开发的微框架，严格来说，它仅提供 Web 服务器支持，不提供全栈开发支持。然而，Flask 非常轻量、非常简单，基于它搭建 Web 系统都以分钟来计时，特别适合小微原型系统的开发。花少时间、产生可用系统，是非常划算的选择。
* 缺点：对于大型网站开发，需要设计路由映射的规则，否则导致代码混乱。对新手来说，容易使用低质量的代码创建 “不良的 web 应用程序”。

8. nameko
* 优点：AMQP RPC 和事件（发布 - 订阅），HTTPGET、POST 和 websockets，CLI 实现简单快速的开发，用于单元和集成测试的实用程序。
* 缺点：nameko 微服务出错不会自动打印错误日志，需要加上监控相关的依赖，计算密集型任务导致任务重试。

9. Sanic
* 优点：Sanic 是一个 Python 3.7+ web 服务器和 web 框架，它的编写速度很快。它允许使用 Python 3.5 中添加的 async/await 语法，这使您的代码无阻塞且快速。该项目的目标是提供一种简单的方法来启动和运行一个高性能的 HTTP 服务器，该服务器易于构建、扩展和最终扩展。
* 缺点：就功能方面 Sanic 模仿 Flask，比如通过共享 Blueprints 的概念，微小的子应用程序，允许开发人员在更大的应用程序中拆分和组织其代码。对于光光是数据增删改查 CRUD 应用，Sanic 也不是一个好的选择。

10. Tornado
* 优点：Tornado 是一个基于异步网络功能库的 Web 开发框架，因此，它能支持几万个开放连接，Web 服务高效稳定。可见，Tornado 适合高并发场景下的 Web 系统，开发过程需要采用 Tornado 提供的框架，灵活性较差，确定场景后再考虑使用不迟。
* 缺点：Tornado 5.0 改进了与 Python 的本机异步功能的集成。因此不再支持 Python 3.3，并且 Python 3.5 用户必须使用 Python 3.5.2 或更高版本。Tornado 6.0 将需要 Python 3.5 及更高版本，并将完全放弃 Python 2 支持。

11. Twisted
* 优点：
* 缺点：

12. Webpy
* 优点：web.py 是一个采用 Python 作为开发语言的 Web 框架，简单且强大。俄罗斯排名第一的 Yandex 搜索引擎基于这个框架开发，Guido van Rossum 认为这是最好的 Python Web 框架。
* 缺点：Web.py 并未像其他框架一样保持与 Python 3 兼容性的最新状态。这不仅意味着缺乏对异步语法的支持，还意味着缺少对已弃用的函数的错误。此外，目前尚不清楚维护者是否有计划在 Python 2 到达其支持生命周期结束后保持 Web.py 的最新状态。

### 定时任务框架
13. celery
    
14. airflow
    
15. apscheduler

### 其他框架
16. pyscript
