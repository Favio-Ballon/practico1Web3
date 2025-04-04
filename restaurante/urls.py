from django.urls import path, re_path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # platos
    path("platos", views.platos_list, name="platos_list"),
    path("platos/create", views.platos_create, name="platos_create"),
    path("platos/<int:id>", views.platos_edit, name="platos_edit"),
    path("platos/<int:id>/delete", views.platos_delete, name="platos_delete"),

    # mesas
    path("mesas", views.mesas_list, name="mesas_list"),
    path("mesas/create", views.mesas_create, name="mesas_create"),
    path("mesas/<int:id>", views.mesas_edit, name="mesas_edit"),
    path("mesas/<int:id>/delete", views.mesas_delete, name="mesas_delete"),

    # Meseros
    path("meseros", views.meseros_list, name="meseros_list"),
    path("meseros/create", views.meseros_create, name="meseros_create"),
    path("meseros/<int:id>", views.meseros_edit, name="meseros_edit"),
    path("meseros/<int:id>/delete", views.meseros_delete, name="meseros_delete"),

    # Ordenes
    path("ordenes", views.ordenes_list, name="ordenes_list"),

    path("ordenes/create", views.ordenes_create, name="ordenes_create"),
    path("ordenes/<int:id>", views.ordenes_edit, name="ordenes_edit"),
    path("ordenes/<int:id>/delete", views.ordenes_delete, name="ordenes_delete"),
    path("ordenes/<int:id>/plato", views.agregar_plato, name="agregar_plato"),
    path("ordenes/plato/<int:id>", views.eliminar_plato, name="eliminar_plato"),

    # Clientes
    path("clientes", views.clientes_list, name="clientes_list"),
    path("clientes/create/<int:id>", views.clientes_create, name="clientes_create"),
    path("clientes/<int:id>", views.clientes_edit, name="clientes_edit"),
    path("clientes/<int:id>/delete", views.clientes_delete, name="clientes_delete"),


    re_path(r'^.*$', lambda request: redirect('platos_list')),

    ]