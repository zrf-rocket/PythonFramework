from django.urls import path
from . import views

app_name = "drf_pro"

urlpatterns = [
    # http://{HOSTNAME}/mongo_pro/index/
    path('index/', views.index, name="主页"),
    path('create_user/', views.user_info, name="创建人员")
]
