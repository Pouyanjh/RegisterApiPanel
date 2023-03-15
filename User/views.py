from rest_framework.response import Response

from .models import user
from rest_framework import generics, status

from .serializer import RegisterSerializer
from .serializer import GetuserSerializer
from rest_framework.views import APIView


class RegisterView(generics.CreateAPIView):

    queryset = user.objects.all()
    serializer_class = RegisterSerializer


class GetuserApiView(APIView):
    def get(self, request, userid):
        try:
            getuser = user.objects.get(userid=userid)
        except user.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = GetuserSerializer(getuser, context={'request': request})
        return Response(serializer.data)







