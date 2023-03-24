import os
from celery import Celery

#设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'language_characteristic.settings')

# 实例化
app = Celery("language_characteristic")

# namespace='CELERY'作用是允许你在Django配置文件中对Celery进行配置
# 但所有Celery配置项必须以CELERY开头，防止冲突
app.config_from_object('django.conf:settings', namespace="CELERY")
# app.config_from_cmdline()
# app.config_from_envvar()

# app.autofinalize()


# Load task modules from all registered Django apps.
# 自动从Django的已注册app中发现任务
app.autodiscover_tasks()

# 测试任务
@app.task(bind=True)
def debug_task(self):
    print(f"Request:{self.request!r}")

@app.task
def test():
    print("专属于language_characteristic项目的任务.....")

# 使用celery定义任务时，避免在一个任务中调用另一个异步任务，容易造成阻塞。
# 当我们使用@app.task装饰器定义我们的异步任务时，那么这个任务依赖于根据项目名myproject生成的Celery实例。然而我们在进行Django开发时为了保证每个app的可重用性，
# 我们经常会在每个app文件夹下编写异步任务，这些任务并不依赖于具体的Django项目名。使用@shared_task 装饰器能让我们避免对某个项目名对应Celery实例的依赖，使app的可移植性更强。