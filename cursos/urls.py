from django.urls import path
from .views import (
    inicio, cursos_create, cursos_read, cursos_update, cursos_delete, 
    AlumnosCreate, AlumnosRead, AlumnosUpdate, AlumnosDelete
)

urlpatterns = [
    path('', inicio, name='inicio'),  # Página de inicio

    path('cursos_create/', cursos_create, name='cursos_create'),  # Crear un curso
    path('cursos_read/', cursos_read, name='cursos_read'),  # Leer un curso
    path('cursos_update/', cursos_update, name='cursos_update'),  # Actualizar un curso
    path('cursos_delete/', cursos_delete, name='cursos_delete'),  # Eliminar un curso

    # Rutas de Alumnos
    path('alumnos_leer/', AlumnosRead.as_view(), name='alumnos_leer'),
    path('alumnos_crear/', AlumnosCreate.as_view(), name='alumnos_crear'),
    path('alumnos_actualizar/<int:pk>/', AlumnosUpdate.as_view(), name='alumnos_actualizar'),
    path('alumnos_borrar/<int:pk>/', AlumnosDelete.as_view(), name='alumnos_borrar'),
]
