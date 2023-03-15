from django.urls import path
from .views import RegisterView, GetuserApiView
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('getuser/<userid>',GetuserApiView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]