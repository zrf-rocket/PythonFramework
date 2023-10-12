from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(verbose_name="FIRST_NAME",max_length=10, null=False)
    last_name = models.CharField("LAST_NAME", max_length=10, null=False)
    nick_name = models.CharField(max_length=10, null=False)
    age = models.IntegerField(null=False)