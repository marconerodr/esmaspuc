from django.shortcuts import render
from . import views
from django.http import HttpResponse
from .models import PopulacaoUsuaria, Evolucao
import re

# Create your views here.

def usuarios(request):
    if request.method == "GET":
        return render(request, 'usuarios.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        dia = request.POST.getlist('dia')
        demanda = request.POST.getlist('demanda')
        descricao = request.POST.getlist('descricao')
        
        testecpf = PopulacaoUsuaria.objects.filter(cpf=cpf)
        if testecpf.exists():
            return render(request, 'usuarios.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'evolucao': zip (dia, demanda, descricao)})
        
        if not re.fullmatch(re.compile(r'^(?:(?:(?:(?:(?:(\d)\1{2})\1{2})|(\d{3}))\.?){2}(\d{3})\-?(\d{2}))$'), cpf):
            return HttpResponse('CPF inválido')
            return render(request, 'usuarios.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'evolucao': zip (dia, demanda, descricao)})

        populacaoUsuaria = PopulacaoUsuaria(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        populacaoUsuaria.save()

        for dia, demanda, descricao in zip(dia, demanda, descricao):
            evolucao = Evolucao(dia=dia, demanda=demanda, descricao=descricao, usuario=populacaoUsuaria)
            evolucao.save()
         
        return HttpResponse('teste')
