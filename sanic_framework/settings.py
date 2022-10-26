import os

db_settings = {
    "DB_HOST": "127.0.0.1",
    "DB_PORT": "3306",
    "DB_USER": "root",
    "DB_PWD": "123456",
}

BASE_DIR = os.path.dirname(__file__)

# Sanic 使用了三个 loggers ， 如果要创建自己的日志配置，则必须定义 ：root、error、access
LOGGING_CONFIG = {
    # "version": 1,
    # 'disable_existing_loggers': True,
    # 'handlers': {
        # 'console': {
        #     'class': 'logging.StreamHandler',
        #     # 'class': 'logging.handlers.RotatingFileHandler',
        #     # 'filename': './log/error.log',
        #     'level': 'DEBUG',
        #     'formatter': 'default',
        #     # 'encoding': 'utf-8'
        # },
        # 'error': {
            # 'class': 'logging.StreamHandler',
            # 'class': 'logging.handlers.RotatingFileHandler',
            # 'level': 'ERROR',
            # 'formatter': 'debug',
            # 'filename': './log/error.log',
            # 'maxBytes': 1024 * 1024 * 200,
            # 'backupCount': 5,
            # 'encoding': 'utf-8'
        # },
    # },
    # 'formatters': {
    #     'default': {
    #         'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)d | %(message)s',
    #     },
    #     'debug': {
    #         'format': '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d | %(message)s',
    #     }
    # },
    # 'loggers': {
        # 'access': {
        #     'level': 'DEBUG',
        #     'handlers': ['console', 'error'],
        #     'propagate': True
        # },
    # }
}
# %(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d
