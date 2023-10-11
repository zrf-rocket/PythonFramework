# @author:SteveRocket 
# @Date:2023/10/12
# @File:urls
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from django.urls import path, re_path
from . import views

app_name = "foundation_app"

urlpatterns = [
    re_path(r'index/$', views.request_obj, name='request_obj', ),
    re_path(r'index02/$', views.request_obj02, name='request_obj', ),
    re_path(r'request_meta/$', views.request_meta, name='request_meta', ),
    re_path(r'register/$', views.register, name='register', ),
    re_path(r'^show_information/$', views.show_information, name='show_information'),
]
