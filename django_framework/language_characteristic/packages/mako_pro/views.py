from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# 每个视图函数的第一个默认参数都必需是request, 它是一个全局变量。Django把每个用户请求封装成了request对象，它包含里当前请求的所有信息，比如请求路径request.path,
# 当前用户request.user以及用户通过POST提交的数据request.POST。
def index(request):
    return HttpResponse("请求路径：{}".format(request.path))



