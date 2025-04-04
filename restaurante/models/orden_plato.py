from django.db import models

from restaurante.models import Ordenes, Platos


class OrdenPlato(models.Model):
    orden = models.ForeignKey("Ordenes", on_delete=models.CASCADE, related_name="orden_platos")
    plato = models.ForeignKey("Platos", on_delete=models.CASCADE, related_name="orden_platos")
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} de {self.plato}"
