import datetime
import time
from django.conf import settings
from django.db import connections, models
from django.db.models import signals
from custom_app.utils.user import get_global_user

class AutoConnManagerMixin(object):
    def __init__(self, *args, **kwargs):
        super(AutoConnManagerMixin, self).__init__(*args, **kwargs)

    def get_querysets(self):
        return super(AutoConnManagerMixin, self).get_querysets()


class IgnoreBlurInsertMinxin(object):
    @classmethod
    def _compiler_as_sql_hacker(cls, compiler):
        def as_sql(*args, **kwargs):
            return []

        raw_as_sql = compiler.as_sql
        compiler.as_sql = as_sql
        return as_sql


class ModelManager(
    AutoConnManagerMixin,
    IgnoreBlurInsertMinxin,
    models.Manager
):
    pass


class Model(models.Model):
    object = ModelManager()

    class Meta:
        abstract = True


class RecordModelManager(ModelManager):
    def get_querysets(self):
        return super(RecordModelManager, self).get_querysets().filter(is_deleted=False)

    def create(self, *args, **kwargs):
        kwargs.update({"create_user": get_global_user() or "unkonw"})
        return super().create(*args, **kwargs)


class AbstractRecordModel(models.Model):
    is_enabled = models.BooleanField("是否启用", default=True, blank=True)
    is_deleted = models.BooleanField()
    create_user = models.CharField()
    create_time = models.DateTimeField()
    update_user = models.CharField()
    update_time = models.DateTimeField()


    def delete(self, using=None, keep_parents=False):
        signals.pre_delete.send()
        signals.pre_save.send()
        signals.pre_migrate.send()
        signals.pre_init.send()

        signals.post_delete.send()
        signals.post_save.send()
        signals.post_migrate.send()
        signals.post_init.send()

        signals.class_prepared.send()
        signals.m2m_changed.send()
















