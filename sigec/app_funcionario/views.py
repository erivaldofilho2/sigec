# -*- coding: utf-8 -*-
from django.shortcuts import render
from app_funcionario.models import *
# Create your views here.
from app_funcionario.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages



def funcionarios(request):
    
    funcionarios = Funcionario.objects.all()    
    return render(request,'funcionarios.html',{
                'funcionarios': funcionarios,
                })
    
    
def add_funcionario(request):
    if request.method == 'POST':
        form_funcionario = FormFuncionario(request.POST, request.FILES)
        if form_funcionario.is_valid():
            funcionario = form_funcionario.save(commit=True)
            form_funcionario.save()
#             funcionario.save()
            messages.add_message(
                request, messages.INFO, 'Funcionario '+str(funcionario)+' adicionado')
            return HttpResponseRedirect('/funcionarios')
        else:
            return render(request, 'add_funcionario.html', {
            'form_funcionario':form_funcionario,
            })
        
        return HttpResponseRedirect('/funcionarios')
    else:
        form_funcionario = FormFuncionario()
        return render(request, 'add_funcionario.html', {
            'form_funcionario':form_funcionario,
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
    