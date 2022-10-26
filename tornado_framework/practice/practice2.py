# tornado实例化加载路由和配置
import settings
import logging
import tornado.httpserver as httpserver
import tornado.ioloop as ioloop
import tornado.web as web
from tornado.options import options
from urls import handlers

logger = logging.getLogger(__name__)

print(settings.BASE_DIR)


class Application(web.Application):
    def __init__(self):
        # 加载路由、加载配置
        web.Application.__init__(self, handlers=handlers, **settings.settings)


main_loop = ioloop.IOLoop.instance()


def main():
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port, address=options.address)
    main_loop.start()


if __name__ == '__main__':
    logger.info("server start.....")
    main()
