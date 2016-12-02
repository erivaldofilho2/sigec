from django import forms
from django.forms import ModelForm, URLInput, TextInput, Select, EmailInput, DateInput, NumberInput, Textarea, FileInput
from .models import *
from app_comum.forms import *

class FormFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome','cpf','foto']
         
        widgets = {
            'nome': TextInput({'class':'form-control'}),
            'cpf': TextInput({'class':'form-control'}),
            'foto': FileInput({'class':'form-control'}),
            }
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