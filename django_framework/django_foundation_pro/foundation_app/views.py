from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

def request_obj(request):
    return HttpResponse(f"请求路径：{request.path}")


def request_obj02(request):
    print(request.is_secure())  # False
    print(request.get_port())  # 80
    print(request.get_host())  # localhost
    print(request.get_full_path())  # /foundation/index02/

    infos = {
        'request.path': request.path,
        "method": request.method,
        "get": request.GET,
        "post": request.POST,
        "post_name": request.POST.get('name', default=None),
        "get_name": request.GET.getlist('name', default=None),
        "meta": request.META,
        "user": request.user,
        "is_superuser": request.user.is_superuser
    }
    return HttpResponse(str(infos))

def request_meta(req):
    """
    此处也可以协程req等任何标识符（效果如同上面代码示例中的request）
    """
    cnts = [f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in req.META.items()]
    return HttpResponse(f'<table>{"".join(cnts)}</table>')


def register(request):
    if request.method == "POST":
        #TODO 这里为了演示 直接获取用户名密码和邮箱，不做校验，后面将介绍使用序列化的方式来做参数校验
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        #TODO 处理用户注册逻辑 省略
        send_mail('欢迎关注公众号：CTO Plus', 'rocket_2014@126.com', [email])
        return render(request, 'registration/success.html')
    return render(request, 'registration/register.html')

def show_information(request):
    context = {
        'user': request.user,
        'user_agent': request.META.get('HTTP_USER_AGENT', 'Unknown'),
        'ip': request.META.get('REMOTE_ADDR', "")
    }
    return render(request, 'index.html', context=context)

def show_information02(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR', "*")  # 这里获得代理ip
    context = {
        'user': request.user.username,
        'is_superuser': request.user.is_superuser,
        'user_agent': request.META.get('HTTP_USER_AGENT', 'Unknown'),
        'ip': ip
    }
    return render(request, 'index.html', context=context)







































