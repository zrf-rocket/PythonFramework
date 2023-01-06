import global_settings_base
from bottle import (run,  # 启动服务
                    route,  # 可以将一个函数与一个URL进行绑定
                    template,
                    request,
                    response,
                    Route,
                    Router,
                    Bottle,
                    Request,
                    Response,
                    Jinja2Template,
                    ServerAdapter)
import gevent.monkey

gevent.monkey.patch_all()

# 创建一个Bottle对象app，然后我们会将所有的函数都映射到app的URL地址上
app = Bottle()


# 浏览器访问：http://localhost/ 或 http://localhost/index
@app.route("/")
@app.route("/index", method=["GET", "POST"])
@app.route('/home/:name', method=["GET"])  # http://localhost/home/rocket
def index(name=global_settings_base.author):
    return "<strong>Hello {0}!,this is Python bottle framework.query_str:{1}".format(name, request.query.str)


if __name__ == '__main__':
    run(app=app, host="0.0.0.0", port=80, server="gevent", debug=True)
