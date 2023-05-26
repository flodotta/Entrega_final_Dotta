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
#Se requiere autentificar
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ( 'titulo','subtitulo', 'cuerpo', 'autor', 'fecha_publicacion')
    success_url = reverse_lazy('listar_articulos') #mismo que usaba en url exitosa pero con reverse_lazy

    # def form_valid(self, form):
    #     form.instance.creador = self.request.user
    #     return super().form_valid(form)   

#Ver Detalle de un Articulo
#NO Se requiere autentificar
class ArticuloDetailView(DetailView):
    model = Articulo
    succes_url= reverse_lazy('listar_articulos') 

#Editar un Articulo
#Se requiere autentificar
class ArticuloUpdateView(LoginRequiredMixin,UpdateView):
    model = Articulo
    fields = ( 'titulo','subtitulo', 'cuerpo', 'autor', 'fecha_publicacion')
    success_url = reverse_lazy('listar_articulos')

#Borrar un Articulo
#Se requiere autentificarse
class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('listar_articulos')   

