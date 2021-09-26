from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path(r'', views.blog, name="Blog"),
    path(r'categoria/<int:categoria_id>/', views.categoria, name="categoria")
 
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
