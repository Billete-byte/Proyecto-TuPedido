from django.contrib import admin
from.models import Comuna,Usuario

# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','celular')
    search_fields = ('nombre', 'apellido')
    list_filter = ('comuna',)

admin.site.register(Comuna)
admin.site.register(Usuario,UsuarioAdmin)