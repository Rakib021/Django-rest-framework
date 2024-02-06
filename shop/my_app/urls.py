from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.shoplist,name='shoplist'),
    path('list/<int:pk>/',views.shoplist_detail,name='shoplist_detail'),
]
