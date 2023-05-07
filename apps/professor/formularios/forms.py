from django import forms
from apps.professor.models import Professores

class Cadastro(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'value':''}))
    senha = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'value':''}))
    senha_conf = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'value':''}),
                                 label='Repetir senha')
    nascimento = forms.CharField(widget=forms.DateInput(attrs=({'type':'date'})))
    class Meta:
        model = Professores
        fields = '__all__'

    def clean_senha_conf(self):
        senha = self.cleaned_data['senha']
        senha2 = self.cleaned_data['senha_conf']
        if senha != senha2:
            raise forms.ValidationError('Senhas não coincidem')
        return senha2

class Login(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'value':''}))
    senha = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'value':''}))
    class Meta:
        model = Professores
        fields = ['matricula', 'senha']
