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



class ArticleSerializer3(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    # status = serializers.ReadOnlyField(source='get_status_display')
    # 此处定义了一个仅可读的status字段把原来的status字段覆盖了，这样反序列化时用户将不能再对文章发表状态进行修改（原来的status字段是可读可修改的）。
    # 一个更好的方式是在ArticleSerializer新增一个为full_status的可读字段，而不是简单覆盖原本可读可写的字段。
    full_status = serializers.ReadOnlyField(source='get_status_display')
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')



class ArticleSerializer4(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    status = serializers.ReadOnlyField(source='get_status_display')
    cn_status = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')

    def get_cn_status(self, obj):
        if 'p' == obj.status:
            return "已发布"
        elif 'd' == obj.status:
            return '草稿'
        else:
            return '编辑中'



# 嵌套序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ArticleSerializer5(serializers.ModelSerializer):
    author = UserSerializer(read_only=True) # 设置required=False表示可以接受匿名用户
    status = serializers.ReadOnlyField(source='get_status_display')
    cn_status = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')

    def get_cn_status(self, obj):
        if 'p' == obj.status:
            return "已发布"
        elif 'd' == obj.status:
            return '草稿'
        else:
            return '编辑中'



# 设置关联模型的深度depth
class ArticleSerializer6(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    status = serializers.ReadOnlyField(source='get_status_display')
    cn_status = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')
        depth = 1

    def get_cn_status(self, obj):
        if 'p' == obj.status:
            return "已发布"
        elif 'd' == obj.status:
            return '草稿'
        else:
            return '编辑中'



class ArticleSerializer7(serializers.Serializer):
    """
    字段级别验证 (Field-level validation)
    """
    title = serializers.CharField(max_length=10)
    def validate_title(self, value):
        """
        Check that the article is about drf.
        :param value:
        :return:
        """
        if 'drf' not in value.lower():
            raise serializers.ValidationError("Article is not about drf")
        return value



class EventSerializer(serializers.Serializer):
    """
    对象级别验证 (Object-level validation)
    """
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that the start is before the stop.
        :param data:
        :return:
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError('finish must occur after start')
        return data



def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class GameRecord(serializers.Serializer):
    """
    验证器 (Validators)
    """
    score = serializers.IntegerField(validators=[multiple_of_ten])



# class EventSerializer2(serializers.Serializer):
#     name = serializers.CharField()
#     room_number = serializers.IntegerField(choices=[101, 102, 103, 201])
#     date = serializers.DateField()
#
#     class Meta:
#         # Each room only has one event per day.
#         validators = serializers.UniqueTogetherValidator(
#             queryset=Article.objects.all(),
#             fields=['room_number', 'date']
#         )



from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    pass

# 通过一个序列化器创建两个模型对象示例
class UserSerializer2(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    # 同时更新两个关联模型实例时也同样需要重写update方法
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')  # 除非应用程序正确地强制始终设置该字段，否则就应该抛出一个需要处理的`DoesNotExist`
        profile = instance.profile
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.is_premium_member = profile_data.get(
            'is_premiun_member',
            profile.is_premium_member
        )
        profile.has_support_contract = profile_data.get(
            'has_support_contract',
            profile.has_support_contract
        )
        profile.save()
        return instance
