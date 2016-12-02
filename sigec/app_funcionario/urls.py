"""sigec URL Configuration
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.funcionarios, name='funcionarios'),
    url(r'^add_funcionario$', views.add_funcionario, name='add_funcionario'),
    url(r'^(?P<id_funcionario>\d+)/delete_funcionario$', views.delete_funcionario, name='delete_funcionario'),
    url(r'^(?P<id_funcionario>\d+)/info_funcionario$', views.info_funcionario, name='info_funcionario'),
#     url(r'^(?P<id_funcionario>\d+)/edit_funcionario$', views.edit_funcionario, name='edit_funcionario'),
]