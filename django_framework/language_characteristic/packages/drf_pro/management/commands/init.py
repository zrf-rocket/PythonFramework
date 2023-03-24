import os
import json
from django.conf import settings
from django.core.management.base import BaseCommand
from packages.drf_pro.models import Config


class Command(BaseCommand):
    help = "系统初始化配置"
    tags = "[init conf]"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write(f"{self.tags} start initializer config tbale...")

        conf_file = os.path.join(settings.BASE_DIR, "static", "files", "sys_config.json").replace("\\","/")
        if os.path.exists(conf_file):
            with open(conf_file,encoding="utf-8") as conf_f:
                configs = json.loads(conf_f.read())

                try:
                    for conf in configs:
                        is_exists = Config.objects.filter(name_en=conf["name_en"])
                        if is_exists:
                            conf_item = is_exists.first()
                            conf_item.name_zh = conf.get("name_zh", "")
                            conf_item.remark = conf.get("remark", "")
                            conf_item.conf_type = conf.get("conf_type", "")
                            conf_item.save()
                        else:
                            Config.objects.create(**conf)
                    self.stdout.write(f"{self.tags} sync over.....")
                except Exception as e:
                    self.stderr.write(f"{self.tags} sync error, info:{e}")
        else:
            self.stderr.write(f"not exists:{conf_file}")