from django.shortcuts import render

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