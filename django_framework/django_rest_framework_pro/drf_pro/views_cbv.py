# 类视图

#####
# 基础APIView类
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Article
from .serializers import (
    ArticleSerializer2,
    ArticleSerializer3,
    ArticleSerializer4,
    ArticleSerializer5,
    ArticleSerializer6
)


class ArticleList(APIView):
    """
    List all articles, or create a new article.
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer2(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer2(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer2(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer2(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#####
# 使用Mixin类和generics.GenericAPI类重写的类视图
from rest_framework import mixins
from rest_framework import generics
class ArticleList2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    GenericAPIView 类继承了APIView类，提供了基础的API视图。
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, reqeust, *args, **kwargs):
        return self.create(reqeust, *args, **kwargs)

    # 将request.user与author绑定
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        print("由UpdateModelMixin提供的方法perform_update被执行")

    def perform_destroy(self, instance):
        print("由DestroyModelMixin提供的方法perform_destroy被执行")



#####
# generic class-based views
from rest_framework import generics
class ArticleList3(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2 # important
    # 将request.user与author绑定
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail3(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2



#####
# 视图集(viewset)
from rest_framework import viewsets
class ArticleViewSet(viewsets.ModelViewSet):
    # 用一个视图集替代ArticleList和ArticleDetail两个视图
    queryset = Article.objects.all()

    # 自行添加，将request.user与author绑定
    # serializer_class = ArticleSerializer2

    # 演示status和author字段转义
    # serializer_class = ArticleSerializer3

    # 演示SerializerMethodField动态添加字段
    # serializer_class = ArticleSerializer4

    # 演示嵌套序列化器
    # serializer_class = ArticleSerializer5

    # 设置关联模型的深度depth
    serializer_class = ArticleSerializer6

    def perform_create(self, serializer):
        print("perform_create function")
        serializer.save(author = self.request.user)

    def perform_destroy(self, instance):
        print("perform_destroy function")

    def perform_update(self, serializer):
        print("perform_update function")

    def perform_authentication(self, request):
        print("perform_authentication function")



















