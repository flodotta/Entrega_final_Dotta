from django.contrib import admin

from AppBlog.models import Lector, Escritor, Articulo 
# Register your models here.
admin.site.register(Lector)
admin.site.register(Escritor)
admin.site.register(Articulo)
