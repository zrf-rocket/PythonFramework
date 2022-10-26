import settings
from sanic import Sanic
from sanic.log import logger
from sanic.response import json, text

app = Sanic("scanic_framework", log_config=settings.LOGGING_CONFIG)

app.config["DB_HOST"] = "127.0.0.1"
app.config.DB_USER = 'root'
app.config.DB_NAME = "sanic_db"

app.config.update(settings.db_settings)


# json （任意）-JSON正文
@app.route("/")
async def index(request):
    return json({"framework_name": "sanic", "message": request.json})


# args （dict）-查询字符串变量。查询字符串是类似于 ?key1=value1&key2=value2
@app.route("/query_args")
async def query_args(request):
    """
    http://localhost/query_args?key1=value1&key2=value2
    """
    return json({
        "args": request.args,
        "query_args": request.query_args,
        "url": request.url,
        "query_string": request.query_string
    })


@app.route("/text")
async def show_text(request):
    logger.info("this is sanic logging....")
    return text("this is sanic text")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True, access_log=True)
