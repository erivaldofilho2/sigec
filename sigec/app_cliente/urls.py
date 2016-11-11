"""sigec URL Configuration
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clientes, name='clientes'),
    url(r'^add_cliente$', views.add_cliente, name='add_cliente'),
]