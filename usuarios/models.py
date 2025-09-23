from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    rol = models.CharField(max_length=50, choices=[
        ('admin', 'Administrador'),
        ('compras', 'Operador de Compras'),
        ('inventario', 'Operador de Inventario'),
        ('produccion', 'Operador de Producción'),
        ('ventas', 'Operador de Ventas'),
        ('finanzas', 'Analista Financiero'),
    ])
    estado = models.BooleanField(default=True)
    ultimo_acceso = models.DateTimeField(blank=True, null=True)
    mfa_habilitado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"