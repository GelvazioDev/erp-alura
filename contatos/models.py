from django.db import models
from enums.cargos import TIPOS_DE_CARGOS
from enums.carga_horaria import CARGA

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20, choices=TIPOS_DE_CARGOS, blank=False, null=False,default='0')
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    carga_horaria = models.CharField(max_length=20, choices=CARGA, blank=False, null=False,default='0')


    def __str__(self):
        return self.nome

    class  Meta: 
        verbose_name_plural  =  "Contatos, e-mail e cargos"
