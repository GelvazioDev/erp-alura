from operator import mod
from sys import maxsize
from django.db import models

class Instrutor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class  Meta: 
        verbose_name_plural  =  "Instrutoras(os)"