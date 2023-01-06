# Python Falcon framework
### 介绍
Python falcon是可靠高性能的构建大规模应用以及微服务的python web框架，一种更接近于python wsgi的框架，它拥有比flask和Django更快的速度，更高的性能。框架过于年轻和接近底层，许多东西都要自己写。

[介绍](http://falconframework.org/)


### 安装部署
pip install falcon gunicorn

gunicorn practice:app
携带使用配置文件方式启动
gunicorn --config gunicorn-conf.py practice:app










Falcon-Web 服务器文件监控平台
============================
Falcon 是一款基于 inotify-tools 开发的 Web 服务器文件安全监控平台，能够实时监控 Web 目录文件变化 (新增，修改，删除)，判断文件内容是否包含恶意代码，自动隔离常见 Webshell，保证 Web 目录文件安全

[GitHub](https://github.com/secrule/falcon)
