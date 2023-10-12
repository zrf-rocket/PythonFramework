from django.db import models

# Create your models here.

class MyModel(models.Model):
    author = models.CharField(null=False, max_length=22)
    blog = models.URLField()
    create_datetime = models.DateTimeField()

class DocsModel(models.Model):
    document_path = models.CharField(null=False, max_length=200)
    content = models.TextField(null=True)
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.document_path


class DocsModel2(models.Model):
    path = models.CharField(null=False, max_length=200)
    content = models.TextField(null=True)
    product_name = models.CharField(max_length=100)
    document_name = models.CharField(max_length=100)

    def __str__(self):
        return self.path



