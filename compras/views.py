from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import CreateView
from .models import SolicitudCompra  # asegúrate de tener este modelo creado
from django.urls import reverse_lazy

class SolicitudCompraListView(ListView):
    model = SolicitudCompra
    template_name = "compras/solicitud_list.html"  # crea este template
    context_object_name = "solicitudes"

class SolicitudCompraCreateView(CreateView):
    model = SolicitudCompra
    fields = "__all__"  # puedes personalizar los campos
    template_name = "compras/solicitud_form.html"
    success_url = reverse_lazy("solicitud_list")