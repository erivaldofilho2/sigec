from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos')
    def __unicode__(self):
        return self.nome or u''
