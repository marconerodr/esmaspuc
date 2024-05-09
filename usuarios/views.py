from django.shortcuts import render
from . import views
from django.http import HttpResponse, JsonResponse
from .models import PopulacaoUsuaria, Evolucao, DadosPessoais, Residencia
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.

# Aqui, fazemos a conexão entre os campos do banco de dados e os campos na página Usuarios
@login_required(login_url="minha_auth/login/")
def usuarios(request):
    if request.method == "GET":
        usuarios_list = PopulacaoUsuaria.objects.all()
        dados_pessoais_list = DadosPessoais.objects.all()
        residencia_list = Residencia.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios_list, 'dados_pessoais': dados_pessoais_list, 'residencia': residencia_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        dia = request.POST.getlist('dia')
        demanda = request.POST.getlist('demanda')
        descricao = request.POST.getlist('descricao')

         # Obter os novos campos de entrada para os dados pessoais
        nome_social = request.POST.get('nome_social')
        nis = request.POST.get('nis')
        data_nascimento = request.POST.get('data_nascimento')
        identidade_genero = request.POST.get('identidade_genero')
        cor_raca = request.POST.get('cor_raca')
        estado_civil = request.POST.get('estado_civil')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        naturalidade = request.POST.get('naturalidade')
        tempo_residencia_municipio = request.POST.get('tempo_residencia_municipio')
        rg = request.POST.get('rg')
        certidao_nascimento_casamento = request.POST.get('certidao_nascimento_casamento')
        titulo_eleitor = request.POST.get('titulo_eleitor')
        nivel_escolaridade = request.POST.get('nivel_escolaridade')
        ocupacao = request.POST.get('ocupacao')
        renda = request.POST.get('renda')
        extrema_pobreza = request.POST.get('extrema_pobreza')
        pessoa_com_deficiencia = request.POST.get('pessoa_com_deficiencia')

        # Obter os campos para os dados da residência
        tipo_imovel = request.POST.get('tipo_imovel')
        valor_aluguel = request.POST.get('valor_aluguel')
        numero_comodos = request.POST.get('numero_comodos')
        material_paredes = request.POST.get('material_paredes')
        material_piso = request.POST.get('material_piso')
        material_telhado = request.POST.get('material_telhado')
        estado_conservacao = request.POST.get('estado_conservacao')
        fornecimento_agua = request.POST.get('fornecimento_agua')
        fornecimento_energia = request.POST.get('fornecimento_energia')
        coleta_esgoto = request.POST.get('coleta_esgoto')
        coleta_lixo = request.POST.get('coleta_lixo')
        
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

        dados_pessoais = DadosPessoais(
            nome_social=nome_social,
            nis=nis,
            data_nascimento=data_nascimento,
            identidade_genero=identidade_genero,
            cor_raca=cor_raca,
            estado_civil=estado_civil,
            endereco=endereco,
            telefone=telefone,
            naturalidade=naturalidade,
            tempo_residencia_municipio=tempo_residencia_municipio,
            rg=rg,
            certidao_nascimento_casamento=certidao_nascimento_casamento,
            titulo_eleitor=titulo_eleitor,
            nivel_escolaridade=nivel_escolaridade,
            ocupacao=ocupacao,
            renda=renda,
            extrema_pobreza=extrema_pobreza,
            pessoa_com_deficiencia=pessoa_com_deficiencia,
            usuario=populacaoUsuaria  # Associar os dados pessoais ao usuário criado
        )
        dados_pessoais.save()
        
        residencia = Residencia(
            tipo_imovel=tipo_imovel,
            valor_aluguel=valor_aluguel,
            numero_comodos=numero_comodos,
            material_paredes=material_paredes,
            material_piso=material_piso,
            material_telhado=material_telhado,
            estado_conservacao=estado_conservacao,
            fornecimento_agua=fornecimento_agua,
            fornecimento_energia=fornecimento_energia,
            coleta_esgoto=coleta_esgoto,
            coleta_lixo=coleta_lixo,
            usuario=populacaoUsuaria  # Associar a residência ao usuário criado
        )
        residencia.save()


        for dia, demanda, descricao in zip(dia, demanda, descricao):
            evolucao = Evolucao(dia=dia, demanda=demanda, descricao=descricao, usuario=populacaoUsuaria)
            evolucao.save()
         
        return HttpResponse('Usuário cadastrado com sucesso!')

# A função abaixo seleciona o usuário pela id, filtra no banco de dados as informações dele e retorna em formato json apenas as informações necessários. 
@login_required(login_url="minha_auth/login/")
def att_usuario(request):
    id_usuario = request.POST.get('id_usuario')
    usuario = PopulacaoUsuaria.objects.filter(id=id_usuario)
    evolucoes = Evolucao.objects.filter(usuario=usuario[0])
    dadospessoais = DadosPessoais.objects.filter(usuario=usuario[0])
    residencia = Residencia.objects.filter(usuario=usuario[0])
        
    usuario_json = json.loads(serializers.serialize('json', usuario))[0]['fields']

    usuario_id = json.loads(serializers.serialize('json', usuario))[0]['pk']
    
    evolucoes_json = json.loads(serializers.serialize('json', evolucoes))
    evolucoes_json = [{'fields': i['fields'], 'id': i['pk']} for i in evolucoes_json]

    dadospessoais_json = json.loads(serializers.serialize('json', dadospessoais))
    residencia_json = json.loads(serializers.serialize('json', residencia))

    dados_pessoais = {
    **dadospessoais_json[0]['fields'],  # Assumindo que dadospessoais_json é uma lista
    'id': dadospessoais_json[0]['pk']
    }

    residencia_campos = {
    **residencia_json[0]['fields'],
    'id': residencia_json[0]['pk']
    }
    
    data = {'usuario': usuario_json, 'evolucoes': evolucoes_json, 'usuario_id': usuario_id, 'dadospessoais': dados_pessoais, 'residencia': residencia_campos}

    # print(usuario_json, dados_pessoais, residencia_campos)
    return JsonResponse(data)


@login_required(login_url="minha_auth/login/")
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

@login_required(login_url="minha_auth/login/")
def excluir_evolucao(request, id):
    try:
        evolucao = Evolucao.objects.get(id=id)
        evolucao.delete()
        return redirect(reverse('usuarios')+f'?aba=att_usuario&id_usuario={id}')
    except:
        #TODO: exibir mensagem de erro
        return redirect(reverse('usuarios')+f'?aba=att_usuario&id_usuario={id}')

@login_required(login_url="minha_auth/login/")
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