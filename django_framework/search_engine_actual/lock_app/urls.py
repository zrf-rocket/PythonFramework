from django.urls import path
from . import views
app_name = "lock"

urlpatterns = [
    path("search", views.update_table, name="search")
]