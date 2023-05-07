from django.urls import path
from apps.educador.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('projeto', projeto, name='projeto'),
    path('contato', contato, name='contato'),
]