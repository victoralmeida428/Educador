from django.urls import path
from apps.painel.views import perfil

urlpatterns = [
    path('perfil', perfil, name='perfil'),
]
