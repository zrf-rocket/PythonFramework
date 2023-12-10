# @author:SteveRocket 
# @Date:2023/12/9
# @File:main
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from flask import Flask

from flask_classful import FlaskView

quotes = ["this is flask3", "Flask Classful libs", "Python3.11", "SteveRocket"]

app = Flask(__name__)

app.debug = True


class QuotesView(FlaskView):
    def index(self):
        """
        访问：http://127.0.0.1:5000/quotes/
        """
        return "<br>".join(quotes)


class DemoView(FlaskView):
    def index(self):
        """
        http://127.0.0.1:5000/demo/
        """
        return {"msg": "success", "code": 1}


class Demo02View(FlaskView):
    def index(self):
        """
        http://127.0.0.1:5000/demo02/
        """
        return {"msg": "success", "code": 1}


class Demo03Class(FlaskView):
    def index(self, request):
        """
        """
        return "this is get methods"


QuotesView.register(app)
DemoView.register(app)
Demo02View.register(app)
Demo03Class.register(app)

if __name__ == '__main__':
    app.run(debug=True, port=80)
