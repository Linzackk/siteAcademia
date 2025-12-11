from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno, Instrutor
from .forms import AlunoForm, InstrutorForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'usuarios/home.html')

def is_staff(user):
    return user.is_staff

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

def registrar_aluno(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        plano = request.POST.get('plano')

        if form.is_valid():
            user = form.save()
            Aluno.objects.create(
                user=user,
                nome=nome,
                idade=idade,
                cpf=cpf,
                telefone=telefone,
                plano=plano
            )
            messages.success(request, 'Aluno cadastrado com Sucesso! Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados.')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registrar_aluno.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def registrar_instrutor(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        codigo_ef = request.POST.get('codigo_ef')
        
        if form.is_valid():
            user = form.save()
            Instrutor.objects.create(
                user=user,
                nome=nome,
                idade=idade,
                cpf=cpf,
                telefone=telefone,
                codigo_ef=codigo_ef
            )
            messages.success(request, 'Instrutor cadastrado com Sucesso! Faça login.')
            return redirect('listar_instrutores')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados.')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registrar_instrutor.html', {'form': form})
        
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

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Você saiu da sua conta com segurança.')
        return super().dispatch(request, *args, **kwargs)
    
def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da conta com segurança.')
    return redirect('home')

from django.contrib.auth.models import User
from django.http import HttpResponse

def criar_superusuario(request):
    if User.objects.filter(username="admin").exists():
        return HttpResponse("Superusuário já existe.")

    User.objects.create_superuser(
        username="admin",
        password=">-7I}5LF1Zde",
        email="admin@example.com"
    )
    
    return HttpResponse("Superusuário criado com sucesso!")