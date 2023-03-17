
from rest_framework.response import Response

from .models import user, Product
from rest_framework import generics, status

from .serializer import RegisterSerializer, ProductSerializer

from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username,
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):

    queryset = user.objects.all()
    serializer_class = RegisterSerializer



class GetListProduct(APIView):

    def get(self, request):
        products =  Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
















