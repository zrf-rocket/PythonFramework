from handlers import handler
from handlers import handler_render

handlers = [
    (r"/", handler.IndexHandler),  # 浏览器访问：http://localhost:5000/
    (r"/index", handler.ShowHandler), # http://localhost:5000/index
    (r"/home", handler_render.IndexHandler)
]


