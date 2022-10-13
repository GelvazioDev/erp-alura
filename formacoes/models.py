from django.db import models
from figma.models import Figma
from cursos.models import Curso

class Formacao(models.Model):
    # https://docs.google.com/spreadsheets/d/1hZdARQ9g7T9yfJtVA9VWRfNPXUTf2Du6XP5TMM2Lphg/edit#gid=0
    STATUS_DA_FORMACAO = (('1', 'Planejamento'),('2', 'Early Access'),('3', 'Finalizada'),)
    
    titullo = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso)
    status = models.CharField(max_length=3, choices=STATUS_DA_FORMACAO, blank=False, null=False, default='1')

    def __str__(self):
        return self.titulo

    class  Meta: 
        verbose_name_plural  =  "Formações"
