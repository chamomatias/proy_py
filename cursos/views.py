from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alumnos, Cursos



def inicio(request):
    return render(request, 'cursos/inicio.html')  # Ajustamos la ruta del template

def cursos_create(request):
    return render(request, 'cursos/cursos_create.html')  # Ajustamos la ruta del template

def cursos_read(request):
    return render(request, 'cursos/cursos_read.html')  # Ajustamos la ruta del template

def cursos_update(request):
    return render(request, 'cursos/cursos_update.html')  # Ajustamos la ruta del template

def cursos_delete(request):
    return render(request, 'cursos/cursos_delete.html')  # Ajustamos la ruta del template




class AlumnosCreate(CreateView):
    model = Alumnos
    template_name = 'cursos/alumnos_crear.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'activo']
    success_url = reverse_lazy('alumnos_leer')

class AlumnosRead(ListView):
    model = Alumnos
    template_name = 'cursos/alumnos_leer.html'  # ✅ Agregamos el prefijo correcto
    context_object_name = 'alumnos'

class AlumnosUpdate(UpdateView):
    model = Alumnos
    template_name = 'cursos/alumnos_actualizar.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'activo']
    success_url = reverse_lazy('alumnos_leer')

class AlumnosDelete(DeleteView):
    model = Alumnos
    template_name = 'cursos/alumnos_borrar.html'
    success_url = reverse_lazy('alumnos_leer')
    

class CursosCreate(CreateView):
    model = Cursos
    fields = ['nombre', 'descripcion']
    template_name = 'cursos/cursos_crear.html'
    success_url = reverse_lazy('cursos_leer')
    
class CursosRead(ListView):
    model = Cursos
    template_name = 'cursos/cursos_leer.html'
    context_object_name = 'cursos'
    
class CursosUpdate(UpdateView):
    model = Cursos
    fields = ['nombre', 'descripcion']
    template_name = 'cursos/cursos_actualizar.html'
    success_url = reverse_lazy('cursos_leer')
    
class CursosDelete(DeleteView):
    model = Cursos
    template_name = 'cursos/cursos_borrar.html'
    success_url = reverse_lazy('cursos_leer')