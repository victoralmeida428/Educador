from django.contrib import admin
from apps.professor.models import Professores

class ListaProfessores(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'email', 'nascimento']
    list_display_links = ['nome', 'matricula']
    list_per_page = 10
    search_fields = ['nome', 'matricula']

admin.site.register(Professores, ListaProfessores)
    
