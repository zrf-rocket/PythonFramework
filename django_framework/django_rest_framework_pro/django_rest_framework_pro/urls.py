"""django_rest_framework_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from djangoapp import views as v1
from djanoapp import views as v2

from . import view as v3, testdb, search

from drf_pro import views as v4

from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # drf用户登录页面
    path('drf-api-auth/', include('rest_framework.urls')),
    # 暴露用户获取token的url地址
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),


    # url(r'^admin/index',v2.index),  #http://10.11.115.62:8089/admin/index
    # url(r'^admin/index',v1.index),

    # http://10.11.115.62:8089
    # url(r'^$', v2.index),
    # url(r'^$', v1.index),

    # http://10.11.115.62:8089/index1
    url(r'^index1$', v1.index),
    url(r'^index2$', v2.index),
    url(r'^index3$', v3.index),

    # django操作数据库
    url(r'^hello$', v3.hello),  # http://{HOSTNAME}/hello
    url(r'^insertdb$', testdb.insertdb),
    url(r'^getdb$', testdb.getdb),
    url(r'^updatedb$', testdb.updatedb),
    url(r'^deletedb$', testdb.deletedb),

    # 表单请求GET
    url(r'^search-form', search.search_form),
    url(r'^search', search.search),

    # 表单请求POST
    url(r'^search-post', search.search_post),


    # 引入APP中的urls
    url(r"^serializer_demo", v4.serializer_demo),

    path('v1/', include('drf_pro.urls')),
]
