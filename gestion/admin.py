from django.contrib import admin
from .models import (
    Bodega,
    CategoriaVino,
    Proveedor,
    Cliente,
    Vino,
    Venta,
    DetalleVenta,
)


@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "provincia")
    search_fields = ("nombre", "provincia")


@admin.register(CategoriaVino)
class CategoriaVinoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "email")
    search_fields = ("nombre", "email")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono", "email")
    search_fields = ("nombre", "apellido", "email")


@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "bodega", "categoria", "precio", "stock", "activo")
    list_filter = ("bodega", "categoria", "activo")
    search_fields = ("nombre", "bodega__nombre", "categoria__nombre")
    ordering = ("nombre",)


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "usuario", "fecha")
    list_filter = ("fecha", "usuario")
    search_fields = ("cliente__nombre", "cliente__apellido", "usuario__username")


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ("venta", "vino", "cantidad", "precio_unitario")
    search_fields = ("vino__nombre",)