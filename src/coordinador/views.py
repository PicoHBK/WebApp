from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import CoordinadorForm
from .models import Coordinador





def listado_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    return render(request, 'coordinadores/listado.html', {'coordinadores': coordinadores})


def activar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)

    # Guardar el campo 'activo' en True
    coordinador.activo = True
    coordinador.save()

    # Mostrar un mensaje de activación exitosa
    messages.success(request, 'Coordinador activado correctamente.')

    # Comentar el redireccionamiento
    return redirect('coordinador:listado_coordinadores')

    # Comentar el return
    return HttpResponse('Empleado activado correctamente.')
    



def desactivar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)

    # Guardar el campo 'activo' en True
    coordinador.activo = False
    coordinador.save()

    # Mostrar un mensaje de activación exitosa
    messages.success(request, 'Coordinador desactivado correctamente.')

    # Comentar el redireccionamiento
    return redirect('coordinador:listado_coordinadores')

    # Comentar el return
    return HttpResponse('Empleado desactivado correctamente.')


def registrar_coordinador(request):
    if request.method == 'POST':
        form = CoordinadorForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            numero_documento = form.cleaned_data['numero_documento']
            fecha_alta = form.cleaned_data['fecha_alta']
            activo = form.cleaned_data['activo']
            
            # Crear un nuevo coordinador en la base de datos
            coordinador = Coordinador(
                nombre=nombre,
                apellido=apellido,
                numero_documento=numero_documento,
                fecha_alta=fecha_alta,
                activo=activo
            )
            coordinador.save()
            
            # Hacer algo después de guardar los datos, si es necesario
            
            # Redireccionar a una página de éxito o a otra vista
            return redirect('coordinador:listado_coordinadores')  # Cambia 'exito' por el nombre de tu vista o URL de éxito
    else:
        form = CoordinadorForm()
    
    return render(request, 'coordinadores/nuevo_coordinador.html', {'form': form})



from django.http import Http404
from .forms import CoordinadorForm
from .models import Coordinador

def actualizar_coordinador(request, pk):
    try:
        coordinador = get_object_or_404(Coordinador, id=pk)
    except Http404:
        coordinador = None

    if request.method == 'POST':
        form = CoordinadorForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos del formulario
            if coordinador is not None:
                coordinador.nombre = form.cleaned_data['nombre']
                coordinador.apellido = form.cleaned_data['apellido']
                coordinador.numero_documento = form.cleaned_data['numero_documento']
                coordinador.fecha_alta = form.cleaned_data['fecha_alta']
                coordinador.activo = form.cleaned_data['activo']
                coordinador.save()
                # Hacer algo después de guardar los cambios, como redireccionar a una página de éxito
                return redirect('coordinador:listado_coordinadores')
    else:
        initial_data = {
            'nombre': coordinador.nombre if coordinador else '',
            'apellido': coordinador.apellido if coordinador else '',
            'numero_documento': coordinador.numero_documento if coordinador else None,
            'fecha_alta': coordinador.fecha_alta if coordinador else None,
            'activo': coordinador.activo if coordinador else False
        }
        form = CoordinadorForm(initial=initial_data)
    
    return render(request, 'coordinadores/modificar_coordinador.html', {'form': form}) 


