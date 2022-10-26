# 最简单的一个sanic服务
from sanic import Sanic
from sanic.response import json

# 通常可以用__name__预置变量，如果name为None，则从之前栈中获得module name
app = Sanic(__name__)
# app = Sanic("scanic_framework")


# 路由装饰器，注册一个路由
@app.route("/")
async def index(request):
    return json({"framework_name": "sanic"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
