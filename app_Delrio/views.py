# app_Delrio/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta, Cliente, Producto, Empleado, Proveedor # Importa los modelos
from django.db import IntegrityError
from django.http import HttpResponse
from django.db.models import Q
# ==========================================
# VISTAS PARA VENTA
# ==========================================

def inicio_Delrio(request):
    """
    Vista principal del sistema.
    """
    return render(request, 'inicio.html')

def ver_ventas(request):
    """
    Muestra una lista de todas las ventas.
    """
    ventas = Venta.objects.all().order_by('-fech_venta')
    return render(request, 'Ventas/ver_venta.html', {'ventas': ventas})


def agregar_venta(request):
    """
    Permite agregar una nueva venta.
    """
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    empleados = Empleado.objects.all()

    if request.method == 'POST':
        try:
            id_clie = request.POST.get('id_clie')
            id_prod = request.POST.get('id_prod')
            total_venta = request.POST.get('total_venta')
            estado = request.POST.get('estado')
            id_empl = request.POST.get('id_empl')

            cliente_obj = get_object_or_404(Cliente, id=id_clie)
            producto_obj = get_object_or_404(Producto, id=id_prod)
            empleado_obj = get_object_or_404(Empleado, id=id_empl)

            Venta.objects.create(
                id_clie=cliente_obj,
                id_prod=producto_obj,
                total_venta=total_venta,
                estado=estado,
                id_empl=empleado_obj,
            )
            return redirect('ver_ventas')
        except Exception as e:
            # Aquí puedes manejar errores si los datos no son válidos
            print(f"Error al agregar venta: {e}")
            # Puedes añadir un mensaje de error al contexto para mostrar en la plantilla
            return render(request, 'Ventas/agregar_venta.html', {
                'clientes': clientes,
                'productos': productos,
                'empleados': empleados,
                'error_message': f"Hubo un error al guardar la venta: {e}"
            })

    return render(request, 'Ventas/agregar_venta.html', {'clientes': clientes, 'productos': productos, 'empleados':empleados})


def actualizar_venta(request, pk):
    """
    Muestra el formulario para actualizar una venta existente.
    """
    venta = get_object_or_404(Venta, pk=pk)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'Ventas/actualizar_venta.html', {
        'venta': venta,
        'clientes': clientes,
        'productos': productos,
        'empleados': empleados,
    })


def realizar_actualizacion_venta(request, pk):
    """
    Procesa la actualización de una venta.
    """
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        try:
            id_clie = request.POST.get('id_clie')
            id_prod = request.POST.get('id_prod')
            total_venta = request.POST.get('total_venta')
            estado = request.POST.get('estado')
            id_empl = request.POST.get('id_empl')

            venta.id_clie = get_object_or_404(Cliente, id=id_clie)
            venta.id_prod = get_object_or_404(Producto, id=id_prod)
            venta.id_empl = get_object_or_404(Empleado, id=id_empl)
            venta.total_venta = total_venta
            venta.estado = estado
            venta.save()
            return redirect('ver_ventas')
        except Exception as e:
            print(f"Error al actualizar venta: {e}")
            clientes = Cliente.objects.all()
            productos = Producto.objects.all()
            empleados = Empleado.objects.all()
            return render(request, 'Ventas/actualizar_venta.html', {
                'venta': venta,
                'clientes': clientes,
                'productos': productos,
                'empleados': empleados,
                'error_message': f"Hubo un error al actualizar la venta: {e}"
            })
    return redirect('ver_ventas') # Redirige si se accede por GET


def borrar_venta(request, pk):
    """
    Borra una venta.
    """
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    # Opcional: puedes renderizar una página de confirmación de borrado
    return render(request, 'Ventas/borrar_venta.html', {'venta': venta})
#-----------------------------------------------------------------------------------------------------------------------------------
# Cliente
#-----------------------------------------------------------------------------------------------------------------------------------

# Función de inicio para Delrio
def inicio_delrio(request):
    return render(request, 'inicio.html') # Asumiendo que tendrás una página de inicio general

