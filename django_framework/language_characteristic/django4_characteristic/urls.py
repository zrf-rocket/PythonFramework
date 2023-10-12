from django.urls import path
from . import views

namespace = "django4_characteristic"

urlpatterns = [
    path('', views.index, name="主页"),
    # http://{HOSTNAME}/index/
    path('index/', views.index, name="d4主页"),
]
