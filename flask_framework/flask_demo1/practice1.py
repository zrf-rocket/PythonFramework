# 最简单的一个flask服务
import global_settings_base
# 导入Flask类
from flask import Flask

# 创建应用
# Flask类的一个对象是我们的WSGI应用程序。
# Flask构造函数使用当前模块（__name __）的名称作为参数
app = Flask(__name__)  # 配置应用程序

# 定义路由：使用装饰器来定义URL路由和对应的处理函数
@app.route("/hello_world")
def hello_world():
    return "<p>Hello, SteveRocket</p>"

# route()函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。
# rule 参数表示与该函数的URL绑定。
@app.route("/")
@app.route("/index")
def index():
    """
    http://localhost/
    或
    http://localhost/index
    """
    return {
        "msg": "Hello {}, this is python flask framework".format(
            global_settings_base.AUTHOR
        )
    }


def say_flask():
    """http://localhost/say"""
    return "hello {}".format(global_settings_base.AUTHOR)


# application对象的add_url_rule()函数也可用于将URL与函数绑定
app.add_url_rule("/say", "say", say_flask)

if __name__ == "__main__":
    # 运行应用：在Python文件中添加如下代码，以运行Flask应用
    # debug 开启调试模式
    # threaded 开启多线程
    app.run(host="0.0.0.0", port=80, debug=True, threaded=True)
