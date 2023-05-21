from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Empleado

def activar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    # Guardar el campo 'activo' en True
    empleado.activo = True
    empleado.save()

    # Mostrar un mensaje de activación exitosa
    messages.success(request, 'Empleado activado correctamente.')

    # Comentar el redireccionamiento
    return redirect('empleado:listado_empleados')

    # Comentar el return
    return HttpResponse('Empleado activado correctamente.')
    

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from .models import Empleado

def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    # Guardar el campo 'activo' en False
    empleado.activo = False
    empleado.save()

    # Mostrar un mensaje de desactivación exitosa
    messages.success(request, 'Empleado desactivado correctamente.')

    # Redireccionar al listado de empleados
    return redirect('empleado:listado_empleados')




def listado_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/listado.html', {'empleados': empleados})



from .forms import EmpleadoForm


def nuevo_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            # Guardar los datos del empleado en la base de datos
            empleado = Empleado(nombre=form.cleaned_data['nombre'], apellido=form.cleaned_data['apellido'], numero_legajo=form.cleaned_data['numero_legajo'])
            empleado.save()
            return redirect('empleado:listado_empleados')
    else:
        form = EmpleadoForm()
    
    return render(request, 'empleados/nuevo_empleado.html', {'form': form})




def modificar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)  # Obtener el objeto Empleado a editar
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            # Actualizar los datos del empleado en la base de datos
            empleado.nombre = form.cleaned_data['nombre']
            empleado.apellido = form.cleaned_data['apellido']
            empleado.numero_legajo = form.cleaned_data['numero_legajo']
            empleado.save()
            return redirect('empleado:listado_empleados')
    else:
        # Rellenar el formulario con los datos actuales del empleado
        form = EmpleadoForm(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'numero_legajo': empleado.numero_legajo})
    
    return render(request, 'empleados/modificar_empleado.html', {'form': form})









