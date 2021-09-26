from django.shortcuts import render
from tienda.models import Producto, CategoriaProd
# Crea tus vistas aquí.

def Tienda(request): 
    shop = Producto.objects.all()
    categoria = CategoriaProd.objects.all()
    return render(request, 'tienda/tienda.html', {'shop':shop, 'categoria':categoria})