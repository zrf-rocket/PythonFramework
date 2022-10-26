# Sanic配置
import settings
from sanic import Sanic
from sanic.log import logger, LOGGING_CONFIG_DEFAULTS
from sanic.response import json, text

# 默认情况下， log_config 参数设置为使用 sanic.log.LOGGING_CONFIG_DEFAULTS 配置字典
# app = Sanic("scanic_framework", log_config=LOGGING_CONFIG_DEFAULTS)

# 使用自定义的日志配置
app = Sanic("scanic_framework", log_config=settings.LOGGING_CONFIG)


app.config["DB_HOST"] = "127.0.0.1"
app.config.DB_USER = 'root'
app.config.DB_NAME = "sanic_db"
# 配置sanic：从dict
app.config.update(settings.db_settings)


# 从py文件
# app.update_config(f"{settings.BASE_DIR}\conf.py")

@app.route("/")
async def index(request):
    return json({"framework_name": "sanic"})


@app.route("/text")
async def show_text(request):
    logger.info("this is sanic logging....")
    return text("this is sanic text")


if __name__ == '__main__':
    # access_log控制日志的关闭与开启
    # app.run(host="0.0.0.0", port=80, debug=False, access_log=False) # 在处理请求时跳过调用日志记录函数。
    app.run(host="0.0.0.0", port=80, debug=True, access_log=True)
