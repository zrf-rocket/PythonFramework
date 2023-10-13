# @author:SteveRocket 
# @Date:2023/10/14
# @File:custom_tags
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from django.template import Library, TemplateSyntaxError, Variable, Node

register = Library()

class DisplayDataNode(Node):
    def __init__(self, data):
        self.data = Variable(data)

    def render(self, context):
        data = self.data.resolve(context)
        if isinstance(data, str):
            return '<span style="color:red">{}</span>'.format(data)
        elif isinstance(data, int):
            return '<span style="color:blue">{}</span>'.format(data)
        else:
            return str(data)

@register.tag(name='display_data')
def display_data(parser, token):
    try:
        # 将标签内容解析为参数
        tag_name, data = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError('%r tag requires a single argument' % token.contents.split()[0])

    # 解析参数
    data = parser.compile_filter(data)
    # 返回自定义的节点
    return DisplayDataNode(data.token)