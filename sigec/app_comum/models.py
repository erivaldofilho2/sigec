# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Endereco(models.Model):
    endereco = models.CharField(max_length=100)
    numero = models.DecimalField(max_digits = 5, decimal_places=0, blank=True, null=True)
    complemento = models.CharField(max_length=100,blank=True, null=True)
    bairro = models.CharField(max_length=50,blank=True, null=True)
    cidade = models.CharField(max_length=50,blank=True, null=True)
    estado = models.CharField(max_length=50,blank=True, null=True)
    cep = models.CharField(max_length=10,blank=True, null=True)
    
    def __unicode__(self):
        return self.endereco or u''
    

class Contato(models.Model):
    tel_fixo = models.CharField(max_length=13,blank=True, null=True)
    tel_celular = models.CharField(max_length=14)
    email = models.EmailField(null=True)
    
    def __unicode__(self):
        return self.email or u''
    