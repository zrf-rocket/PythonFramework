# @author:SteveRocket 
# @Date:2023/10/12
# @File:urls
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from django.urls import path, re_path
from . import views

app_name = "django_template_app"

urlpatterns = [
    path('template', views.template, name='template'),
]
