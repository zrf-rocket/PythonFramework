# @author:SteveRocket 
# @Date:2023/10/13
# @File:template_tags
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

import datetime
from django import template

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

@register.filter(name='prefix') # 使用name参数为自定义标签指定别名
def sorted_filter(value):
    return sorted(value)


from django.templatetags import i18n, l10n, tz