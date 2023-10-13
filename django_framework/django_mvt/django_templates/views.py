from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from mvt_design.models import Article
from django.conf import settings


def template(request):
    html = "<h1>公众号：CTO Plus</h1><b  style='color: red'>作者：SteveRocket</b>"
    return HttpResponse(html)


userinfo = {"author": "SteveRocket", "blog": "公众号：CTO Plus", "age": 28}


def template1(request):
    # #根据字典数据生成动态模板
    return render(request, "index.html", {"userinfo": userinfo})


# 导入loader方法
from django.template import loader


def loader_template(request):
    # 通过loader加载模板
    temp = loader.get_template("django_templates/index_loader.html")
    # 将temp转换成HTML字符串，以字典形式传递数据并生成html
    html = temp.render(userinfo)
    # 用响应对象将转换的字符串内容返回给浏览器
    return HttpResponse(html)


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


# 内置模板标签的使用
def inner_template_tags(request):
    """
    模板的内置标签
    :param request:
    :return:
    """

    return render(request, 'inner_tags/index.html', {
        'age': settings.AGE, 'blog': settings.BLOG, 'platform': settings.PLATFORM
    })


def index(request, id):
    """
    模板的内置过滤器
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


import datetime


def custom_template_tags(request):
    article = {'article': {
        'content': '欢迎关注微信公众号：CTO Plus',
        'pub_date': datetime.datetime.now(),
        'pub_date_str': '2023-10-14'
    }}
    return render(request, 'template_tags/template_tags.html', article)


def custom_template_tags_params(request):
    return render(request, 'template_tags/custom_tags_params.html', {'article': {"title": '微信公众号：CTO Plus，自定义Django模板标签'}})


from django.template import Template, Context


def filter_content(request):
    template = Template("""{% load template_tags %}
    {{information | filter_tags}}""")
    return HttpResponse(template.render(Context({'information': "微信公众号：CTO Plus"})))


def sorted_tags(request):
    template = Template("""{% load template_tags %}
    使用自定义的标签别名{{ numbers | prefix }}""")
    return HttpResponse(template.render(Context({"numbers": [98, 76, 54, 32, 11, 23, 45, 78, 9]})))


def custom_simple_tags(request):
    template = Template("""
    {% load template_tags %}
    {% simple_formatstr_tag '自定义简单模板标签' %}""")
    return HttpResponse(template.render(Context()))


def custom_include_tag1(request):
    template = Template("""
    {% load template_tags %}
    {% include_tag 'SteveRocket' '微信公众号：CTO Plus' %}""")
    return HttpResponse(template.render(Context({'author': 'cramer', 'wechat': 'CTO Plus'})))


def custom_include_tag2(request):
    template = Template("""
    {% load template_tags %}
    {% include_tag2 'https://mp.weixin.qq.com/s/0t63QjARFIcJUCnCZDDqQg' %}""")
    return HttpResponse(template.render(Context({'author': 'SteveRocket', 'wechat': '公众号：CTO Plus'})))


def show_article(request):
    # return render(request, 'blog/index.html')
    return render(request, 'template_tags/custom_tags.html')
