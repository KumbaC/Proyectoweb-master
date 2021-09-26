from django.contrib import admin
from django.urls import path
from Appweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.home, name="Home"),
    #path(r'servicios/', views.servicos, name="Servicios"),
    #path(r'tienda/', views.Tienda, name="Tienda"),
    #path(r'blog/', views.Blog, name="Blog"),
    #path(r'contacto/', views.Contacto, name="Contacto")
    
 
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
