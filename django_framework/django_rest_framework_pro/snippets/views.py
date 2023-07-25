import json

from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ViewSet):
    def snippet(self, request):
        """
        # 序列化
        snippet = Snippet(code='name = "SteveRocket"\n')
        snippet.save()

        snippet = Snippet(code='print("i love python programming")\n')
        snippet.save()

        serializer = SnippetSerializer(snippet)
        print(serializer.data, type(serializer.data))
        # {'pk': 2, 'title': '', 'code': 'print("i love python programming")\n', 'linenos': False, 'language': 'SteveRocket', 'style': 'friendly'} <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

        content = JSONRenderer().render(serializer.data)
        print(content, type(content))
        # b'{"pk":2,"title":"","code":"print(\\"i love python programming\\")\\n","linenos":false,"language":"SteveRocket","style":"friendly"}' <class 'bytes'>
        """

        # 改造成从地址栏输入内容
        # code = request.query_params.get('code', "")  # 此处通过GET方法传递进来的数据都是字符串
        # print(type(code), code)
        # # <class 'str'> {"code":"this is Python3 Django WebFramework"}
        # if not code:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        # 反序列化
        # # data = json.loads(code)
        # # print(type(data), data)
        # serializer = SnippetSerializer(data=code)
        # # serializer.is_valid()
        # # print(type(serializer.validated_data), serializer.validated_data)
        # serializer.save()
        # print(type(serializer.data), serializer.data)

        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        return Response(data=serializer.data)

    def create_snippet(self, request):
        # 获取GET请求的地址栏参数
        print(request.query_params)
        # 获取POST请求的Body数据
        print(request.data)
        return Response(data={})
