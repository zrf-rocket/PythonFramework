from django.http import HttpResponse
from django.shortcuts import render
import time
# Create your views here.

from django.db import transaction, connection
from django.db.models import F
from lock_app.models import Lock

def operator_table():
    # for index in range(22):
    #     Lock.objects.update_or_create({"name":f"SteveRocket{index}"})
    #     print(index)
    #     time.sleep(10)

    for index in range(3):
        names = []
        for num in range(10, 20):
            names.append(f"SteveRocket{index}-{num}")
        print("批量添加......")
        Lock.objects.bulk_create(names)
        time.sleep(10)

@transaction.atomic
def update_table(request):
    print("update table.......")
    operator_table()

    #
    # # 行级的排它锁
    # lock = Lock.objects.select_for_update().get(name="my_lock")
    #
    # if lock.is_locked:
    #     return HttpResponse("table is locked")
    #
    # lock.is_locked = True
    # lock.save()
    # try:
    #     print("正在执行更新操作")
    #     time.sleep(60)
    #     print("更新操作执行完毕.....")
    #     lock.is_locked = False
    #     lock.save()
    # except Exception:
    #     # 发生异常时，确保解锁表
    #     lock.is_locked = False
    #     lock.save()
    #     raise
    return HttpResponse("table updated successfully")