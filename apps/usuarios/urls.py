from django.urls import path
from apps.usuarios.views import *

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('cadastro', cadastro, name='cadastro'),
    path('recuperacao', recuperacao, name='recuperacao'),
    path('painel', painel, name='painel'),
]