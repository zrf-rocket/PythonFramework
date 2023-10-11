# Mako 
Mako是一个高性能的Python模板库，它的语法和API借鉴了很多其他的模板库，如Django、Jinja2等等。 Mako最大的特点在与，可以在 html 中随意书写 python代码。
Django的模板，模板内不能运行原生的python语句，第三方模板中，性能较好的是mako和jinja2。mako相比较而言会更为简洁。

## 环境准备
安装Python3.11 + Django4.*
pip install django

安装mako
pip install Mako django-mako
或
pip install -r requirements.txt

创建项目
django-admin startproject mako_pro
cd mako_pro
创建APP
django-admin startapp mako_frame


## 功能点
### Django 添加manage自定义命令
### Django admin

### mako变量
    获取值
### mako循环
for
continue
break

### mako判断
if...else..if

### mako代码块

### mako定义函数
def 

### mako继承模板


### mako调用文件

### mako引用标签
1. <%page>  

2. <%include>  
    包含一个HTML文件
    <%include file="metric_header.html",args="realtime_server_conf=realtime_server_conf" />

3. <%def>  


4. <%block>  


5. <%namespace>  


6. <%inherit>  


7. <%nsname:defname>  


8. <%call>  


9. <%doc>  


10. <%text>  









## 错误解决记录
以前
1.在mako模板中，python块<% %>要放在 def里面，不然会弹出“undefined"错误，例如变量的定义  a='aa'
2.当模板报错 <mako.runtime.Undefined object at 0x2edd750> 时是因为模板中存在没定义的变量
3.当模板报错 Undefined  时是因为模板中存在没定义的变量


执行 mw_instance = middleware(handler) 报错TypeError: xxx takes 1 positional argument but 2 were given
解决: 修改类djangomako.middleware.MakoMiddleware 如下图所示: django3.1的中间件都要继承MiddlewareMixin
class MakoMiddleware(MiddlewareMixin):  # update : MakoMiddleware(Object)
def __init__(self, get_response=None):
    """Setup mako variables and lookup object"""
    super().__init__(get_response)  # add for : mw_instance = middleware(handler) 报错TypeError: xxx takes 1 positional argument but 2 were given
    from django.conf import settings


报错: ModuleNotFoundError: No module named 'middleware’
修改: import middleware 为 import djangomako.middleware 这里导包有问题

报错: AttributeError: ‘Settings’ object has no attribute 'TEMPLATE_DIRS’
解决: settings中加入配置项: TEMPLATE_DIRS = [os.path.join(BASE_DIR, ‘templates’)]

报错: mako.exceptions.TopLevelLookupException: Cant locate template for uri ‘polls/index.mako’
解决: settings 中加入:TEMPLATE_DIRS = [os.path.join(BASE_DIR, ‘templates’), os.path.join(BASE_DIR, ‘polls/templates’)]










## 参考资料
