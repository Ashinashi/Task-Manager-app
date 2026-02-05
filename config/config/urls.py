from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect


def splash_page(request):
    return render(request, "splash.html")


def home_page(request):
    return render(request, "home.html")


def redirect_login(request):
    return redirect('login') 


def redirect_register(request):
    return redirect('register')  



urlpatterns = [
    
    path('admin/', admin.site.urls),

   
    path('accounts/', include('accounts.urls')),  

   
    path('api/tasks/', include('tasks.urls')),


    path('', splash_page, name='splash'),
    path('home/', home_page, name='home_page'),

   
    path('login/', redirect_login, name='login_page'),
    path('register/', redirect_register, name='register_page'),
]
