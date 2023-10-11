from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from .models import Events

# Django ORM CookBook


def practice_django_orm_cookiebook(request):
    """
    Django ORM CookBook
    :param request:
    :return:
    """
    """
    # 使用qs.query方法快速生成SQL原生语句
    queryset = Events.objects.all()
    print(str(queryset.query))


    # 使用Annotate方法快速查询数据表字段重复条目
    duplicates = Events.objects.values('first_name').annotate(name_count=Count('first_name')).filter(name_count__gt=1)
    # Events.objects.values_list()
    print(duplicates)
    
    
    # 使用order_by('?').first()随机获取一个对象
    random_object = Events.objects.order_by('?').first()
    print(random_object)

    # random_object2 = Events.objects.order_by('?').afirst()
    # print(random_object2) #<coroutine object QuerySet.afirst at 0x00000197AE36C740>
    # for item in random_object2:
    #     print(item)
"""

    return HttpResponse()
