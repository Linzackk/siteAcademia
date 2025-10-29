from django import forms
from .models import Aluno, Instrutor

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'cpf', 'telefone', 'plano']
        
class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome', 'idade', 'cpf', 'telefone', 'codigo_ef']