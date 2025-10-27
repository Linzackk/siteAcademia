from django.shortcuts import render
from .models import Aluno


def home(request):
    # Exemplo de Dados Dinâmicos (mudam com as informações)
    alunos = Aluno.objects.all()
    return render(request, 'usuarios/home.html', {'alunos': alunos})
