from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

@api_view(['GET','POST'])

def registrationApi(request):
    if request.method =='POST':
       username = request.data['username']
       email = request.data['email']
       first_name = request.data['first_name']
       last_name = request.data['last_name']
       password1 = request.data['password1']
       password2 = request.data['password2']
       
       if User.objects.filter(username=username).exists():
           return Response({"error":"Username already exists"})
       
       if password1 !=password2:
           return Response({"error":"password didn't matched"})
       
       user= User()
       user.username = username
       user.first_name = first_name
       user.last_name = last_name
       user.email = email
       user.is_active = True
       user.set_password(raw_password=password1)
       user.save()
       
       return Response({"success":"successfully registered"})