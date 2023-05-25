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


from AppBlog.views import ArticuloListView, ArticuloCreateView,\
    ArticuloDetailView, ArticuloUpdateView , ArticuloDeleteView 

urlpatterns = [
    #URL de Articulos
    path("articulos/",ArticuloListView.as_view(),name="listar_articulos"),
    path("crear-articulo/",ArticuloCreateView.as_view(),name="crear_articulo"),
    path("Articulos/<int:pk>/",ArticuloDetailView.as_view(),name="ver_articulo"),
    path("editar-articulo/<int:pk>/",ArticuloUpdateView.as_view(),name="editar_articulo"),
    path("eliminar-articulo/<int:pk>/",ArticuloDeleteView.as_view(),name="eliminar_articulo")
]
