# Create your tasks here
import time
# from packages.drf_pro.models import Publisher, Book
from celery import shared_task


@shared_task
def add(x, y):
    print("add sleep seconds.....")
    time.sleep(3)
    return x + y


@shared_task
def mul(x, y):
    time.sleep(6)
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    count = 100
    # count = Publisher.objects.count()
    print(f"Publisher count：{count}")
    return count


# @shared_task
# def rename_widget(widget_id, name):
#     w = Book.objects.get(id=widget_id)
#     w.name = name
#     w.save()


from django.core.management import call_command
# 将django自定义的指令放入到定时任务中
@shared_task
def send_email():
    call_command("send_email", )