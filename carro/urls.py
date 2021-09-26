#from django.contrib import admin
from django.urls import path
from . import views

app_name="carro"

urlpatterns = [
   
    path('agregar/<int:producto_id>', views.agg_carro, name="agregar"),
    path('eliminar/<int:producto_id>', views.eliminar_carro, name="eliminar"),
    path('restar/<int:producto_id>', views.restar_carro, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),
]

#urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)