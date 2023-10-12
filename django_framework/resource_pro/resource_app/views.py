from core.drf_resource.viewsets import ResourceViewSet, ResourceRoute
from resource_app.resources import NameGaneratorResource
from django.shortcuts import render


# Create your views here.

class NamesGeneratorViewSet(ResourceViewSet):
    resource_routes = [
        # ResourceRoute(method="GET", resource_class=NameGaneratorResource),
        # GET http://localhost/names_generator/
        # {
        #     "detail": "Resource[NameGanerator] 请求参数格式错误：(姓) This field is required."
        # }
        # GET http://localhost/names_generator/?first_name=zhou&last_name=ruifu
        # {
        #     "full_name": "zhou ruifu"
        # }


        ResourceRoute(method="GET", resource_class=NameGaneratorResource, endpoint="name_ganerators"),
        # GET http://localhost/names_generator/name_ganerators/?first_name=zhou&last_name=ruifu



        ResourceRoute(method="POST", resource_class=NameGaneratorResource)
        # POST http://localhost/names_generator/
        # Body {"first_name":"zhou","last_name":"ruifu"}
        # {
        #     "full_name": "zhou ruifu"
        # }
    ]




from rest_framework import generics
from resource_app.models import Person
from resource_app.serializers import PersonSerializer

class PersonCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    # 这里的 `serializer_class` 指定了使用 `PersonSerializer` 进行序列化和反序列化
    serializer_class = PersonSerializer

class PersonList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

