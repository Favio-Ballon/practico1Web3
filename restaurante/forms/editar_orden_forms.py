from django import forms
from restaurante.models import Ordenes, Meseros, Mesa, Platos



class OrdenesEditForm(forms.ModelForm):
    mesero = forms.ModelChoiceField(
        queryset=Meseros.objects.all(),
        label="Mesero",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Ordenes
        fields = ["mesero"]
