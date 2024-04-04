from django.db.models import TextChoices

class ChoicesCategoriaBeneficio(TextChoices):
    BENEFICIO = "BEN1", "Solicitação de benefício"
    ATENDIMENTO = "ATEN", "Atendimento do CRAS"
    ATIVIDADE = "ATIV", "Atividades do CRAS"