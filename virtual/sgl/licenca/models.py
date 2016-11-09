from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from const import *
from django.contrib.auth.models import User

class Cargo(models.Model):
    nome= models.CharField(max_length= 50)
    descricao= models.CharField(max_length=200, blank = True)

    def __str__(self):
    	return '{0}'.format(self.nome)

class Setor(models.Model):
    nome= models.CharField(max_length= 50)
    descricao= models.CharField(max_length=200, blank = True)

    def __str__(self):
		return '{0}'.format(self.nome)

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    nome= models.CharField(max_length= 100)
    cpf= models.CharField(max_length= 11)
    dataAdmissao= models.DateField('Data admissao')

    def __str__(self):
		return '{0}'.format(self.nome)


class Funcionario_Cargo(models.Model):
    funcionario = models.ForeignKey(Funcionario)
    cargo = models.ForeignKey(Cargo)
    dataInicio = models.DateField('Data de Inicio')
    dataTermino = models.DateField('Data de Termino')


class Funcionario_Setor(models.Model):
    funcionario = models.ForeignKey(Funcionario)
    setor = models.ForeignKey(Setor)
    dataInicio = models.DateField('Data de Inicio')
    dataTermino = models.DateField('Data de Termino')


class TipoLicenca(models.Model):
    nome= models.CharField(max_length= 50)
    descricao= models.CharField(max_length= 200, blank = True)
    dias= models.IntegerField()

    def __str__(self):
		return '{0}'.format(self.nome)

class RequerimentoLicenca(models.Model):

    dataRequisicao= models.DateField(auto_now =True)
    funcionario= models.ForeignKey(Funcionario)
    tipoLicenca= models.ForeignKey(TipoLicenca)
    dataLicenca= models.DateField('Data desejada')
    status = models.CharField(max_length = 2, choices = STATUS_LICENCA, default = 'AV')

    def __str__(self):
		return '{0} - {1}'.format(self.funcionario, self.dataRequisicao)


class Recusa(models.Model):
    motivo= models.CharField(max_length= 200)
    data= models.DateField('Data de recusa')
    requerimentoLicenca= models.ForeignKey(RequerimentoLicenca)

class Licenca(models.Model):
    dataDeferimento= models.DateField('Data do deferimento')
    documento= models.CharField(max_length= 200)
    requerimentoLicenca= models.ForeignKey(RequerimentoLicenca)


class Revogacao(models.Model):
    data= models.DateField('Data de revogacao')
    motivo= models.CharField(max_length= 200)
    documento= models.CharField(max_length= 200)
    licenca= models.ForeignKey(Licenca)
