from django.db import models
from usuarios.models import PopulacaoUsuaria
from .choices import ChoicesCategoriaBeneficio
from datetime import datetime
from secrets import token_hex, token_urlsafe


# Create your models here.

class CategoriaBeneficio(models.Model):
    titulo = models.CharField(max_length=4, choices=ChoicesCategoriaBeneficio.choices)

    def __str__(self) -> str:
        return self.titulo

class ServicoAdicional(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.titulo



class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    usuario = models.ForeignKey(PopulacaoUsuaria, on_delete=models.SET_NULL, null=True)
    categoria_beneficio = models.ManyToManyField(CategoriaBeneficio)
    data_solicitação = models.DateField(null=True)
    data_concessao = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocolo = models.CharField(max_length=52, null=True, blank=True)
    identificador = models.CharField(max_length=24, null=True, blank=True)
    servicos_adicionais = models.ManyToManyField(ServicoAdicional)

    def __str__(self) -> str:
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime("%d/%m/%Y-%H:%M:%S-") + token_hex(16)
        
        if not self.identificador:
            self.identificador = token_urlsafe(16)

        super(Servico, self).save(*args, **kwargs)
