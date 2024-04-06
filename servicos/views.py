from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from .models import Servico, ServicoAdicional
from fpdf import FPDF
from io import BytesIO
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="minha_auth/login/")
def novo_servico(request):
    if request.method =="GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')
        else:
            return render(request, 'novo_servico.html', {'form': form})
        
@login_required(login_url="minha_auth/login/")
def listar_servico(request):
    if request.method == "GET":
        servicoss = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicoss})

@login_required(login_url="minha_auth/login/")
def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})

@login_required(login_url="minha_auth/login/")
def relatorio(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 10)

    pdf.set_fill_color(240,240,240)
    pdf.cell(35, 10, 'Usuário:', 1, 0, 'L', 1)
    pdf.cell(35, 10, f'{servico.usuario}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Evoluções', 1, 0, 'L', 1)

    categoria_beneficio = servico.categoria_beneficio.all()
    for i, beneficio in enumerate(categoria_beneficio):
        pdf.cell(0, 10, f'- {servico.titulo}', 1, 1, 'L', 1)
        if not i==len(categoria_beneficio) -1:
            pdf.cell(30, 10, '', 0, 0)
    
    pdf.cell(35, 10, 'Data de solicitação', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_solicitação}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Data de concessão', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_concessao}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Protocolo', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocolo}', 1, 1, 'L', 1)
    
    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"relatorio-{servico.protocolo}.pdf")

@login_required(login_url="minha_auth/login/")
def servico_adicional(request):
    identificador_servico = request.POST.get('identificador_servico')
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')

    servico_adicional = ServicoAdicional(titulo=titulo, descricao=descricao)
    servico_adicional.save()

    servico = Servico.objects.get(identificador=identificador_servico)
    servico.servicos_adicionais.add(servico_adicional)
    servico.save()

    return render(request, 'confirmacao.html', {'identificador_servico': identificador_servico})