from django.db import models
from pickle import TRUE
from django.contrib.auth.models import User

#class UserEmpresa(models.Model):

class Empresa(models.Model):
    userEmpresa = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=120, null=True)
    CNPJ = models.IntegerField( null=True)
    contato = models.IntegerField(null=True)
    rua = models.CharField(max_length=120, null=True)
    numero = models.IntegerField(null=True)
    bairro = models.CharField(max_length=120, null=True)
    CEP= models.IntegerField(null=True)
    razaosocial = models.CharField('Razão Social', max_length=70, null=True)

    def __str__(self):
        return self.nome

    