from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def page_view(request):
    return HttpResponse("<h1>微信公众号：CTO Plus</h1>")


def page_view0(request, number):
    return HttpResponse(f"请求编号为：{number}")


def page_view1(request, num1, lan, num2):
    return HttpResponse(f"{num1} {lan} {num2}")


def page_view2(request, name, age):
    return HttpResponse(f"My name is {name}, age is {age}")


def article_detail(request):
    return HttpResponse(f"响应文章{id}的详情内容")
