# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenca', '0003_auto_20161101_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='requerimentolicenca',
            name='statusLicenca',
            field=models.CharField(choices=[('AV', 'AVALIACAO'), ('RE', 'RECUSADA'), ('AP', 'APROVADA'), ('RV', 'REVOGADA')], default='AV', max_length=2),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='descricao',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='requerimentolicenca',
            name='dataRequisicao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='setor',
            name='descricao',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tipolicenca',
            name='descricao',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]