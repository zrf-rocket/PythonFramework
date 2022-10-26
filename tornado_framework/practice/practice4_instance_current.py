from tornado_framework import settings
import logging
import tornado.httpserver as httpserver
import tornado.ioloop as ioloop
import tornado.web as web
from tornado.options import options
from urls import handlers

from handlers.send_msg import (
    send_msgs,
    send_numbers,
    send_ws
)

logger = logging.getLogger(__name__)

print(settings.BASE_DIR)


class Application(web.Application):
    def __init__(self):
        web.Application.__init__(self, handlers=handlers, **settings.settings)


main_loop = ioloop.IOLoop.instance()
# IOLoop.instance()
# 返回一个全局 IOLoop实例。
# 大多数应用程序在主线程上运行着一个全局IOLoop，使用IOLoop.instance()方法可以在其他线程上获取这个实例。

# IOLoop.current()
# 返回当前线程的IOLoop，如果IOLoop当前正在运行或已被make_current标记为当前，则返回该实例。如果没有当前IOLoop，默认情况下返回IOLoop.instance()，即返回主线程的IOLoop，如果没有，则进行创建。
# 一般情况下，当构造异步对象时，你默认应该使用IOLoop.current()，当你在另外一个线程上和主线程进行通信时，使用IOLoop.instance()。
# 一般来说，当你构造一个异步对象时，应该使用 IOLoop.current() 作为默认值，如果你在另外一个线程上和主线程进行通信，则使用IOLoop.instance()。

# 在tornado 5.0之后的版本，instance()已经成为current()的别称，即就是调用instance方法时，实际上调用的是current方法。

for i in range(6):
    # 循环6次   每隔 i*10 秒调用
    main_loop.call_later(i*10, send_numbers, 5555)
# 带参
main_loop.call_later(5, send_msgs, "tornado call_later")
# 不带参
main_loop.call_later(5, send_ws, )

def main():
    options.parse_command_line()
    # 命令行输入： python *.py --showname=zhouruifu
    print(options.showname)  # zhouruifu
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port, address=options.address)
    main_loop.start()


if __name__ == '__main__':
    logger.info("server start.....")
    main()
