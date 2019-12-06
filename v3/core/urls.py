from django.urls import path
from .views import home,galeria,listado_producto, nuevo_producto,modificar_producto,eliminar_producto,registro_usuario

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listado-productos/',listado_producto,name="listado_productos"),
    path('nuevo-producto/',nuevo_producto,name="nuevo_producto"),
    path('modificar-producto/<id>/',modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto , name="eliminar_producto"),
    path('registro/', registro_usuario, name='registro_usuario')
]
