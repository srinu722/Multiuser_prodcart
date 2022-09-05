"""Multiuser_prodcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
#from django.urls import path
#from users import views as user_views
from To_Do_list import views as tdl
from user_auth import views as ua

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', ua.home),
    path('products/',tdl.additemview),
    path('display/', tdl.displayitemview),
    #path('home/', ua.home),
    #path('login/',ua.login, name='login'),
    #path('logout/',ua.logout, name='logout'),
    path('register/', ua.register),
    path('login/', ua.login),
    path('logout/', ua.logout),
]
