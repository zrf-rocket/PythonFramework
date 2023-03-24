import os
from django.http import HttpResponse

def index(request):
    return HttpResponse("current work path in:{0}".format(os.path.abspath(__file__)))

# 每个 view 函数的第一个参数是一个 HttpRequest 对象
# HttpRequest对象包含当前请求URL的一些信息
def hello(request):
    return HttpResponse("APP 下的测试hello")

