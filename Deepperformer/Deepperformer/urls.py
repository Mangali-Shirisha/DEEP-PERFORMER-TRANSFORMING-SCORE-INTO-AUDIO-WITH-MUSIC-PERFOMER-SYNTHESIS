"""Deepperformer URL Configuration

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
from Deepperformer import views as mainview
from Admins import views as admins
from Users import views as usr


urlpatterns=[

    path("admin/",admin.site.urls),
    path("", mainview.index, name="index"),
    path("index/",mainview.index,name="index"),
    path("AdminLogin/",mainview.AdminLogin,name="AdminLogin"),
    path("UserLogin/",mainview.UserLogin,name="UserLogin"),
    path("UserRegister/",mainview.UserRegister,name="UserRegister"),

    path("AdminHome/",admins.AdminHome,name="AdminHome"),
    path("AdminLoginCheck/",admins.AdminLoginCheck,name="AdminLoginCheck"),
    path("RegisterUsersView/",admins.RegisterUsersView,name="RegisterUsersView"),
    path("ActivaUsers/",admins.ActivaUsers,name="ActivaUsers"),


    path("UserRegisterActions/",usr.UserRegisterActions,name="UserRegisterActions"),
    path("UserLoginCheck/",usr.UserLoginCheck,name="UserLoginCheck"),
    path("UserHome/",usr.UserHome,name="UserHome"),
    path("viewData/",usr.viewData,name="viewData"),
    path("violin_audio/",usr.violin_audio,name="violin_audio"),
    path("piano_audio/",usr.piano_audio,name="piano_audio"),
    path("violin_cll/",usr.violin_cll,name="violin_cll"),
    path("piano_rfcll/",usr.piano_rfcll,name="piano_rfcll")

]
