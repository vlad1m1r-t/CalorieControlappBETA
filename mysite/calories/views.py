from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from rest_framework import generics

from calories.forms import CreateUserForm, DataUser, AddFood
from .models import *
import datetime

from .serializers import CaloriesSerializer


class CaloriesAPIView(generics.ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = CaloriesSerializer

def index(requests):
    username = requests.user.username
    return render(requests, 'calories/index.html', {'title': 'Главная страница', 'username': username})

@login_required(login_url='login')
def resume(requests):
    return render(requests, 'calories/resume.html', {'title': 'Резюме'})

@login_required(login_url='login')
def calories2(requests, username):
    username = requests.user.username
    year, moth, day = datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day
    form = AddFood()
    if requests.method == 'POST':
        form = AddFood(requests.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.userid = requests.user.username
            visitor.save()
    allowance = UserProfile.objects.filter(userid=requests.user.username).values('allowance')[0]['allowance']
    get_info = Visitor.objects.filter(userid=requests.user.username, time_create=f'{year}-{moth}-{day}')
    get_info_all_caldj = Visitor.objects.filter(userid=requests.user.username, time_create=f'{year}-{moth}-{day}').aggregate(Sum('caldj'))['caldj__sum']

    return render(requests, 'calories/calories2.html', {'title': 'Учет калорий', 'username': username, 'form': form, 'allowance': allowance, 'get_info': get_info,
                                                        'get_info_all_caldj': get_info_all_caldj})


@login_required(login_url='login')
def calories(requests):
    form = DataUser()
    if requests.method == 'POST':
        form = DataUser(requests.POST)
        if form.is_valid():
            if UserProfile.objects.filter(userid=f'{requests.user.username}') is None:
                profile = form.save(commit=False)
                profile.userid = requests.user.username
                profile.save()
            else:
                UserProfile.objects.filter(userid=f'{requests.user.username}').delete()
                profile = form.save(commit=False)
                profile.userid = requests.user.username
                profile.save()
    try:
        allowance = UserProfile.objects.filter(userid=requests.user.username).values('allowance')[0]['allowance']
    except:
        allowance = 0
    username = requests.user.username
    return render(requests, 'calories/calories.html', {'title': 'Контроль калорий', 'form': form, 'username': username, 'allowance': allowance})


@login_required(login_url='login')
def telegram(requests):
    return render(requests, 'calories/telegram.html', {'title': 'Удобный телеграмм-бот'})

@login_required(login_url='login')
def contact(requests):
    return render(requests, 'calories/contact.html', {'title': 'Контакты'})

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Логин или пароль введены неправильно')
        context = {}
        return render(request,'calories/login.html',context)

def RegisterPage(request):
            form = CreateUserForm()
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, "Аккаунт создан " + user)
                    return redirect('login')

            context = {'form': form}
            return render(request,'calories/register.html', context)

def LogOutPage(request):
    logout(request)
    return redirect('login')