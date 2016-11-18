# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_comum.models import *

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, null=True,blank=True)
    contato = models.ForeignKey(Contato, null=True,blank=True)
    
class ClientePF(Cliente):
    cpf = models.CharField(max_length=14,blank=True)
    observacao = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.nome or u''
    
        
class ClientePJ(Cliente):
    razao = models.CharField(max_length=100)# Razão social da empresa
    responsavel = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    observacao = models.TextField()

    
    def __unicode__(self):
        return self.nome or u''