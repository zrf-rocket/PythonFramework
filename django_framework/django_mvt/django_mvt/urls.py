from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mvt_design/', include('mvt_design.urls')),
    path("tpl/", include("django_templates.urls")),
    path('cookie_book/', include('django_orm_senior.urls')),
    path('users/', include('users.urls')),
]
