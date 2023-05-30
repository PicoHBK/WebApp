from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ClienteForm
from .models import Cliente




def listado_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listado.html', {'clientes': clientes})

def activar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    # Guardar el campo 'activo' en True
    cliente.activo = True
    cliente.save()

    # Mostrar un mensaje de activación exitosa
    messages.success(request, 'Cliente activado correctamente.')

    # Redireccionar al listado de clientes
    return redirect('cliente:listado_clientes')

def desactivar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    # Guardar el campo 'activo' en False
    cliente.activo = False
    cliente.save()

    # Mostrar un mensaje de desactivación exitosa
    messages.success(request, 'Cliente desactivado correctamente.')

    # Redireccionar al listado de clientes
    return redirect('cliente:listado_clientes')


def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            activo = form.cleaned_data['activo']
            
            cliente = Cliente(nombre=nombre, apellido=apellido, activo=activo)
            cliente.save()
            
            return redirect('cliente:listado_clientes')  # Redirige al listado de clientes después de guardar
            
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/nuevo_cliente.html', {'form': form})


from django.http import HttpResponseRedirect

def modificar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            # Actualizar más campos del cliente según sea necesario
            cliente.save()
            return HttpResponseRedirect(reverse('cliente:listado_clientes'))

    else:
        form = ClienteForm(initial={
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            # Cargar más campos del cliente en el formulario según sea necesario
        })

    return render(request, 'clientes/modificar_cliente.html', {'form': form})



