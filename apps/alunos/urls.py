from django.urls import path
from apps.alunos.views import ListaProfessor
urlpatterns = [
    path('lista_professores', ListaProfessor.as_view(), name='lista_professores'),
    path('buscar_prof', ListaProfessor.as_view(), name='buscar_prof'),
]