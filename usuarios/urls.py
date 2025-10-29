from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar_aluno', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastar_instrutor', views.cadastrar_instrutor, name='cadastrar_instrutor'),
    path('listar_alunos', views.listar_alunos,name ="listar_alunos"),
    path('listar_instrutores', views.listar_instrutores, name="listar_instrutores"),
    path('editar_aluno/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('editar_instrutor/<int:instrutor_id>/', views.editar_instrutor, name="editar_instrutor"),
    path('deletar_aluno/<int:aluno_id>/', views.deletar_aluno, name='deletar_aluno'),
    path('deletar_instrutor/<int:instrutor_id>/', views.deletar_instrutor, name='deletar_instrutor'),
]
