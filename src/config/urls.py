# EXAMEN_COMPLETO/urls.py (archivo principal de URLs)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peliculas.urls')),
]