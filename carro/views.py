from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto


# Create your views here.
def agg_carro(request, producto_id):
    carro = Carro(request) 
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)
    return redirect('Tienda')

def eliminar_carro(request, producto_id):
    carro = Carro(request) 
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto = producto)
    return redirect('Tienda')

def restar_carro(request, producto_id):
    carro = Carro(request) 
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto = producto)
    return redirect('Tienda')

def limpiar_carro(request, producto_id):
    carro = Carro(request) 
    #producto = Producto.objects.get(id = producto_id)
    carro.limpiar_carro()
    return redirect('Tienda')