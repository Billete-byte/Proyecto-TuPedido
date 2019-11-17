from django.shortcuts import render,redirect
from .models import Comuna,Usuario
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):

    comunas = Comuna.objects.all()
    variables ={
        'comunas':comunas
    }

    if request.POST:
        persona=Usuario()
        persona.celular = request.POST.get('txtCelular')
        persona.nombre = request.POST.get('txtNombre')
        persona.apellido = request.POST.get('txtApellido')
        persona.correo = request.POST.get('txtCorreo')
        persona.direccion = request.POST.get('txtDireccion')
        persona.fecha = request.POST.get('txtFechaN')
        comuna = Comuna()
        comuna.id = request.POST.get('cboComuna')
        persona.comuna = comuna

        try:
            persona.save()
            variables['mensaje'] = 'guardado correctamente'
        except:
            variables['mensaje'] = 'No se a podido guardar'


    return render(request, 'core/formulario.html',variables)
#CRUD
def listar_usuario(request):

    personas=Usuario.objects.all()

    return render(request, 'core/listar_usuario.html',{
        'personas': personas
    })

def eliminar_usuario(request,id):
    #buscar persona que queremos eliminar
    persona= Usuario.objects.get(id=id)

    try:
        persona.delete()
        mensaje= "Eliminado correctamente"
        messages.success(request,mensaje)
    except:
        mensaje= "No se Ha podido eliminar"
        messages.error(request,mensaje)
    
    return redirect('listar_usuario')


def modificar_usuario(request,id):
    #buscamos al usuario para poder modificarlo
    persona = Usuario.objects.get(id=id)
    comunas = Comuna.objects.all()
    variables ={
        'persona':persona,
        'comunas':comunas
    }

    if request.POST:
        persona=Usuario()
        persona.id = request.POST.get('txtId')
        persona.celular = request.POST.get('txtCelular')
        persona.nombre = request.POST.get('txtNombre')
        persona.apellido = request.POST.get('txtApellido')
        persona.correo = request.POST.get('txtCorreo')
        persona.direccion = request.POST.get('txtDireccion')
        persona.fecha = request.POST.get('txtFechaN')
        comuna = Comuna()
        comuna.id = request.POST.get('cboComuna')
        persona.comuna = comuna

            

        try:
            persona.save()
            messages.success(request, 'modificado correctamente')
            
        except:
            messages.error(request, 'no se ha podido modificar')

          
        return redirect('listar_usuario')

    return render(request, 'core/modificar_usuario.html', variables)


