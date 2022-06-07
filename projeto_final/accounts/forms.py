from dataclasses import fields
from django.contrib.auth.models import User
from accounts.models import Empresa
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CadastrarUserEmpresa(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )

class CadastrarEmpresa(ModelForm):
    
    class Meta:
        model = Empresa
        fields = (
            'userEmpresa',
            'nome',
            'CNPJ',
            'contato',
            'CEP',
        )
