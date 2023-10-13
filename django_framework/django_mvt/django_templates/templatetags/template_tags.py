# @author:SteveRocket 
# @Date:2023/10/13
# @File:template_tags
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

import datetime
from django import template

# 自定义模板过滤器和模板标签
register = template.Library()


@register.filter
def truncate_text(value, length):
    if len(value) <= length:
        return value
    else:
        return value[:length] + '...'


@register.filter
def format_date(value):
    if isinstance(value, datetime.datetime):
        return f"{value.year}年{value.month}月{value.day}日"
    else:
        return f"字符串的日期：{value}"


@register.filter
def filter_tags(value):
    return value.replace('公众号', '博客')


@register.filter(name='prefix')  # 使用name参数为自定义标签指定别名
def sorted_filter(value):
    return sorted(value)


# 自定义模板标签
# @register.tag

# 自定义简单模板标签
@register.simple_tag
# @register.simple_tag(name="custom_simple_tag")
def simple_formatstr_tag(value):
    return f'微信公众号：CTO Plus，{value}'


# 自定义包含(引用)模板标签
@register.inclusion_tag("template_tags/inclustion.html")
# @register.inclusion_tag("template_tags/inclustion.html", takes_context=True)
def include_tag(value1='SteveRocket', value2='CTO Plus'):
    # 执行一些逻辑操作
    return {'author': value1, "wechat": value2}


# 注册自定义引用标签
@register.inclusion_tag("template_tags/inclustion2.html", takes_context=True)
# 定义函数渲染模板文件 inclusion2.html
def include_tag2(context, content):
    # 使用takes_context=True此时第一个参数必须为context
    return {'information': f'{context["author"]} {content}'}





# @register.filter_function
# @register.tag_function


from django.templatetags import i18n, l10n, tz
