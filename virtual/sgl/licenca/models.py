from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

class Cargo(models.Model):
    nome= models.CharField(max_length= 50)
    descricao= models.CharField(max_length=200)

class Setor(models.Model):
    nome= models.CharField(max_length= 50)
    descricao= models.CharField(max_length=200)

class Funcionario(models.Model):
    nome= models.CharField(max_length= 100)
    cpf= models.CharField(max_length= 11)
    dataAdmissao= models.DateTimeField('Data admissao')
    cargo= models.ForeignKey(Cargo)
    setor= models.ForeignKey(Setor)

class TipoLicenca(models.Model):
    nome= models.CharField(max_length= 50)
    descricao= models.CharField(max_length= 200)
    dias= models.IntegerField()

class RequerimentoLicenca(models.Model):
    dataRequisicao= models.DateTimeField('Data de requisicao')
    funcionario= models.ForeignKey(Funcionario)
    tipoLicenca= models.ForeignKey(TipoLicenca)
    dataLicenca= models.DateTimeField('Data desejada')

class Recusa(models.Model):
    motivo= models.CharField(max_length= 200)
    data= models.DateTimeField('Data de recusa')
    requerimentoLicenca= models.ForeignKey(RequerimentoLicenca)

class Licenca(models.Model):
    dataDeferimento= models.DateTimeField('Data do deferimento')
    documento= models.CharField(max_length= 200)
    requerimentoLicenca= models.ForeignKey(RequerimentoLicenca)

class Revogacao(models.Model):
    data= models.DateTimeField('Data de revogacao')
    motivo= models.CharField(max_length= 200)
    documento= models.CharField(max_length= 200)
    licenca= models.ForeignKey(Licenca)
