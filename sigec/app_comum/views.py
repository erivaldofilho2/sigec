# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth

from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = password = request.POST.get('senha')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            if usuario.is_active:
                login_auth(request, usuario)                
                if usuario.has_perm('lrh.secretaria'):
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/colaboradores/info')
            else:
                mensagem = 'Usuário desabilitado, '\
                           'contate o Administrador do sistema.'
                template = loader.get_template('login.html')
                context = RequestContext(request, {'mensagem': mensagem})
                return HttpResponse(template.render(context))
        else:
            mensagem = 'Usuário ou senha inválido.'
            template = loader.get_template('login.html')
            context = RequestContext(request, {'mensagem': mensagem})
            return HttpResponse(template.render(context))

    else:
        context = RequestContext(request)
        return HttpResponse(template.render(context))


def logout(request):
    logout_auth(request)
    return HttpResponseRedirect('/login')


@login_required(login_url='/login')
def home(request):
    template = loader.get_template('home.html')
    context = RequestContext(request, {'chave': 'valor'})
    return HttpResponse(template.render(context))