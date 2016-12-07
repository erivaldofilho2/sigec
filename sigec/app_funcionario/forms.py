from django import forms
from django.forms import ModelForm, URLInput, TextInput, Select, EmailInput, DateInput, NumberInput, Textarea, FileInput
from .models import *
from app_comum.forms import *
from django.contrib.auth.models import User


class FormFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['cpf','foto','data_entrada','data_saida']
         
        widgets = {
#             'nome': TextInput({'class':'form-control'}),
            'cpf': TextInput({'class':'form-control'}),
            'foto': FileInput({'class':'form-control'}),
            }
        

class FormUser(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password']
# 
# 
# class FormClientePJ(ModelForm):
#     tipo = 'pj'
#     class Meta:
#         model = ClientePJ
#         fields = ['nome','razao','responsavel','cnpj','observacao']
#         
#         widgets = {
#             'nome': TextInput({'class':'form-control'}),
#             'razao': TextInput({'class':'form-control'}),
#             'responsavel': TextInput({'class':'form-control'}),
#             'cnpj': TextInput({'class':'form-control'}),
#             'observacao': Textarea({'class':'form-control'}),
#             }