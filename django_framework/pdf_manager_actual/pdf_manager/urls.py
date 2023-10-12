from django.urls import path, re_path
from . import views

app_name = 'pdf_manager'

urlpatterns = [
    # 上传pdf，用户输入需要提取的页面, 返回需要提取的页面
    path('extract/', views.pdf_extract, name='pdf_extract'),

] + [
    # django-mptt
    # http://localhost/pdf/extract/
    path('category/', views.category, name='category'),
] + [
    # whitenoise
    # http://localhost/pdf/whitenoise_server/
    # path('whitenoise_server/', views.whitenoise_server, name='whitenoise_server'),
]