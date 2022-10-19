import tornado.web as web
import tornado.ioloop as ioloop

class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello SteveRocket, This is tornado framework")


application = web.Application([
    (r"/index", IndexHandler),  # 浏览器访问：http://localhost:8080/index
])


if __name__ == '__main__':
    application.listen(8080)
    ioloop.IOLoop.instance().start()

