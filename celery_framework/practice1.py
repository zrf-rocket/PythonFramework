import settings
from celery import Celery

# 使用redis作为broker
app = Celery("test1", broker=settings.REDIS_URL)

# 创建任务函数  使用app.task注册到broker中
@app.task
def my_task():
    print("celery task running.....")

# celery -A practice1 worker --loglevel=info
