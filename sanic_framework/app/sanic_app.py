from sanic import Sanic
from sanic.response import json

app = Sanic("sanic_framework")

app2 = Sanic("sanic_framework2")


@app.route("/app1")
def app1_func(request):
    return json({"name": "app1"})


@app.route("/app1_sanic_framework")
def app1_sanic_framework(request):
    # 获取网络请求的方法和参数
    return json({
        "ip": request.ip,
        "method": request.method,
        "name": request.name,
        "path": request.path,
        "query_args": request.query_args,
        "server_name": request.server_name,
        "server_path": request.server_path,
        "server_port": request.server_port,
        "url": request.url
    })


@app2.route("/app2")
def app2_func(request):
    return json({"name": "app2"})
