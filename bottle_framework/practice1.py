import global_settings_base
from bottle import run, route


@route("/")
@route("/index")
def index(name=global_settings_base.author):
    return "<strong>Hello {}!,this is Python bottle framework.".format(name)


if __name__ == '__main__':
    run(host="0.0.0.0", port=80)


    # def application(environ, start_response):
    #     start_response('200 OK', [('Content-Type', 'text/html')])
    #     return ['<h1>This bottle framework html</h1>']

    #
    # run(app=application, host="0.0.0.0", port=80)
# Bottle v0.12.23 server starting up (using WSGIRefServer())...
# using WSGIRefServer()表明使用的web服务器是python自带的wsgiref
