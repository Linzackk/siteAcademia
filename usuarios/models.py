from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    curso = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome