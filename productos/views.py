from django.shortcuts import render
from .models import Producto

# Create your views here.
def productos(request):
    productos = Producto.objects.filter(user=request.user, fecha_completado__isnull=True)
    return render(request, 'productos.html', {'productos': productos})

