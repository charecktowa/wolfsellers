# productos/tests.py
from django.test import TestCase

from .models import Producto


class ProductoModelTest(TestCase):
    def test_create_producto(self) -> None:
        p = Producto.objects.create(nombre="Test", precio=9.99)
        self.assertEqual(p.nombre, "Test")

    def test_producto_str(self) -> None:
        p = Producto(nombre="Test")
        self.assertEqual(str(p), "Test")

    def test_producto_default_disponible(self) -> None:
        p = Producto(nombre="Test", precio=9.99)
        self.assertTrue(p.disponible)

    def test_guardar_descripcion(self) -> None:
        descripcion = "Este es un producto de prueba."
        p = Producto.objects.create(nombre="Test", precio=9.99, descripcion=descripcion)
        self.assertEqual(p.descripcion, descripcion)
