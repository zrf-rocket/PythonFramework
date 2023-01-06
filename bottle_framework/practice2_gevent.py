from bottle import run
import gevent.monkey

gevent.monkey.patch_all()


def application(environ, start_response):
    start_response('200 OK', [("Content-Type", "text/html")])
    return ['<p>Python bottle框架</p>']


if __name__ == '__main__':
    # server： wsgi http server，字符串
    # host：port： 监听端口
    run(app=application, host="localhost", port=80, server="gevent")

# Bottle v0.12.23 server starting up (using GeventServer())...
# using GeventServer()表明使用的web服务器是gevent
