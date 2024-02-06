from django.urls import path
from .views import *

urlpatterns = [
    path('',homeData),
    path('api/reg/',registrationApi)
]
