from django.shortcuts import render
from . import views
from django.http import HttpResponse
from .models import PopulacaoUsuaria, Evolucao

# Create your views here.

def usuarios(request):
    if request.method == "GET":
<<<<<<< HEAD
        return render(request, 'usuarios.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        dia = request.POST.getlist('dia')
        demanda = request.POST.getlist('demanda')
        descricao = request.POST.getlist('descricao')

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
=======
    	return render(request, 'usuarios.html')
    elif request.method == "POST":
        nome = request.POST.get()
        sobrenome = request.POST.get()
>>>>>>> 35fdcea366f444effca808e33302d944599adb38
