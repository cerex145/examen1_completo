# peliculas/forms.py
from django import forms
from .models import Peliculas, Autor

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = ['titulo', 'estreno', 'genero', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el título de la película'
            }),
            'estreno': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'genero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Drama, Acción, Comedia'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-select'
            })
        }
        labels = {
            'titulo': 'Título de la Película',
            'estreno': 'Fecha de Estreno',
            'genero': 'Género',
            'autor': 'Director'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el queryset de autores si es necesario
        self.fields['autor'].queryset = Autor.objects.all().order_by('nombre')
        self.fields['autor'].empty_label = "Selecciona un director"

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'nacionalidad']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del director'
            }),
            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Estadounidense, Mexicano, Español'
            })
        }
        labels = {
            'nombre': 'Nombre del Director',
            'nacionalidad': 'Nacionalidad'
        }

class BuscarPeliculaForm(forms.Form):
    q = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por título, género o director...',
            'autocomplete': 'off'
        }),
        label=''
    )