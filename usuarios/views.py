from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Academia do Zackinho!</h1><p>Minha primeira Página em Django!!!</p><h2>Hello, World!</h2>")
