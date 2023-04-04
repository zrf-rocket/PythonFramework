from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'status', 'create_date')
    list_filter = ('status',)
    list_per_page = 10


admin.site.register(Article, ArticleAdmin)



# 给用户创建token
from rest_framework.authtoken.admin import TokenAdmin
TokenAdmin.raw_id_fields=['user']



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request':request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
