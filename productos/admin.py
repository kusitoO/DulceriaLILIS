from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_interno', 'nombre', 'categoria', 'precio_venta', 'stock_actual')
    search_fields = ('id_interno', 'nombre')
    list_filter = ('categoria', 'perecible', 'control_por_lote')