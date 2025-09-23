from django.urls import path
from . import views

urlpatterns = [
    path('solicitudes/', views.SolicitudCompraListView.as_view(), name='solicitud_list'),
    path('solicitudes/nueva/', views.SolicitudCompraCreateView.as_view(), name='solicitud_create'),
    # Puedes agregar más rutas luego
]