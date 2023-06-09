from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from AppPerfiles.forms import UserRegisterForm, UserUpdateForm , AvatarFormulario, AvatarUpdateForm
from AppPerfiles.models import Avatar

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

# Create your views here.
def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='AppPerfiles/signup.html',
       context={'form': formulario},
   )


def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data #es el diccionario
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password) #authenticate es una funcion ayudante de django
           # user puede ser un usuario o None. None si el usuario si la contraseña esta bien
           if user: #chequea que user no sea none
               login(request=request, user=user) #funcion ayudante login
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='AppPerfiles/login.html',
       context={'form': form},
   )
class CustomLogoutView(LogoutView):
   template_name = 'AppPerfiles/logout.html'

#vista para ver mi perfil
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'AppPerfiles/formulario_perfil.html'

   def get_object(self, queryset=None):
       return self.request.user

#Agregar un avatar a mi perfil
def agregar_avatar(request):
  if request.method == "POST":
      formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

      if formulario.is_valid():
          avatar = formulario.save()
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('inicio')
          return redirect(url_exitosa)
  else:  # GET
      formulario = AvatarFormulario()
  return render(
      request=request,
      template_name="AppPerfiles/formulario_avatar.html",
      context={'form': formulario},
  )

#modificar un avatar de mi perfil

def modificar_avatar(request):
    avatar = request.user.avatar

    if request.method == "POST":
        formulario = AvatarUpdateForm(request.POST, request.FILES, instance=avatar)

        if formulario.is_valid():
            avatar = formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarUpdateForm(instance=avatar)

    return render(
        request=request,
        template_name="AppPerfiles/modificar_avatar.html",
        context={'form': formulario},
    )
