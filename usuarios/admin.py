from django.contrib import admin
from .models import PopulacaoUsuaria, Evolucao, DadosPessoais, Residencia

# Register your models here.

admin.site.register(PopulacaoUsuaria)
admin.site.register(Evolucao)
admin.site.register(DadosPessoais)
admin.site.register(Residencia)