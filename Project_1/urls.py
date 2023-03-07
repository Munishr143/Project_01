"""Project_1 URL Configuration

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
from app1.views import *
from app2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Sample_1/', Sample_1, name='Sample_1'),
    path('Second_Sample/', Second_Sample, name='Second_Sample'),
    path('Cmd_1/', Cmd_1, name='Cmd_1'),
    path('first_cmd/', first_cmd, name='first_cmd'),
    path('Cmd_2/', Cmd_2, name='Cmd_2'),
    path('Second_cmd/', Second_cmd, name='Second_cmd'),
    
]
