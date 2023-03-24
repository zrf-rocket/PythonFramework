from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

# 使用REST framework提供的Serializer类和ModelSerializer类两种方式自定义序列化器

User = get_user_model()

class ArticleSerializer(serializers.Serializer):
    # ID和create_date都是由模型自动生成，每个article的author也希望在视图中与request.user绑定，
    # 而不是由用户通过POST或PUT自行修改，所以这些字段都是read-only。
    id = serializers.IntegerField(read_only=True)
    author = serializers.ReadOnlyField(source='author.id')
    create_date = serializers.DateTimeField(read_only=True)
    # title，body和status是用户可以添加或修改的字段，所以不能设成read-only。
    title = serializers.CharField(required=True, allow_blank=True, max_length=90)
    body = serializers.CharField(required=False, allow_blank=True)
    status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')

    def create(self, validated_data):
        """
        Create a new 'article' instance
        :param instance:
        :param validated_data:
        :return:
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Use validated data to return an existing `Article` instance.
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class ArticleSerializer2(serializers.ModelSerializer):
    # ArticleSerializer类中重复了很多包含在Article模型（model）中的字段信息。
    # 使用ModelSerializer类可以重构序列化器类，使整体代码更简洁。
    # ArticleSerializer和ArticleSerializer2效果一样
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')