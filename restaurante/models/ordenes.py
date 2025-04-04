from django.db import models
from restaurante.models import Platos, Meseros, Mesa, Cliente


class Ordenes(models.Model):
    estado = models.BooleanField()
    fechaHora = models.DateTimeField()

    # los platos deberian tener una cantidad que se puede agregar
    platos = models.ManyToManyField(
        Platos,
        through='OrdenPlato',
        related_name='ordenes',
    )

    mesero = models.ForeignKey(
        Meseros,
        related_name='ordenes',
        on_delete=models.CASCADE,
    )

    mesa = models.ForeignKey(
        Mesa,
        related_name='ordenes',
        on_delete=models.CASCADE,
    )

    cliente = models.ForeignKey(
        Cliente,
        related_name='ordenes',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return str(self.mesero)
