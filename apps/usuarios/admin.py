from django.contrib import admin
from apps.usuarios.models import Usuarios
class ListaUsuarios(admin.ModelAdmin):
    list_display = ('nome', 'login', 'email', 'nascimento')
    list_display_links = ('nome', 'login')
    list_filter = ('login', 'email')
    search_fields = ('login', 'email')

admin.site.register(Usuarios, ListaUsuarios)

