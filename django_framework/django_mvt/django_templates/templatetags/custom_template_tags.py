# @author:SteveRocket 
# @Date:2023/10/13
# @File:custom_template_tags
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from django import template

register = template.Library()


@register.filter
def add_params(value, args):
    return f"[{args}]{value}"
