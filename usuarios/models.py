from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    PLANO_CHOICES = [
        ('BASICO', 'Básico'),
        ('PREMIUM', 'Premium'),
        ('VIP', 'VIP'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, null=True, blank=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    plano = models.CharField(max_length=7, choices=PLANO_CHOICES, null=True, blank=True)
    
class Instrutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, null=True, blank=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    codigo_ef = models.CharField(max_length=7)