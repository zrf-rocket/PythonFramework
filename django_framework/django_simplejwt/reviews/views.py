from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    def perform_destroy(self, instance):
        print(instance)


class ImageViewSet(viewsets.ModelViewSet):
    def perform_destroy(self, instance):
        print(instance)



from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = MyTokenObtainPairSerializer

