# Función para agregar un nuevo cliente
def agregar_cliente(request):
    if request.method == 'POST':
        nom_clie = request.POST.get('nom_clie')
        apellido_clie = request.POST.get('apellido_clie')
        C_E_clie = request.POST.get('C_E_clie')
        tel_clie = request.POST.get('tel_clie')
        direc_clie = request.POST.get('direc_clie')
        fech_compra = request.POST.get('fech_compra') # Asegúrate de que el formato sea YYYY-MM-DD

        Cliente.objects.create(
            nom_clie=nom_clie,
            apellido_clie=apellido_clie,
            C_E_clie=C_E_clie,
            tel_clie=tel_clie,
            direc_clie=direc_clie,
            fech_compra=fech_compra
        )
        return redirect('ver_clientes') # Redirigir a la lista de clientes después de agregar
    return render(request, 'clientes/agregar_clientes.html')

# Función para ver todos los clientes
def ver_clientes(request):
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter(
            Q(nom_clie__icontains=query) |
            Q(apellido_clie__icontains=query) |
            Q(C_E_clie__icontains=query)
        ).order_by('apellido_clie')
    else:
        clientes = Cliente.objects.all().order_by('apellido_clie')
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

# Función para mostrar el formulario de actualización de un cliente
def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})

# Función para procesar la actualización de un cliente
def realizar_actualizacion_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nom_clie = request.POST.get('nom_clie')
        cliente.apellido_clie = request.POST.get('apellido_clie')
        cliente.C_E_clie = request.POST.get('C_E_clie')
        cliente.tel_clie = request.POST.get('tel_clie')
        cliente.direc_clie = request.POST.get('direc_clie')
        cliente.fech_compra = request.POST.get('fech_compra')
        cliente.save()
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', cliente_id=cliente.id) # En caso de que se acceda directamente sin POST

# Función para borrar un cliente
def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})
#---------------------------------------------------------------------------------------------------------
# Producto
#---------------------------------------------------------------------------------------------------------
# Función para agregar un nuevo producto
def agregar_producto(request):
    if request.method == 'POST':
        nom_prod = request.POST.get('nom_prod')
        desc_prod = request.POST.get('desc_prod')
        precio_unidad = request.POST.get('precio_unidad')
        stock = request.POST.get('stock')
        id_prov = request.POST.get('id_prov')

        Producto.objects.create(
            nom_prod=nom_prod,
            desc_prod=desc_prod,
            precio_unidad=precio_unidad,
            stock=stock,
            id_prov_id=id_prov   # <- clave correcta para ForeignKey
        )

        return redirect('ver_productos')

    #  Cargar todos los proveedores disponibles para el formulario
    proveedores = Proveedor.objects.all()
    return render(request, 'productos/agregar_productos.html', {'proveedores': proveedores})

# Función para ver todos los productos
def ver_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(nom_prod__icontains=query) |
            Q(desc_prod__icontains=query)
        ).order_by('nom_prod')
    else:
        productos = Producto.objects.all().order_by('nom_prod')
    return render(request, 'productos/ver_productos.html', {'productos': productos})

# Función para mostrar el formulario de actualización de un producto
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    proveedores = Proveedor.objects.all()  # 🔹 Agregamos los proveedores disponibles
    return render(request, 'productos/actualizar_productos.html', {
        'producto': producto,
        'proveedores': proveedores
    })

# Función para procesar la actualización de un producto
def realizar_actualizacion_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nom_prod = request.POST.get('nom_prod')
        producto.desc_prod = request.POST.get('desc_prod')
        producto.precio_unidad = request.POST.get('precio_unidad')
        producto.stock = request.POST.get('stock')

        # 🔹 Actualizar proveedor correctamente
        id_prov = request.POST.get('id_prov')
        producto.id_prov_id = id_prov  # así Django guarda la relación correctamente

        producto.save()
        return redirect('ver_productos')

    return redirect('actualizar_producto', producto_id=producto.id)

# Función para borrar un producto
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'productos/borrar_productos.html', {'producto': producto})

