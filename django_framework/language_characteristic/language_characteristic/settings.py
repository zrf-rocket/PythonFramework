"""
Django settings for language_characteristic project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import crontab
import os
import sys
from datetime import timedelta
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # WindowsPath
# Django项目文件夹所在目录的绝对路径（项目根目录），项目中的所有的文件都需要依赖此路径
# 老版本写法
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # str类型



sys.path.insert(0, os.path.join(BASE_DIR, 'packages'))
# 解决自定义packages文件夹 下面放置app的问题
# django.core.exceptions.ImproperlyConfigured: Cannot import 'mako_pro'. Check that 'packages.mako_pro.apps.MakoProConfig.name' is correct.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!hh4oj&-(8xp$d-17!bzmx+ilgkccym32ovkx7hr4f#9cs5y-6'
# 是Django根据自己算法生成的一大串随机数，本质是个加密盐，一般配合加密算法 Hash、MD5 一起使用，用于防止CSRF（Cross-site request forgery）跨站请求伪造攻击。
# 用户密码的加密或者建立会话时用到的 sessionid 都需要用到 SECRET_KEY
# 当部署Django项目到生产环境中时，Django文档建议不直接在settings.py里输入字符串，而是采取下面几种方法读取SECRET_KEY。
# 从环境变量中读取SECRET_KEY
# SECRET_KEY = os.environ['SECRET_KEY']

# 从服务器上Django项目文件价外的某个文件读取
# with open('/etc/secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 默认值是True。在本地开发测试环境下设置DEBUG=True可以显示bug信息，便于开发者找出代码错误所在。
# 当部署项目在生产环境时，请切记设置DEBUG=False。因为生产环境下打开Debug一旦发生错误或异常会暴露很多敏感设置信息（比如数据库密码)。
# 注意: 当设置DEBUG=False, 一定要设置ALLOWED_HOSTS选项, 否则会抛出异常。



ALLOWED_HOSTS = []
# 允许的主机
# 默认值为空[]。设置ALLOWED_HOSTS是为了限定用户请求中的host值，以防止黑客构造包来进行头部攻击。
# DEBUG=True: ALLOWED_HOSTS可以为空，也可设置为['127.0.0.1', 'localhost']
# 用于配置能够访问当前站点的域名（IP地址），当 DEBUG = False 时，必须填写

# DEBUG=False: ALLOWED_HOSTS=['123.124.78.123', 'www.domain.com'，'127.0.0.1']
# 当关闭DEBUG时，HOST一般为服务器公网IP或者注册域名。 当还需要使用子域名时，可以用.bat.com。它将匹配bat.com, www.bat.com和news.bat.com。
# 在正式部署项目时，尽量不要设置ALLOWED_HOSTS=['*']，表示任何网络地址都能访问到当前项目。


############################################################ 注册APP
# Application definition
# 用来安装的应用（APP）的列表，增删一个项目(Project)所包含的应用(APP)。只有对列入此项的APP, Django才会生成相应的数据表
# Django 把默认自带的应用放在这个列表里，比如 Admin 后台应用、Auth 用户管理系统等
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    ### 三方APP
    # 'haystack'

    'rest_framework',
    #### allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',


    ### celery app
    'django_celery_results',
    'django_celery_beat',

    ### 自己的APP
    'django4_characteristic',
    ### packages中自己的APP
    'packages.mako_pro',
    'packages.drf_pro',
    'packages.mongo_orm_pro'
]

SITE_ID = 1


############################################################ 中间件
MIDDLEWARE = [
    # 自带中间件
    'django.middleware.security.SecurityMiddleware', # 为request/response提供了几种安全改进;
    'django.contrib.sessions.middleware.SessionMiddleware', # 开启session会话支持，用于处理会话
    'django.middleware.common.CommonMiddleware', # 基于APPEND_SLASH和PREPEND_WWW的设置来重写URL，如果APPEND_SLASH设为True，并且初始URL 没有以斜线结尾以及在URLconf 中没找到对应定义，这时形成一个斜线结尾的新URL；
    'django.middleware.csrf.CsrfViewMiddleware', # 添加跨站点请求伪造的保护，通过向POST表单添加一个隐藏的表单字段，并检查请求中是否有正确的值；
    'django.contrib.auth.middleware.AuthenticationMiddleware', # 在视图函数执行前向每个接收到的user对象添加HttpRequest属性，表示当前登录的用户，无它用不了request.user
    'django.contrib.messages.middleware.MessageMiddleware', # 开启基于Cookie和会话的消息支持
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # 对点击劫持的保护
    # 自定义中间件
    'packages.drf_pro.middleware.calc_middleware',  # 以方法命名的中间件
    'packages.drf_pro.middleware.SimpleMiddleware',
    'packages.drf_pro.middleware.LoginRequiredMiddleware'
]

# 项目根URL
# 指定了当前项目的根 URL，是 Django 路由系统的入口
ROOT_URLCONF = 'language_characteristic.urls'

LOGIN_URL = "/admin/login/"
OPEN_URLS = ["/admin/"]

# 项目部署时，Django 的内置服务器将使用的 WSGI 应用程序对象的完整 Python 路径。
WSGI_APPLICATION = 'language_characteristic.wsgi.application'

############################################################ HAYSTACK
HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.elasticsearch7_backend.Elasticsearch7SearchEngine',  # 引擎版本需要根据自己的版本进行选择
        # 'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine', # error django框架在2.0版本以上已经不存在whoosh_cn_backend
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'URL': 'http://127.0.0.1:9200/',  # es的服务地址
        'INDEX_NAME': 'steverocket', # 索引的名称，必须是小写
    }
}


############################################################ PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',   # 数据库引擎
        'NAME': 'steverocket',         # 数据库名，Django不会帮你创建，需要自己进入数据库创建。
        'USER': 'postgres',     # 设置的数据库用户名
        'PASSWORD': '123456',     # 设置的密码
        'HOST': 'localhost',    # 本地主机或数据库服务器的ip
        'PORT': '5432',         # 数据库使用的端口
        # 设置持久化连接时间
        # 如果没有持久化连接，每个请求都会与数据库创建一个连接，直到请求结束关闭连接。每次建立和关闭连接也需要花费一些时间
        'CONN_MAX_AGE': 60,     # 60秒  不宜设置过大。当并发请求数量很高时，应该设置低一点。反之可以设置高一点。
    }
}


############################################################ MySQL
# Database
# Django默认使用轻量级的SQLite数据库，无需进行任何设置开箱即用。
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

'''
# MySQL
# pip install pymysql
# pip install mysqlclient
# 配置方式1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 数据库引擎
        'NAME': 'test3',   # 数据库名，Django不会帮你创建，需要自己进入数据库创建。
        'HOST': '127.0.0.1',  # 数据库服务器的ip
        'USER': 'root',  # 设置的数据库用户名
        'PASSWORD': '123456', # 设置的密码
        'PORT': 3306,  # 数据库使用的端口
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci'
        },
    },
}
# 配置方式2：采取读取外部配置文件的方式，更安全
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # 数据库引擎
#         'OPTIONS': {
#             'read_default_file': 'my.cnf',
#         }
#     },
# }

'''

############################################################ MongoDB
# MongoDB djongo
"""
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': "django4",
        'ENFORCE_SCHEMA': False,  # 如果您希望 Djongo 免迁移，请在您的数据库配置中设置 ENFORCE_SCHEMA: False。使用此设置，集合是动态创建的，Djongo 不会将 SQL 语句转换为 MongoDB 命令。
        'CLIENT': {
            'host': 'mongodb://127.0.0.1:27017/django4',
            # 'username': '',
            # 'password': '',
            # 'authSource': 'admin1',
            # 'authMechanism': 'SCRAM-SHA-1',
        }
    }
}
"""

import mongoengine

# conn = mongoengine.connect('mongodb://:@127.0.0.1:27017/django4/')  # pymongo.errors.InvalidName: database names cannot contain the character '.'
mongoengine_conn = mongoengine.connect(host="127.0.0.1", port=27017, db="django4")
############################################################ Elasticsearch
# Elasticsearch








############################################################ 缓存设置 Redis
# CACHES Redis
import fakeredis

CACHES = {
    'default': {
        # "BACKEND": "django_redis.cache.RedisCache",
        "BACKEND": "django.core.cache.backends.redis.RedisCache",

        # 默认客户端
        "LOCATION": "redis://127.0.0.1:6379/1",  # redis服务器地址信息

        # 默认客户端支持主从配置  以下第一个字段代表 master 服务器, 第二个字段代表 slave 服务器.
        # "LOCATION": [
        #     "redis://127.0.0.1:6379/1",
        #     "redis://127.0.0.1:6378/1"
        # ],
        # 分片客户端
        # "LOCATION": [
        #     "redis://127.0.0.1:6379/1",
        #     "redis://127.0.0.1:6379/2"
        # ],

        "OPTIONS": {
            # 可扩展客户端
            # django_redis 设计的非常灵活和可配置。它提供了可扩展的后端，拥有易扩展的特性
            # 默认客户端
            # "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # 分片客户端
            # "CLIENT_CLASS": "django_redis.client.ShardClient",
            # 集群客户端
            # "CLIENT_CLASS": "django_redis.client.HerdClient",
            # 设置集群超时 (默认值为: 60s)
            # "CACHE_HERD_TIMEOUT": 100,


            # 选择数据库
            # 'db': '1',

            # 设置密码
            # "PASSWORD": "mysecret"


            # 可扩展 Redis 客户端
            # 定制基于 Redis 的客户端可以用来测试 可以不用依赖真的 redis server 做集成测试.
            "REDIS_CLIENT_CLASS": "fakeredis.FakeStrictRedis",
            # django-redis 默认使用 redis.client.StrictClient 作为 Redis 客户端, 你可以使用其他客户端替代, 比如上面用于测试时用 fakeredis 代替真实客户端
            # 使用 REDIS_CLIENT_CLASS in the CACHES 来配置你的客户端, 使用 REDIS_CLIENT_KWARGS 提供配置客户端的参数 (可选).
            # "REDIS_CLIENT_CLASS": "my.module.ClientClass",
            # "REDIS_CLIENT_KWARGS": {"some_setting": True},


            # django-redis 使用 pickle 序列化几乎所有数据.默认使用最新的 pickle. 如果你想设置其他版本, 使用 PICKLE_VERSION 参数
            "PICKLE_VERSION": -1,  # Use the latest protocol version

            # 套接字超时设置使用 SOCKET_TIMEOUT 和 SOCKET_CONNECT_TIMEOUT 参数
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds  socket 建立连接超时设置
            "SOCKET_TIMEOUT": 5,  # in seconds  连接建立后的读写操作超时设置

            # django-redis 支持压缩, 但默认是关闭的. 可以激活它
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            # 使用 lzma 压缩
            # "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",

            # 当redis关闭时 如果不希望触发异常，为了忽略连接异常, 使用 IGNORE_EXCEPTIONS 参数
            "IGNORE_EXCEPTIONS": True,

            # 连接池
            # django-redis 使用 redis-py 的连接池接口, 并提供了简单的配置方式. 除此之外, 你可以为 backend 定制化连接池的产生.
            # redis-py 默认不会关闭连接, 尽可能重用连接
            # 配置默认连接池，CONNECTION_POOL_KWARGS 设置连接池的最大连接数量即可
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},

            # 可扩展解析器
            # redis-py (django-redis 使用的 Redis 客户端) 支持的纯净 Python Redis 解析器可以满足大部分普通任务, 但如果你想要性能更好, 可以使用 hiredis
            # hiredis 是一个用 C 写的 Redis 客户端, 并且他的解析器可以用在 django-redis 中
            "PARSER_CLASS": "redis.connection.HiredisParser",
            'POOL_CLASS': 'redis.ConnectionPool',


            # 可扩展序列器
            # 客户端在将数据发给服务器之前先会序列化数据. django-redis 默认使用 Python pickle 序列化数据.
            # 如果需要使用 json 序列化数据, 使用 JSONSerializer
            "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
            # 使用 MsgPack http://msgpack.org/ 进行序列化 (需要 msgpack-python 库支持)
            # "SERIALIZER": "django_redis.serializers.msgpack.MSGPackSerializer",
        }
    }
}
# 为了忽略所有缓存连接异常, 使用 DJANGO_REDIS_IGNORE_EXCEPTIONS 也可以给所有缓存配置相同的忽略行为
DJANGO_REDIS_IGNORE_EXCEPTIONS = True

# 日志忽略异常
# 当使用 IGNORE_EXCEPTIONS 或者 DJANGO_REDIS_IGNORE_EXCEPTIONS 参数忽略异常时, 你也许会用到 DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS 参数来配置日志异常
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True
# 如果你想设置指定的 logger 输出异常, 只需要设置全局变量 DJANGO_REDIS_LOGGER 为 logger 的名称或其路径即可. 如果没有 logger 被设置并且 DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS=True 时此参数将取 name
DJANGO_REDIS_LOGGER = 'some.specified.logger'


## Memcached缓存

# Memcached是基于内存的缓存，Django原生支持的最快最有效的缓存系统。对于大多数场景，推荐使用Memcached，数据缓存在服务器端。使用前需要通过pip安装memcached的插件python-memcached和pylibmc，可以同时支持多个服务器上面的memcached
### localhost
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }


### unix soket
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'unix:/tmp/memcached.sock',
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'TIMEOUT': 300, # 缓存超时时间（默认300秒，None表示永不过期，0表示立即过期）
#         'LOCATION': [
#             '192.168.1.89:11211',
#             '192.168.1.90:11211',
#         ],
#         'MAX_ENTRIES': 3,  # 当前最大缓存数
#         # 也可以给缓存机器加权重，权重高的承担更多的请求，如下
#         # 'LOCATION': [
#         #     ('192.168.1.89:11211',5),
#         #     ('192.168.1.90:11211',1),
#         # ]
#         'CULL_FREQUENCY': 3,  # 缓存到达最大个数之后，剔除缓存个数的比例，即 1/CULL_FREQUENCY（默认3）
#     }
#  }



### 数据库缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }


# ### 文件系统缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',# Linux 这个是文件夹的路径
#         # 'LOCATION': 'c:\tmp\bar',#windows下的示例
#     }
# }


# ### 本地内存缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake'
#     }
# }








########################################################## COOKIE与SESSION设置
# 缓存临时性数据，如session
# SESSION_ENGINE = "django.contrib.sessions.backends.db"  # 引擎（默认）
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SESSION_CACHE_ALIAS = "default"

# SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，

# SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）

# SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）

# SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）

# SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）

# SESSION_COOKIE_AGE = 60 * 30  # Session的cookie失效日期（30min）（默认）

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 是否关闭浏览器使得Session过期（默认）

# SESSION_SAVE_EVERY_REQUEST = True  # 是否每次请求都保存Session，默认修改之后才保存


########################################################## 模板设置 - 模板缓存
# django默认情况下每处理一个请求都会使用模板加载器  都会去文件系统搜索模板。然后渲染模板。 可以通过cached.Loader开启模板缓存加载，此时只会查找并且解析模板一次，可以大大提升模板渲染效率
# 如果在根目录下建立了一个templates文件夹，专门用于存放属于项目的模板文件，还需要在settings.py中显示地将模板目录设置为BASE_DIR目录下的templates文件夹。
TEMPLATES = [
    {
        #  Django 默认自带模板引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 设置项目模板目录
        # 'DIRS': [BASE_DIR / 'templates'],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'DIRS': [],

        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 以下包含了4个默认的全局上下文处理器
                'django.template.context_processors.debug',  # 在模板里面可以直接使用settings的DEBUG参数以及强大的sql_queries:它本身是一个字典，其中包括当前页面执行SQL查询所需的时间
                'django.template.context_processors.request', # 在模板中可以直接使用request对象
                'django.contrib.auth.context_processors.auth', # 在模板里面可以直接使用user，perms对象
                'django.contrib.messages.context_processors.messages', #在模板里面可以直接使用message对象
                # Django另外的几个全局上下文处理器
                'django.template.context_processors.i18n', # 在模板里面可以直接使用settings的LANGUAGES和LANGUAGE_CODE
                'django.template.context_processors.media', # 可以在模板里面使用settings的MEDIA_URL参数
                'django.template.context_processors.csrf', # 给模板标签 csrf_token提供值
                'django.template.context_processors.tz',  # 可以在模板里面使用 TIME_ZONE参数。
                # 自定义的全局上下文处理器
                'packages.mako_pro.context_processors.global_site_name'
            ],
            # 开启模板缓存加载
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    # 'path.to.custom.Loader',
                ]),
            ],
        },
    },
]



############################################################
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# 支持插拔的密码验证器，且可以一次性配置多个，Django 通过这些内置组件来避免用户设置的密码等级不足的问题。
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 国际化 Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# 语言配置项  英文：'en-us' 或 中文：'zh-Hans'
LANGUAGE_CODE = 'en-us'

# 设置时区 服务端时区的配置项 世界时区 'UTC' 或中国时区 'Asia/Shanghai'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'


# USE_118N 和 USE_L10N 这两个变量值表示是否需要开启国际化和本地化功能。默认开启的状态。
# I18N 指的是国际化英文缩写，L10N 指的是本地化英文缩写。
# 默认为True，是否启用自动翻译系统
USE_I18N = True

# 默认False，以本地化格式显示数字和时间
# USE_L10N = True


USE_TZ = False
# 对时区的处理方式，当设置为 True 的时候，存储到数据库的时间是世界时间'UTC'
# 默认值True，若使用了本地时间，必须设为False



STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# 静态资源的存放位置，静态资源包括 CSS、JS、Images
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# STATIC_URL和STATIC_ROOT 关于静态文件(如CSS, JS,和图片)的最重要的设置，一般设置如下。
# STATIC_URL是静态文件URL，设置后可以通过使用{% static 'assets/imges/xxx.jpg' %}方式直接访问/static/文件夹里的静态文件。
# 如果你设置了STATIC_ROOT, 当运行python manage.py collectstatic命令的时候，Django会将各app下所有名为static的文件夹及其子目录复制收集到STATIC_ROOT。
# 把静态文件集中一起的目的是为了更方便地通过Apache或Nginx部署。

# 一般情况下会尽量把静态文件只放在static文件夹或它的子目录下，所以上述两个设置对于一般项目是够的。那么问题来了，如果还有一些文件夹中也有静态文件，
# 可是文件夹并不是以static命名也不在static子目录里，此时也希望搜集使用那些静态文件，该怎么办呢？这时就要设置静态文件目录STATICFILES_DIRS值了。
# STATICFILES_DIRS = [
#     "/home/user/practice",
#     "/guides", # Django会将此处两个文件夹内容也复制到STATIC_ROOT
# ]
# 默认值为空。当设置该选项后，"python manage.py collectstatic"命令会把static文件夹及静态文件目录STATICFILES_DIRS里的静态文件都复制到一份到STATIC_ROOT。注意里面的路径必需是绝对路径。



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





############################################################ Celery
# 最重要的配置，设置消息broker,格式为：db://user:password@host:port/dbname
# 如果redis安装在本机，使用localhost
# 如果docker部署的redis，使用redis://redis:6379
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'

# celery时区设置，建议与Django settings中TIME_ZONE同样时区，防止时差
# Django设置时区需同时设置USE_TZ=True和TIME_ZONE = 'Asia/Shanghai'
CELERY_TIMEZONE = TIME_ZONE

# 为django_celery_results存储Celery任务执行结果设置后台
# 格式为：db+scheme://user:password@host:port/dbname
# 支持数据库django-db和缓存django-cache存储任务状态及结果
CELERY_RESULT_BACKEND = "django-db"  # 任务结果数据的储存
# CELERY_CACHE_BACKEND = 'django-cache' # 也可以使用缓存

# celery内容等消息的格式设置，默认json
CELERY_ACCEPT_CONTENT = ['application/json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# 为任务设置超时时间，单位秒。超时即中止，执行下个任务。
# CELERY_TASK_TIME_LIMIT = 5

# 为存储结果设置过期日期，默认1天过期。如果beat开启，Celery每天会自动清除。
# 设为0，存储结果永不过期
# CELERY_RESULT_EXPIRES = 0

# 任务限流
# CELERY_TASK_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

# Worker并发数量，一般默认CPU核数，可以不设置
# CELERY_WORKER_CONCURRENCY = 2

# 每个worker执行了多少任务就会死掉，默认是无限的
# CELERY_WORKER_MAX_TASKS_PER_CHILD = 200

# 消息中间件的连接
BROKER_URL = CELERY_BROKER_URL

# 任务注册路径
# CELERY_INCLUDE =""


# 配置文件添加周期性任务
CELERY_BEAT_SCHEDULE = {
    # 同一任务可以设置成不同的调用周期，定义成不同的任务名即可。
    "add-every-30s": {
        "task": "django4_characteristic.tasks.show",
        'schedule': 30.0, # 每30秒执行1次
        'args': (3, 8) # 传递参数-
    },
    "add-every-day": {
        "task": "django4_characteristic.tasks.show",
        'schedule': timedelta(hours=1), # 每小时执行1次
        'args': (3, 8) # 传递参数-
    },
    # 可以通过crontab设置定时任务
    # 希望在特定的时间(某月某周或某天)执行一个任务，
    # 'add-every-monday-morning': {
    #     'task': 'app.tasks.add',
    #     'schedule': crontab(hour=7, minute=30, day_of_week=1),
    #     'args': (7, 8),
    # },
}


CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'




############################################################ django 文件存储系统
DEFAULT_FILE_STORAGE = ""



############################################################ 邮箱服务配置
ACCOUNT_AUTHENTICATION_METHOD = 'username_emial'
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/accounts/profile/'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
'''
EMAIL_HOST = 'smtp.qq.com' # 发送者邮箱服务器
EMAIL_PORT = 25 # 端口
EMAIL_HOST_USER = ''        # 发送者用户名（邮箱地址）
EMAIL_HOST_PASSWORD = ''    # 发送者密码
EMAIL_USE_SSL = True
EMAIL_USE_TLS = True        # 这里必须是 True，否则发送不成功
EMAIL_FROM = 'xxxx@qq.com'   # QQ 账号
DEFAULT_FROM_EMAIL = 'xxx@qq.com'
'''



############################################################
# AUTH_USER_MODEL = auth.user
# 默认为auth.user。也可以为自定义用户模型, 如users.user。



# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# media文件夹一般用于放置用户上传的文件。对于此文件夹的权限设置异常重要，因为用户可能会上传可执行的文件，影响网站和服务器的安全。
# 对于此文件夹权限，建议使用sudo chmod 755 media命令设置成755，而不要使用777（可读、可写、可执行)



###################################### 数据库设置
# DATABASE_ROUTERS = ["bkmonitor.db_routers.BackendRouter"]
# DATABASE_APPS_MAPPING = {
#     'platform_***':'default',
#     'data_***':'data_***',
# }


###################################### Email配置
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "rocket_2014@126.com"
ADMINS = [("steverocket", "rocket_2014@126.com"), ]
