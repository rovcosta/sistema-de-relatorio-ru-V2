# Generated by Django 4.0.5 on 2022-07-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0006_alter_tableactionmodel_descricao_acao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tableeventmodel',
            old_name='instituiao_ofertante',
            new_name='instituicao_ofertante',
        ),
    ]
