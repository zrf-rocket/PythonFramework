# Create your tasks here
from celery import shared_task

# Django项目中所有需要Celery执行的异步或周期性任务都放在tasks.py文件里，该文件可以位于project目录下，也可以位于各个app的目录下。
# 各个app目录下可以复用的task建议使用@shared_task定义。
@shared_task
def show(num1, num2):
    result = num1+num2
    print(f"this is django4_characteristic app......{result}")
    return result
