# Python aiohttp framework

### 简介
bottle 是一个轻量级(非常小巧但高效)的微型python web框架， 可以适配各种web服务器，包括python自带的wsgiref（默认），gevent， cherrypy，gunicorn等等。bottle是单文件形式发布，[源码](https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py) 在这里可以下载，代码量不多，可以用来学习web框架。这里也有[官方文档](https://blog.csdn.net/huithe/article/details/8087645) 的中文翻译。它被设计为仅仅只有一个文件的Python模块，并且除Python标准库外，它不依赖于任何第三方模块。
整个框架只有一个文件，几十K，却自带了路径映射、模板、简单的数据库访问等web框架组件，确实是个可用的框架。
[官方文档](http://bottlepy.org/docs/dev/)

    · 路由（Routing）：将请求映射到函数，可以创建十分优雅的 URL
    · 模板（Templates）：Pythonic 并且快速的 Python 内置模板引擎，同时还支持 mako, jinja2, cheetah 等第三方模板引擎
    · 工具集（Utilites）：快速的读取 form 数据，上传文件，访问 cookies，headers 或者其它 HTTP 相关的 metadata
    · 服务器（Server）：内置HTTP开发服务器，并且支持 paste, fapws3, bjoern, Google App Engine, Cherrypy 或者其它任何 WSGI HTTP 服务器

### 安装部署
pip install bottle








