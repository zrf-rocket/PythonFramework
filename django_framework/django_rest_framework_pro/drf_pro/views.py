# 函数视图
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from drf_pro.models import SerializerDemo


def serializer_demo(request):
    """
    http://localhost/serializer_demo
    :param request:
    :return:
    """
    # 使用Django自带的serializer进行Django QuerySet序列化
    peoples = serializers.serialize("json", SerializerDemo.objects.all())
    peoples2 = serializers.serialize("json", SerializerDemo.objects.all(), fields=("name", "id"))
    people = serializers.serialize("json", SerializerDemo.objects.filter(name="SteveRocket"))

    value_query_set = SerializerDemo.objects.filter(name="SteveRocket").values("age", "description")
    people_desc = json.dumps(list(value_query_set), cls=DjangoJSONEncoder)

    return HttpResponse(people_desc)






from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleSerializer2

@api_view(['GET', 'POST'])
def article_list(request, format=None):
    """
    DRF提供的序列化器类Serializer和ModelSerializer
    list all articles or create a new article.
    :param request:
    :return:
    """
    print(request.user.username, request.user.is_superuser)  # admin True
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：由于序列化器中author是read-only字段，用户无法通过POST提交来修改的，在创建Article实例时需手动将author和request.user绑定
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# api_view限定了可以接受的请求方法
@api_view(['GET','PUT',"DELETE"])
def article_detail(request, pk, format=None):
    """
    retrieve, update or delete an article instance
    :param request:
    :param pk:
    :return:
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer2(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer2(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)