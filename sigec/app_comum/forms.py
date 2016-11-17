from django.forms import ModelForm, URLInput, TextInput, Select, EmailInput, DateInput, NumberInput, Textarea
from .models import *


class FormEndereco(ModelForm):
    
    class Meta:
        model = Endereco
        fields = ['endereco','numero','complemento','bairro','cidade','estado','cep']
        
        widgets = {
            'endereco': TextInput({'class':'form-control'}),
            'numero': TextInput({'class':'form-control'}),
            'complemento': TextInput({'class':'form-control'}),
            'bairro': TextInput({'class':'form-control'}),
            'cidade': TextInput({'class':'form-control'}),
            'estado': TextInput({'class':'form-control'}),
            'cep': TextInput({'class':'form-control'})
                 
            }
        

class FormContato(ModelForm):
    
    class Meta:
        model = Contato
        fields = ['tel_fixo','tel_celular','email']
        
        widgets = {
            'tel_fixo': TextInput({'class':'form-control'}),
            'tel_celular': TextInput({'class':'form-control'}),
            'email': TextInput({'class':'form-control'}),
                 
            }