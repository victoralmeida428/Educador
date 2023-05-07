from django.db import models

# Create your models here.

class Professores(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    escola = models.CharField(max_length=100, blank=False, null=False)
    matricula = models.CharField(max_length=20, blank=False, null=False, default='0000000')
    senha = models.CharField(max_length=20, blank=False, null=False, default='123456')
    senha_conf = models.CharField(max_length=20, blank=False, null=False, default='123456')
    email = models.EmailField(blank=False, null=False)
    nascimento = models.DateField(blank=False, null=False)

