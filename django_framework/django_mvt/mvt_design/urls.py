from django.urls import path
from . import views

# namespace
app_name = "tasks"

urlpatterns = [
    path('', views.task_list, name='task_list'),
]






#     ^show_tasks/$