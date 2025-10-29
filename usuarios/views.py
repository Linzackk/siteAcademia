from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Instrutor
from .forms import AlunoForm, InstrutorForm


def home(request):
    # Exemplo de Dados Dinâmicos (mudam com as informações)
    alunos = Aluno.objects.all()
    return render(request, 'usuarios/home.html', {'alunos': alunos})

def irParaCadastro(request):
    return render(request, 'usuarios/cadastrar_aluno.html')

def cadastrar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlunoForm()
        
    return render(request, 'usuarios/cadastrar_aluno.html', {'form': form})

def cadastrar_instrutor(request):
    if request.method == "POST":
        form = InstrutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InstrutorForm()
        
    return render(request, 'usuarios/cadastrar_instrutor.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'usuarios/listar_alunos.html', {'alunos': alunos})

def listar_instrutores(request):
    instrutores = Instrutor.objects.all()
    return render(request, 'usuarios/listar_instrutores.html', {'instrutores': instrutores})

def editar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'usuarios/editar_aluno.html', {'form': form})

def editar_instrutor(request, instrutor_id):
    instrutor = get_object_or_404(Instrutor, id=instrutor_id)
    
    if request.method == "POST":
        form = InstrutorForm(request.POST, instance=instrutor)
        if form.is_valid():
            form.save()
            return redirect('listar_instrutores')
    else:
        form = InstrutorForm(instance=instrutor)
    return render(request, 'usuarios/editar_instrutor.html', {'form': form})

def deletar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    aluno.delete()
    return redirect('listar_alunos')

def deletar_instrutor(request, instrutor_id):
    instrutor = get_object_or_404(Instrutor, instrutor_id)
    instrutor.delete()
    return redirect('listar_instrutores')

