from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate 

from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def register(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
              messages.info(request,'username is already exist')
              return redirect('/')
            else: 
                user = User.objects.create(username=username, email=email,first_name = first_name,last_name=last_name,password=password)
                user.set_password(password)
                user.save()
                
                return redirect('auth/')
    else:
    
     return render(request, 'main/register.html')







def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate (username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('auth/')
        
    else:
        return render(request,'main/auth.html')
   