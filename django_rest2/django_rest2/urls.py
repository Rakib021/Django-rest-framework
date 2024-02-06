
from django.contrib import admin
from django.urls import path,include

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('firstApp.urls')),
    path('api/login/',obtain_auth_token),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
]
