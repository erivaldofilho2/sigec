from django.forms import ModelForm, URLInput, TextInput, Select, EmailInput, DateInput, NumberInput, Textarea
from .models import *


class FormEndereco(ModelForm):
    
    class Meta:
        model = Endereco
        fields = ['endereco','numero','complemento','bairro','cidade','estado','cep']
        
#         widgets = {
#             'endereco': TextInput(),
#             'numero': TextInput(),
#             'complemento': TextInput(),
#             'bairro': TextInput(),
#             'cidade': TextInput(),
#             'estado': TextInput(),
#             'cep': TextInput()
#                 
#             }
        

class FormContato(ModelForm):
    
    class Meta:
        model = Contato
        fields = ['tel_fixo','tel_celular','email']