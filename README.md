# ABOUT

**【关于我们】**

* [Articulate v1.0](https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q)
* [Articulate v2.0](https://mp.weixin.qq.com/s/V5Axn-ZWi22ubh5Jiocb9g)

[![](https://img.shields.io/badge/GitHub-zrf--rocket-blue?logo=gitpod)](https://github.com/zrf-rocket)
[![](https://img.shields.io/badge/Gitee-SteveRocket-pink)](https://gitee.com/SteveRocket/)
![CTO Plus](https://img.shields.io/badge/微信公众号：CTO%20Plus-8A2BE2) 🥰

<img src="./static/wechat.png" style="width:500px">


**【代码工程系列】**

* [Python和Go的设计模式](https://github.com/zrf-rocket/DesignPattern)
    * GitHub：https://github.com/zrf-rocket/DesignPattern
    * Gitee：https://gitee.com/SteveRocket/design_pattern

* [Python、Go的编码技巧cookbook](https://github.com/zrf-rocket/CookBook)
    * GitHub：https://github.com/zrf-rocket/CookBook
    * Gitee：https://gitee.com/SteveRocket/cook-book

* [Go代码示例](https://github.com/zrf-rocket/PracticeGo)
    * GitHub：https://github.com/zrf-rocket/PracticeGo
    * Gitee：https://gitee.com/SteveRocket/practice_go

* [Python代码示例](https://github.com/zrf-rocket/PracticePython)
    * GitHub：https://github.com/zrf-rocket/PracticePython
    * Gitee：https://gitee.com/SteveRocket/practice_python

* [Python Web框架的示例代码](https://github.com/zrf-rocket/PythonFramework)
    * GitHub：https://github.com/zrf-rocket/PythonFramework
    * Gitee：https://gitee.com/SteveRocket/python_framework

* [Rust代码示例](https://github.com/zrf-rocket/PracticeRust)
    * GitHub：https://github.com/zrf-rocket/PracticeRust
    * Gitee：https://gitee.com/SteveRocket/practice_rust

* [Vue代码示例](https://github.com/zrf-rocket/PracticeVue)
    * GitHub：https://github.com/zrf-rocket/PracticeVue
    * Gitee：https://gitee.com/SteveRocket/practice_vue

* [前端代码示例](https://github.com/zrf-rocket/PracticeFronted)
    * GitHub：https://github.com/zrf-rocket/PracticeFronted
    * Gitee：https://gitee.com/SteveRocket/practice_fronted

* [Python自动化测试框架](https://github.com/zrf-rocket/PythonTestAutomationFramework)
    * GitHub：https://github.com/zrf-rocket/PythonTestAutomationFramework
    * Gitee：https://gitee.com/SteveRocket/python_test_automation_framework

* [Python和Go的算法代码示例](https://github.com/zrf-rocket/Algorithms)
    * GitHub：https://github.com/zrf-rocket/Algorithms
    * Gitee：https://gitee.com/SteveRocket/Algorithms

* [Python和Go的数据结构代码示例](https://github.com/zrf-rocket/DataStructure)
    * GitHub：https://github.com/zrf-rocket/DataStructure
    * Gitee：https://gitee.com/SteveRocket/data_structure

* [编码规范](https://github.com/zrf-rocket/DevGuide)
    * GitHub：https://github.com/zrf-rocket/DevGuide
    * Gitee：https://gitee.com/SteveRocket/develop_guide

* [编码安全规范](https://github.com/zrf-rocket/SecGuide)
    * GitHub：https://github.com/zrf-rocket/SecGuide
    * Gitee：https://gitee.com/SteveRocket/security_guide

**【产品系列】**

* [主机监控系统-日志收集与报警管理系统（SIEM）](https://github.com/zrf-rocket/SIEM)
    * GitHub：https://github.com/zrf-rocket/SIEM
    * Gitee：https://gitee.com/SteveRocket/siem

* [安全运营中心（SOC）-终端侦测与响应系统（EDR）](https://github.com/zrf-rocket/EDR_SOC)
    * GitHub：https://github.com/zrf-rocket/EDR_SOC
    * Gitee：https://gitee.com/SteveRocket/edr_soc

* [DevSecOps-SDLC](https://github.com/zrf-rocket/DevSecOps-SDLC)
    * GitHub：https://github.com/zrf-rocket/DevSecOps-SDLC
    * Gitee：https://gitee.com/SteveRocket/dev-sec-ops-sdlc

* [AI图像识别-智能缺陷检测系统]()
    * [基于AI图像识别的工业缺陷检测应用系统（GPU&FPGA）](https://mp.weixin.qq.com/s/04qefQFg-Pg1Gcqq1vBLQQ)
    * [基于AI图像识别的智能缺陷检测系统，在钢铁行业的应用-技术方案](https://mp.weixin.qq.com/s/dSHbnuOwQZzE4CvPr1JYjg)


# Python_Framework

## 介绍

[Python开发框架](README_PythonFramework.md)是一组用于简化和加速Python应用程序开发的库和工具。它们提供了一系列预定义的功能和结构，以便开发者能够快速构建、测试和维护应用程序。
总结Python的开发框架，包括：Web框架、爬虫框架、定时任务框架、自动化测试框架、以及其他常用的框架。最新更新，请查看[本文GitHub地址](https://gitee.com/SteveRocket/python_framework/blob/master/README_PythonFramework.md)

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
