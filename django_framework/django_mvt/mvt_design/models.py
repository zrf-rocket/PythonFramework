from django.db import models


# Create your models here.


class Status(models.TextChoices):
    UNSTARTED = "u", "Not started yet"
    ONGOING = "o", "Ongoing"
    FINISHED = "f", "Finished"


class Task(models.Model):
    """
    Task模型
    """

    name = models.CharField(verbose_name="Task Name", max_length=65, unique=True)
    status = models.CharField(
        verbose_name="Task Status", max_length=1, choices=Status.choices
    )

    def __str__(self):
        return self.name

    class Meta:
        # 自定义表名
        db_table = "tasks_task"


class Article(models.Model):
    """文章模型"""
    # 通过db_column自定义数据表中字段名
    title = models.CharField('标题', max_length=200, db_column='article_title')
    article_slug = models.SlugField('slug', max_length=60, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'  # 通过db_table自定义数据表名
