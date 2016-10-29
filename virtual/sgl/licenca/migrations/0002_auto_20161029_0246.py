# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataDeferimento', models.DateTimeField(verbose_name='Data do deferimento')),
                ('documento', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recusa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=200)),
                ('data', models.DateTimeField(verbose_name='Data de recusa')),
            ],
        ),
        migrations.CreateModel(
            name='RequerimentoLicenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataRequisicao', models.DateTimeField(verbose_name='Data de requisicao')),
                ('dataLicenca', models.DateTimeField(verbose_name='Data desejada')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licenca.Funcionario')),
                ('tipoLicenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licenca.TipoLicenca')),
            ],
        ),
        migrations.CreateModel(
            name='Revogacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Data de revogacao')),
                ('motivo', models.CharField(max_length=200)),
                ('documento', models.CharField(max_length=200)),
                ('licenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licenca.Licenca')),
            ],
        ),
        migrations.AddField(
            model_name='recusa',
            name='requerimentoLicenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licenca.RequerimentoLicenca'),
        ),
        migrations.AddField(
            model_name='licenca',
            name='requerimentoLicenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licenca.RequerimentoLicenca'),
        ),
    ]