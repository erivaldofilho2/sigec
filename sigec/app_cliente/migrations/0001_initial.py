# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_comum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientePF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('observacao', models.TextField(blank=True)),
                ('contato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_comum.Contato')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_comum.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='ClientePJ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('razao', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=14)),
                ('observacao', models.TextField()),
                ('contato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_comum.Contato')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_comum.Endereco')),
            ],
        ),
    ]
