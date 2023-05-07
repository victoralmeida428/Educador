from django.urls import path
from apps.professor.views import *

urlpatterns = [
    path('login_prof', login, name='login_prof'),
    path('cadastro_prof', cadastro, name='cadastro_prof'),
    path('recuperacao', recuperacao, name='recuperacao'),
]