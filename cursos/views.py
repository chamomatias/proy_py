from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alumnos, Cursos
from .forms import ContactosForm
from django.contrib import messages

def inicio(request):
    return render(request, 'cursos/inicio.html')  # Ajustamos la ruta del template

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
    
    
def contactos_crear(request):
    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado con éxito. Te contactaremos pronto.')
            return redirect('contactos_exitosos')  # Redirige a la página de éxito
        else:
            messages.error(request, 'Hubo un error al enviar el formulario. Revisa los campos.')

    else:
        form = ContactosForm()

    return render(request, 'cursos/contactos_crear.html', {'form': form})
