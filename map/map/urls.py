"""
URL configuration for map project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mapapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.p1),
    path('new/',views.p2,name='manali'),
    path('file/',views.p3,name='park'),
    path('new1/',views.p4,name='oil'),
    path('file1/',views.p5,name='petrol'),
    path('new2/',views.p6,name='lake'),
    ]
