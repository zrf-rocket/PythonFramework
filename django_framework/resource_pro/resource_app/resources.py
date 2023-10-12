from core.drf_resource.base import Resource
from rest_framework import serializers
from resource_app import serializers


# 所有resource的入口。由于resource采用了动态加载属性方式，IDE的代码自动补全功能会失效，可能会导致开发效率降低及bug发生概率增加。因此采用了自动脚本生成pyi文件的方式实现代码的类型提示。
class NameGaneratorResource(Resource):
    RequestSerializer = serializers.NameGeneratorRequestSerializer
    ResponseSerializer = serializers.NameGeneratorResponseSerializer

    def perform_request(self, validated_request_data):
        full_name = "{first_name} {last_name}".format(**validated_request_data)
        return {"full_name": full_name}


# class GetNameGaneratorResource(Resource):
#     class RequstSerializer(serializers.Serializer):
#         name = serializers