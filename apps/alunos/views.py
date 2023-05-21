from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from apps.professor.models import Professores
from django.db.models import Q


class ListaProfessor(ListView):
    context_object_name = "professores"
    template_name='alunos/buscar_prof.html'
    queryset = Professores.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = 'aluno'
        return context
    
    def get_queryset(self):
        if len(self.request.GET)>0:
            self.queryset = self.queryset.filter(Q(nome__icontains=self.request.GET['nome'])|
                                                 Q(escola__icontains=self.request.GET['nome'])|
                                                 Q(matricula__icontains=self.request.GET['nome']))
        
        return self.queryset

# Create your views here.
