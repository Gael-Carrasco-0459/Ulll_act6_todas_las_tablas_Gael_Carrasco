# app_Delrio/admin.py
from django.contrib import admin
from .models import Cliente, Producto, Venta, Empleado, Proveedor

# Registra los modelos aquí.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Empleado)
admin.site.register(Proveedor)
