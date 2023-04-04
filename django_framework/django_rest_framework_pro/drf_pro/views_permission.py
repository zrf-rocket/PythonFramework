from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class EampleView(APIView):
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )



from .permissions import permission_classes, permission_groups, authentication_classes
from rest_framework.decorators import api_view

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def example_view(request, format=None):
    content = {
        'user': request.user, # `django.contrib.auth.User` 实例
        'auth': request.auth, # None
    }
    return Response(content)



# 使用角色组权限控制
class ExampleGroupS():
    group_names = ['开发组', '测试组']


@api_view(['GET'])
@permission_groups(['开发组', '测试组'])
def example_groups(request):
    return Response()



# 自定义认证示例
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        """
        要实现自定义的认证方案，要继承BaseAuthentication类并且重写.authenticate(self, request)方法。
        如果认证成功，该方法应返回(user, auth)的二元元组，否则返回None。
        :param request:
        :return:
        """
        username = request.META.get('X_USERNAME')
        if not username:
            return
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return user, None

    def authenticate_header(self, request):
        """
        如果重写.authenticate_header(self, request)方法。如果实现该方法，则应返回一个字符串，该字符串将用作HTTP 401 Unauthorized响应中的WWW-Authenticate头的值
        如果.authenticate_header()方法未被重写，则认证方案将在未验证的请求被拒绝访问时返回HTTP 403 Forbidden响应。
        :param request:
        :return:
        """
        pass



# 创建用户时自动生成token，借助Django的信号(signals)实现
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)

