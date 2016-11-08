# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_comum.models import *

# Create your models here.


class ClientePF(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    endereco = models.ForeignKey(Endereco, null=True,blank=True)
    contato = models.ForeignKey(Contato, null=True,blank=True)
    observacao = models.TextField()
    
    def __unicode__(self):
        return self.nome or u''
    
        
class ClientePJ(models.Model):
    nome = models.CharField(max_length=100) #Nome fantasia da empresa
    razao = models.CharField(max_length=100)# Razão social da empresa
    responsavel = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    endereco = models.ForeignKey(Endereco, null=True,blank=True)
    contato = models.ForeignKey(Contato, null=True,blank=True)
    observacao = models.TextField()

    
    def __unicode__(self):
        return self.nome or u''