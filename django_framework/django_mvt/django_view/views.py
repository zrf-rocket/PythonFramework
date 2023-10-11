from django.http import HttpResponse


# FBV
def login_fbv(request):
    if "POST" == request.method:
        return HttpResponse("这是Django的FBV POST方法")
    elif "GET" == request.method:
        return HttpResponse("这是Django FBV的GET方法")


# CBV
from django.views import View


# 类视图CBV，需要继承自View类
class LoginView(View):
    author = "SteveRocket"
    desc = "微信公众号：CTO Plus"

    def get(self, request):
        """

        :param request: 请求对象这个参数必须存在
        :return:
        """
        return HttpResponse("这是Django的CBV GET")

    def post(self, request):
        return HttpResponse("这是Django的CBV POST")


class LoginView2(LoginView):
    # 继承后重写类属性
    author = "Cramer"

    def get(self, request):
        return HttpResponse(f"{self.author}的{self.desc}")
