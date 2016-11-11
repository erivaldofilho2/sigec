# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import * 
from app_comum.forms import *
# Create your views here.

def clientes(request):
    clientes = ClientePF.objects.all()
    template = loader.get_template('clientes.html')
    context = RequestContext(request, {'clientes': clientes})
    return HttpResponse(template.render(context))


def add_cliente(request):
    
    if request.method == 'POST':
        form_clientePF = FormClientePF(request.POST or None)
        form_endereco = FormEndereco(request.POST or None)
        form_contato = FormContato(request.POST or None)
        
        if form_clientePF.is_valid() and form_endereco.is_valid() and\
        form_contato.is_valid():
        
            cliente = form_clientePF.save(commit=False)
            endereco = form_endereco.save(commit=False)
            contato = form_contato.save(commit=False)
            
            messages.add_message(
                request, messages.INFO, 'Cliente PF adicionado')
            
            return render(request,'clientes.html',{
                'cliente': cliente,
                'endereco': endereco,
                'contato': contato
                })
        else:
            messages.add_message(
                request, messages.INFO, 'Erro no formulário! Verifique os campos destacados!')
            
            return render(request,'add_cliente.html',{
                'form_clientePF': form_clientePF,
                'form_endereco': form_endereco,
                'form_contato': form_contato
                })
        
    
    form_clientePF = FormClientePF()
    form_endereco = FormEndereco()
    form_contato = FormContato()
    
    return render(request,'add_cliente.html',{
        'form_clientePF': form_clientePF,
        'form_endereco': form_endereco,
        'form_contato': form_contato
        
        })