from django.db import models
from figma.models import Figma
from cursos.models import Curso

class Formacao(models.Model):
    STATUS_DA_FORMACAO = (('1', 'Planejamento'),('2', 'Early Access'),('3', 'Finalizada'),)
    
    titullo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=450)
    projeto = models.ForeignKey(Figma, on_delete=models.CASCADE, related_name='projeto')
    quantidade_de_cursos = models.IntegerField(default=0)
    cursos = models.ManyToManyField(Curso)
    descricao_passo_1 = models.TextField(max_length=450, default='')
    descricao_passo_2 = models.TextField(max_length=450, default='')
    descricao_passo_3 = models.TextField(max_length=450, default='')
    status = models.CharField(max_length=3, choices=STATUS_DA_FORMACAO, blank=False, null=False, default='1')

    def __str__(self):
        return self.titulo

    class  Meta: 
        verbose_name_plural  =  "Formações"
