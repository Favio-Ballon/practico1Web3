from django import forms

from restaurante.models import Platos


class PlatosForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    descripcion = forms.CharField(
        label="Descripcion",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Platos
        fields = ["nombre", "descripcion"]