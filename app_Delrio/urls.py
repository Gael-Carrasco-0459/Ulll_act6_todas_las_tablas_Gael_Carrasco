# app_Delrio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #URLs para Ventas
    path('', views.inicio_Delrio, name='inicio_delrio'),
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/actualizar/<int:pk>/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/actualizar/realizar/<int:pk>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('ventas/borrar/<int:pk>/', views.borrar_venta, name='borrar_venta'),
    # URLs para Clientes
    path('', views.inicio_delrio, name='inicio_delrio'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:cliente_id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
    # URLs para Productos
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.ver_productos, name='ver_productos'),
    path('productos/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/realizar_actualizacion/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('productos/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    # URLs para Empleados
    path('', views.inicio_Delrio, name='inicio_Delrio'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id_empl>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/realizar_actualizacion/<int:id_empl>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:id_empl>/', views.borrar_empleado, name='borrar_empleado'),
    # URLs para Proveedores
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedores/actualizar/<int:id_prov>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/realizar_actualizacion/<int:id_prov>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedores/borrar/<int:id_prov>/', views.borrar_proveedor, name='borrar_proveedor'),
]
