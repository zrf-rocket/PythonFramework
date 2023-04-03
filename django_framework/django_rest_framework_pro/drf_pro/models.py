import datetime
from django.db import models
# from django.utils.translation import ugettext as _
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model


class SerializerDemo(models.Model):
    name = models.CharField(max_length=128, null=False)
    age = models.IntegerField(default=0, null=False)
    hobby = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)  # TextField可以不设置max_length
    datatime = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "people"  # 指定生产的表名


# 用户模型 此处直接使用了Django自带的用户模型
User = get_user_model()


class Article(models.Model):
    """
    存储文章数据

    """
    STATUS_CHOICES = (('p', _('Published')), ('d', _('Draft')),)
    title = models.CharField(verbose_name=_('Title (*)'), max_length=90, db_index=True)
    body = models.TextField(verbose_name=_('Body'), blank=True)
    # 用户(User)与文章(Article)是单对多的关系(ForeinKey)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(verbose_name=_('Status (*)'), max_length=1, choices=STATUS_CHOICES, default='s', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        verbose_name = "Article"
        verbose_name_plural = 'Articles'
        db_table = "articles"




class Profile(models.Model):
    pass
