from typing import Any
from django import forms
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class RegistroForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=20)
    correo = forms.EmailField()
    contra = forms.CharField()
    confirmacion = forms.CharField()

    #clean esta hecho para validaciones.
    #Sintaxis clean_<campo>
    def clean_nombre_usuario(self):
        usuario = self.cleaned_data.get('nombre_usuario')
        #Si en todos los objetos de la tabla de usuario, filtra, y en el campo de nombre de usuario hay un usuario con el nombre
        if Usuario.objects.filter(nombre_usuario=usuario) or \
        Usuario.objects.filter(username=usuario):#Valida que no se pueda poner admin como usuario
            raise forms.ValidationError('Nombre de usuario no disponible')
        return usuario
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if '@alumnos.udg.mx' not in correo:
            raise forms.ValidationError('Correo no válido.')
        return correo
    
    def clean(self):
        datos = self.cleaned_data
        contra = datos.get('contra')
        confirmacion = datos.get('confirmacion')
        if contra != confirmacion:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return datos
    
    def save(self):
        datos = self.cleaned_data
        datos['username'] = datos['nombre_usuario']
        datos['password'] = datos['contra']
        datos['email'] = datos['correo']
        datos.pop('correo')
        datos.pop('confirmacion')
        datos.pop('contra')
        return Usuario.objects.create_user(**datos)
