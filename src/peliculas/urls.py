# peliculas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs para películas
    path('', views.listar_peliculas, name='listar_peliculas'),
    path('pelicula/crear/', views.crear_pelicula, name='crear_pelicula'),
    path('pelicula/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('pelicula/<int:pk>/editar/', views.editar_pelicula, name='editar_pelicula'),
    path('pelicula/<int:pk>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),
    
    # URLs para autores/directores
    path('directores/', views.listar_autores, name='listar_autores'),
    path('director/crear/', views.crear_autor, name='crear_autor'),
    path('director/<int:pk>/', views.detalle_autor, name='detalle_autor'),
    path('director/<int:pk>/editar/', views.editar_autor, name='editar_autor'),
    path('director/<int:pk>/eliminar/', views.eliminar_autor, name='eliminar_autor'),
]