import time
from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.BooleanField()
    login_datetime = models.DateTimeField(auto_now_add=time.time())

    def __str__(self):
        return self.name
