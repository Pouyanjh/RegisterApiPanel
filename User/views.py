from .models import user
from rest_framework import generics

from .serializer import RegisterSerializer




class RegisterView(generics.CreateAPIView):

    queryset = user.objects.all()
    serializer_class = RegisterSerializer








