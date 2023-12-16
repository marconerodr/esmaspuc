from django.shortcuts import render
from . import views
from django.http import HttpResponse

# Create your views here.

def usuarios(request):
    if request.method == "GET":
    	return render(request, 'usuarios.html')
    elif request.method == "POST":
        nome = request.POST.get()
        sobrenome = request.POST.get()