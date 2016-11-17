from django import forms
from django.forms import ModelForm, URLInput, TextInput, Select, EmailInput, DateInput, NumberInput, Textarea
from .models import *
from app_comum.forms import *

class FormClientePF(ModelForm):
    
    class Meta:
        model = ClientePF
        fields = ['nome','cpf','observacao']
        
        widgets = {
            'nome': TextInput({'class':'form-control'}),
            'cpf': TextInput({'class':'form-control'}),
            'observacao': Textarea({'class':'form-control'}),
            }

