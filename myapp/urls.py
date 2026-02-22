"""
URL configuration for myapp project.

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

from django.urls import path, include
from main.views import patient_list, add_patient, update_patient, delete_patient, user_login, user_logout, register
urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',include('main.urls')),
    #path("",patient_list,name='patient_list'),
    path("",user_login,name='home'),
    path('login/', user_login, name='login'),
    path('register/',register,name='register'),
    path('logout/',user_logout,name='logout'),
    path('patients/',patient_list,name='patient_list'),
    path('add/',add_patient,name='add_patient'),
    path('update/<int:pk>/',update_patient,name='update_patient'),
    path('delete/<int:pk>/',delete_patient,name='delete_patient'),
    path('api/',include('main.api_urls')),
]
