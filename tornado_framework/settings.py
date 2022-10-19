import global_settings_base
import logging
import logging.config
import os
from os import path
from tornado.options import options, define

PORT = 5000
define("port", default=PORT, help="run on the given port, default:5000", type=int)
define("address", default="127.0.0.1", help="bind address, default:127.0.0.1", type=str)
options.parse_command_line()

LOG = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(__file__)

# 开启调试模式

LOG_FILE = os.environ.get("LOG_FILE", "/tmp/tornado.log")

settings = dict(
    template_path=os.path.join(BASE_DIR, "templates"),
    static_path=os.path.join(BASE_DIR, "static"),
    xsrf_cookies=False,
    cookie_secret="bb904fe1b095cab9499a85f864e6c612",
    port=PORT,
    debug=global_settings_base.DEBUG
)
