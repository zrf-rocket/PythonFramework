from django.db import models
from mptt.models import TreeForeignKey, TreeOneToOneField, TreeManyToManyField, TreeManager, MPTTOptions, MPTTModelBase, MPTTModel
# Create your models here.

class pdf_list(models.Model):
    is_pdf = models.JSONField(null=True, verbose_name='是否是PDF文件')

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Categoryv2(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
