from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, CustomUserForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,authenticate
# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def galeria(request):

    data = {
        'productos':Producto.objects.all()
    }
    return render(request, 'core/galeria.html',data)



@permission_required('core.add_producto')
def listado_producto(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'core/listado_productos.html',data)

@login_required
def nuevo_producto(request):
    data ={
        'form':ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        data['form'] = formulario

    return render(request, 'core/nuevo_producto.html',data)

def modificar_producto(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "modificado correctamente"
            data['form'] = formulario
        data['form'] = ProductoForm(instance=Producto.objects.get(id=id))

    return render(request, 'core/modificar_producto.html',data)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="listado_productos")

def registro_usuario(request):
    data ={
        'form': CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y mandarlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html',data)