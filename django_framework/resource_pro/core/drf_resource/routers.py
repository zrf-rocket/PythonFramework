import six
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet

from core.drf_resource.tools import get_underscore_viewset_name
from core.drf_resource.viewsets import ResourceViewSet


class ResourceRouter(DefaultRouter):
    @staticmethod
    def _init_resource_viewset(viewset):
        """
        初始化ResourceViewset，动态增加方法，在register router前必须进行调用
        @:param viewset: ResourceViewset类
        """
        if isinstance(viewset, type) and issubclass(viewset, ResourceViewSet):
            viewset.generate_endpoint()

    def register(self, prefix, viewset, base_name=None):
        """
        注册单个ResourceViewset
        """
        self._init_resource_viewset(viewset)
        super(ResourceRouter, self).register(prefix, viewset, base_name)

    def register_module(self, viewset_module):
        """
        注册整个ResourceViewset模块，并根据类的命名规则自动生成对应的url
        """
        for attr, viewset in six.iteritems(viewset_module.__dict__):
            # 全小写的属性不是类，忽略
            if attr.startswith("_") or attr[0].islower():
                continue

            if isinstance(viewset, type) and issubclass(viewset, GenericViewSet):
                prefix = self.get_default_base_name(viewset)
                self.register(prefix, viewset)

    def get_default_base_name(self, viewset):
        return get_underscore_viewset_name(viewset)
