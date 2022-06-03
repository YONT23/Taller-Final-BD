"""librostll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from apps.libro.views import home
from apps.ejemplares.views import consultas

urlpatterns = [
    path('/', home, name='home'),
    path('/', consultas, name='home'),
    path('admin/', admin.site.urls),
    path('libro/', include('apps.libro.urls', namespace='libro')),
    path('autor/', include('apps.libro.urls', namespace='autor')),
    path('ejemplar/', include('apps.ejemplares.urls', namespace='ejemplar')),
    path('prestar/', include('apps.ejemplares.urls', namespace='prestar')),
     
]