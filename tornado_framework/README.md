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
```

### 安装部署

pip install -r requirements.txt

## tornado登录注册功能

## tornado redis

## tornado websocket

tornado在websocket模块中提供了一个WebSocketHandler类，这个类提供了和已连接的客户端通信的WebSocket事件和方法的钩子。

### 什么是WebSocket

WebSocket是一种网络通信协议，与Http协议不同的是，WebSocket 连接允许客户端和服务器之间进行全双工通信，以便任一方都可以通过建立的连接将数据推送到另一端。WebSocket 只需要建立一次连接，就可以一直保持连接状态。     
协议使用ws://URL格式，是在标准HTTP上实现的。

#### WebSocket和长轮询

WebSocket和长轮询的不同之处在于使用了一个持久的长连接，来代替长轮询中循环发送请求连接。

## tornado 模板

## tornado 异步任务与AsyncHTTPClient

## 项目案例

基于tornado、tornado-web、websocket开发的web小游戏
[项目案例](https://gitee.com/SteveRocket/python_game_eat_beans.git)
