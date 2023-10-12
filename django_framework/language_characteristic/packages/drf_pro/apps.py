import sys
sys.path.append(".")
from django.apps import AppConfig, apps
from django.conf import settings
from django.db.models.signals import post_migrate

class DrfProConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # Django APP默认是直接在项目的根目录下面，此处换在了packages目录下
    name = "packages.drf_pro"
    verbose_name = "drf_pro"
    label = "drf_pro"

    def ready(self):
        # TODO 目录在库的搜索路径下会首先被搜索，目录会代替同名的模块被加载。如果尝试导入同名的模块和包时，包会被导入。注意避免：包名和模块名相同
        # handlers
        from .handler import (
            custom_migrate,
            custom_migrate2
        )
        post_migrate.connect(custom_migrate, sender=self)  # 参数 sender=self 必填
        if settings.DATABASES.get("rocket"):
            post_migrate.connect(custom_migrate2, sender=self)
