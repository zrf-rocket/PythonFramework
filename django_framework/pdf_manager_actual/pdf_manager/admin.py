from django.contrib import admin

from .models import Category
# Register your models here.

from mptt.admin import MPTTModelAdmin
admin.site.register(Category, MPTTModelAdmin)