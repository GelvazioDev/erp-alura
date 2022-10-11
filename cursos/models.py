from email.policy import default
from django.db import models
from instrutores.models import Instrutor
from figma.models import Figma

class Curso(models.Model):
    STATUS_DO_CURSO = (('P', 'Pausado'),('A', 'Andamento'),('F', 'Finalizado'),)
    
    nome = models.CharField(max_length=50)
    id_do_curso = models.CharField(default='0000', max_length=10)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Figma, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=450)
    github = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS_DO_CURSO, blank=False, null=False, default='P')

    def __str__(self):
        return self.nome