# CineManager - Sistema de Gestión de Películas

## Descripción del Proyecto

Sistema web desarrollado en Django para administrar una colección de películas y sus directores. Permite realizar operaciones CRUD completas en ambas entidades con búsqueda integrada.

### Funcionalidades
- Listado de películas 
- Creación de películas 
- Edición de películas 
- Eliminación de películas 
- Buscador de películas por título, género o director 
- Relación películas-directores 
- CRUD básico de directores 


## Tecnologías Utilizadas

- Django 5.2.6
- Python 3.13.7
- Bootstrap 5
- SQLite
- HTML/CSS/JavaScript

## Instalación y Ejecución

### Prerrequisitos
- Python 3.8+
- pip

### Pasos

1. **Crear entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

2. **Instalar Django**
   ```bash
   pip install django
   ```

3. **Configurar base de datos**
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Ejecutar servidor**
   ```bash
   python manage.py runserver
   ```

5. **Acceder**
   - URL: http://127.0.0.1:8000

## Estructura del Proyecto (peliculas) oñoooooo


├── peliculas/
│   ├── templates/peliculas/
│   │   ├── base.html
│   │   ├── listar_peliculas.html
│   │   ├── form_pelicula.html
│   │   ├── eliminar_pelicula.html
│   │   ├── detalle_pelicula.html
│   │   ├── listar_autores.html
│   │   ├── form_autor.html
│   │   ├── eliminar_autor.html
│   │   └── detalle_autor.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
└── manage.py
```

## Modelos

```python
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

class Peliculas(models.Model):
    titulo = models.CharField(max_length=100)
    estreno = models.DateField()
    genero = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
```

## URLs Principales

- `/` - Lista de películas
- `/pelicula/crear/` - Crear película
- `/pelicula/<id>/` - Ver película
- `/pelicula/<id>/editar/` - Editar película
- `/pelicula/<id>/eliminar/` - Eliminar película
- `/directores/` - Lista de directores
- `/director/crear/` - Crear director
- `/director/<id>/` - Ver director

## Características

- Búsqueda por título, género y director
- Validación de formularios
- Interfaz responsiva
- Relaciones entre entidades
- Confirmación de eliminación
- Mensajes de éxito/error



## Uso

1. **Películas**: Crear, editar, eliminar y buscar películas
2. **Directores**: Gestionar directores y ver sus películas
3. **Búsqueda**: Usar la barra de búsqueda para filtrar contenido
4. **Navegación**: Enlaces entre películas y directores relacionados

