from django.urls import path
from .views import home,galeria,formulario,listar_usuario,eliminar_usuario,modificar_usuario

urlpatterns = [
    path('',home, name="home"),
    path('galeria/',galeria ,name="galeria"),
    path('formulario/',formulario, name="formulario"),
    path('listar-usuario/',listar_usuario, name="listar_usuario"),
    path('eliminar-usuario/<id>/',eliminar_usuario, name="eliminar_usuario"),
    path('modificar-usuario/<id>/',modificar_usuario, name="modificar_usuario")
]