from django.db import models
from django.utils import timezone


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30, default="未知", verbose_name="用户名")
    email = models.EmailField(default="rocket_2014@126.com", verbose_name="邮箱")
    phone = models.CharField(max_length=15, default="-", verbose_name="联系电话")
    home_page = models.CharField(
        max_length=50,
        default="https://blog.csdn.net/zhouruifu2015/",
        verbose_name="个人主页",
    )
    create_date = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
