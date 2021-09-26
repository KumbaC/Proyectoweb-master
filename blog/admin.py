from django.contrib import admin
from .models import Post, Categoria

# Registra tus modelos aquí.
class PostAdmin(admin.ModelAdmin):
      list_display = ('titulo', 'contenido', 'autor_id', 'imagen')
      readonly_fields = ('created', 'updated')
      search_fields = ("titulo",)
class CategoriaAdmin(admin.ModelAdmin):
      list_display = ('nombre',)
      readonly_fields = ('created', 'updated')
      search_fields = ('nombre',)



admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)