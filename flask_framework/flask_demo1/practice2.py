import global_settings_base
from flask import Flask, render_template

app = Flask(__name__)  # 配置应用程序

app.config["DEBUG"] = True
app.config["host"] = "0.0.0.0"
app.config["port"] = 80
app.config["threaded"] = True
app.config["SECRET_KEY"] = "your_secret_key"


# 注册路由和视图函数
@app.route("/hello_world")
def hello_world():
    return "<p>Hello, SteveRocket</p>"


@app.route("/user/<name>")
def user(name):
    return "Hello, %s!" % name


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template(
        "steverocket.html",
        data={
            "author": global_settings_base.AUTHOR,
            "blog": global_settings_base.BLOG,
        },
        name=name,
    )


if __name__ == "__main__":
    app.run()
