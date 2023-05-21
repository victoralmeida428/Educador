from django.shortcuts import render, redirect
from apps.usuarios.formularios.forms import *
from django.contrib import auth, messages
from apps.usuarios.models import Usuarios
from django.contrib.auth.models import User

def login(request):   
    if request.method == 'GET':
        form = Login()
        context = {
            'form': form
        }
        
        return render(request, 'usuarios/login.html', context)
    else:
        form = Login(request.POST)
        if form.is_valid():
            user = form.cleaned_data['login']
            senha = Usuarios.objects.filter(login=user).values()
            usuario = auth.authenticate(
                request,
                username=user,
                password=senha[0]['senha']
            )
            auth.login(request, usuario)

            messages.success(request, f'{user} Logado com sucesso')            
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'usuarios/login.html', context)
        

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

        return render(request, 'usuarios/cadastro.html', context)
    else:
        form = Cadastro(request.POST)
        if form.is_valid():
            form.save()
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            print(login, senha)
            usuario = User.objects.create_user(
                username=login,
                password=senha,
                email=email
            )
            usuario.save()
            messages.success(request, f'{login} cadastrado com sucesso') 
            return redirect ('index')
        else:
            context = {
                'form': form
                }
            return render(request, 'usuarios/cadastro.html', context)
        

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


def painel(request):
    padrao = re.compile('[A-Za-z]')
    user = request.user
    if padrao.findall(str(user)):
        usuario = 'aluno'
    else:
        usuario = 'professor'
    
    context = {'usuario':usuario}
    return render(request, 'usuarios/painel.html', context)