from django.contrib import admin
from servicios.models import Servicio

# Registra tus modelos aquí.
class ServiciosAdmin(admin.ModelAdmin):
      list_display = ('titulo', 'contenido', 'imagen')
      readonly_fields = ('created', 'updated')
      search_fields = ("titulo",)
admin.site.register(Servicio, ServiciosAdmin)

