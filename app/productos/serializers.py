from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
        read_only_fields = ["id"]

    # Dado que 'nombre' es requerido, se hace una validación
    def validate_nombre(self, nombre: str) -> str:
        if not nombre:
            raise serializers.ValidationError("El nombre es obligatorio.")
        return nombre.strip()

    def validate_precio(self, precio: float) -> float:
        if precio <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que cero.")
        return precio
