from django.shortcuts import render
from . import views
from django.http import HttpResponse, JsonResponse
from .models import PopulacaoUsuaria, Evolucao
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404


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
    
    usuario_id = json.loads(serializers.serialize('json', usuario))[0]['pk']
    
    evolucoes_json = json.loads(serializers.serialize('json', evolucoes))
    evolucoes_json = [{'fields': i['fields'], 'id': i['pk']} for i in evolucoes_json]
    
    data = {'usuario': usuario_json, 'evolucoes': evolucoes_json, 'usuario_id': usuario_id}

    print(evolucoes_json)
    return JsonResponse(data)

@csrf_exempt
def update_evolucao(request, id):
    demanda = request.POST.get('demanda')
    descricao = request.POST.get('descricao')

    evolucao = Evolucao.objects.get(id=id)
    list_evolucao = Evolucao.objects.filter(demanda=demanda).exclude(id=id)
    if list_evolucao.exists():
        return HttpResponse('Demanda já existente')
    
    evolucao.demanda = demanda
    evolucao.descricao = descricao
    evolucao.save()
    return HttpResponse('Dados alterados')

def excluir_evolucao(request, id):
    try:
        evolucao = Evolucao.objects.get(id=id)
        evolucao.delete()
        return redirect(reverse('usuarios')+f'?aba=att_usuario&id_usuario={id}')
    except:
        #TODO: exibir mensagem de erro
        return redirect(reverse('usuarios')+f'?aba=att_usuario&id_usuario={id}')

def update_usuario(request, id):
    body = json.loads(request.body)
    
    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']

    usuario = get_object_or_404(PopulacaoUsuaria, id=id)
    try:
        usuario.nome = nome
        usuario.sobrenome = sobrenome
        usuario.email = email
        usuario.cpf = cpf
        usuario.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:
        return JsonResponse({'status':'500'})

    return JsonResponse({'teste': 'teste'})