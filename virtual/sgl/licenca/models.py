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
    nome= models.CharField(max_length=100)
    cpf= models.CharField(max_length=11)
    dataAdmissao= models.DateTimeField('Data admissao')
    cargo= models.ForeignKey(Cargo, on_delete=models.CASCADE)
    setor= models.ForeignKey(Setor, on_delete=models.CASCADE)

class TipoLicenca(models.Model):
    nome= models.CharField(max_length= 50)
    descricao= models.CharField(max_length=200)
    dias= models.IntegerField()
    
