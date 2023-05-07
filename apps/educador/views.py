from django.shortcuts import render
from apps.educador.formularios.forms import EnviarContato

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'educador/about.html')

def projeto(request):
    return render(request, 'educador/projeto.html')

def contato(request):
    if request.method == 'GET':
        form = EnviarContato()
        context = {'form': form}
        return render(request, 'educador/contato.html', context)
    else:
        form = EnviarContato(request.POST)
        if form.is_valid():
            context = {'form': EnviarContato()}
            return render(request, 'educador/contato.html', context)

        context = {'form':form}
        return render(request, 'educador/contato.html', context)