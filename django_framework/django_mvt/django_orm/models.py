from django.db import models
from django.db.models.indexes import Index


class Product(models.Model):
    """
    商品表
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 单价
    stock = models.IntegerField()  # 库存
    description = models.TextField(null=True)  # 描述
    create = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    订单表
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 单价
    stock = models.IntegerField()  # 库存
    description = models.TextField(null=True)  # 描述
    address = models.TextField(default="")

    def __str__(self):
        return self.name
