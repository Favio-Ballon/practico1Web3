from django import forms

from restaurante.models import Meseros


class MeserosForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    apellido = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    telefono = forms.CharField(
        label="Telefono",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Meseros
        fields = ["nombre", "apellido", "telefono"]