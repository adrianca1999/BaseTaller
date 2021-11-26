from django.shortcuts import redirect, render
from apps.componentes.models import Componentes
from apps.componentes.form import ComponenteForm

# Create your views here.

def index(request):
    componente = Componentes.objects.all()
    context = {'componentes': componente}
    return render (request,'componentes/index.html',context)

def componentesCreate(request):
    if(request.method == 'POST'):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('componentes:index')
    else:
        form = ComponenteForm()
        return render(request, 'componentes/formComponente.html', {'form': form})

def componentesEdit(request, id_componente):
    componente = Componentes.objects.get(pk=id_componente)
    if(request.method == 'GET'):
        form = ComponenteForm(instance=componente)
    else:
        form = ComponenteForm(request.POST, instance=componente)
        if form.is_valid():
            form.save()

        return redirect('componentes:index')

    return render(request, 'componentes/formComponente.html', {'form': form})
