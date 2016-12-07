# -*- coding: utf-8 -*-
from django.shortcuts import render
from app_funcionario.models import *
# Create your views here.
from app_funcionario.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from app_comum.forms import *



def funcionarios(request):
    
    funcionarios = Funcionario.objects.all()    
    return render(request,'funcionarios.html',{
                'funcionarios': funcionarios,
                })
    
    
def add_funcionario(request):
    if request.method == 'POST':
        form_funcionario = FormFuncionario(request.POST, request.FILES)
        form_endereco = FormEndereco(request.POST)
        form_contato = FormContato(request.POST)
        form_user = FormUser(request.POST)
        
        if form_funcionario.is_valid() and form_endereco.is_valid() and form_contato.is_valid() and form_user.is_valid():
            funcionario = form_funcionario.save(commit=False)
            funcionario.endereco = form_endereco.save(commit=True)
            funcionario.contato = form_contato.save(commit=True)
            funcionario.user = form_user.save(commit=True)
            funcionario.save()
            
            messages.add_message(
                request, messages.INFO, 'Funcionario '+str(funcionario)+' adicionado')
            return HttpResponseRedirect('/funcionarios')
        else:
            return render(request, 'add_funcionario.html', {
            'form_funcionario':form_funcionario,
            'form_endereco':form_endereco,
            'form_contato':form_contato,
            'form_user': form_user
            })
        
        return HttpResponseRedirect('/funcionarios')
    else:
        form_funcionario = FormFuncionario()
        form_endereco = FormEndereco()
        form_contato = FormContato()
        form_user = FormUser()
        
        return render(request, 'add_funcionario.html', {
            'form_funcionario':form_funcionario,
            'form_endereco': form_endereco,
            'form_contato': form_contato,
            'form_user': form_user
            })



def info_funcionario(request, id_funcionario):
    funcionario = Funcionario.objects.get(id=id_funcionario)
    return render(request,'info_funcionario.html',{'funcionario':funcionario})


def delete_funcionario(request,id_funcionario):
    funcionario = Funcionario.objects.get(id=id_funcionario)
    funcionario.delete()
    messages.add_message(
                request, messages.INFO, 'Cliente '+str(funcionario)+' foi deleteado!')
    
    return HttpResponseRedirect('/funcionarios')


def edit_funcionario(request, id_funcionario):
    funcionario = Funcionario.objects.get(id=id_funcionario)
    if request.method == 'POST':
        form_funcionario = FormFuncionario(request.POST, request.FILES,instance=funcionario)
        form_endereco = FormEndereco(request.POST)
        form_contato = FormContato(request.POST)
        
        if form_funcionario.is_valid() and form_endereco.is_valid() and form_contato.is_valid():
            funcionario = form_funcionario.save(commit=False)
            funcionario.endereco = form_endereco.save(commit=True)
            funcionario.contato = form_contato.save(commit=True)
            funcionario.save()
            
            messages.add_message(
                request, messages.INFO, 'Funcionario '+str(funcionario)+' atualizado')
            
            return HttpResponseRedirect('/funcionarios/'+str(funcionario.id)+'/info_funcionario')
        else:
            return render(request, 'add_funcionario.html', {
            'form_funcionario':form_funcionario,
            'form_endereco':form_endereco,
            'form_contato':form_contato
            })
        
    else:
        form_funcionario = FormFuncionario(instance=funcionario)
        form_endereco = FormEndereco(instance=funcionario.endereco)
        form_contato = FormContato(instance=funcionario.contato)
        
        return render(request, 
                      'edit_funcionario.html',{
                          'form_funcionario':form_funcionario,
                          'form_endereco':form_endereco,
                          'form_contato':form_contato
                          })

    
    
    
    
    
    
    
    
    
    
