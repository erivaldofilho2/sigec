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
            'data_entrada': TextInput({'class':'form-control'}),
            'data_saida': TextInput({'class':'form-control'}),
            }
        

class FormUser(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password']
        
        widgets = {
                'first_name': TextInput({'class':'form-control'}),
                'last_name': TextInput({'class':'form-control'}),
                'username': TextInput({'class':'form-control'}),
                'password': TextInput({'class':'form-control'}),
            } 