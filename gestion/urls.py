from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path(
        "vinos-disponibles/",
        views.vinos_disponibles,
        name="vinos_disponibles"
    ),

    path(
        "gestion-vinos/",
        views.vino_listar,
        name="vino_listar"
    ),

    path(
        "vinos/crear/",
        views.vino_crear,
        name="vino_crear"
    ),

    path(
        "vinos/editar/<int:id>/",
        views.vino_editar,
        name="vino_editar"
    ),

    path(
        "vinos/eliminar/<int:id>/",
        views.vino_eliminar,
        name="vino_eliminar"
    ),

    path(
        "vinos/toggle/<int:id>/",
        views.vino_toggle,
        name="vino_toggle"
    ),

    path(
        "clientes/",
        views.cliente_listar,
        name="cliente_listar"
    ),

    path(
        "clientes/crear/",
        views.cliente_crear,
        name="cliente_crear"
    ),

    path(
        "clientes/editar/<int:id>/",
        views.cliente_editar,
        name="cliente_editar"
    ),

    path(
        "clientes/eliminar/<int:id>/",
        views.cliente_eliminar,
        name="cliente_eliminar"
    ),

    path(
        "ventas/",
        views.venta_listar,
        name="venta_listar"
    ),

    path(
        "ventas/crear/",
        views.venta_crear,
        name="venta_crear"
    ),

]