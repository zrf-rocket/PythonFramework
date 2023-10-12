from django.db import models

# Create your models here.

class Lock(models.Model):
    """演示排它锁"""
    name = models.CharField(max_length=125, unique=True)
    is_locked = models.BooleanField(default=False)