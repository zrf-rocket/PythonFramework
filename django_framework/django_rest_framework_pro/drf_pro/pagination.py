from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response


class MyPageNumberPagination(PageNumberPagination):
    """
    自定义的分页类
    """
    page_size = 2  # default page size
    page_size_query_description = "page size query description"
    page_size_query_param = 'size'  # ?page=xx&size=??
    max_page_size = 10  # max page size

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5 # default limit per age
    limit_query_param = 'limit'
    limit_query_description = 'this is limit query description'
    offset_query_param = 'offset' # default param is offset
    offset_query_description = 'this is offset query description'
    max_limit = 10 # max limit per age



# 使用CursorPagination类需要的模型里有created这个字段，否则需要手动指定ordering字段。这是因为CursorPagination类只能对排过序的查询集进行分页展示
from rest_framework.pagination import CursorPagination
class MyArticleCursorPagination(CursorPagination):
    """
    这个ordering字段与模型相关，并不推荐全局使用自定义的CursorPagination类
    """
    page_size = 3 # Default number of records per
    page_size_query_param = 'page_size'
    cursor_query_param = 'cursor' # Default is cursor
    ordering = '-create_date'  # 指定排序字段








