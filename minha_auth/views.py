from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
import logging

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)

        return HttpResponse('Usuário cadastrado com sucesso')



def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST["username"]
        senha = request.POST["password"]

        # Verifica se o username e senha foram fornecidos
        if not (username and senha):
            return render(request, 'login.html', {'error_message': 'Por favor, forneça um username e senha.'})

        user = authenticate(username=username, password=senha)

        # Verifica se o usuário existe e está ativo
        if user is not None:
            login_django(request, user)
            return render(request, 'home.html')  # Corrigido o retorno da renderização
        else:
            return render(request, 'login.html', {'error_message': 'E-mail ou senha inválidos.'})  # Corrigido o retorno da renderização

def home(request):
    return render(request, 'home.html')
