"""sigec URL Configuration
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clientes, name='clientes'),
    url(r'^add_cliente$', views.add_cliente, name='add_cliente'),
    url(r'^(?P<id_cliente>\d+)/delete_cliente$', views.delete_cliente, name='delete_cliente'),
    url(r'^(?P<id_cliente>\d+)/info_cliente$', views.info_cliente, name='info_cliente'),
    url(r'^(?P<id_cliente>\d+)/edit_cliente$', views.edit_cliente, name='edit_cliente'),
]