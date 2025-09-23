from django.contrib import admin
from .models import SolicitudCompra, RecepcionCompra, DetalleRecepcion

@admin.register(SolicitudCompra)
class SolicitudCompraAdmin(admin.ModelAdmin):
    list_display = ('producto', 'proveedor', 'cantidad', 'estado', 'fecha_solicitud')
    list_filter = ('estado', 'proveedor')
    search_fields = ('producto__nombre', 'proveedor__nombre')

@admin.register(RecepcionCompra)
class RecepcionCompraAdmin(admin.ModelAdmin):
    list_display = ('solicitud', 'recibido_por', 'fecha_recepcion')
    search_fields = ('solicitud__producto__nombre',)

@admin.register(DetalleRecepcion)
class DetalleRecepcionAdmin(admin.ModelAdmin):
    list_display = ('recepcion', 'cantidad_recibida', 'estado_producto', 'lote')
    list_filter = ('estado_producto',)