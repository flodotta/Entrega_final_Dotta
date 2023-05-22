from django import forms

class ArticuloFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256) 
    codigo = forms.CharField(required=True, max_length=20)
    categoria = forms.CharField(required=True, max_length=256)
    fecha_publicacion = forms.DateField(required=True)    
