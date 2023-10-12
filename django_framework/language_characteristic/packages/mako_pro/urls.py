from django.urls import include, path, re_path  # 使用 re_path 替代 url
from . import views
from django.conf.urls import i18n, static
# from django.conf.urls import url   # django4 以后就不能再使用

app_name = "mako_pro"
namespace = "mako_pro"
# https://docs.djangoproject.com/pl/4.0/releases/4.0/#features-removed-in-4-0
# https://forum.djangoproject.com/t/django-4-0-url-import-error/11065/3
# https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to


urlpatterns = [
    # http://localhost:99/mako/
    re_path(r'^$', views.index, name="主页"),

    # http://localhost:99/mako/index
    path("index", views.index, name="主页2"),

    # re_path(r"^my_index/", include('myapp.urls')),
    # re_path(r'^show_version/$', views.render_mako, name="使用mako显示版本信息"),

    # path("my_index2/", include('myapp.urls'))
]














urlpatterns = [

    # http://{HOSTNAME}/mako_pro/index/
    path('index/', views.index, name="index"),
]