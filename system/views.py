from django.forms import ModelForm, forms
from django.shortcuts import render, redirect
from system.forms import UserRegisterForm, UserLoginForm, ClientForm, CheckForm
from django.contrib.auth import login as dj_login, logout as log

from system.models import Question, Program, FormVarAnswer


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

def anketa(request):
    form = ClientForm()
    if request.method == 'POST':
        print(request.POST)
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'system/anketa.html', context)

def anketa_ch(request):
    form1 = CheckForm()
    if request.method == 'POST':
        print(request.POST)
        form1 = CheckForm(request.POST)
        if form1.is_valid():
            form1.save()
    context = {'form1': form1}
    return render(request, 'system/anketa.html', context)



def test(request):
    return render(request, 'system/test.html')


def plan(request):
    article = Program.objects.all()
    context = {
        'articles': article
    }

    return render(request, 'system/plan.html', context)
