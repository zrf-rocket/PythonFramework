# 过滤
# 自定义FilterSet类
from django_filters import FilterSet, CharFilter
from .models import Article

class ArticleFilter(FilterSet):
    q = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ('title', 'status')