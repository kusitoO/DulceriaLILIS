from django import forms
from .models import SolicitudCompra, RecepcionCompra, DetalleRecepcion

class SolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = SolicitudCompra
        fields = [
            'producto',
            'proveedor',
            'solicitado_por',
            'cantidad',
            'estado',
            'observaciones',
        ]
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

class RecepcionCompraForm(forms.ModelForm):
    class Meta:
        model = RecepcionCompra
        fields = [
            'solicitud',
            'recibido_por',
            'observaciones',
        ]
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

class DetalleRecepcionForm(forms.ModelForm):
    class Meta:
        model = DetalleRecepcion
        fields = [
            'recepcion',
            'cantidad_recibida',
            'estado_producto',
            'lote',
            'fecha_vencimiento',
        ]
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }