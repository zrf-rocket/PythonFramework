from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .pagination import MyPageNumberPagination
from .serializers import ArticleSerializer2
from .models import Article

class ArticleList2(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('q')
        if not keyword:
            queryset = Article.objects.all()
        else:
            queryset = Article.objects.filter(title__icontains=keyword)
        return queryset

    # associate user with article author.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



# New for django-filter
from django_filters import rest_framework
from .filters import ArticleFilter

class ArticleList3(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = MyPageNumberPagination
    # new: filter backends and classes
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_class = ArticleFilter

    # associate request.user with author.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



# DRF SearchFilter类
from rest_framework import filters
from .throttles import (
    ArticleListAnonRateThrottle,
    ArticleListUserRateThrottle,
    HourUserRateThrottle,
    MinuteUserRateThrottle
    )

class ArticleList4(generics.ListCreateAPIView):
    """
    默认情况下，SearchFilter类搜索将使用不区分大小写的部分匹配(icontains)
    视图类或视图集中使用自定义限流类
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = MyPageNumberPagination

    # 限流
    # throttle_classes = [ArticleListAnonRateThrottle, ArticleListUserRateThrottle]
    # 对一个认证用户进行限流不仅要限制每分钟的请求次数，还需要限制每小时的请求次数
    throttle_classes = [HourUserRateThrottle, MinuteUserRateThrottle]

    # new: add SearchFilter and search_fields
    # filter_backends = (filters.SearchFilter, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )

    search_fields = ('title', )
    # 同时搜索标题或用户名含有某个关键词的文章资源列表
    # search_fields = ('title', 'author__username', )

    ordering_fields = ('create_date')
    # associate request.user with author.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


























