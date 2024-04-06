from django.contrib import admin
from .models import CategoriaBeneficio, Servico, ServicoAdicional

# Register your models here.

admin.site.register(CategoriaBeneficio)
admin.site.register(Servico)
admin.site.register(ServicoAdicional)