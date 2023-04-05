# 限流
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class ArticleListAnonRateThrottle(AnonRateThrottle):
    """
    视图类或视图集中使用限流类
    """
    THROTTLE_RATES = {'anon': '5/min'}

class ArticleListUserRateThrottle(UserRateThrottle):
    THROTTLE_RATES = {'user': '30/min'}


# 有时对一个认证用户进行限流不仅要限制每分钟的请求次数，还需要限制每小时的请求次数
# 可以自定义两个UserRateThrottle子类，并设置不同的scope
class MinuteUserRateThrottle(UserRateThrottle):
    scope = 'limit_per_minute'
    # THROTTLE_RATES = {'anon': '5/min'}  # 也可以settings中设置

class HourUserRateThrottle(UserRateThrottle):
    scope = 'limit_per_hour'
    # THROTTLE_RATES = {'user': '30/min'}  # 也可以settings中设置
















