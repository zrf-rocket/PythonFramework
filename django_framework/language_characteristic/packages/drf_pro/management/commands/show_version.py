import sys
from importlib import import_module
from django.core.management.base import BaseCommand

# class CommandHello(BaseCommand): # error 错误的命名
class Command(BaseCommand):
    """
    执行指令：python manage.py show_version
    显示帮助信息 python manage.py show_version -h
    输入库名称，显示库的帮助信息 python manage.py show_version sys
    """
    # 帮助信息 用于备注命令的用途及如何使用
    help = f"帮助信息"

    # 可选
    def add_arguments(self, parser):
        # 给命令添加一个名为name的参数
        parser.add_argument('name')

    # 业务逻辑 通过options字典接收name参数值
    def handle(self, *args, **options):
        self.stdout.write(f"{self.help}，当前系统环境版本：{sys.version}")
        self.stdout.write("this is django custom command line")
        help(import_module(options.get("name")))