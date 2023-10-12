import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)

ResourceCache = set()
ResourceCount = {}

class ResourceDataManager(models.Manager):
    @staticmethod
    def get_data_string(data):
        """
        数据转换为字符串，同时避免QuerySet查询
        """
        pass

    def request(self,resource, *args, **kwargs):
        """
        请求并记录数据
        :type resource: Resource
        :type args: list
        :type kwargs: dict
        :return: Resource response
        """
        # 如果没有配置则退出
        pass


class ResourceData(models.Model):
    """
    Resource请求数据
    """
    name = models.CharField(_("名称"), max_length=128, db_index=True)
    start_time = models.DateTimeField(_("开始时间"))
    end_time = models.DateTimeField(_("结束事件"))
    request_data = models.TextField(_("请求参数"))
    response_data = models.TextField(_("响应参数"))

    objects = ResourceDataManager()

    class Meta:
        db_table = "resource_data"