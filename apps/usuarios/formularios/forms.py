from django import forms
from apps.usuarios.models import Usuarios
import re

class Login(forms.Form):
    login = forms.CharField(max_length=50, required=True)
    senha = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
    
    def clean_login(self):
        login = self.cleaned_data.get('login')
        banco = Usuarios.objects.filter(login=login).values()
        if len(banco) == 0:
            raise forms.ValidationError('Usuário não existe')
        return login

    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        login = self.cleaned_data.get('login')
        banco = Usuarios.objects.filter(login=login).values()
        if len(banco) == 0:
            return senha
        if banco[0]['senha'] != senha:
            raise forms.ValidationError('Senha incorreta')
        return senha
    
class Cadastro(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    senha_conf = forms.CharField(widget=forms.PasswordInput, required=True)
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Usuarios
        fields = '__all__'

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        padrao = re.compile('\d')
        if len(padrao.findall(nome))>0:
            raise forms.ValidationError('Somente Letras')
        return nome
    
    def clean_senha_conf(self):
        senha = self.cleaned_data['senha']
        senha2 = self.cleaned_data['senha_conf']
        if senha!=senha2:
            raise forms.ValidationError('Senhas não coincidem')
        return senha2
    
    def clean_login(self):
        login = self.cleaned_data['login']
        padrao = re.compile('[A-ZA-z]')
        erro = re.compile('[À-Úà-ú]')
        if erro.findall(login):
            raise forms.ValidationError('Não é permitido caracteres acentuações')
        elif not padrao.findall(login):
            raise forms.ValidationError('não é permitido apenas valores numérico')           
        else:
            return login
    
class Recuperacao(forms.Form):
    email = forms.EmailField(max_length=50, required=True)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        banco = Usuarios.objects.filter(email=email).values()
        if not banco:
            raise forms.ValidationError('Email não cadastrado')
        
        return email
        

