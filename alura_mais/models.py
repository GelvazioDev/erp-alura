from django.db import models
from instrutores.models import Instrutor
from enums.categoria import CATEGORIA_DO_CURSO
from enums.status import STATUS

class Alura_mais(models.Model):
    
    titulo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_DO_CURSO, blank=False, null=False, default='0')
    publico_alvo = models.TextField(max_length=450)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='P')

    def __str__(self):
        return self.titulo

    class  Meta: 
        verbose_name_plural  =  "Alura+"