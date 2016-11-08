# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Endereco(models.Model):
    endereco = models.CharField(max_length=100,blank=True)
    numero = models.DecimalField(max_digits = 5, decimal_places=0)
    complemento = models.CharField(max_length=100,blank=True)
    bairro = models.CharField(max_length=50,blank=True)
    cidade = models.CharField(max_length=50,blank=True)
    estado = models.CharField(max_length=50,blank=True)
    cep = models.CharField(max_length=10,blank=True)
    
    def __unicode__(self):
        return self.endereco or u''
    

class Contato(models.Model):
    tel_fixo = models.CharField(max_length=13,blank=True)
    tel_celular = models.CharField(max_length=14,blank=True)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.email or u''
    