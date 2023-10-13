# @author:SteveRocket 
# @Date:2023/10/14
# @File:simple_inclusion_tags
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from django.template import Library
from mvt_design.models import Article

register = Library()


@register.simple_tag
def total_article():
    return Article.objects.filter(status='p').count()


@register.simple_tag
def get_first_article():
    return Article.objects.filter(status='p').order_by('-pub_date').first()


@register.inclusion_tag('blog/latest_article_list.html')
def show_latest_articles(count=2):
    return {'latest_articles': Article.objects.filter(status='p').order_by('-pub_date')[:count]}



# 向模板中传递多个参数
@register.inclusion_tag('template_tags/multiargs_tags.html')
def multi_param_template_tags(arg1, arg2, *args, **kwargs):
    warning = kwargs['warning']
    profile = kwargs['profile']

    return

