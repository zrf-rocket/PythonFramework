from django.shortcuts import render
from .models import Task


def task_list(request):
    """
    任务清单
    """
    # 获取Task对象列表
    tasks = Task.objects.all()
    # 指定渲染模板并向模板传递数据
    return render(request, "mvt_design/task_list.html", {"tasks": tasks})
