from aiohttp import (
    web,
    web_ws,
    web_app,
    web_log,
    web_runner,
    web_request,
    web_server,
    web_response
)
import global_settings_base


async def handle(request):
    # 从请求获取name的属性信息，如果没有则取配置中的author
    name = request.match_info.get("name", global_settings_base.author)
    print(request.match_info, name)
    # 把text作为相应返回，如果访问为/{name}则返回对应的 "Hello,{name}"
    return web.Response(text="Hello {}, this is Python aiohttp framework.".format(name))


app = web.Application()
# 添加两个路由访问/和访问/{name}都去调用函数handle
# 如果使用/访问则默认用户，如果使用/{name}访问则用户为对应的{name}
app.add_routes([
    web.get("/", handle),
    web.get("/{name}", handle)
])
# app.add_domain()
# app.add_subapp()

if __name__ == '__main__':
    web.run_app(app=app, host="0.0.0.0", port=80)
