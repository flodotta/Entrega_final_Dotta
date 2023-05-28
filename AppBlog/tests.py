from django.test import TestCase

# Create your tests here.
from django.db import IntegrityError
from AppBlog.models import Articulo


class ArticuloTests(TestCase):
   """En esta clase van todas las pruebas del modelo Articulo."""

   def test_creacion_articulo(self):
       # caso uso esperado
       articulo = Articulo(titulo="Titulo", subtitulo="Subtitulo", cuerpo="Cuerpo", autor="Autor", fecha_publicacion="2023-05-10")
       articulo.save()
  #'''user '''
    #agrego el modo creador para que registre quien fue el creador
    

       # Compruebo que el curso fue creado y la data fue guardad correctamente
       self.assertEqual(Articulo.objects.count(), 1)
       self.assertEqual(articulo.titulo, "Titulo")
       self.assertEqual(articulo.subtitulo, "Subtitulo")
       self.assertEqual(articulo.cuerpo, "Cuerpo")
       self.assertEqual(articulo.autor, "Autor")
       self.assertEqual(articulo.fecha_publicacion, "2023-05-10")

   def test_articulo_str(self):
       articulo = Articulo(titulo="Titulo2", subtitulo="Subtitulo2", cuerpo="Cuerpo2", autor="Autor2", fecha_publicacion="2023-05-10")
       articulo.save()
    # Compruebo el str funciona como se desea
       expected_str = "Titulo2, Autor2, 2023-05-10"
       self.assertEqual(str(articulo), expected_str)
