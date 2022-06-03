from django import forms
from apps.ejemplares.models import Ejemplares, Prestar

class ejemplarForm(forms.ModelForm):
    class Meta:
        model = Ejemplares

        fields = [
            'localizacion',
            'user',
            'libro',
        ]

        labels = {
            'localizacion': 'Ingrese la Localizacion',
            'user': 'Ingrese el Usuario',
            'libro': 'Ingrese el Libro',
        }

        Widget = {
            'localizacion':forms.TextInput(attrs={'class': 'forms-control'}),
            'user':forms.Select(attrs={'class': 'forms-control'}),
            'libro':forms.Select(attrs={'class': 'forms-control'}),
        }


class prestarForm(forms.ModelForm):
    class Meta:
        model = Prestar

        fields = [
            'ejemplares',
            'user',
            'fecha_dev',
            'fecha_pres',
        ]

        labels = {
            'ejemplares': 'Ingrese el Ejemplar',
            'user': 'Ingrese el Usuario',
            'fecha_dev': 'Ingrese el Fecha Dev',
            'fecha_pres': 'Ingrese el Fecha Pres',
        }

        Widget = {
            'ejemplares':forms.Select(attrs={'class': 'forms-control'}),
            'user':forms.Select(attrs={'class': 'forms-control'}),
            'fecha_dev': forms.DateInput(),
            'fecha_pres': forms.DateInput(),
        }