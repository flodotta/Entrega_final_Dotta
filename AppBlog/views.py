from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from AppBlog.models import  Articulo

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# #vistas basadas en clases

#Vistas de Articulos
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'AppBlog/lista_articulos.html' #mismo que le pasaba al render

#Crear un Articulo

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ( 'titulo','subtitulo', 'cuerpo', 'autor', 'fecha_publicacion')
    success_url = reverse_lazy('lista_articulos') #mismo que usaba en url exitosa pero con reverse_lazy

class ArticuloDetailView(DetailView):
    model = Articulo
    succes_url= reverse_lazy('lista_articulos') 

class ArticuloUpdateView(LoginRequiredMixin,UpdateView):
    model = Articulo
    fields = ( 'titulo','subtitulo', 'cuerpo', 'autor', 'fecha_publicacion')
    success_url = reverse_lazy('lista_articulos')

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('lista_articulos')   
