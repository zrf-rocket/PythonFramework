"""resource_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from core.drf_resource import routers
from django.conf.urls import url, include
from django.contrib import admin
from resource_app import views

router = routers.ResourceRouter()
router.register_module(views)  # OK
# router.register_module(r"", views.NamesGeneratorViewSet, base_name="name_ganerators")
# router.register_module(r"", views)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include(router.urls)),

    # 此接口添加了event
    url(r"^event/", include(router.urls)),
    # http://localhost/event/names_generator/name_ganerators/?first_name=zhou&last_name=ruifu


]
