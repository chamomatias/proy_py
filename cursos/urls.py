from django.urls import path
from .views import (
    inicio,  
    AlumnosCreate, AlumnosRead, AlumnosUpdate, AlumnosDelete, CursosCreate, CursosRead, CursosUpdate, CursosDelete
)

urlpatterns = [
    path('', inicio, name='inicio'),  # Página de inicio
    path('cursos_inicio/', inicio, name='cursos_inicio'),  # ✅ Nueva ruta para cursos_inicio
    
    # Rutas de Alumnos
    path('alumnos_leer/', AlumnosRead.as_view(), name='alumnos_leer'),
    path('alumnos_crear/', AlumnosCreate.as_view(), name='alumnos_crear'),
    path('alumnos_actualizar/<int:pk>/', AlumnosUpdate.as_view(), name='alumnos_actualizar'),
    path('alumnos_borrar/<int:pk>/', AlumnosDelete.as_view(), name='alumnos_borrar'),

    # Rutas de Cursos
    path('cursos_leer/', CursosRead.as_view(), name='cursos_leer'),
    path('cursos_crear/', CursosCreate.as_view(), name='cursos_crear'),
    path('cursos_actualizar/<int:pk>/', CursosUpdate.as_view(), name='cursos_actualizar'),
    path('cursos_borrar/<int:pk>/', CursosDelete.as_view(), name='cursos_borrar'),
]
