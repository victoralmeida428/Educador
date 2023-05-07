from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from apps.professor.formularios.forms import *
from apps.professor.models import Professores
from apps.usuarios.formularios.forms import Recuperacao

def login(request):   
    if request.method == 'GET':
        form = Login()
        context = {
            'form': form
        }
        
        return render(request, 'professor/login.html', context)
    else:
        form = Login(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data['matricula']
            senha = Professores.objects.filter(matricula=matricula).values()
            usuario = auth.authenticate(
                request,
                username=matricula,
                password=senha[0]['senha']
            )
            auth.login(request, usuario)

            messages.success(request, f'{matricula} Logado com sucesso')            
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'professor/login.html', context)
        

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect('login')

def cadastro(request):
    if request.method == 'GET':
        form = Cadastro()
        context = {
            'form': form
        }

        return render(request, 'professor/cadastro.html', context)
    else:
        form = Cadastro(request.POST)
        if form.is_valid():
            form.save()
            matricula = form.cleaned_data['matricula']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            usuario = User.objects.create_user(
                username=matricula,
                password=senha,
                email=email
            )
            usuario.save()
            messages.success(request, f'{matricula} cadastrado com sucesso') 
            return redirect ('index')
        else:
            context = {
                'form': form
                }
            return render(request, 'professor/cadastro.html', context)
        

def recuperacao(request):
    if request.method == 'GET':
        form = Recuperacao()
        context = {'form': form}
        return render(request, 'usuarios/recuperacao.html', context)
    else:
        form = Recuperacao(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            messages.success(request, f'Foi enviado um email de recuperação para o {email}')
            return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'usuarios/recuperacao.html', context)

