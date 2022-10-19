from handlers import handler

handlers = [
    (r"/", handler.IndexHandler),  # 浏览器访问：http://localhost:5000/
    (r"/index", handler.ShowHandler) # http://localhost:5000/index
]


