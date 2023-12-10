# @author:SteveRocket
# @Date:2023/12/10
# @File:main
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
import datetime

from flask import Flask, request, Response, jsonify, json, make_response
from flask_cors import CORS
from global_settings_base import BLOG, AUTHOR

app = Flask(__name__)
# 跨域处理 resources=r'/*' 表示针对所有路由有效
CORS(app, resources=r'/*', supports_credentials=True)

PERSONS = [
    {"name": "SteveRocket", "age": 28, "BLOG": BLOG},
    {"name": "SteveRocket02", "age": 27, "BLOG": "微信公众号：CTO Plus"},
    {"name": "SteveRocket03", "age": 26, "BLOG": None},
    {"name": "SteveRocket04", "age": 29, "BLOG": BLOG},
    {"name": "Cramer", "age": 18, "BLOG": None}
]

ARTICLES = [
    {"title": "Vue3进阶：组件开发指南之使用 Props 传递和管理组件之间的数据", "url": "https://mp.weixin.qq.com/s/j15DvXsNNWPdWitvJVQp1w"},
    {"title": "Vue3进阶：计算属性（computed）的介绍、使用详解和代码实战案例", "url": "https://mp.weixin.qq.com/s/EgZ0eDYlY3Z3XETM7YTvGg"},
    {"title": "Vue3进阶：监听属性的介绍、使用详解和代码实战案例", "url": "https://mp.weixin.qq.com/s/SCLp6eohFG-LcuQg6IXOuA"},
    {"title": "Vue3进阶：简化前端开发的利器，以及常用指令汇总和案例详解", "url": "https://mp.weixin.qq.com/s/-kq2g5Eu_joc2mualwhWTg"},
    {"title": "Vue3进阶：常用的指令缩写详解，以及代码使用示例", "url": "https://mp.weixin.qq.com/s/euM7Opssl-t14aa9lGPPlg"},
    {"title": "Vue3进阶：循环语句的介绍和编码使用详解（附代码与群资料）", "url": "https://mp.weixin.qq.com/s/pO_qYpxLrbp_ra8YXN2RAg"},
    {"title": "Vue3进阶：条件语句控制内容展示的介绍和编码使用详解（附代码与群资料）", "url": "https://mp.weixin.qq.com/s/59yiConjcuP5zUezRQEZ_Q"},
    {"title": "Vue3进阶：模板语法的介绍和编码使用详解（附代码与群资料）", "url": "https://mp.weixin.qq.com/s/jOvPYrwMUreUpfhJlYFkog"},
    {"title": "Vue3进阶：Vue与Web components的初步介绍和转换", "url": "https://mp.weixin.qq.com/s/FqrCbVUE9AjcBJ92jl4UZw"},
    {"title": "Vue3进阶：组件开发指南之构建可复用的UI组件详解和代码示例", "url": "https://mp.weixin.qq.com/s/O4PrgstiWOZDk9E3vyCqhQ"},
    {"title": "Vue3进阶：Vue开发必备的基本功之双向数据v-model绑定详解及代码实战示例（文末群资料）", "url": "https://mp.weixin.qq.com/s/2OIa_BI70pchfd-N_B3aAg"}
]


@app.route("/articles/")
def index():
    page = int(request.args.get("page", 1))
    size = int(request.args.get("size", 1))
    articles = ARTICLES[(page - 1) * size:page * size]
    results = {"platform": "微信公众号：CTO Plus", "data": articles, "total": len(ARTICLES)}
    # return results
    # return jsonify(results)
    # 上下两种本质是一样的
    # return Response(json.dumps(results))

    # 返回json数据的同时指定状态码
    return make_response(jsonify(results), 201)
    # https://flask.palletsprojects.com/en/1.0.x/quickstart/#about-responses

@app.route("/persons/")
def persons():
    print(request.method)
    page = int(request.args.get("page", 1))
    size = int(request.args.get("size", 1))
    data = PERSONS[(page - 1) * size:page * size]
    return {"platform": "微信公众号：CTO Plus", "data": data, "total": len(PERSONS)}


@app.route("/login", methods=["POST"])
def login():
    return {"msg": "login success", "name": AUTHOR, "login_datetime": datetime.datetime.now()}


if __name__ == '__main__':
    app.run(port=8083)
