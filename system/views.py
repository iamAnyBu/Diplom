from django.shortcuts import render, redirect
from system.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login as dj_login, logout as log

def base(request):
    return render(request, 'system/base.html')

def base_login(request):
    return render(request, 'system/base_login.html')

def whoau(request):
    return render(request, 'system/whoau.html')

def empl(request):
    return render(request,'system/empl.html')

def shef(request):
    return render(request,'system/shef.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            dj_login(request, user)
            return redirect('whoau')
    else:
        form = UserLoginForm()
    return render(request, 'system/login.html', {"form": form})

def logout(request):
    log(request)
    return redirect('base')

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'system/registration.html', {"form": form})
