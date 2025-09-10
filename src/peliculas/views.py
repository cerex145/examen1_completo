# peliculas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Peliculas, Autor
from .forms import PeliculaForm, AutorForm

# ============= VISTAS PARA PELÍCULAS =============

def listar_peliculas(request):
    """Vista para listar todas las películas con búsqueda opcional"""
    query = request.GET.get('q', '')
    
    if query:
        peliculas = Peliculas.objects.filter(
            Q(titulo__icontains=query) | 
            Q(genero__icontains=query) |
            Q(autor__nombre__icontains=query)
        ).order_by('-estreno')
    else:
        peliculas = Peliculas.objects.all().order_by('-estreno')
    
    context = {
        'peliculas': peliculas,
        'query': query,
    }
    return render(request, 'peliculas/listar_peliculas.html', context)

def crear_pelicula(request):
    """Vista para crear una nueva película"""
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Película creada exitosamente.')
            return redirect('listar_peliculas')
    else:
        form = PeliculaForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nueva Película'
    }
    return render(request, 'peliculas/form_pelicula.html', context)

def editar_pelicula(request, pk):
    """Vista para editar una película existente"""
    pelicula = get_object_or_404(Peliculas, pk=pk)
    
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            messages.success(request, 'Película actualizada exitosamente.')
            return redirect('listar_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    
    context = {
        'form': form,
        'pelicula': pelicula,
        'titulo': f'Editar: {pelicula.titulo}'
    }
    return render(request, 'peliculas/form_pelicula.html', context)

def eliminar_pelicula(request, pk):
    """Vista para eliminar una película"""
    pelicula = get_object_or_404(Peliculas, pk=pk)
    
    if request.method == 'POST':
        titulo = pelicula.titulo
        pelicula.delete()
        messages.success(request, f'Película "{titulo}" eliminada exitosamente.')
        return redirect('listar_peliculas')
    
    context = {
        'pelicula': pelicula
    }
    return render(request, 'peliculas/eliminar_pelicula.html', context)

def detalle_pelicula(request, pk):
    """Vista para mostrar el detalle de una película"""
    pelicula = get_object_or_404(Peliculas, pk=pk)
    context = {
        'pelicula': pelicula
    }
    return render(request, 'peliculas/detalle_pelicula.html', context)

# ============= VISTAS PARA AUTORES/DIRECTORES =============

def listar_autores(request):
    """Vista para listar todos los autores"""
    autores = Autor.objects.all().order_by('nombre')
    context = {
        'autores': autores
    }
    return render(request, 'peliculas/listar_autores.html', context)

def crear_autor(request):
    """Vista para crear un nuevo autor"""
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Director creado exitosamente.')
            return redirect('listar_autores')
    else:
        form = AutorForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Director'
    }
    return render(request, 'peliculas/form_autor.html', context)

def editar_autor(request, pk):
    """Vista para editar un autor existente"""
    autor = get_object_or_404(Autor, pk=pk)
    
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Director actualizado exitosamente.')
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    
    context = {
        'form': form,
        'autor': autor,
        'titulo': f'Editar: {autor.nombre}'
    }
    return render(request, 'peliculas/form_autor.html', context)

def eliminar_autor(request, pk):
    """Vista para eliminar un autor"""
    autor = get_object_or_404(Autor, pk=pk)
    
    if request.method == 'POST':
        nombre = autor.nombre
        autor.delete()
        messages.success(request, f'Director "{nombre}" eliminado exitosamente.')
        return redirect('listar_autores')
    
    context = {
        'autor': autor
    }
    return render(request, 'peliculas/eliminar_autor.html', context)

def detalle_autor(request, pk):
    """Vista para mostrar el detalle de un autor y sus películas"""
    autor = get_object_or_404(Autor, pk=pk)
    peliculas = autor.peliculas.all().order_by('-estreno')
    
    context = {
        'autor': autor,
        'peliculas': peliculas
    }
    return render(request, 'peliculas/detalle_autor.html', context)