<<<<<<< HEAD
from django.urls import path, include
=======
from django.contrib import admin
from django.urls import path
>>>>>>> d7ec2c25f06fb9af9bc4e744f0a9afd969b6e0db
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
