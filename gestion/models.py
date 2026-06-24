from django.db import models
from django.conf import settings


class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class CategoriaVino(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaVino, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to="vinos/", null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta #{self.id}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vino} x {self.cantidad}"