#---------------------------------------------------------------------------------------------------------
# Empleado
#---------------------------------------------------------------------------------------------------------
def inicio_Delrio(request):
    return render(request, 'inicio.html') # Puedes ajustar la plantilla inicial si tienes una página de inicio diferente.

def agregar_empleado(request):
    if request.method == 'POST':
        try:
            nom_empl = request.POST['nom_empl']
            apellido_empl = request.POST['apellido_empl']
            puesto_empl = request.POST['puesto_empl']
            salario = request.POST['salario']
            fech_ingreso = request.POST['fech_ingreso']

            empleado = Empleado(
                nom_empl=nom_empl,
                apellido_empl=apellido_empl,
                puesto_empl=puesto_empl,
                salario=salario,
                fech_ingreso=fech_ingreso
            )
            empleado.save()
            return redirect('ver_empleados')
        except IntegrityError:
            return HttpResponse("Error: Ya existe un empleado con esa ID.", status=400)
    return render(request, 'empleados/agregar_empleado.html')

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, id_empl):
    empleado = get_object_or_404(Empleado, id=id_empl)
    return render(request, 'empleados/actualizar_empleado.html', {'empleado': empleado})

def realizar_actualizacion_empleado(request, id_empl):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id=id_empl)
        empleado.nom_empl = request.POST['nom_empl']
        empleado.apellido_empl = request.POST['apellido_empl']
        empleado.puesto_empl = request.POST['puesto_empl']
        empleado.salario = request.POST['salario']
        empleado.fech_ingreso = request.POST['fech_ingreso']
        empleado.save()
        return redirect('ver_empleados')
    return redirect('ver_empleados') # Redirige si se accede directamente con GET o algo inesperado

def borrar_empleado(request, id_empl):
    empleado = get_object_or_404(Empleado, id=id_empl)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})

#---------------------------------------------------------------------------------------------------------
# Proveedor
#---------------------------------------------------------------------------------------------------------
# Función para agregar un nuevo proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        id_prov = request.POST.get('id_prov')
        nom_prov = request.POST.get('nom_prov')
        contacto_prov = request.POST.get('contacto_prov')
        tel_prov = request.POST.get('tel_prov')
        C_E_prov = request.POST.get('C_E_prov')
        direc_prov = request.POST.get('direc_prov')

        Proveedor.objects.create(
            id_prov=id_prov,
            nom_prov=nom_prov,
            contacto_prov=contacto_prov,
            tel_prov=tel_prov,
            C_E_prov=C_E_prov,
            direc_prov=direc_prov
        )
        return redirect('ver_proveedores') # Redirigir a la lista de proveedores
    return render(request, 'proveedores/agregar_proveedores.html')

# Función para ver todos los proveedores
def ver_proveedores(request):
    query = request.GET.get('q')
    if query:
        proveedores = Proveedor.objects.filter(
            Q(nom_prov__icontains=query) |
            Q(contacto_prov__icontains=query) |
            Q(C_E_prov__icontains=query)
        ).order_by('nom_prov')
    else:
        proveedores = Proveedor.objects.all().order_by('nom_prov')
    return render(request, 'proveedores/ver_proveedores.html', {'proveedores': proveedores})

# Función para mostrar el formulario de actualización de un proveedor
def actualizar_proveedor(request, id_prov):
    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    return render(request, 'proveedores/actualizar_proveedores.html', {'proveedor': proveedor})

# Función para procesar la actualización de un proveedor
def realizar_actualizacion_proveedor(request, id_prov):
    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    if request.method == 'POST':
        proveedor.nom_prov = request.POST.get('nom_prov')
        proveedor.contacto_prov = request.POST.get('contacto_prov')
        proveedor.tel_prov = request.POST.get('tel_prov')
        proveedor.C_E_prov = request.POST.get('C_E_prov')
        proveedor.direc_prov = request.POST.get('direc_prov')
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', id_prov=proveedor.id_prov)

# Función para borrar un proveedor
def borrar_proveedor(request, id_prov):
    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedores/borrar_proveedores.html', {'proveedor': proveedor})