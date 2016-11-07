"""sigec URL Configuration
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]