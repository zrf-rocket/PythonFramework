from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from snippets.models import Snippet
from snippets.serializers import SnippetSerializerv2


class JSONResponse(HttpResponse):
    """
    用于返回json数据
    """
    def __init__(self, data, **kwargs):
        data = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(data, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    函数视图
    展示所有的snippets或创建新的Snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serailizer = SnippetSerializerv2(snippets, many=True)
        return JSONResponse(serailizer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializerv2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def snippet_detail(request, pk):
    """
    修改或删除一个Snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # 获取单条记录
        serializer = SnippetSerializerv2(snippet)
        return JSONResponse(serializer.data)
    if request.method == 'PUT':
        # 更新单条记录
        data = JSONParser().parse(request)
        serializer = SnippetSerializerv2(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        # 删除单条记录
        snippet.delete()
        return JSONResponse(status=status.HTTP_204_NO_CONTENT)


























