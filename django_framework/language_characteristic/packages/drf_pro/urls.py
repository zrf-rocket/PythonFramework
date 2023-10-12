from django.urls import path
from . import views

app_name = "drf_pro_namespace"

urlpatterns = [
    # http://{HOSTNAME}/drf_pro/index/
    path('index/', views.index, name="主页"),
    path('req_celery/', views.req_celery, name="celery")

]
