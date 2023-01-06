# 最简单的一个falcon服务
import global_settings_base
import falcon
from wsgiref.simple_server import make_server


class Index:
    def on_get(self, req, resp):
        """Handler get request"""
        quote = {
            "author": global_settings_base.author,
            "email": global_settings_base.email,
            "msg": "this is python falcon web framework"
        }
        resp.media = quote


class RequestResp:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "\nname\t\nage\t\nframework\n\n"
        resp.json = {"name": "falcon", "age": 123.34}


app = falcon.App()
app.add_route("/", Index())  # 浏览器访问：http://localhost/
app.add_route("/index", Index())
app.add_route("/resp", RequestResp())

if __name__ == '__main__':
    with make_server("0.0.0.0", 80, app) as httpd:
        print("server starting on 0.0.0.0:80")
        httpd.serve_forever()
