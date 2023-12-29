from django.db import models

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


    # # Nome completo
    # nome_completo = models.CharField(max_length=100)

    # # Nome social (opcional)
    # nome_social = models.CharField(max_length=100, blank=True)

    # # NIS (Número de Identificação Social)
    # nis = models.CharField(max_length=11, unique=True)

    # # Data de nascimento
    # data_nascimento = models.DateField()

    # # Identidade de gênero
    # identidade_genero = models.CharField(max_length=20)

    # # Cor/Raça
    # cor_raca = models.CharField(max_length=20)

    # # Estado civil
    # estado_civil = models.CharField(max_length=20)

    # # Endereço
    # endereco = models.CharField(max_length=200)

    # # Telefone
    # telefone = models.CharField(max_length=15)

    # # Naturalidade
    # naturalidade = models.CharField(max_length=50)

    # # Tempo de residência no município (em meses)
    # tempo_residencia_municipio = models.PositiveIntegerField()

    # # RG (Registro Geral)
    # rg = models.CharField(max_length=20)

    # # Filiação
    # filiacao = models.CharField(max_length=100)

    # # CPF (Cadastro de Pessoas Físicas)
    # cpf = models.CharField(max_length=14, unique=True)

    # # Número da certidão de nascimento ou casamento
    # certidao_nascimento_casamento = models.CharField(max_length=20)

    # # Número do título de eleitor
    # titulo_eleitor = models.CharField(max_length=12, blank=True)

    # # Nível de escolaridade
    # nivel_escolaridade = models.CharField(max_length=50)

    # # Ocupação
    # ocupacao = models.CharField(max_length=50)

    # # Renda (em reais)
    # renda = models.DecimalField(max_digits=10, decimal_places=2)

    # # Esta pessoa vive em condições de extrema pobreza? Sim ou Não
    # extrema_pobreza = models.BooleanField()

    # # Esta é uma PcD (Pessoa com Deficiência)? Sim ou Não
    # pessoa_com_deficiencia = models.BooleanField()

    """ VINCULO_CHOICES = (
        ('Filho', 'Filho'),
        ('Pai', 'Pai'),
        ('Irmão', 'Irmão'),
        ('Tio', 'Tio'),
        ('Amigo', 'Amigo'),
        ('Companheiro', 'Companheiro'),
        ('Marido/esposa', 'Marido/esposa'),
        ('Outros', 'Outros'),
    )

    ESCOLARIDADE_CHOICES = (
        ('Ensino fundamental incompleto', 'Ensino fundamental incompleto'),
        ('Ensino fundamental completo', 'Ensino fundamental completo'),
        ('Ensino médio incompleto', 'Ensino médio incompleto'),
        ('Ensino médio completo', 'Ensino médio completo'),
        ('Ensino superior incompleto', 'Ensino superior incompleto'),
        ('Ensino superior completo', 'Ensino superior completo'),
    )

    cpf_populacao_usuaria = models.ForeignKey('PopulacaoUsuaria', on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nis = models.CharField(max_length=11)
    vinculo_parentesco = models.CharField(max_length=20, choices=VINCULO_CHOICES)
    escolaridade = models.CharField(max_length=50, choices=ESCOLARIDADE_CHOICES)
    ocupacao = models.CharField(max_length=50)
    renda = models.DecimalField(max_digits=10, decimal_places=2)

     TIPO_IMOVEL_CHOICES = (
        ('Próprio', 'Próprio'),
        ('Alugado', 'Alugado'),
        ('Cessão', 'Cessão'),
        ('Posse', 'Posse'),
        ('Invasão', 'Invasão'),
        ('Outro', 'Outro'),
    )

    MATERIAL_CHOICES = (
        ('Alvenaria', 'Alvenaria'),
        ('Madeira', 'Madeira'),
        ('Outro', 'Outro'),
    )

    ESTADO_CONSERVACAO_CHOICES = (
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    )

    SIM_NAO_CHOICES = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

    tipo_imovel = models.CharField(max_length=20, choices=TIPO_IMOVEL_CHOICES)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_comodos = models.PositiveIntegerField()
    material_paredes = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    material_piso = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    material_telhado = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    estado_conservacao = models.CharField(max_length=20, choices=ESTADO_CONSERVACAO_CHOICES)
    fornecimento_agua = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    fornecimento_energia = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    coleta_esgoto = models.CharField(max_length=3, choices=SIM_NAO_CHOICES)
    coleta_lixo = models.CharField(max_length=3, choices=SIM_NAO_CHOICES) """

