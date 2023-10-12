# 自定义的全局上下文管理器
from django.conf import settings


# 自定义的全局上下文处理器本质上是个函数，使用它必须满足3个条件：
# 传入参数必须有request对象
# 返回值必须是个字典
# 使用前需要在settings的context_processors里申明。
def global_site_name(request) -> dict:
    return {
        "site_name": settings.SITE_NAME,
    }
