import time
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from packages.drf_pro.tasks import add, mul, xsum, count_widgets


# Create your views here.
# pip install djangorestframework
# pip install djangorestframework-simplejwt
##########  CVT类视图
class RegisterView(View):
    """
    类视图:处理注册
    使用类视图可以将视图对应的不同请求方式以类中的不同方法来区别定义。
    类视图相对于函数视图有更高的复用性， 如果其他地方需要用到某个类视图的某个特定逻辑，直接继承该类视图即可
    """

    def get(self, request):
        return HttpResponse("")

    def post(self, request):
        return JsonResponse({})


##########  FVT函数视图
def index(request):
    """
    视图函数:处理注册
    以函数的方式定义的视图称为函数视图，函数视图便于理解。但是遇到一个视图对应的路径提供了多种不同HTTP请求方式的支持时，便需要在一个函数中编写不同的业务逻辑，代码可读性与复用性都不佳。
    """
    time.sleep(1)
    return HttpResponse(f"请求地址：{request.path}")


########## DRF


##########celery
# 异步调用任务
def req_celery(request):
    # Celery提供了2种以异步方式调用任务的方法，delay和apply_async方法
    # 方法一：delay方法
    add.delay(11, 22)

    # 方法二： apply_async方法，与delay类似，但支持更多参数
    result2 = mul.apply_async(args=[100, 20])
    # Celery会为每个加入到队列的任务分配一个独一无二的uuid, 可以通过task.status获取状态和task.result获取结果。
    print(result2.task_id, result2.status, result2.result)

    xsum.delay([1, 2, 3, 4, 5, 6])

    # count_widgets.delay()

    return HttpResponse("request celery")
