from rest_framework import viewsets

from app.productos.models import Producto
from app.productos.serializer import ProductoSerializer


# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
