import datetime
# from django.conf import settings
# settings.mongoengine_conn
from language_characteristic.settings import mongoengine_conn
# MySQL的ORM
# from django.db import models
# models.Model
# models.CharField

# MongoDB的ORM
from mongoengine import Document, fields


# Document
# fields.StringField
# 当使用 MongoEngine 时，模型被文档和字段替换。

# Create your models here.
class Review(fields.EmbeddedDocument):
    name = fields.StringField(max_length=30, required=True, verbose_name="名称")
    image = fields.ImageField()
    time = fields.DateTimeField(default=datetime.datetime.now(), required=True)
    other = fields.StringField(max_length=225, required=True)


# 自动在数据库中创建集合：user_info
class UserInfo(Document):
    name = fields.StringField(max_length=30)
    age = fields.IntField(default=0)
    addr = fields.StringField(max_length=30, null=True)
    sex = fields.BooleanField(null=False)  # 不允许为空
    time = fields.DateTimeField(default=datetime.datetime.now(), required=True)
    review = fields.ListField(fields.EmbeddedDocumentField(Review))

# models中不会像使用MySQL那样,有智能补全
# models不需要数据库迁移
# models的增删改查和mysql的ORM一样,都是使用同样的ORM,只是数据库不同


# 模型类属性命名限制
# 1）不能是python的保留关键字。
# 2）不允许使用连续的下划线，这是由django的查询方式决定的。例如：b__title = models.CharField(max_length=20)就不行
# 3）定义属性时需要指定字段类型，通过字段类型的参数指定选项


# 字段类型
# AutoField	自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性。
# BooleanField	#布尔类型 布尔字段，值为True或False。
# NullBooleanField	支持Null、True、False三种值。
# CharField(max_length=最大长度)	字符串。 # 参数max_length表示最大字符个数。
# TextField	大文本字段，一般超过4000个字符时使用。
# IntField(min_value=None,max_value=None) #整数类型
# DecimalField(max_digits=None, decimal_places=None)	十进制浮点数。
    # 参数max_digits表示总位。
    # 参数decimal_places表示小数位数。
    # 常用于商品价格（精确度高）。
# FloatField(min_value=None,max_value=None) # 浮点类型 浮点数。参数同上（精确度比上一个低）
# DateField：([auto_now=False, auto_now_add=False])	日期。
    # 1)参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false。
    # 2) 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false。
    # 3)参数auto_now_add和auto_now是相互排斥的，组合将会发生错误。
# TimeField	时间，参数同DateField。
# DateTimeField	#时间类型 日期时间，参数同DateField。
# DictField() #字典类型
# FileField	上传文件字段。
# ImageField	# 图像文件存储字段 继承于FileField，对上传的内容进行校验，确保是有效的图片。

# EmailField()  # 邮箱地址字段
# ListField，#嵌套文档，这个列表中的每一个元素都是一个字典 可以插入列表的
# ReferenceField() #参照类型 这是一个保存相关文档的filed
# StringFiled(regex=None,max_length=None,min_lenght=None) # 字符串类型
# SequenceField() #自动产生一个数列、 递增的



# 字段选项（字段参数），模型中设置数据库字段默认值，字段限制：
# (1)null 赋值是否可以为空
# 如果为True，Django将用NULL来在数据库中存储空值（允许为空）。默认值是False.

# (2)default 默认值 也可以是一个函数 可调用类型
# 字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用。

# (3)primary_key 插入数据是否重复
# 如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
# Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，默认值是False，一般作为AutoField的选项使用。
# 否则没必要设置任何一个字段的primary_key=True。

# (4)unique 当前field只能是唯一的
# 如果该值设置为True, 这个数据字段的值在整张表中必须是唯一的，默认值是False。

# (5)choices 列表的范围
# 由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，而且这个选择框的选项就是choices中的选项。

# (6)blank
# 如果为True，该字段允许不填（允许为空白）。默认为False。
# 要注意，这与null不同。null纯粹是数据库范畴的，而blank是数据验证范畴的（后台管理页面表单验证）。（一般是后台管理处输入是否可为空格等）
# 如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。

# (7)max_length，# 最大长度

# (8)required
# 是否必须填写（默认值：False），如果设置为True且未在文档实例上设置字段，则在ValidationError验证文档时将引发

# (9)db_index	若值为True, 则在表中会为此字段创建索引（相当于目录），默认值是False。

# (10)db_column	字段的名称，如果未指定，则使用属性的名称。

# (11)verbose_name

# 当修改模型类之后，如果添加的选项不影响表的结构，则不需要重新做迁移，商品的选项中default和blank不影响表结构。






