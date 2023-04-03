# Python_Framework

## 介绍

## WSGI

Web Server Gateway Interface（Web服务器网关接口，WSGI）已被用作Python Web应用程序开发的标准。 WSGI是Web服务器和Web应用程序之间通用接口的规范。

## Gunicorn

- Gunicorn ‘Green Unicorn’ 是一个 UNIX 下的 WSGI HTTP 服务器，它是一个 移植自 Ruby 的 Unicorn 项目的 pre-fork worker 模型。它既支持 eventlet ， 也支持 greenlet。
- 在管理 worker 上，使用了 pre-fork 模型，即一个 master 进程管理多个 worker 进程，所有请求和响应均由 Worker 处理。Master 进程是一个简单的 loop, 监听 worker 不同进程信号并且作出响应。比如接受到 TTIN 提升 worker 数量，TTOU 降低运行 Worker 数量。如果 worker 挂了，发出 CHLD, 则重启失败的 worker, 同步的 Worker 一次处理一个请求。  
  它拥有稳定、高效等诸多优点。


- [Gunicorn 配置与最佳实践](./gunicorn_server/README.md)
- [Github for gunicorn](https://github.com/benoitc/gunicorn)

## 安装教程

> 虚拟环境可以使用virtualenv、pipenv：virtualenv c:\env
>
> 进入虚拟环境：c:\env\Scripts\activate
>
> 安装依赖包：pip install -r requirements_base.txt

## 规范性参考文档

1. [Python编码规范](https://bk.tencent.com/docs/document/7.0/250/46136?r=1)
1. [web安全](https://bk.tencent.com/docs/document/7.0/250/46147?r=1)
1. [接口规范](https://bk.tencent.com/docs/document/7.0/250/46083?r=1)
1. [Vuejs 编码规范](https://v2.cn.vuejs.org/v2/style-guide/index.html)
1. [JavaScript 编码规范](https://bk.tencent.com/docs/document/7.0/250/46179?r=1)
1. [表单数据校验-用户体验规范](https://bk.tencent.com/docs/document/7.0/250/46108?r=1)
1. [页面性能要求](https://bk.tencent.com/docs/document/7.0/250/46248)
