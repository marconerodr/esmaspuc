from django.shortcuts import render
from . import views
from django.http import HttpResponse, JsonResponse
from .models import PopulacaoUsuaria, Evolucao
import re
from django.core import serializers
import json

# Create your views here.

def usuarios(request):
    if request.method == "GET":
        usuarios_list = PopulacaoUsuaria.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios_list})
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

def att_usuario(request):
    id_usuario = request.POST.get('id_usuario')
    usuario = PopulacaoUsuaria.objects.filter(id=id_usuario)
    usuario_json = json.loads(serializers.serialize('json', usuario))[0]['fields']
    return JsonResponse(usuario_json)