from django.urls import path, re_path
from django.conf.urls import url
from snippets import views
from snippets import views_django, views_api_view
urlpatterns = [
    # 添加一个snippet的GET请求   http://localhost:9898/snippet/
    path(r'', views.SnippetViewSet.as_view({'get': 'snippet'})),
    # 同时支持GET和POST请求  http://localhost:9898/snippet/create_snippet
    path(r'create_snippet', views.SnippetViewSet.as_view({
        'post': 'create_snippet',
        # 'get': 'create_snippet',
        'get': 'snippet'
    })),

    # 下面的视图函数路由使用url、re_path、path效果都是等同的
    # http://localhost:9898/snippet/snippets/
    url(r'^snippets/$', views_django.snippet_list, name="lists"),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views_django.snippet_detail, name="details"),

    # re_path(r'^snippets/$', views_django.snippet_list, name="lists"),
    # re_path(r'^snippets/(?P<pk>[0-9]+)/$', views_django.snippet_detail, name="details"),

    # path(r'snippets/', views_django.snippet_list, name="lists"),
    # path(r'snippets/(?P<pk>[0-9]+)/$', views_django.snippet_detail, name="details"),

    url(r'^snippets_v2/$', views_api_view.snippet_list, name="lists for api view"),
    url(r'^snippets_v2/(?P<pk>[0-9]+)$', views_api_view.snippet_detail, name="details for api view")
]
