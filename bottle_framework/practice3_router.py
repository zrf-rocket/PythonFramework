import global_settings_base
from bottle import (run,  # 启动服务
                    route,  # 可以将一个函数与一个URL进行绑定
                    template,
                    Route,
                    Router,
                    Bottle,
                    Request,
                    Response,
                    Jinja2Template,
                    ServerAdapter)
import gevent.monkey

gevent.monkey.patch_all()


# Bottle的URL路由器，它将 URL 请求地址绑定到回调函数上，每请求URL，其对应的 回调函数就会运行，而回调函数返回值将被发送到浏览器，可以在应用中通过 route() 函数添加不限数目的路由器。
# 如果其一个URL没有被绑定到任何回调函数上，那么 Bottle 将返回“404 Page Not Found” 的错误页面
# 浏览器访问：http://localhost/ 或 http://localhost/index
@route("/")
@route("/index")
@route('/home/:name')  # http://localhost/home/rocket
def index(name=global_settings_base.author):
    return "<strong>Hello {}!,this is Python bottle framework.".format(name)


@route('/tmps/:name')
def tmps(name="world"):
    """http://localhost/tmps/rocket"""
    return template("<b>this is bottle {{name}}<b>", name=name)


if __name__ == '__main__':
    run(host="0.0.0.0", port=80, server="gevent", debug=True)
