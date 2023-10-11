# @author:SteveRocket 
# @Date:2023/10/11
# @File:urls
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.profile_update, name="user_profile"),
]