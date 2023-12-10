# @author:SteveRocket 
# @Date:2023/12/9
# @File:main
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from flask import Flask, request, make_response
from flask_cors import CORS
from flask_classful import FlaskView

quotes = ["this is flask3", "Flask Classful libs", "Python3.11", "SteveRocket"]

app = Flask(__name__)
# CORS(app)  # 无法解决跨域问题
CORS(app, resources={r"/*": {"origins": "*"}})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')  # 'Access-Control-Allow-Origin,Content-Type'
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

class PersonsView(FlaskView):
    def index(self):
        """
        访问：http://127.0.0.1:8081/persons/
        """
        method = request.method
        page = request.args.get("page", 1)
        size = request.args.get("size", 10)
        # print(page, size)
        return "微信公众号：CTO Plus"

    def delete(self):
        return "删除方法"

    def patch(self):
        return "patch修改方法"

    def post(self):
        return "post方法"

    def put(self):
        return "put方法"


PersonsView.register(app)
