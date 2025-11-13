# app_Delrio/models.py
from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nom_clie = models.CharField(max_length=100)
    apellido_clie = models.CharField(max_length=100)
    C_E_clie = models.CharField(max_length=100)  # Correo electrónico
    tel_clie = models.CharField(max_length=20)
    direc_clie = models.TextField()
    fech_compra = models.DateField()

    def __str__(self):
        return f"{self.nom_clie} {self.apellido_clie}"

    
# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    id_prov = models.IntegerField(primary_key=True)
    nom_prov = models.CharField(max_length=255)     # nom_prov (company name)
    contacto_prov = models.CharField(max_length=255) # contacto_prov (contact person)
    tel_prov = models.CharField(max_length=50)       # tel_prov (phone number)
    C_E_prov = models.CharField(max_length=255)     # C_E_prov (email)
    direc_prov = models.TextField()                  # direc_prov (address)

    def __str__(self):
        return self.nom_prov

# ==========================================
# MODELO: PRODUCTO
# ==========================================
class Producto(models.Model):
    nom_prod = models.CharField(max_length=100)
    desc_prod = models.TextField(blank=True, null=True)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fech_creacion = models.DateTimeField(auto_now_add=True)
    id_prov = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="productos")  # Si existiera tabla 'proveedor', sería ForeignKey

    def __str__(self):
        return f"Producto:{self.nom_prod} - Proveedor: {self.id_prov.nom_prov}"

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nom_empl = models.CharField(max_length=255)     # nom_empl (first name)
    apellido_empl = models.CharField(max_length=255) # apellido_empl (last name)
    puesto_empl = models.CharField(max_length=255)   # puesto_empl (job position)
    salario = models.DecimalField(max_digits=10, decimal_places=2)  # salario (salary)
    fech_ingreso = models.DateField()  # fech_ingreso (hire date)

    def __str__(self):
        return f"{self.nom_empl} {self.apellido_empl}"
    

# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    fech_venta = models.DateTimeField(auto_now_add=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)

    # Relaciones foráneas
    id_clie = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas")
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="ventas")
    id_empl = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="ventas") 

    def __str__(self):
        return f"Venta #{self.id} - Cliente: {self.id_clie.nom_clie} - Producto: {self.id_prod.nom_prod} - Empleado: {self.id_empl.nom_empl} - Total: ${self.total_venta}"    