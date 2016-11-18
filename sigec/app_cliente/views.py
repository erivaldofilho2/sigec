# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import * 
from app_comum.forms import *
# Create your views here.

def clientes(request):
    clientes = Cliente.objects.all()    
    messages.add_message(
                request, messages.INFO, 'Erro no formulário! Verifique os campos destacados!')
    return render(request,'clientes.html',{
                'clientes': clientes,
                })


def add_cliente(request):
    
    if request.method == 'POST':
        if(request.POST.get('tipo_cliente') is not None and request.POST.get('tipo_cliente') == 'pf'):
            form_cliente = FormClientePF()            
        elif(request.POST.get('tipo_cliente') is not None and request.POST.get('tipo_cliente') == 'pj'):
            form_cliente = FormClientePJ()
        else:
            
            if(request.POST.get('cpf')):
                form_cliente = FormClientePF(request.POST or None)
            elif(request.POST.get('cnpj')):
                form_cliente = FormClientePJ(request.POST or None)                
            
            form_endereco = FormEndereco(request.POST or None)
            form_contato = FormContato(request.POST or None)
            
            if form_cliente.is_valid() and form_endereco.is_valid() and\
            form_contato.is_valid():
            
                cliente = form_cliente.save(commit=False)
                endereco = form_endereco.save(commit=True)
                contato = form_contato.save(commit=True)
                cliente.endereco = endereco
                cliente.contato = contato
                cliente.save()
                
                messages.add_message(
                    request, messages.INFO, 'Cliente PF adicionado')
                
                return HttpResponseRedirect('/clientes')
        
        form_endereco = FormEndereco()
        form_contato = FormContato()
        
        return render(request,'add_cliente.html',{
            'form_cliente': form_cliente,
            'form_endereco': form_endereco,
            'form_contato': form_contato
            
            })
    
    return render(request,'tipo_cliente.html',{})
    
    
def delete_cliente(request,id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.endereco.delete()
    cliente.contato.delete()
    cliente.delete()
    messages.add_message(
                request, messages.INFO, 'Cliente '+str(cliente)+' foi deleteado!')
    
    return HttpResponseRedirect('/clientes')
        