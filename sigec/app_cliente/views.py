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
            if(request.POST.get('cpf') is not None):
                form_cliente = FormClientePF(request.POST or None)
            elif(request.POST.get('cnpj') is not None):
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
                    request, messages.INFO, 'Cliente '+str(cliente)+' adicionado')
                
                return HttpResponseRedirect('/clientes')
            else:
                
                return render(request,'add_cliente.html',{
                    'form_cliente': form_cliente,
                    'form_endereco': form_endereco,
                    'form_contato': form_contato
                    })
        
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
    if(cliente.endereco is not None):
        cliente.endereco.delete()
    if(cliente.contato is not None):
        cliente.contato.delete()
    cliente.delete()
    messages.add_message(
                request, messages.INFO, 'Cliente '+str(cliente)+' foi deleteado!')
    
    return HttpResponseRedirect('/clientes')


def info_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    return render(request,'info_cliente.html',{'cliente':cliente})
        
def edit_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        if(request.POST.get('cpf') is not None):
            cliente = ClientePF.objects.get(id=id_cliente)
            form_cliente = FormClientePF(request.POST, instance=cliente)

        elif(request.POST.get('cnpj') is not None):
            cliente = ClientePJ.objects.get(id=id_cliente)
            form_cliente = FormClientePJ(request.POST, instance=cliente)                
        print form_cliente
        form_endereco = FormEndereco(request.POST, instance=cliente.endereco)
        form_contato = FormContato(request.POST, instance=cliente.contato)

        if form_cliente.is_valid() and form_endereco.is_valid() and\
        form_contato.is_valid():
        
            cliente = form_cliente.save(commit=False )
            endereco = form_endereco.save(commit=True)
            contato = form_contato.save(commit=True)
            cliente.endereco = endereco
            cliente.contato = contato
            cliente.save()
            
            messages.add_message(
                request, messages.INFO, 'Cliente '+str(cliente)+' atualizado')
            
            return HttpResponseRedirect('/clientes/'+str(cliente.id)+'/info_cliente') 
    else:
        try:
            if cliente.clientepf:
                cliente = ClientePF.objects.get(id=id_cliente)
                form_cliente = FormClientePF(instance=cliente)
                
        except:
            if cliente.clientepj:
                cliente = ClientePJ.objects.get(id=id_cliente)
                form_cliente = FormClientePJ(instance=cliente)
            else:
                messages.add_message(
                    request, messages.INFO,'Não foi possível criar o formulario do tipo PF ou PJ, contate o administrador')
                return HttpResponseRedirect('/clientes')
        
        form_endereco = FormEndereco(instance=cliente.endereco)
        form_contato = FormContato(instance=cliente.contato)
        
        return render(request, 
                      'edit_cliente.html',{
                          'form_cliente':form_cliente,
                          'form_endereco':form_endereco,
                          'form_contato':form_contato
                          })
        