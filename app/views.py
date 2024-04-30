from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

from .models import Register


from django.contrib import messages
from django.contrib.auth.models import User,auth

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')
        print(username+":"+pass1+":"+pass2)
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return redirect('login')  # Redirect to the login page
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('index')  # Redirect to the index page
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('registration')  # Redirect to the registration page
    else:
        return render(request, 'registration.html')  # Render the registration form for GET requests
def login(request):
    return render(request, 'login.html')
from django.shortcuts import render, redirect
def login1(request):
    if request.method== 'POST':
        username = request.POST['username']
        pass1=request.POST['password']

        user= auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username)==1:
                return redirect('index')
            else:
                return redirect('login')
        else:
            messages.info(request,'Invalid Credentials')
    else:
        return render(request,'login.html')



def index(request):
    return render(request,"index.html")

def categories(request):
    return render(request,"categories.html")

def contact(request):
    return render(request,"contact.html")

def merlin(request):
    return render(request,"merlin.html")

def products(request):
    return render(request,"products.html")

def logout(request):
    return redirect('merlin')




