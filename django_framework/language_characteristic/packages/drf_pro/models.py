from django.db import models
from django.urls import reverse


# Create your models here.

# Model (模型) 简而言之即数据模型，是一个Django应用的核心。模型不是数据本身（比如数据表里的数据), 而是抽象的描述数据的构成和逻辑关系。
# 每个Django的模型(model)实际上是个类，继承了models.Model。每个Model应该包括属性(字段)，关系（比如单对单，单对多和多对多)和方法。当你定义好Model模型后，Django的接口会自动帮你在数据库生成相应的数据表(table)。这样你就不用自己用SQL语言创建表格或在数据库里操作创建表格了
# Django模型的组成: 字段(基础字段和关系字段), META选项和方法。

class Publisher(models.Model):
    name = models.CharField(max_length=30)  # max_length必选参数
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        # app_label = "drf_pro"
        app_label = "packages.drf_pro"

class Config(models.Model):
    """
    系统配置表
    """
    name_zh = models.CharField("配置名称", max_length=50, unique=True, null=False)
    name_en = models.CharField('配置名称(英文)', max_length=50, unique=True, null=False)
    conf_value = models.TextField("配置值")
    remark = models.TextField('配置描述', null=False)
    conf_type = models.CharField('配置分类', max_length=10, default='0')

    class Meta:
        db_table = "config"

# models.Model提供的常用模型字段包括基础字段和关系字段。
class Book(models.Model):
    name = models.CharField(max_length=30)

    description = models.TextField(blank=True, null=True, default='')  # Field是否必需(blank = True or False)，是否可以为空 (null = True or False)

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # on_delete必选参数

    # DateField/DateTimeField可通过default=xx选项设置默认日期和时间。
    # 如果希望自动记录一次修改日期(modified)，可以设置: auto_now = True
    # 如果希望自动记录创建日期(created),可以设置auto_now_add=True
    add_date = models.DateField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True)  # 对于DateTimeField: default=timezone.now - 先要from django.utils import timezone

    # 包括排序、索引等等(可选)。
    class Meta():
        # model里面Meta选项
        app_label = "packages.drf_pro"
        # app_label这个选项只在一种情况下使用，就是模型类不在默认的应用程序包下的models.py文件中，这时候需要指定这个模型类是那个应用程序的。
        pass

    # 定义单个模型实例对象的名字(可选)。给单个模型对象实例设置人为可读的名字
    def __str__(self):  # Django模型自带的标准方法
        return self.name

    # 重写save方法(可选)。
    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):  # Django模型自带的标准方法
        pass

    # 为单个模型实例对象生成独一无二的url(可选)
    def get_absolute_url(self):  # Django模型自带的标准方法
        # 为每篇文章生成独一无二的url
        return reverse("blog:article_detil", args=[str(self.id)])

    # 自定义方法：计数器
    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __dict__(self):
        return



#####
# 自定义manager方法
# class HighRatingManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(rating=1)
#
#
# # CHOICES选项
# class Rating(models.IntegerChoices):
#     VERYGOOD = 1, 'Very Good'
#     GOOD = 2, 'Good'
#     BAD = 3, 'Bad'
#
#
# class Product(models.Model):
#     # 数据表字段
#     name = models.CharField('product_name', max_length=30)
#     rating = models.IntegerField(choices=Rating.choices)
#     # MANAGERS方法
#     objects = models.Manager()
#     high_rating_products = HighRatingManager()
#
#     # META类选项
#     class Meta:
#         verbose_name = 'product'
#         verbose_name_plural = 'products'
#
#     # __str__ 方法
#     def __str__(self):
#         return self.name
#
#     # 重写save方法
#     def save(self, *args, **kwargs):
#         # ......
#         super().save(*args, **kwargs)
#         # ......
#
#     # 定义单个对象绝对路径
#     def get_absolute_url(self):
#         return reverse("product_details", kwargs={"pk": self.id})
#
#     # 其他自定义方法
#     def do_something(self):
#         pass





# from django_mysql.models import JSONField as OriginJSONField