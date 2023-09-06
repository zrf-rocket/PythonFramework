# Python Falcon framework
### 介绍
Python falcon是可靠高性能的构建大规模应用以及微服务的python web框架，一种更接近于python wsgi的框架，它拥有比flask和Django更快的速度，更高的性能。框架过于年轻和接近底层，许多东西都要自己写。

[介绍](http://falconframework.org/)


### 安装部署
pip install falcon gunicorn

gunicorn practice:app
携带使用配置文件方式启动
gunicorn --config gunicorn-conf.py practice:app


### 特点
* ASGI, WSGI ，以及 WebSocket 支持。
* 原生的 asyncio 支持。
* 不依赖魔术全局进行路由和状态管理。
* 稳定的接口，强调向后兼容性。
* 通过集中式RESTful进行简单的API建模 routing。
* 高度优化、可扩展的代码库。
* 通过以下方式轻松访问页眉和正文 request and response 对象。
* 通过以下方式处理干请求 middleware 组件和挂钩。
* 严格遵守RFC。
* 惯用语 HTTP error 回应。
* 简单的异常处理。
* 时髦的 testing 使用WSGI/ASGI帮助器和模拟。
* 支持CPython 3.5+和PyPy 3.5+。

### Falcon不同之处
Falcon来支持大规模微服务和响应式应用程序后端的需求。Falcon通过在任何需要的地方提供裸机性能、可靠性和灵活性来补充更通用的PythonWeb框架。

* 快。 相同的硬件，更多的请求。Falcon将请求转换为比大多数其他Python框架快几倍的速度。为了获得额外的速度提升，Falcon在有条件的情况下会与赛通一起编译，并且也能很好地与 PyPy .考虑转移到另一种编程语言？先与Falcon+Pypy进行基准测试。
* 可靠。 我们会尽最大努力避免引入破坏性的变更，当我们这样做时，它们会被完整地记录下来，并且只会被引入（本着 [SemVer](https://semver.org/) ）主要版本递增。该代码经过了大量输入的严格测试，我们始终需要100%的覆盖率。Falcon不依赖于任何外部python包。
* 可调试。 Falcon避开魔法。很容易分辨出哪些输入通向哪些输出。为了避免激励使用难以调试的全局状态，Falcon不使用装饰器来定义路由。从未封装或屏蔽未处理的异常。可能令人惊讶的行为，比如自动请求正文解析，都有很好的文档记录，并且默认情况下是禁用的。最后，我们注意保持框架内的逻辑路径简单、浅显和易于理解。所有这些都使得在大规模部署中对代码进行推理和调试边缘案例变得更容易。
* 很灵活。 Falcon将很多决策和实现细节留给了API开发人员。这给了您很大的自由来定制和调优您的实现。由于Falcon的极简主义设计，Python社区成员可以自由地自主创新 [Falcon add-ons and complementary packages](https://github.com/falconry/falcon/wiki)。




Falcon-Web 服务器文件监控平台
============================
Falcon 是一款基于 inotify-tools 开发的 Web 服务器文件安全监控平台，能够实时监控 Web 目录文件变化 (新增，修改，删除)，判断文件内容是否包含恶意代码，自动隔离常见 Webshell，保证 Web 目录文件安全

[GitHub](https://github.com/secrule/falcon)
https://www.osgeo.cn/falcon/user/index.html