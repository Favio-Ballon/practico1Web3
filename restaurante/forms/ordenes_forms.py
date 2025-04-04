from django import forms
from restaurante.models import Ordenes, Meseros, Mesa, Platos
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class OrdenesForm(forms.ModelForm):
    mesa = forms.ModelChoiceField(
        queryset=Mesa.objects.all(),
        label="Mesa",
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Selecciona una mesa",
        required = True
    )
    mesero = forms.ModelChoiceField(
        queryset=Meseros.objects.all(),
        label="Mesero",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    plato = forms.ModelChoiceField(
        queryset=Platos.objects.all(),
        label="Primer Plato",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Ordenes
        fields = ["mesa", "mesero", "plato"]

    def clean_mesa(self):
        mesa = self.cleaned_data.get("mesa")
        if Ordenes.objects.filter(mesa=mesa, estado=True).exists():
            raise ValidationError("Ya existe una orden activa para esta mesa.")
        return mesa

    def save(self, commit=True):
        orden = super().save(commit=False)
        orden.estado = True  # Estado siempre en "abierto"
        orden.fechaHora = now()  # Fecha y hora actual

        if commit:
            orden.save()
            orden.platos.add(self.cleaned_data["plato"])  # Se añade el primer plato a la orden

        return orden
