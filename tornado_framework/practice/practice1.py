# 最简单的tornado服务程序
import tornado.web as web
import tornado.ioloop as ioloop

# 最重要的一个模块是web，它就是包含了Tornado的大部分主要功能的Web框架。其它的模块都是工具性质的，以便让web模块更加有用
class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello SteveRocket, This is tornado framework")


application = web.Application([
    (r"/index", IndexHandler),  # 浏览器访问：http://localhost:8080/index
])


if __name__ == '__main__':
    application.listen(8080)
    ioloop.IOLoop.instance().start()

