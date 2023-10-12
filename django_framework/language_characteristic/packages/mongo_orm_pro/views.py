from django.shortcuts import render, HttpResponse as st_HttpResponse
from django.http import HttpResponse
from .models import UserInfo


# Create your views here.

def index(request):
    return HttpResponse(f"{request.path}")


def user_info(request):
    UserInfo.objects.create(
        name="python",
        age=22,
        addr="python.org.com",
        sex=True
    )
    return st_HttpResponse(f"请求路径：{request.path}, 集合总数：{UserInfo.objects.count()}")
