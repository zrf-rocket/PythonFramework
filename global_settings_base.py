import logging.config
import os

url = "https://gitee.com/SteveRocket/python_framework.git"
author = "zhouruifu"
name_en = "SteveRocket"
email = "rocket_2014@126.com"

##### 数据库相关配置
# redis配置
REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_DB = os.environ.get("REDIS_DB", "0")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")

# MySQL配置
MYSQL_HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = os.environ.get("MYSQL_PORT", "3306")
MYSQL_USER = os.environ.get("MYSQL_USER", "")
MYSQL_PWD = os.environ.get("MYSQL_PWD", "")
MYSQL_DB = os.environ.get("MYSQL_DB", "")
# MongoDB配置
MONGO_HOST = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
MONGO_USER = os.environ.get("MONGO_USER", "")
MONGO_PDW = os.environ.get("MONGO_PDW", "")
# Elasticsearch配置
ES_HOST = os.environ.get("ES_HOST", "127.0.0.1")
ES_PORT = os.environ.get("ES_PORT", "7200")
ES_PWD = os.environ.get("ES_PWD", "")

# 调试模式
DEBUG = os.environ.get("DEBUG", False)

##### 日志相关配置
# 日志文件配置
LOG_FILE = os.environ.get('LOG_FILE', '/tmp/framework.log')
# 服务和端口
NAMESPACE_NAME = "{NAMESPACE_NAME}"

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] {NAMESPACE_NAME} %(levelname)s  %(name)s: %(message)s'.format(
                **{'NAMESPACE_NAME': NAMESPACE_NAME}
            )  # noqa
        }
    },
    'handlers': {
        'console_simple': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_simple': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': LOG_FILE,
        },
    },
    'loggers': {
        'tornado': {
            'handlers': ['console_simple'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console_simple'],
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
