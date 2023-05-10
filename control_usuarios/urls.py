"""
URL configuration for proyecto_blog project.

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


from control_usuarios.views import listar_escritores , listar_lectores , listar_articulos, crear_lector

urlpatterns = [
    path('lectores/', listar_lectores, name= "listar_lectores"),
    path('escritores/', listar_escritores, name= "listar_escritores"),
    path('articulos/', listar_articulos, name= "listar_articulos"),
    path('crear-lector/', crear_lector, name= "crear_lector")
]