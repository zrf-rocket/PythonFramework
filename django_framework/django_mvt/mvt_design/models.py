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