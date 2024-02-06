from django.shortcuts import render
from .models import Shoplist
from django.http import JsonResponse

# Create your views here.
def shoplist(request):
  shop = Shoplist.objects.all()
  
  data ={
    'shop':list(shop.values())
  }
  return JsonResponse(data)

def shoplist_detail(request,pk):
  shops = Shoplist.objects.get(pk=pk)
  
  data ={
    'name':shops.name,
    'description':shops.description,
    'active':shops.active
  }
  
  return JsonResponse(data)