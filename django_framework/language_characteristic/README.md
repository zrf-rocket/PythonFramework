## Django
本环境采用基于Python3.11-django4.1.6

1. 创建项目  
django-admin startproject language_characteristic
2. 切换到项目根目录  
cd language_characteristic
3. 项目根目录下创建APP  
django-admin startapp django4_characteristic
4. 项目迁移  
python manage.py makemigrations # 检查模型有无变化   
python manage.py migrate # 将变化迁移至数据表
5. 创建管理员用户  
createsuperuser
6. 创建packages目录，用于后续其他的APP示例  
cd packages  
django-admin startapp mako_pro  
django-admin startapp drf_pro

   
### 单元测试


#### Django 单元测试  ModuleNotFoundError: No module named 
```
在测试脚本所在目录下新建 __init__.py文件即可
```

#### 通过单元测试迁移数据库







### 目录结构
```
custom_app 纯手动建(目录和文件)的自定义app
|- django4_characteristic   # Django4新特性 APP
|- language_characteristic  # 生成项目的初始目录，项目相关配置目录
    |-- __init__.py # 包含初始化文件，该文件用于标识当前所在的目录是一个Python包，如果在此文件中，通过import导入其他方法或者包，会被Django自动识别。
    |-- asgi.py # 异步服务网关接口，一个介于网络协议服务和Python应用之间的标准接口，能够处理多种通用的协议类型，包括HTTP，HTTP2和WebSocket。同WSGI一样，Django也支持使用ASGI来部署，它是为了支持异步网络服务器和应用而新出现的Python标准。
    |-- settings.py # 包括app路径，数据库配置，sql语句，静态文件目录，中间件，session存储的相关配置。
    |-- urls.py # 是django的主路由，可以在此处关联不同app中的子路由。
    |-- wsgi.py # WSGI（WebServerGatewayInterfac）Web服务网关接口，用来描述Web服务器如何与Web应用通信的规范。
|- packages             # 用于存放其它的APP
    |-- drf_pro         # Django Rest Framework APP  ORM
        |--- handlers
        |--- migrations
        |--- admin.py（默认）
        |--- apps.py（默认）
        |--- constants.py
        |--- context_processors.py
        |--- filtersets.py
        |--- forms.py
        |--- handler.py
        |--- middleware.py
        |--- models.py（默认）
        |--- operation_records.py
        |--- resources.py  此处编写业务逻辑（工作重点）
        |--- schedulers.py
        |--- serializers.py  负责请求数据与返回数据的校验，包括简单的数据渲染
        |--- signals.py
        |--- tasks.py celery任务文件
        |--- tests.py（默认）
        |--- urls.py 路由配置文件
        |--- utils.py
        |--- views.py（默认）定义视图文件，定义请求方法、使用到的Resource、是否分页、鉴权等配置（几乎没有代码量）
        |--- viewsets.py
    |-- mako_pro        # mako模板引擎 APP   
    |-- mongo_orm_pro   # MongoDB ORM APP
|- static
|- templates
|- tests 单元测试目录
|- units
|- utils
```
[点击查看mako_pro工程特性](https://gitee.com/SteveRocket/python_framework/tree/master/django_framework/mako_pro)



