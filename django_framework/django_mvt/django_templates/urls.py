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
    path('template1', views.template1, name='template1'),
    path('loader_template', views.loader_template, name='loader_template'),
    path('index/<int:id>', views.index, name='django_template'),

    # 自定义标签
    path('custom_template_tags', views.custom_template_tags, name='custom_template_tags'),
    path('custom_template_tags_params', views.custom_template_tags_params, name='custom_template_tags_params'),
    path('filter_content', views.filter_content, name='filter_content'),
    path('sorted_tags', views.sorted_tags, name='sorted_tags'),

    # 自定义过滤器

]
