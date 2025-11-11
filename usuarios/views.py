from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno, Instrutor
from .forms import AlunoForm, InstrutorForm


def home(request):
    return render(request, 'usuarios/home.html')

def irParaCadastro(request):
    return render(request, 'usuarios/cadastrar_aluno.html')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada com Sucesso! Faça Login para acessar.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao criar a conta. Verifique os dados.')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registrar.html', {'form': form} )

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

@login_required
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'usuarios/listar_alunos.html', {'alunos': alunos})

@login_required
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
    instrutor = get_object_or_404(Instrutor, id=instrutor_id)
    instrutor.delete()
    return redirect('listar_instrutores')

