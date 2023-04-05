# 8、DRF实战总结：分页(Pagination)详解
from rest_framework import viewsets
from .models import Article
from .pagination import MyPageNumberPagination, MyArticleCursorPagination
from .serializers import ArticleSerializer2

# 在基于类的视图中，可以使用pagination_class这个属性使用自定义的分页类
class ArticleViewSet(viewsets.ModelViewSet):
    # 用一个视图集替代ArticleList和ArticleDetail两个视图
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2
    # pagination_class = MyPageNumberPagination

    # 并不推荐全局使用自定义的CursorPagination类，更好的方式是在此通过pagination_class属性指定
    pagination_class = MyArticleCursorPagination

    def perform_create(self, serializer):
        """
        自行添加，将request.user与author绑定
        :param serializer:
        :return:
        """
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """
        自行添加，将request.user与author绑定
        :param serializer:
        :return:
        """
        serializer.save(author=self.request.user)


from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
class ArticleList0(APIView):
    """
    List all articles, or create a new article.
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        page = PageNumberPagination() # 产生一个分页器对象
        page.page_size = 3 # 默认每页显示的多少条记录
        page.page_query_param = 'page'  # 默认查询参数名为 page
        page.page_size_query_param = 'size'  # 前台控制每页显示的最大条数  默认查询参数名为 size
        page.max_page_size = 10   # 后台控制显示的最大记录条数，防止用户输入的查询条数过大
        ret = page.paginate_queryset(articles, request)
        serializer = ArticleSerializer2(ret, many=True)
        return Response(serializer.data)







# 9、DRF实战总结：过滤(filter)与排序，以及第三方库django-filter的使用