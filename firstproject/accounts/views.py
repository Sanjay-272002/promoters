from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.warning(request, 'you are logged in')
            return redirect('dashboard') 
        else:
            messages.warning(request,'invalid user')
            return redirect('login') 
    
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                   messages.warning(request,'email already exists')
                   return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname,username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    print("user saved")
                    return  redirect('login')
                    
        else:
            messages.warning(request,'Password do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')