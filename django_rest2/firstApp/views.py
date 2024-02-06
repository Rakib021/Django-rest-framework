from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def homeData(request):
   if request.method =='POST':
       data1 = request.data['data1']
       data2 = request.data['data2']
      
   context ={
       'name':'Rakibul Islam',
       'university':'Port city international University'
   }
  
   return Response(context)






from django.contrib.auth.models import User

@api_view(['POST'])
def registrationApi(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

       

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"})

        if password1 != password2:
            return Response({"error": "Passwords didn't match"})

        user = User()
        user.username=username,
        user.email=email,
        user.first_name=first_name,
        user.last_name=last_name,
        user.is_active = True
        user.set_password(raw_password=password1)
        user.save()

        

        return Response({"success": "Successfully registered"})
    
    return Response({"error": "Invalid request method"})
