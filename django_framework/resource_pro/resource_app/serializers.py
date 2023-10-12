from rest_framework import serializers
from resource_app.models import Person

# 定义两个数据校验类，分别用于处理请求数据和相应数据
class NameGeneratorRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, label="姓")
    last_name = serializers.CharField(required=True, label="名")


class NameGeneratorResponseSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=True, label="全名")




class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # `fields` 参数指定了要序列化的字段，这里使用了特殊值 `'__all__'`，表示序列化所有字段
        fields = '__all__'
