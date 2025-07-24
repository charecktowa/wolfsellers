from django.db import models
from decimal import Decimal


# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(
        max_digits=8, decimal_places=2, default=Decimal("0.00")
    )
    disponible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre
