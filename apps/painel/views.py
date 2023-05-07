from django.shortcuts import render
import re

def perfil(request):
    padrao = re.compile('[A-Za-z]')
    user = request.user
    if padrao.findall(str(user)):
        usuario = 'aluno'
    else:
        usuario = 'professor'
    
    context = {'usuario':usuario}
        
    
    return render(request, 'painel/conta.html', context)
    
