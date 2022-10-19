import tornado.web as web


class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.write("main handler")

class ShowHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.write("show handler")
