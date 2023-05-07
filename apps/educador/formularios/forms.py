from django import forms
from apps.usuarios.models import Usuarios
import re

class EnviarContato(forms.Form):
    email = forms.EmailField(max_length=50, required=True,
                             widget=forms.EmailInput(attrs=({'placeholder':'email@dominio.com'})))
    nome = forms.CharField(max_length=50, required=True)
    mensagem = forms.CharField(max_length=1000, required=True, widget=(forms.Textarea()))
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        padrao = re.compile('\d')
        if len(padrao.findall(nome))>0:
            raise forms.ValidationError('Somente Letras')
        return nome