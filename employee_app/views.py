from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

# Create your views here.

def login(request):
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        UserModel = get_user_model
        print(UserModel)
        username=UserModel.objects.get(email=lower(email)).username
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            
            # A backend authenticated the credentials
            return render(request,'view_employee.html')
        else:
            # No backend authenticated the credentials
            context={'message':'email or password incorrect'}
            return render(request,'login.html',context)
    else:
         return render(request,'login.html')
        