from django.contrib import admin
from .models import CategoriaProd, Producto

# Registra tus modelos aquí.
class CategoriaAdmin(admin.ModelAdmin):
      list_display = ('nombre',)
      readonly_fields = ('created', 'updated')
      search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
      list_display = ('nombre','precio', 'disponibilidad')
      readonly_fields = ('created', 'updated')
      search_fields = ('nombre',)

admin.site.register(CategoriaProd, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
