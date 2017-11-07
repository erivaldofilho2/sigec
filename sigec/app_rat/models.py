from __future__ import unicode_literals

from django.db import models
from app_comum.models import *
from app_cliente.models import *


# Create your models here.
class Atividade(models.Model)
    funcionario = models.ForeignKey(funcionario)

	descricao = models.CharField(max_length=255)
	data = models.DateField()

class Solucao(models.Model):
	    funcionario = models.ForeignKey(funcionario)

		descricao = models.CharField(max_length=255)
	data = models.DateField()
		


class Rat(models.Model):
    cliente = models.ForeignKey(Cliente)
    funcionario = models.ForeignKey(funcionario)
    data_abertura = models.DateField()
    data_fechamento = models.DateField()
    descricao = models.TextField()



