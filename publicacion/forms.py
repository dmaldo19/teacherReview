# forms.py
from django import forms
from .models import Publicacion

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['profesor', 'materia', 'titulo', 'fecha', 'comentario', 'dominio', 'puntualidad', 'asistencia', 'dificultad', 'seguimiento']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control'}),
            'dominio': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'}),
            'puntualidad': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'}),
            'asistencia': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'}),
            'dificultad': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'}),
            'seguimiento': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'}),
        }
