# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 15:01
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
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClientePF',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_cliente.Cliente')),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('observacao', models.TextField(blank=True)),
            ],
            bases=('app_cliente.cliente',),
        ),
        migrations.CreateModel(
            name='ClientePJ',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_cliente.Cliente')),
                ('razao', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=14)),
                ('observacao', models.TextField()),
            ],
            bases=('app_cliente.cliente',),
        ),
        migrations.AddField(
            model_name='cliente',
            name='contato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_comum.Contato'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_comum.Endereco'),
        ),
    ]
