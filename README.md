# Academia em Django — Sistema de Gestão de Academia
Site desenvolvido com Django e hospedado no Render, permitindo o gerenciamento completo de alunos e instrutores.

## Demonstração
Projeto online: https://siteacademia.onrender.com

---

## Sobre o Projeto

Este projeto consiste em um sistema web para uma academia, onde é possível realizar:

- CRUD completo de Alunos
- CRUD completo de Instrutores (somente superusuários podem criar instrutores)
- Login e Logout de usuários
- Listagem detalhada de todos os usuários
- Painel administrativo para superadmins
- Deploy final utilizando Render

A estilização do front-end foi feita utilizando **Bootstrap 5**, garantindo responsividade e uma interface organizada.

---

## Tecnologias Utilizadas

- Python 3.x  
- Django 5  
- HTML5 / CSS3  
- Bootstrap 5  
- SQLite (para desenvolvimento)  
- Render (deploy)  

---

## Testes Unitários

O projeto inclui testes criados com o framework de testes padrão do Django, cobrindo:

- Criação de usuários  
- Autenticação (login e logout)  
- Permissões (restrição para criação de instrutores)  
- Funcionamento das views principais
- Resposta das rotas e templates  

## Contas para Teste

Use as seguintes contas para explorar o sistema online:

### ADMIN

Usuário: admin

Senha: >-7I}5LF1Zde

### Aluno

Usuário: JoaoCarlos

Senha: 123

### Instrutor

Usuário: PedroHenrique

Senha: 123

## Como Rodar Localmente

```

git clone <URL do repositório>
cd nome-do-projeto
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

## Estrutura Geral do Projeto

```

projeto/
│── academiasite/
│── app/
│── templates/
│── static/
│── tests/
│── manage.py

```

## Contribuições

Contribuições são bem-vindas. Para sugerir melhorias, abra uma issue ou envie um pull request.
