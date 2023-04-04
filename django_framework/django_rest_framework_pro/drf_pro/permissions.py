from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限:只允许对象的创建者才能编辑它。
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限被允许用于任何请求
        if request.method in permissions.SAFE_METHODS:
            # 所以始终允许 GET，HEAD 或 OPTIONS 请求。
            return True
        # 写入权限只允许给 article 的作者。
        return obj.author == request.user




def authentication_classes(permission_classes):
    pass


def permission_classes(permission_classes):
    pass


def permission_groups(group_names):
    """
    组权限装饰器
    :param group_names:
    :return:
    """
    pass






