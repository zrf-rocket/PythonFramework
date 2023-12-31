from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views, views_cbv, views_validate
from .admin import CustomAuthToken

# 使用视图集后，需要使用DRF提供的路由router来分发urls，因为一个视图集现在对应多个urls的组合
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles4', viewset=views_cbv.ArticleViewSet)


# 分页
from .views_pagination import ArticleViewSet
router.register('articles6', viewset=ArticleViewSet)

# 过滤与排序
from .views_filter import ArticleList2, ArticleList3, ArticleList4
# router.register('articles7', viewset=ArticleList2, basename='filter')
# 由于ArticleList2类视图函数不是继承自视图集ViewSet，所以不支持使用router拼接


# 针对只需要其中的几种操作 使用方法映射
article_list = views_cbv.ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
article_detail = views_cbv.ArticleViewSet.as_view({
    'get': 'retrieve'  # 只处理get请求，获取单个记录
})

urlpatterns = [
    # 基于函数的视图
    re_path(r'^articles/$', views.article_list),
    # http://localhost/v1/articles/
    # http://localhost/v1/articles/?format=json

    re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),


    # 基于类的视图
    re_path(r'^articles_cbv/$', views_cbv.ArticleList.as_view()),
    # http://localhost/v1/articles_cbv/

    re_path(r'^articles_cbv/(?P<pk>[0-9]+)/$', views_cbv.ArticleDetail.as_view()),
    # http://localhost/v1/articles_cbv/4/


    # 使用Mixin类和generics.GenericAPI类重写的类视图
    re_path(r'^articles_cbv2/$', views_cbv.ArticleList2.as_view()),
    re_path(r'^articles_cbv2/(?P<pk>[0-9]+)/$', views_cbv.ArticleDetail2.as_view()),


    # generic class-based views
    re_path(r'articles_cbv3/$', views_cbv.ArticleList3.as_view()),
    re_path(r'articles_cbv3/(?P<pk>[0-9]+)/$', views_cbv.ArticleDetail3.as_view()),


    # 视图集(viewset)
    re_path(r'^articles5/$', article_list),
    re_path(r'^articles5/(?P<pk>[0-9]+)/$', article_detail),


    # 继承ObtainAuthToken类定制视图，获取更多的信息
    path('api-token-auth/', CustomAuthToken.as_view()),


    # filter
    path('articles7/', ArticleList2.as_view()),
    # django-filter
    path('articles8/', ArticleList3.as_view()),
    # DRF SearchFilter类
    path('articles9/', ArticleList4.as_view()),



    # 使用Serializer校验请求的数据格式示例
    re_path(r'^serializer_validate/$', views_validate.RequestMD.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)

urlpatterns += router.urls