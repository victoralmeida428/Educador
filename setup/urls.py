from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.educador.urls')),
    path('', include('apps.usuarios.urls')),
    path('', include('apps.professor.urls')),
]
