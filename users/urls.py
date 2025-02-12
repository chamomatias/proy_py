from django.urls import path
from users.views import usuarios_ingresar, usuarios_registrar, usuarios_salir

urlpatterns = [
    path("usuarios_ingresar/", usuarios_ingresar, name="usuarios_ingresar"),
    path("usuarios_registrar/", usuarios_registrar, name="usuarios_registrar"),
    path("usuarios_salir/", usuarios_salir, name="usuarios_salir"),
]
