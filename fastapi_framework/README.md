# Python fastapi framework
### 简介
FastAPI 是一个用于构建API的现代、快速（高性能）的web框架，要求使用Python 3.6及以上版本。
[FastApi模板渲染](https://fastapi.tiangolo.com/advanced/templates/)

### 特性
> ·快速：可与 NodeJS 和 Go 比肩的极高性能（归功于 Starlette 和 Pydantic）。最快的 Python web 框架之一。
> 
> ·高效编码：提高功能开发速度约 200％ 至 300％。*
> 
> ·更少 bug：减少约 40％ 的人为（开发者）导致错误。*
> 
> ·智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
> 
> ·简单：设计的易于使用和学习，阅读文档的时间更短。
> 
> ·简短：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
> 
> ·健壮：生产可用级别的代码。还有自动生成的交互式文档。
> 
> ·标准化：基于（并完全兼容）API 的相关开放标准：OpenAPI (以前被称为 Swagger) 和 JSON Schema。
> 

### 安装部署
安装
pip install fastapi uvicorn

运行
uvicorn practice1:app --reload


服务运行起来后可直接查看自带生成的API文档
http://localhost/redoc 或 http://localhost/docs
