from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from mvt_design.models import Article
from django.conf import settings


def template(request):
    html = "<h1>公众号：CTO Plus</h1><b  style='color: red'>作者：SteveRocket</b>"
    return HttpResponse(html)


def template1(request):
    userinfo = {"author": "SteveRocket", "blog": "公众号：CTO Plus", "age": 28}
    return render(request, "index.html", {"userinfo": userinfo})


class SteveRocket:
    def __say_hello(self) -> str:
        return "微信公众号：CTO Plus"

    def say_name(self) -> str:
        return settings.AUTHOR


def show_name() -> str:
    return "作者：SteveRocket"


def template_variable(request):
    """
    模板的变量
    :param request:
    :return:
    """
    var_result = {}
    var_result["numbers"] = [11, 22, 33, 44, 55, 66]
    var_result["information"] = {
        "author": settings.AUTHOR,
        "age": settings.AGE,
        "blog": settings.BLOG,
        "platform": settings.PLATFORM,
    }
    var_result["methods"] = show_name
    var_result["class_func"] = SteveRocket()
    var_result["name"] = "SteveRocket"
    return render(request, "django_templates/template_variable.html", var_result)


def template_args(request):
    name = settings.AUTHOR
    platform = settings.PLATFORM
    return render(request, "django_templates/template_args.html", locals())


def index(request, id):
    """
    模板的标签
    :param request:
    :param id:
    :return:
    """
    article = get_object_or_404(Article, pk=id)
    return render(
        request,
        "django_templates/index.html",
        {
            "article": article,
            "information": "this is django templates demo",
            "numbers": [11, 22, 33, 0, False, None, 44, 55, 66],
            "html_cnts": '<h4 style="color: red">safe</h4>',
            "html_cnts2": "&lt;b&gt;hello&lt;/b&gt;",
            "persons": [
                {"name": "steverocket", "blog": "https://blog.csdn.net/zhouruifu2015/"},
                {"name": "steverocket", "email": "rocket_2014@126.com"},
            ],
        },
    )


def template_tags(request):
    """
    模板标签
    :param request:
    :return:
    """
    tags_results = {}
    return render(request, "django_templates/template_tags.html", tags_results)


def template2(request, index):
    base_name = f"base{index}.html".replace("1", "")
    template_name = f"django_templates/template{index}.html".replace("1", "")
    return render(request, template_name, {"index": index, "base_name": base_name})


def material_dashboard(request):
    return render(request, "django_templates/dashboard/dashboard.html")
