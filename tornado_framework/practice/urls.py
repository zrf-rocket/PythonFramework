from handlers import handler, handler_render, handler_gen, send_msg

handlers = [
    (r"/", handler.IndexHandler),  # 浏览器访问：http://localhost:5000/
    (r"/index", handler.ShowHandler), # http://localhost:5000/index
    (r"/home", handler_render.IndexHandler),
    (r"/gen", handler_gen.IndexHandlerGen),
    (r"/ws", send_msg.MyWebSocketHandler)
]


