from django import forms

from restaurante.models import Platos


class AddPlato(forms.ModelForm):
    plato = forms.ModelChoiceField(
        label="Plato",
        queryset=Platos.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        empty_label="Selecciona un plato",
        required=False,
    )
    cantidad = forms.IntegerField(
        label="Cantidad",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Platos
        fields = ["plato", "cantidad"]