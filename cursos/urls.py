from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),  # Página de inicio

    path('cursos_create/', cursos_create, name='cursos_create'),  # Crear un curso
    path('cursos_read/', cursos_read, name='cursos_read'),  # Leer un curso
    path('cursos_update/', cursos_update, name='cursos_update'),  # Actualizar un curso
    path('cursos_delete/', cursos_delete, name='cursos_delete'),  # Eliminar un curso
]
