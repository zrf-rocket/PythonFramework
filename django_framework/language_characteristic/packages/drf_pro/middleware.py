# 自定义的中间件
import time
from django.shortcuts import redirect
from django.conf import settings


# 使用函数编写中间件
def calc_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        end_time = time.time()
        print(f"请求执行时间：{end_time - start_time}秒")
        return response

    return middleware


# 使用类编写中间件
class SimpleMiddleware:
    def __init__(self, get_response):
        # 一次性设置和初始化
        self.get_response = get_response

    def __call__(self, request):
        print("视图函数执行前的代码")
        response = self.get_response(request)
        print("视图函数执行后的代码")
        return response


# 编写一个名为LoginRequiredMiddleware的中间件，实现全站要求登录，但是登录页面和开放白名单上的urls除外
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        # 开放白名单，比如['/login/', '/admin/']
        self.open_urls = [self.login_url] + getattr(settings, 'OPEN_URLS', [])

    def __call__(self, request):
        '''
        print("校验用户")
        # request.path_info用于获取当前请求的相对路径，如/articles/
        # request.get_full_path()用于获取当前请求完整的相对路径，包括请求参数，如/articles/?page=2。使用request.get_full_path()时需要括号，否则返回的是uwsgi请求对象，不是字符串。
        if not request.user.is_authenticated and request.path_info not in self.open_urls:
            print("校验用户失败.....")
            return redirect(self.login_url + '?next=' + request.get_full_path())
        '''
        response = self.get_response(request)
        print("视图函数执行后..........")
        return response
