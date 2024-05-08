from django.db.models import TextChoices

class ChoicesEtnia(TextChoices):
    BRANCO = "BRAN", "Branco"
    PRETO = "PRET", "Preto"
    PARDO = "PARD", "Pardo"
    INDIGENA = "INDI", "Indígena"
    AMARELO = "AMAR", "Amarelo"
    OUTROS = "OUTR", "Outros"

class ChoicesGenero(TextChoices):
    HOMEM_CIS = "HCIS", "Homem cisgênero"
    MULHER_CIS = "MCIS", "Mulher cisgênero"
    HOMEM_TRANS = "HTRA", "Homem transgênero"
    MULHER_TRANS = "MTRA", "Mulher transgênero"
    NAOBIN = "NBIN", "Pessoa não-binária"
    OUTROS = "OUTR", "Outros"

class ChoicesEstadoCivil(TextChoices):
    SOLTEIRO = "SOLT", "Solteiro"
    CASADO = "CASA", "Solteiro"
    DIVORCIADO = "DIVO", "Solteiro"
    VIUVO = "VIUV", "Solteiro"
    UNIAO_ESTAVEL = "UNES", "Solteiro"

class ChoicesEscolaridade(TextChoices):
    FUND_INCOMPLETO = "FUNI", "Ensino Fundamental Incompleto"
    FUND_COMPLETO = "FUNC", "Ensino Fundamental Completo"
    MEDIO_INCOMPLETO = "MEDI", "Ensino Médio Incompleto"
    MEDIO_COMPLETO = "MEDC", "Ensino Médio Completo"
    SUPERIOR_INCOMPLETO = "SUPI", "Ensino Superior Incompleto"
    SUPERIOR_COMPLETO = "SUPC", "Ensino Superior Completo"

class ChoicesTipoImovel(TextChoices):
    PROPRIO = "PRO", "Próprio"
    ALUGADO = "ALU", "Alugado"
    CESSAO = "CES", "Cessão"
    POSSE = "POS", "Posse"
    INVASAO = "INV", "Invasão"
    OUTRO = "OUT", "Outro"

class ChoicesMaterialImovel(TextChoices):
    ALVENARIA = "ALV", "Alvenaria"
    MADEIRA = "MAD", "Madeira"
    OUTROS = "OUT", "Outros"

class ChoicesCondicaoImovel(TextChoices):
    BOM = "BOM", "Bom"
    REGULAR = "REG", "Regular"
    RUIM = "RUI", "Ruim"