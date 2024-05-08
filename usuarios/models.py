from django.db import models
from .choices import ChoicesEtnia, ChoicesGenero, ChoicesEstadoCivil, ChoicesEscolaridade, ChoicesMaterialImovel, ChoicesTipoImovel, ChoicesCondicaoImovel

class PopulacaoUsuaria(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome

class Evolucao(models.Model):
    dia = models.DateTimeField(default='2023-12-18 12:00:00')
    demanda = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    usuario = models.ForeignKey(PopulacaoUsuaria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.demanda

class DadosPessoais(models.Model):
    nome_social = models.CharField(max_length=100, blank=True)
    nis = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    identidade_genero = models.CharField(max_length=4, choices=ChoicesGenero.choices)
    cor_raca = models.CharField(max_length=4, choices=ChoicesEtnia.choices)
    estado_civil = models.CharField(max_length=4, choices=ChoicesEstadoCivil.choices)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    naturalidade = models.CharField(max_length=50)
    tempo_residencia_municipio = models.PositiveIntegerField()
    rg = models.CharField(max_length=20)
    certidao_nascimento_casamento = models.CharField(max_length=20)
    titulo_eleitor = models.CharField(max_length=12, blank=True)
    nivel_escolaridade = models.CharField(max_length=4, choices=ChoicesEscolaridade.choices)
    ocupacao = models.CharField(max_length=50)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    extrema_pobreza = models.BooleanField(default=False)
    pessoa_com_deficiencia = models.BooleanField(default=False)
    usuario = models.ForeignKey(PopulacaoUsuaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nis

class Residencia(models.Model):
    tipo_imovel = models.CharField(max_length=4, choices=ChoicesTipoImovel.choices)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_comodos = models.PositiveIntegerField()
    material_paredes = models.CharField(max_length=4, choices=ChoicesMaterialImovel.choices)
    material_piso = models.CharField(max_length=4, choices=ChoicesMaterialImovel.choices)
    material_telhado = models.CharField(max_length=4, choices=ChoicesMaterialImovel.choices)
    estado_conservacao = models.CharField(max_length=4, choices=ChoicesCondicaoImovel.choices)
    fornecimento_agua = models.BooleanField(default=True)
    fornecimento_energia = models.BooleanField(default=True)
    coleta_esgoto = models.BooleanField(default=True)
    coleta_lixo = models.BooleanField(default=True)
    usuario = models.ForeignKey(PopulacaoUsuaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_imovel