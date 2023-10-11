from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login")
def index(request):
    return HttpResponse("login required login url")


@login_required(redirect_field_name="self_redirect_field_name")
def index2(request):
    return HttpResponse("login required redirect field name")
