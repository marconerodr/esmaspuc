from django.shortcuts import render
from . import views
from django.http import HttpResponse, JsonResponse
from .models import PopulacaoUsuaria, Evolucao
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Aqui, fazemos a conexão entre os campos do banco de dados e os campos na página Usuarios
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
        
        # Aqui, testamos se o CPF inserido já existe no banco de dados e testamos se é um CPF válido, usando uma expressão regular, para poder salvar as alterações.
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

# A função abaixo seleciona o usuário pela id, filtra no banco de dados as informações dele e retorna em formato json apenas as informações necessários. 

def att_usuario(request):
    id_usuario = request.POST.get('id_usuario')
    usuario = PopulacaoUsuaria.objects.filter(id=id_usuario)
    evolucoes = Evolucao.objects.filter(usuario=usuario[0])
        
    usuario_json = json.loads(serializers.serialize('json', usuario))[0]['fields']
    evolucoes_json = json.loads(serializers.serialize('json', evolucoes))
    evolucoes_json = [{'fields': i['fields'], 'id': i['pk']} for i in evolucoes_json]
    
    data = {'usuario': usuario_json, 'evolucoes': evolucoes_json}

    print(evolucoes_json)
    return JsonResponse(data)

@csrf_exempt
def update_evolucao(request, id):
    demanda = request.POST.get('demanda')
    descricao = request.POST.get('descricao')

    evolucao = Evolucao.objects.get(id=id)
    list_evolucao = Evolucao.objects.filter(demanda=demanda)
    if list_evolucao.exists():
        return HttpResponse('Demanda já existente')
    return HttpResponse('Dados alterados com sucesso')
