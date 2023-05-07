from django import forms
from apps.professor.models import Professores

class Cadastro(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'value':''}))
    senha = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'value':''}))
    senha_conf = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'value':''}),
                                 label='Repetir senha')
    class Meta:
        model = Professores
        fields = '__all__'

class Login(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'value':''}))
    senha = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'value':''}))
    class Meta:
        model = Professores
        fields = ['matricula', 'senha']
