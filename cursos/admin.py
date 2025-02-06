from django.contrib import admin
from .models import Cursos, Alumnos

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    fields = ('nombre', 'descripcion')


@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'activo')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('activo', 'fecha_nacimiento')
