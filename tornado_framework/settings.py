import global_settings_base
import logging.config
import os
from tornado.options import options, define

PORT = 5000
# define() 用来定义options选项变量的方法，定义的变量可以在全局的tornado.options.options中获取使用
define("port", default=PORT, help="run on the given port, default:5000", type=int)
define(name="address", default="127.0.0.1", help="bind address, default:127.0.0.1", type=str)
define("showname", default=global_settings_base.author, type=str, help="show author username")
# name 选项变量名，须保证全局唯一性，否则会报“Option 'xxx' already defined in ...”的错误；
# default　选项变量的默认值，如不传默认为None；
# type 选项变量的类型，从命令行或配置文件导入参数的时候tornado会根据这个类型转换输入的值，转换不成功时会报错，可以是str、float、int、datetime、timedelta中的某个，若未设置则根据default的值自动推断，若default也未设置，那么不再进行转换。可以通过利用设置type类型字段来过滤不正确的输入。
# multiple 选项变量的值是否可以为多个，布尔类型，默认值为False，如果multiple为True，那么设置选项变量时值与值之间用英文逗号分隔，而选项变量则是一个list列表（若默认值和输入均未设置，则为空列表[]）。
# help 选项变量的帮助提示信息，在命令行启动tornado时，通过加入命令行参数 --help　可以查看所有选项变量的信息（注意，代码中需要加入tornado.options.parse_command_line()）。


# 全局的options对象，所有定义的选项变量都会作为该对象的属性。
# 转换命令行参数，并将转换后的值对应的设置到全局options对象相关属性上。追加命令行参数的方式是--myoption=myvalue
options.parse_command_line()

LOG = logging.getLogger(__name__)

# 根目录下的templates
# BASE_DIR = os.path.dirname(__file__)

# practice目录下的templates
BASE_DIR = os.path.dirname(__file__) + os.sep + 'practice'

TITLE = "This is Python Tornado Freamwork"
STATIC_URL = 'tornado'
STATIC_VERSION = 11
# 持续显示的时间
OVERTIME = 60

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
