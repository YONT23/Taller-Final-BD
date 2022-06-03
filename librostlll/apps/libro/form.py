from django import forms
from apps.libro.models import Libro, Autor

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro

        fields = [
            'titulo',
            'numeropagina',
            'edictorial',
            'isbn',
            'autor',
        ]

        labels = {
            'titulo': 'Ingrese el Titulo',
            'numeropagina': 'Ingrese el Numero de Pagina',
            'edictorial': 'Ingrese el Editorial',
            'isbn': 'Ingrese el ISBN',
            'autor': 'Ingrese el Autor',
        }

        Widget = {
            'titulo': forms.TextInput(attrs={'class': 'forms-control'}),
            'numeropagina': forms.TextInput(attrs={'class': 'forms-control'}),
            'edictorial': forms.TextInput(attrs={'class': 'forms-control'}),
            'isbn': forms.TextInput(attrs={'class': 'forms-control'}),
            'autor': forms.Select(attrs={'class': 'forms-control'}),
        }


class autorForm(forms.ModelForm):
    class Meta:
        model = Autor

        fields = [
            'nombre',
        ]

        labels = {
            'nombre': 'Ingrese el Nombre',
   
        }

        Widget = {
            'nombre': forms.TextInput(attrs={'class': 'forms-control'}),
        }