from django.contrib import admin
from .models import Tipo_producto,Producto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','tipo_prodcuto']
    search_fields =['nombre','precio']
    list_filter = ['tipo_prodcuto']

admin.site.register(Tipo_producto)
admin.site.register(Producto,ProductoAdmin)