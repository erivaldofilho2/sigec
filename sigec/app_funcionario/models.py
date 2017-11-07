from __future__ import unicode_literals

from django.db import models
from app_comum.models import *
from django.contrib.auth.models import User


# Create your models here.

class Funcionario(models.Model):
    user = models.OneToOneField(User,null=True,blank=True)
    cpf = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos',null=True,blank=True)
    data_entrada = models.DateField(null=True,blank=True)
    data_saida = models.DateField(null=True,blank=True)
    endereco = models.ForeignKey(Endereco, null=True,blank=True)
    contato = models.ForeignKey(Contato, null=True,blank=True)
    cargo = models.CharField(max_length=100)
    def __unicode__(self):
        return self.user.first_name or u''
