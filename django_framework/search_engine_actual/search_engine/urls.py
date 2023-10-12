from django.urls import path

from . import views

app_name = "search"

urlpatterns = [
    path("jieba/", views.my_jieba_view, name='jieba'),
    path("haystack/", views.my_haystack_view, name='haystack'),
]