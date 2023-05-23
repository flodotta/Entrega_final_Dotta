from django import forms

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(required=True, max_length=256) 
    subtitulo = forms.CharField(required=True, max_length=20)
    cuerpo = forms.CharField(required=True, max_length=1500)
    autor = forms.CharField(required=True, max_length=256)
    fecha_publicacion = forms.DateField(required=True)    
