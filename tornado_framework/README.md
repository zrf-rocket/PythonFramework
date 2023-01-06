# Python_Framework

### 介绍

Tornado是FriendFeed网络服务器的开源版本，它是最流行和最快速的 Python 网络服务器之一，具有用于构建网络应用程序的非常不错的API。

### 软件架构

Python3 Tornado Web框架（Web framework）。

```
practice为练习代码
· practice1：tornado基础服务
· practice2：封装tornado服务
· practice3：tornado的异步定时任务
· practice4：tornado的模板引擎
· practice5：tornado与websocket的交互
重写RequestHandler的方法函数
Application
template
routing
escape



重定向redirect
模板
cookie和安全cookie
用户认证
跨站伪造请求的防范
静态文件和主动式文件缓存
本地化 locale
UI模块
非阻塞式异步请求

异步和非阻塞IO


异步http客户端和服务器
    httpserver 非阻塞http服务器
    httpclient 异步http客户端
    httputil http头和URL
    http1connection HTTP/1.x客户端/服务器的实现

第三方认证


异步网络
tornado.ioloop 主事件循环
tornado.iostream
tornado.netutil
tornado.tcpclient 
tornado.tcpserver 基于IOStream TCP服务器

协程和并发
tornado.gen
tornado.locks
tornado.queues
tornado.process

tornado.auth
tornado.wsgi
tornado.platform.caresresolver
tornado.platform.twisted
tornado.platform.asyncio


tornado.autoreload 自动检测开发中的代码更改
tornado.concurrent
tornado.log
tornado.options
tornado.testing  异步代码单元测试
tornado.util 通用工具
```

## 性能
一个 Web 应用的性能表现，主要看它的整体架构，而不仅仅是前端的表现。 和其它的 Python Web 框架相比，Tornado 的速度要快很多。  
对于Tornado，使用的部署方案为前端使用nginx做反向代理，带动4个线程模式的Tornado，这种方案也是推荐的在生产环境下的Tornado部署方案（根据具体的硬件情况，推荐一个CPU核对应一个Tornado服务实例，负载测试使用的是四核处理器）。  
使用Apache Benchmark (ab)，在另外一台机器上使用了如下指令进行负载测试：
> ab -n 100000 -c 25 http://10.0.1.x/


### 安装部署

pip install -r requirements.txt

#### 生产环境部署
在FriendFeed中，使用nginx做负载均衡和静态文件服务。在多台服务器上，同时部署了多个Tornado实例，通常，一个CPU内核会对应一个Tornado线程。
https://wizardforcel.gitbooks.io/tornado-overview/content/23.html


由于Tornado提供了自己的httpserver，因此运行和部署它与其他PythonWeb框架有点不同。不是配置一个wsgi容器来查找应用程序，而是编写一个 main() 启动服务器的函数：



## tornado登录注册功能






## tornado redis

## tornado websocket

tornado在websocket模块中提供了一个WebSocketHandler类，这个类提供了和已连接的客户端通信的WebSocket事件和方法的钩子。

### 什么是WebSocket

WebSocket是一种网络通信协议，与Http协议不同的是，WebSocket 连接允许客户端和服务器之间进行全双工通信，以便任一方都可以通过建立的连接将数据推送到另一端。WebSocket 只需要建立一次连接，就可以一直保持连接状态。 协议使用ws://URL格式，是在标准HTTP上实现的。

#### WebSocket和长轮询

WebSocket和长轮询的不同之处在于使用了一个持久的长连接，来代替长轮询中循环发送请求连接。

## tornado 模板

## tornado 异步任务与AsyncHTTPClient

## 项目案例

基于tornado、tornado-web、websocket开发的web小游戏
[项目案例](https://gitee.com/SteveRocket/python_game_eat_beans.git)

## 参考资料
[tornado用户指南](https://www.osgeo.cn/tornado/guide.html#)
[tornado中文文档](https://wizardforcel.gitbooks.io/tornado-overview/content/1.html)

