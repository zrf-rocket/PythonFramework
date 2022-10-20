# 最简单的fastapi服务
import os
import uvicorn
import global_settings_base
from typing import Optional
from fastapi import FastAPI

# 导入Request上下文对象，用来在前后台之间传递参数
from starlette.requests import Request
# 导入jinja2模板引擎对象
from starlette.templating import Jinja2Templates

app = FastAPI()

# 实例化一个模板引擎对象，指定模板所在路径
templates = Jinja2Templates(directory="templates")


@app.get("/")
@app.get("/index/{name}")
@app.post("/post")
@app.patch("/patch")
@app.delete("/delete")
async def index(name: str = global_settings_base.author):
    """
    GET http://localhost/index/123?k=v

    """
    return {"msg": "Hello {}, this is python fastapi framework".format(name)}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    """
    http://localhost/items/123?k=v
    http://localhost/items/123?...
    """
    return {"item_id": item_id, "q": q}


# FastApi中也可以借助第三方的模板引擎来实现后端对网页模板的渲染。
# 虽然FastApi的starlette 已经封装了 Jinja2 相关的类对象，但是你在使用中，仍然需要安装 jinja2 引擎。
@app.get("/templates_func/{info}")
# #在视图函数中传入request对象，用于在模板对象中传递上下文（同时接收路径参数info，将其传递到上下文中）
async def templates_func(request: Request, info: str):
    """
    浏览器访问：http://localhost/templates_func/zhouruifu
    """
    # 返回一个模板对象，同时使用上下文中的数据对模板进行渲染
    return templates.TemplateResponse(name="index.html", context={
        "title": "FastAPI Framework",
        "request": request,
        "info": info,
        "language": ["python", "tornado", "flask", "django"],
        "numbers": [63, 46, 73, 45, 21]
    })


if __name__ == '__main__':
    # reload=True 调试模式，文件有任何改动，服务器自动重启
    uvicorn.run("{0}:app".format(os.path.basename(__file__)[:-3]), host="0.0.0.0", port=80, reload=True)
