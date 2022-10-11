from django.db import models
from instrutores.models import Instrutor

class Alura_mais(models.Model):
    STATUS_DO_ALURA_MAIS = (('P', 'Pausado'),('A', 'Andamento'),('F', 'Finalizado'),)
    
    titulo = models.CharField(max_length=50)
    publico_alvo = models.TextField(max_length=450)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_DO_ALURA_MAIS, blank=False, null=False, default='P')

    def __str__(self):
        return self.titulo