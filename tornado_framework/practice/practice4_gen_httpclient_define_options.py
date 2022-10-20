import settings
import logging
import tornado.httpserver as httpserver
import tornado.ioloop as ioloop
import tornado.web as web
from tornado.options import options
from urls import handlers

logger = logging.getLogger(__name__)

print(settings.BASE_DIR)

from handlers.send_msg import (
    send_msgs,
    send_numbers,
    send_ws
)


class Application(web.Application):
    def __init__(self):
        web.Application.__init__(self, handlers=handlers, **settings.settings)


main_loop = ioloop.IOLoop.instance()
# tornado提供的异步定时任务
scheduler_msgs = ioloop.PeriodicCallback(send_msgs, callback_time=1000)
scheduler_msgs.start()

scheduler_numbers = ioloop.PeriodicCallback(send_numbers, callback_time=2000)
scheduler_numbers.start()

scheduler_ws = ioloop.PeriodicCallback(send_ws, callback_time=3000)
scheduler_ws.start()


def main():
    options.parse_command_line()
    #命令行输入： python *.py --showname=zhouruifu
    print(options.showname) # zhouruifu
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port, address=options.address)
    main_loop.start()


if __name__ == '__main__':
    logger.info("server start.....")
    main()
