from django.db import models
from instrutores.models import Instrutor

class Artigo(models.Model):
    STATUS_DO_ARTIGO = (('P', 'Pausado'),('A', 'Andamento'),('F', 'Finalizado'),)
    
    titulo = models.CharField(max_length=50)
    publico_alvo = models.TextField(max_length=450)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE, related_name='instrutor')
    link_doc = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS_DO_ARTIGO, blank=False, null=False, default='P')

    def __str__(self):
        return self.titulo