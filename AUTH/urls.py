"""
URL configuration for AUTH project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
=======
<<<<<<< HEAD
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
=======
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls'))
>>>>>>> 816ef7971f7a2ad995b7fd1ec57b15db2578f797
>>>>>>> d7ec2c25f06fb9af9bc4e744f0a9afd969b6e0db
]
