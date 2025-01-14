"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from projectapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/',admin.site.urls),
    path('sandhiya',views.sandhiya,name="sandhiya"),
    path('form',views.form,name="form"),
    path('updateData/<int:id>',views.updateData,name="updateData"),
    path('deleteData/<int:id>',views.deleteData,name="deleteData"),
    path('register',views.register,name='register'),
    path('',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name="logout.html"),name="logout"),
    path('home',views.home,name="home"),
   

]

urlpatterns += staticfiles_urlpatterns()
