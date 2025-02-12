from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.forms import UserRegisterForm


def usuarios_ingresar(request):
    """ Maneja el inicio de sesión de usuarios """
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {usuario}")
                return redirect("cursos_inicio")  # ✅ Redirige correctamente

        messages.error(request, "Usuario o contraseña incorrectos")

    form = AuthenticationForm()
    return render(request, "users/usuarios_ingresar.html", {"form": form})



def usuarios_registrar(request):
    """ Maneja el registro de nuevos usuarios """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. ¡Ahora puedes iniciar sesión!")
            return redirect("usuarios_ingresar")  # Redirigir a la página de login
        
        messages.error(request, "Error en los datos ingresados")

    form = UserRegisterForm()
    return render(request, "users/usuarios_registrar.html", {"form": form})


def usuarios_salir(request):
    """ Maneja el cierre de sesión de usuarios """
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente")
    return redirect("usuarios_ingresar")  # Redirigir a la página de login
