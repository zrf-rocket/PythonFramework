from django.http import HttpResponse,JsonResponse
# from django.shortcuts import render_to_response


#表单
def search_form(request):
    return render_to_response("search_form.html")

# http://127.0.0.1:8000/search_form?q=提交数据1
#接收请求数据
def search(request):
    req_method = request.method
    request.encoding = "utf-8"
    if 'q' in request.GET:
        message = "你搜索的内容为：" + request.GET['q']
    else:
        message = "已提交空表单"
    return HttpResponse(message)




from django.shortcuts import render
from django.views.decorators import csrf
# 接收POST请求数据
def search_post(request):
    req_method = request.method
    ctx = {}
    if request.POST:
        ctx["rlt"] = request.POST["q"]
    return render(request, "post.html", ctx)





