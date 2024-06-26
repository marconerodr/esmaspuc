# Generated by Django 5.0 on 2024-04-04 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_evolucao_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaBeneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('BPC1', 'Solicitação de Benefício de Prestação Continuada'), ('CAD1', 'Inserção no CadÚnico'), ('CAD2', 'Atualização do CadÚnico'), ('FUNE', 'Solicitação de auxílio funeral'), ('ALIM', 'Solicitação de auxílio alimentação'), ('BOLS', 'Solicitação de Bolsa Família'), ('INCL', 'Participação em oficina do CIP'), ('SCFV', 'Participação em oficina do SCFV'), ('IDOS', 'Participação em grupo de idosos'), ('INFO', 'Utilização do Telecentro'), ('PAIF', 'Atendimento do PAIF'), ('PARC', 'Participação em parcerias com setor privado')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('data_solicitação', models.DateField(null=True)),
                ('data_concessao', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('protocolo', models.CharField(blank=True, max_length=32, null=True)),
                ('categoria_beneficio', models.ManyToManyField(to='servicos.categoriabeneficio')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.populacaousuaria')),
            ],
        ),
    ]
