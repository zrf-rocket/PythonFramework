from django.db import models

# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"

class Task(models.Model):
    """
    Task模型
    """
    name = models.CharField(verbose_name="Task Name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task Status", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name

    class Meta:
        # 自定义表名
        db_table = "tasks_task"


class Article01(models.Model):
    """文章模型"""
    # 通过db_column自定义数据表中字段名
    title = models.CharField('标题', max_length=200, db_column='article_title')
    article_slug = models.SlugField('slug', max_length=60, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'  # 通过db_table自定义数据表名


from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.shortcuts import redirect

User = get_user_model()

class Article(models.Model):
    STATUS_CHOICES = (('p', _('Published')), ('d', _("Draft")), )
    title = models.CharField(max_length=100, db_index=True, verbose_name=_("标题"))
    body = models.TextField(blank=True, verbose_name=_('内容'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name=_('作者'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='s', null=True, blank=True, verbose_name=_('状态'))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('发布时间'))
    update_date = models.DateTimeField(auto_now=True, verbose_name=_('更新时间'))
    create_date = models.DateTimeField(default=timezone.now, verbose_name=_('创建时间'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        db_table = 'articles'

    def get_absolute_url(self):
        # url = reverse('mvt_design:CustomIndexView') # 不能使用APP的name
        # url = reverse('index_c_v2:CustomIndexView') # :前面 不能使用path中定义的name
        url = reverse('tasks:index_c_v21')  # 正确的做法   : 的前面为urls中定义的app_name  : 的后面为urls path中定义的name
        return url   # 直接重定向到文章列表清单中  即：/mvt_design/blog_c_v2/
        # return redirect(url)  # 会造成这个错 TypeError: quote_from_bytes() expected bytes













