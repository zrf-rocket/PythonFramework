# @author:SteveRocket 
# @Date:2023/12/9
# @File:main
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from flask import Flask

from flask_classful import FlaskView

quotes = ["this is flask3", "Flask Classful libs", "Python3.11", "SteveRocket", "微信公众号：CTO Plus"]

app = Flask(__name__)


class ArticlesView(FlaskView):
    def index(self, request):
        """
        访问：http://127.0.0.1:8080/articles/
        """
        return "<br>".join(quotes)


ArticlesView.register(app)

if __name__ == '__main__':
    app.run()
